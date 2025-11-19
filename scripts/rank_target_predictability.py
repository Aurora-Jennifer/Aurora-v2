"""
Target Predictability Ranking

Uses multiple model families to evaluate which of your 63 targets are most predictable.
This helps prioritize compute: train models on high-predictability targets first.

Methodology:
1. For each target, train multiple model families on sample data
2. Calculate predictability scores:
   - Model R² scores (cross-validated)
   - Feature importance magnitude (mean absolute SHAP/importance)
   - Consistency across models (low std = high confidence)
3. Rank targets by composite predictability score
4. Output ranked list with recommendations

Usage:
  # Rank all enabled targets
  python scripts/rank_target_predictability.py
  
  # Test on specific symbols first
  python scripts/rank_target_predictability.py --symbols AAPL,MSFT,GOOGL
  
  # Rank specific targets
  python scripts/rank_target_predictability.py --targets peak_60m,valley_60m,swing_high_15m
"""

import argparse
import logging
import sys
from pathlib import Path
from typing import List, Dict, Any, Tuple
import pandas as pd
import numpy as np
from dataclasses import dataclass
import yaml
import json
from collections import defaultdict
import warnings

# Suppress expected warnings (harmless)
warnings.filterwarnings('ignore', message='X does not have valid feature names')
warnings.filterwarnings('ignore', category=UserWarning, module='sklearn')
warnings.filterwarnings('ignore', category=RuntimeWarning, module='sklearn')
warnings.filterwarnings('ignore', message='invalid value encountered in divide')
warnings.filterwarnings('ignore', message='invalid value encountered in true_divide')

# Add project root
_REPO_ROOT = Path(__file__).resolve().parents[1]
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


@dataclass
class TargetPredictabilityScore:
    """Predictability assessment for a single target"""
    target_name: str
    target_column: str
    mean_r2: float
    std_r2: float
    mean_importance: float  # Mean absolute importance
    consistency: float  # 1 - CV(R²) - lower is better
    n_models: int
    model_scores: Dict[str, float]
    composite_score: float = 0.0


def load_target_configs() -> Dict[str, Dict]:
    """Load target configurations"""
    config_path = _REPO_ROOT / "CONFIG" / "target_configs.yaml"
    with open(config_path) as f:
        config = yaml.safe_load(f)
    return config['targets']


def discover_all_targets(symbol: str, data_dir: Path) -> Dict[str, Dict]:
    """
    Auto-discover all valid targets from data (non-degenerate).
    
    Discovers:
    - y_* targets (barrier, swing, MFE/MDD targets)
    - fwd_ret_* targets (forward return targets)
    
    Returns dict of {target_name: config} for all valid targets found.
    """
    import pandas as pd
    import numpy as np
    
    # Load sample data to discover targets
    symbol_dir = data_dir / f"symbol={symbol}"
    parquet_file = symbol_dir / f"{symbol}.parquet"
    
    if not parquet_file.exists():
        raise FileNotFoundError(f"Cannot discover targets: {parquet_file} not found")
    
    df = pd.read_parquet(parquet_file)
    
    # Find all target columns
    # 1. y_* targets (barrier, swing, MFE/MDD)
    y_targets = [c for c in df.columns if c.startswith('y_')]
    # 2. fwd_ret_* targets (forward returns)
    fwd_ret_targets = [c for c in df.columns if c.startswith('fwd_ret_')]
    
    all_targets = y_targets + fwd_ret_targets
    
    # Filter out degenerate targets (single class or zero variance)
    valid_targets = {}
    degenerate_count = 0
    first_touch_count = 0
    
    for target_col in all_targets:
        y = df[target_col].dropna()
        if len(y) == 0:
            continue
        
        unique_vals = y.unique()
        n_unique = len(unique_vals)
        
        # Skip degenerate targets (single class)
        if n_unique == 1:
            degenerate_count += 1
            continue
        
        # For regression targets (fwd_ret_*), also check variance
        if target_col.startswith('fwd_ret_'):
            std = y.std()
            if std < 1e-6:  # Zero or near-zero variance
                degenerate_count += 1
                continue
        
        # Skip first_touch targets (they're leaked - correlated with hit_direction features)
        if 'first_touch' in target_col:
            first_touch_count += 1
            continue
        
        # Create a simple config for this target
        if target_col.startswith('y_'):
            target_name = target_col.replace('y_will_', '').replace('y_', '')
            target_type = 'Classification' if n_unique <= 10 else 'Regression'
        else:  # fwd_ret_*
            target_name = target_col  # Keep full name for forward returns
            target_type = 'Regression'
        
        valid_targets[target_name] = {
            'target_column': target_col,
            'description': f"Auto-discovered target: {target_col}",
            'use_case': f"{target_type} target",
            'top_n': 60,
            'method': 'mean',
            'enabled': True
        }
    
    logger.info(f"  Discovered {len(valid_targets)} valid targets")
    logger.info(f"    - y_* targets: {len([t for t in valid_targets.values() if t['target_column'].startswith('y_')])}")
    logger.info(f"    - fwd_ret_* targets: {len([t for t in valid_targets.values() if t['target_column'].startswith('fwd_ret_')])}")
    logger.info(f"  Skipped {degenerate_count} degenerate targets (single class/zero variance)")
    if first_touch_count > 0:
        logger.info(f"  Skipped {first_touch_count} first_touch targets (leaked)")
    
    return valid_targets


def load_sample_data(
    symbol: str,
    data_dir: Path,
    max_samples: int = 10000
) -> pd.DataFrame:
    """Load sample data for a symbol"""
    symbol_dir = data_dir / f"symbol={symbol}"
    parquet_file = symbol_dir / f"{symbol}.parquet"
    
    if not parquet_file.exists():
        logger.warning(f"  Symbol {symbol} not found in dataset, skipping")
        raise FileNotFoundError(f"Data not found: {parquet_file}")
    
    df = pd.read_parquet(parquet_file)
    
    # Sample if too large
    if len(df) > max_samples:
        df = df.sample(n=max_samples, random_state=42)
    
    return df


def prepare_features_and_target(
    df: pd.DataFrame,
    target_column: str
) -> Tuple[np.ndarray, np.ndarray, List[str]]:
    """Prepare features and target for modeling"""
    
    # Check target exists
    if target_column not in df.columns:
        raise ValueError(f"Target '{target_column}' not in data")
    
    # Drop NaN in target
    df = df.dropna(subset=[target_column])
    
    if df.empty:
        raise ValueError("No valid data after dropping NaN in target")
    
    # LEAKAGE PREVENTION: Filter out leaking features
    import sys
    sys.path.insert(0, str(_REPO_ROOT / "scripts"))
    from filter_leaking_features import filter_features
    
    all_columns = df.columns.tolist()
    safe_columns = filter_features(all_columns, verbose=False)
    
    # Keep only safe features + target
    safe_columns_with_target = [c for c in safe_columns if c != target_column] + [target_column]
    df = df[safe_columns_with_target]
    
    # Prepare features (exclude target explicitly)
    X = df.drop(columns=[target_column], errors='ignore')
    
    # Drop object dtypes
    object_cols = X.select_dtypes(include=['object']).columns.tolist()
    if object_cols:
        X = X.drop(columns=object_cols)
    
    y = df[target_column]
    feature_names = X.columns.tolist()
    
    return X.to_numpy(), y.to_numpy(), feature_names


def load_multi_model_config(config_path: Path = None) -> Dict[str, Any]:
    """Load multi-model feature selection configuration"""
    if config_path is None:
        config_path = _REPO_ROOT / "CONFIG" / "multi_model_feature_selection.yaml"
    
    if not config_path.exists():
        logger.debug(f"Multi-model config not found: {config_path}, using defaults")
        return None
    
    try:
        import yaml
        with open(config_path) as f:
            config = yaml.safe_load(f)
        logger.info(f"Loaded multi-model config from {config_path}")
        return config
    except Exception as e:
        logger.warning(f"Failed to load multi-model config: {e}")
        return None


def train_and_evaluate_models(
    X: np.ndarray,
    y: np.ndarray,
    feature_names: List[str],
    model_families: List[str] = None,
    multi_model_config: Dict[str, Any] = None
) -> Tuple[Dict[str, float], float]:
    """
    Train multiple models and return scores + importance magnitude
    
    Returns:
        model_scores: Dict of R² scores per model
        mean_importance: Mean absolute feature importance
    """
    from sklearn.model_selection import cross_val_score
    from sklearn.preprocessing import StandardScaler
    import lightgbm as lgb
    
    if model_families is None:
        # Load from multi-model config if available
        if multi_model_config:
            model_families = [
                name for name, config in multi_model_config.get('model_families', {}).items()
                if config.get('enabled', False)
            ]
            logger.debug(f"Using {len(model_families)} models from config: {', '.join(model_families)}")
        else:
            model_families = ['lightgbm', 'random_forest', 'neural_network']
    
    model_scores = {}
    importance_magnitudes = []
    
    # Determine task type (fixed detection)
    unique_vals = np.unique(y[~np.isnan(y)])
    is_binary = len(unique_vals) == 2 and set(unique_vals).issubset({0, 1, 0.0, 1.0})
    is_multiclass = len(unique_vals) <= 10 and all(isinstance(v, (int, np.integer)) or v.is_integer() for v in unique_vals)
    is_classification = is_binary or is_multiclass
    
    # Use R² for both (works for classification too, measures explained variance)
    scoring = 'r2'
    
    # Check for degenerate target BEFORE training models
    # A target is degenerate if it has < 2 unique values or one class has < 2 samples
    unique_vals = np.unique(y[~np.isnan(y)])
    if len(unique_vals) < 2:
        logger.debug(f"    Skipping: Target has only {len(unique_vals)} unique value(s)")
        return {}, 0.0
    
    # For classification, check class balance
    if is_binary or is_multiclass:
        class_counts = np.bincount(y[~np.isnan(y)].astype(int))
        min_class_count = class_counts[class_counts > 0].min()
        if min_class_count < 2:
            logger.debug(f"    Skipping: Smallest class has only {min_class_count} sample(s)")
            return {}, 0.0
    
    # LightGBM
    if 'lightgbm' in model_families:
        try:
            # GPU settings (will fallback to CPU if GPU not available)
            gpu_params = {}
            try:
                # Try CUDA first (fastest)
                test_model = lgb.LGBMRegressor(device='cuda', n_estimators=1, verbose=-1)
                test_model.fit(np.random.rand(10, 5), np.random.rand(10))
                gpu_params = {'device': 'cuda', 'gpu_device_id': 0}
                logger.info("  Using GPU (CUDA) for LightGBM")
            except:
                try:
                    # Try OpenCL
                    test_model = lgb.LGBMRegressor(device='gpu', n_estimators=1, verbose=-1)
                    test_model.fit(np.random.rand(10, 5), np.random.rand(10))
                    gpu_params = {'device': 'gpu', 'gpu_platform_id': 0, 'gpu_device_id': 0}
                    logger.info("  Using GPU (OpenCL) for LightGBM")
                except:
                    logger.info("  Using CPU for LightGBM")
            
            if is_binary:
                model = lgb.LGBMClassifier(
                    objective='binary',
                    n_estimators=200,
                    learning_rate=0.05,
                    num_leaves=31,
                    verbose=-1,
                    random_state=42,
                    **gpu_params
                )
            elif is_multiclass:
                n_classes = len(unique_vals)
                model = lgb.LGBMClassifier(
                    objective='multiclass',
                    num_class=n_classes,
                    n_estimators=200,
                    learning_rate=0.05,
                    num_leaves=31,
                    verbose=-1,
                    random_state=42,
                    **gpu_params
                )
            else:
                model = lgb.LGBMRegressor(
                    objective='regression',
                    n_estimators=200,
                    learning_rate=0.05,
                    num_leaves=31,
                    verbose=-1,
                    random_state=42,
                    **gpu_params
                )
            
            scores = cross_val_score(model, X, y, cv=3, scoring=scoring, n_jobs=1, error_score=np.nan)
            valid_scores = scores[~np.isnan(scores)]
            model_scores['lightgbm'] = valid_scores.mean() if len(valid_scores) > 0 else np.nan
            
            # Train once to get importance
            model.fit(X, y)
            # Use percentage of total importance in top 10% features (0-1 scale, interpretable)
            importances = model.feature_importances_
            total_importance = np.sum(importances)
            if total_importance > 0:
                top_k = max(1, int(len(importances) * 0.1))  # Top 10% of features
                top_importance_sum = np.sum(np.sort(importances)[-top_k:])
                # Normalize to 0-1: what % of total importance is in top 10%?
                importance_ratio = top_importance_sum / total_importance
            else:
                importance_ratio = 0.0
            importance_magnitudes.append(importance_ratio)
            
        except Exception as e:
            logger.warning(f"LightGBM failed: {e}")
    
    # Random Forest
    if 'random_forest' in model_families:
        try:
            from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
            
            if is_binary or is_multiclass:
                model = RandomForestClassifier(n_estimators=100, max_depth=10, 
                                              random_state=42, n_jobs=2)
            else:
                model = RandomForestRegressor(n_estimators=100, max_depth=10, 
                                             random_state=42, n_jobs=2)
            
            scores = cross_val_score(model, X, y, cv=3, scoring=scoring, n_jobs=1, error_score=np.nan)
            valid_scores = scores[~np.isnan(scores)]
            model_scores['random_forest'] = valid_scores.mean() if len(valid_scores) > 0 else np.nan
            
            model.fit(X, y)
            # Use percentage of total importance in top 10% features (0-1 scale, interpretable)
            importances = model.feature_importances_
            total_importance = np.sum(importances)
            if total_importance > 0:
                top_k = max(1, int(len(importances) * 0.1))  # Top 10% of features
                top_importance_sum = np.sum(np.sort(importances)[-top_k:])
                # Normalize to 0-1: what % of total importance is in top 10%?
                importance_ratio = top_importance_sum / total_importance
            else:
                importance_ratio = 0.0
            importance_magnitudes.append(importance_ratio)
            
        except Exception as e:
            logger.warning(f"RandomForest failed: {e}")
    
    # Neural Network
    if 'neural_network' in model_families:
        try:
            from sklearn.neural_network import MLPRegressor, MLPClassifier
            from sklearn.impute import SimpleImputer
            
            # Handle NaN values (neural networks can't handle them)
            imputer = SimpleImputer(strategy='median')
            X_imputed = imputer.fit_transform(X)
            
            # Scale for NN
            scaler = StandardScaler()
            X_scaled = scaler.fit_transform(X_imputed)
            
            if is_binary or is_multiclass:
                model = MLPClassifier(hidden_layer_sizes=(64, 32), max_iter=200,
                                     early_stopping=True, random_state=42)
            else:
                model = MLPRegressor(hidden_layer_sizes=(64, 32), max_iter=200,
                                    early_stopping=True, random_state=42)
            
            # Neural networks need special handling for degenerate targets
            # Disable stratified split if target is imbalanced
            try:
                scores = cross_val_score(model, X_scaled, y, cv=3, scoring=scoring, n_jobs=1, error_score=np.nan)
                valid_scores = scores[~np.isnan(scores)]
                model_scores['neural_network'] = valid_scores.mean() if len(valid_scores) > 0 else np.nan
            except ValueError as e:
                if "least populated class" in str(e) or "too few" in str(e):
                    logger.debug(f"    Neural Network: Target too imbalanced for CV")
                    model_scores['neural_network'] = np.nan
                else:
                    raise
            
            # Permutation importance magnitude (simplified)
            model.fit(X_scaled, y)
            baseline_score = model.score(X_scaled, y)
            perm_scores = []
            for i in range(min(10, X.shape[1])):  # Sample 10 features
                X_perm = X_scaled.copy()
                np.random.shuffle(X_perm[:, i])
                perm_score = model.score(X_perm, y)
                perm_scores.append(abs(baseline_score - perm_score))
            
            importance_magnitudes.append(np.mean(perm_scores))
            
        except Exception as e:
            logger.warning(f"NeuralNetwork failed: {e}")
    
    # XGBoost
    if 'xgboost' in model_families:
        try:
            import xgboost as xgb
            
            if is_binary:
                model = xgb.XGBClassifier(
                    n_estimators=200,
                    max_depth=6,
                    objective='binary:logistic',
                    verbosity=0,
                    random_state=42
                )
            elif is_multiclass:
                n_classes = len(unique_vals)
                model = xgb.XGBClassifier(
                    n_estimators=200,
                    max_depth=6,
                    objective='multi:softprob',
                    num_class=n_classes,
                    verbosity=0,
                    random_state=42
                )
            else:
                model = xgb.XGBRegressor(
                    n_estimators=200,
                    max_depth=6,
                    objective='reg:squarederror',
                    verbosity=0,
                    random_state=42
                )
            
            # XGBoost needs special handling for degenerate targets
            try:
                scores = cross_val_score(model, X, y, cv=3, scoring=scoring, n_jobs=1, error_score=np.nan)
                valid_scores = scores[~np.isnan(scores)]
                model_scores['xgboost'] = valid_scores.mean() if len(valid_scores) > 0 else np.nan
            except ValueError as e:
                if "Invalid classes" in str(e) or "Expected" in str(e):
                    logger.debug(f"    XGBoost: Target degenerate in some CV folds")
                    model_scores['xgboost'] = np.nan
                else:
                    raise
            
            # Train once to get importance
            model.fit(X, y)
            if hasattr(model, 'feature_importances_'):
                # Use percentage of total importance in top 10% features (0-1 scale, interpretable)
                importances = model.feature_importances_
                total_importance = np.sum(importances)
                if total_importance > 0:
                    top_k = max(1, int(len(importances) * 0.1))  # Top 10% of features
                    top_importance_sum = np.sum(np.sort(importances)[-top_k:])
                    # Normalize to 0-1: what % of total importance is in top 10%?
                    importance_ratio = top_importance_sum / total_importance
                else:
                    importance_ratio = 0.0
                importance_magnitudes.append(importance_ratio)
        except Exception as e:
            logger.warning(f"XGBoost failed: {e}")
    
    # CatBoost
    if 'catboost' in model_families:
        try:
            import catboost as cb
            
            if is_binary:
                model = cb.CatBoostClassifier(iterations=200, depth=6, verbose=False, random_seed=42)
            elif is_multiclass:
                n_classes = len(unique_vals)
                model = cb.CatBoostClassifier(iterations=200, depth=6, verbose=False, random_seed=42)
            else:
                model = cb.CatBoostRegressor(iterations=200, depth=6, verbose=False, random_seed=42)
            
            try:
                scores = cross_val_score(model, X, y, cv=3, scoring=scoring, n_jobs=1, error_score=np.nan)
                valid_scores = scores[~np.isnan(scores)]
                model_scores['catboost'] = valid_scores.mean() if len(valid_scores) > 0 else np.nan
            except (ValueError, TypeError) as e:
                if "Invalid classes" in str(e) or "Expected" in str(e):
                    logger.debug(f"    CatBoost: Target degenerate in some CV folds")
                    model_scores['catboost'] = np.nan
                else:
                    raise
            
            model.fit(X, y)
            importance = model.get_feature_importance()
            if len(importance) > 0:
                total_importance = np.sum(importance)
                if total_importance > 0:
                    top_k = max(1, int(len(importance) * 0.1))
                    top_importance_sum = np.sum(np.sort(importance)[-top_k:])
                    importance_ratio = top_importance_sum / total_importance
                else:
                    importance_ratio = 0.0
            else:
                importance_ratio = 0.0
            importance_magnitudes.append(importance_ratio)
        except ImportError:
            logger.warning("CatBoost not available (pip install catboost)")
        except Exception as e:
            logger.warning(f"CatBoost failed: {e}")
    
    # Lasso
    if 'lasso' in model_families:
        try:
            from sklearn.linear_model import Lasso
            from sklearn.impute import SimpleImputer
            
            # Lasso doesn't handle NaN - need to impute
            imputer = SimpleImputer(strategy='median')
            X_imputed = imputer.fit_transform(X)
            
            model = Lasso(alpha=0.1, max_iter=1000, random_state=42)
            scores = cross_val_score(model, X_imputed, y, cv=3, scoring=scoring, n_jobs=1, error_score=np.nan)
            valid_scores = scores[~np.isnan(scores)]
            model_scores['lasso'] = valid_scores.mean() if len(valid_scores) > 0 else np.nan
            
            model.fit(X_imputed, y)
            importance = np.abs(model.coef_)
            if len(importance) > 0:
                total_importance = np.sum(importance)
                if total_importance > 0:
                    top_k = max(1, int(len(importance) * 0.1))
                    top_importance_sum = np.sum(np.sort(importance)[-top_k:])
                    importance_ratio = top_importance_sum / total_importance
                else:
                    importance_ratio = 0.0
            else:
                importance_ratio = 0.0
            importance_magnitudes.append(importance_ratio)
        except Exception as e:
            logger.warning(f"Lasso failed: {e}")
    
    # Mutual Information
    if 'mutual_information' in model_families:
        try:
            from sklearn.feature_selection import mutual_info_regression, mutual_info_classif
            from sklearn.impute import SimpleImputer
            
            # Mutual information doesn't handle NaN - need to impute
            imputer = SimpleImputer(strategy='median')
            X_imputed = imputer.fit_transform(X)
            
            # Suppress warnings for zero-variance features
            with warnings.catch_warnings():
                warnings.simplefilter("ignore", RuntimeWarning)
                if is_binary or is_multiclass:
                    importance = mutual_info_classif(X_imputed, y, random_state=42, discrete_features='auto')
                else:
                    importance = mutual_info_regression(X_imputed, y, random_state=42, discrete_features='auto')
            
            # Handle NaN/inf
            importance = np.nan_to_num(importance, nan=0.0, posinf=0.0, neginf=0.0)
            
            # Mutual information doesn't have R², so we use a proxy based on max MI
            # Normalize to 0-1 scale for importance
            if len(importance) > 0 and np.max(importance) > 0:
                importance_normalized = importance / np.max(importance)
                total_importance = np.sum(importance_normalized)
                if total_importance > 0:
                    top_k = max(1, int(len(importance_normalized) * 0.1))
                    top_importance_sum = np.sum(np.sort(importance_normalized)[-top_k:])
                    importance_ratio = top_importance_sum / total_importance
                else:
                    importance_ratio = 0.0
            else:
                importance_ratio = 0.0
            
            # For mutual information, we can't compute R² directly
            # Use a proxy: higher MI concentration = better predictability
            # Scale to approximate R² range (0-0.3 for good targets)
            model_scores['mutual_information'] = min(0.3, importance_ratio * 0.3)
            importance_magnitudes.append(importance_ratio)
        except Exception as e:
            logger.warning(f"Mutual Information failed: {e}")
    
    # Univariate Selection
    if 'univariate_selection' in model_families:
        try:
            from sklearn.feature_selection import f_regression, f_classif
            from sklearn.impute import SimpleImputer
            
            # F-tests don't handle NaN - need to impute
            imputer = SimpleImputer(strategy='median')
            X_imputed = imputer.fit_transform(X)
            
            # Suppress division by zero warnings (expected for zero-variance features)
            with warnings.catch_warnings():
                warnings.simplefilter("ignore", RuntimeWarning)
                if is_binary or is_multiclass:
                    scores, pvalues = f_classif(X_imputed, y)
                else:
                    scores, pvalues = f_regression(X_imputed, y)
            
            # Handle NaN/inf in scores (from zero-variance features)
            scores = np.nan_to_num(scores, nan=0.0, posinf=0.0, neginf=0.0)
            
            # Normalize F-statistics
            if len(scores) > 0 and np.max(scores) > 0:
                importance = scores / np.max(scores)
                total_importance = np.sum(importance)
                if total_importance > 0:
                    top_k = max(1, int(len(importance) * 0.1))
                    top_importance_sum = np.sum(np.sort(importance)[-top_k:])
                    importance_ratio = top_importance_sum / total_importance
                else:
                    importance_ratio = 0.0
            else:
                importance_ratio = 0.0
            
            # F-statistics don't have R², use proxy
            model_scores['univariate_selection'] = min(0.3, importance_ratio * 0.3)
            importance_magnitudes.append(importance_ratio)
        except Exception as e:
            logger.warning(f"Univariate Selection failed: {e}")
    
    # RFE
    if 'rfe' in model_families:
        try:
            from sklearn.feature_selection import RFE
            from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
            from sklearn.impute import SimpleImputer
            
            # RFE uses RandomForest which handles NaN, but let's impute for consistency
            imputer = SimpleImputer(strategy='median')
            X_imputed = imputer.fit_transform(X)
            
            n_features_to_select = min(50, X_imputed.shape[1])
            
            if is_binary or is_multiclass:
                estimator = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42, n_jobs=2)
            else:
                estimator = RandomForestRegressor(n_estimators=100, max_depth=10, random_state=42, n_jobs=2)
            
            selector = RFE(estimator, n_features_to_select=n_features_to_select, step=5)
            selector.fit(X_imputed, y)
            
            # Get R² from the underlying estimator
            scores = cross_val_score(selector.estimator_, X_imputed, y, cv=3, scoring=scoring, n_jobs=1, error_score=np.nan)
            valid_scores = scores[~np.isnan(scores)]
            model_scores['rfe'] = valid_scores.mean() if len(valid_scores) > 0 else np.nan
            
            # Convert ranking to importance
            ranking = selector.ranking_
            importance = 1.0 / (ranking + 1e-6)
            if len(importance) > 0:
                total_importance = np.sum(importance)
                if total_importance > 0:
                    top_k = max(1, int(len(importance) * 0.1))
                    top_importance_sum = np.sum(np.sort(importance)[-top_k:])
                    importance_ratio = top_importance_sum / total_importance
                else:
                    importance_ratio = 0.0
            else:
                importance_ratio = 0.0
            importance_magnitudes.append(importance_ratio)
        except Exception as e:
            logger.warning(f"RFE failed: {e}")
    
    # Boruta
    if 'boruta' in model_families:
        try:
            from boruta import BorutaPy
            from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
            from sklearn.impute import SimpleImputer
            
            # Boruta uses RandomForest which handles NaN, but let's impute for consistency
            imputer = SimpleImputer(strategy='median')
            X_imputed = imputer.fit_transform(X)
            
            if is_binary or is_multiclass:
                rf = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42, n_jobs=2)
            else:
                rf = RandomForestRegressor(n_estimators=100, max_depth=10, random_state=42, n_jobs=2)
            
            boruta = BorutaPy(rf, n_estimators='auto', verbose=0, random_state=42, max_iter=100)
            boruta.fit(X_imputed, y)
            
            # Get R² from underlying RF
            scores = cross_val_score(rf, X_imputed, y, cv=3, scoring=scoring, n_jobs=1, error_score=np.nan)
            valid_scores = scores[~np.isnan(scores)]
            model_scores['boruta'] = valid_scores.mean() if len(valid_scores) > 0 else np.nan
            
            # Convert to importance
            ranking = boruta.ranking_
            selected = boruta.support_
            importance = np.where(selected, 1.0, np.where(ranking == 2, 0.5, 0.1))
            if len(importance) > 0:
                total_importance = np.sum(importance)
                if total_importance > 0:
                    top_k = max(1, int(len(importance) * 0.1))
                    top_importance_sum = np.sum(np.sort(importance)[-top_k:])
                    importance_ratio = top_importance_sum / total_importance
                else:
                    importance_ratio = 0.0
            else:
                importance_ratio = 0.0
            importance_magnitudes.append(importance_ratio)
        except ImportError:
            logger.warning("Boruta not available (pip install Boruta)")
        except Exception as e:
            logger.warning(f"Boruta failed: {e}")
    
    # Stability Selection
    if 'stability_selection' in model_families:
        try:
            from sklearn.linear_model import LassoCV, LogisticRegressionCV
            from sklearn.impute import SimpleImputer
            
            # Stability selection uses Lasso/LogisticRegression which don't handle NaN
            imputer = SimpleImputer(strategy='median')
            X_imputed = imputer.fit_transform(X)
            
            n_bootstrap = 50
            stability_scores = np.zeros(X_imputed.shape[1])
            bootstrap_r2_scores = []
            
            for _ in range(n_bootstrap):
                indices = np.random.choice(len(X_imputed), size=len(X_imputed), replace=True)
                X_boot, y_boot = X_imputed[indices], y[indices]
                
                try:
                    if is_binary or is_multiclass:
                        model = LogisticRegressionCV(Cs=10, cv=3, random_state=42, max_iter=1000, n_jobs=1)
                    else:
                        model = LassoCV(cv=3, random_state=42, max_iter=1000, n_jobs=1)
                    
                    model.fit(X_boot, y_boot)
                    coef = model.coef_[0] if len(model.coef_.shape) > 1 else model.coef_
                    stability_scores += (np.abs(coef) > 1e-6).astype(int)
                    
                    # Get R² from this bootstrap
                    r2 = model.score(X_boot, y_boot)
                    bootstrap_r2_scores.append(r2)
                except:
                    continue
            
            # Average R² across bootstraps
            if bootstrap_r2_scores:
                model_scores['stability_selection'] = np.mean(bootstrap_r2_scores)
            else:
                model_scores['stability_selection'] = np.nan
            
            # Normalize stability scores to importance
            importance = stability_scores / n_bootstrap
            if len(importance) > 0:
                total_importance = np.sum(importance)
                if total_importance > 0:
                    top_k = max(1, int(len(importance) * 0.1))
                    top_importance_sum = np.sum(np.sort(importance)[-top_k:])
                    importance_ratio = top_importance_sum / total_importance
                else:
                    importance_ratio = 0.0
            else:
                importance_ratio = 0.0
            importance_magnitudes.append(importance_ratio)
        except Exception as e:
            logger.warning(f"Stability Selection failed: {e}")
    
    # Histogram Gradient Boosting
    if 'histogram_gradient_boosting' in model_families:
        try:
            from sklearn.ensemble import HistGradientBoostingRegressor, HistGradientBoostingClassifier
            
            if is_binary or is_multiclass:
                model = HistGradientBoostingClassifier(
                    max_iter=200,
                    max_depth=6,
                    random_state=42
                )
            else:
                model = HistGradientBoostingRegressor(
                    max_iter=200,
                    max_depth=6,
                    random_state=42
                )
            
            scores = cross_val_score(model, X, y, cv=3, scoring=scoring, n_jobs=1, error_score=np.nan)
            valid_scores = scores[~np.isnan(scores)]
            model_scores['histogram_gradient_boosting'] = valid_scores.mean() if len(valid_scores) > 0 else np.nan
            
            # Train once to get importance
            model.fit(X, y)
            if hasattr(model, 'feature_importances_'):
                # Use percentage of total importance in top 10% features (0-1 scale, interpretable)
                importances = model.feature_importances_
                total_importance = np.sum(importances)
                if total_importance > 0:
                    top_k = max(1, int(len(importances) * 0.1))  # Top 10% of features
                    top_importance_sum = np.sum(np.sort(importances)[-top_k:])
                    # Normalize to 0-1: what % of total importance is in top 10%?
                    importance_ratio = top_importance_sum / total_importance
                else:
                    importance_ratio = 0.0
                importance_magnitudes.append(importance_ratio)
        except Exception as e:
            logger.warning(f"Histogram Gradient Boosting failed: {e}")
    
    mean_importance = np.mean(importance_magnitudes) if importance_magnitudes else 0.0
    
    return model_scores, mean_importance


def calculate_composite_score(
    mean_r2: float,
    std_r2: float,
    mean_importance: float,
    n_models: int
) -> float:
    """
    Calculate composite predictability score
    
    Components:
    - Mean R²: Higher is better (0-1)
    - Consistency: Lower std is better
    - Importance magnitude: Higher is better
    - Model agreement: More models = more confidence
    """
    
    # Normalize components
    r2_component = max(0, mean_r2)  # 0-1
    consistency_component = 1.0 / (1.0 + std_r2)  # Higher when std is low
    
    # R²-weighted importance: Scale importance by R², but don't penalize too harshly
    # Good targets (R²=0.2): importance * 1.2 = boosted
    # Poor targets (R²=-0.45): importance * 0.7 = moderately penalized (still some value)
    # Very poor (R²<-0.5): importance * 0.5 = heavily penalized
    # This creates a bigger gap while acknowledging negative R² might still have signal
    if mean_r2 > 0:
        # Positive R²: boost proportionally (R²=0.2 → 1.2x, R²=0.5 → 1.5x)
        importance_component = mean_importance * (1.0 + mean_r2)
    else:
        # Negative R²: soft penalty (R²=-0.2 → 0.8x, R²=-0.45 → 0.7x, R²=-0.6 → 0.6x)
        # Don't go below 0.5x to preserve some signal even for poor targets
        penalty = abs(mean_r2) * 0.67  # Softer penalty (max 0.67x reduction at R²=-1.0)
        importance_component = mean_importance * max(0.5, 1.0 - penalty)
    
    # Weighted average
    composite = (
        0.50 * r2_component +        # 50% weight on R²
        0.25 * consistency_component + # 25% on consistency
        0.25 * importance_component    # 25% on R²-weighted importance
    )
    
    # Bonus for more models (up to 10% boost)
    model_bonus = min(0.1, n_models * 0.02)
    composite = composite * (1.0 + model_bonus)
    
    return composite


def evaluate_target_predictability(
    target_name: str,
    target_config: Dict[str, Any],
    symbols: List[str],
    data_dir: Path,
    model_families: List[str],
    multi_model_config: Dict[str, Any] = None
) -> TargetPredictabilityScore:
    """Evaluate predictability of a single target across symbols"""
    
    target_column = target_config['target_column']
    logger.info(f"\n{'='*60}")
    logger.info(f"Evaluating: {target_name} ({target_column})")
    logger.info(f"{'='*60}")
    
    all_model_scores = []
    all_importances = []
    
    for symbol in symbols:
        try:
            logger.info(f"  {symbol}...")
            
            # Load data
            df = load_sample_data(symbol, data_dir, max_samples=10000)
            
            # Prepare features
            X, y, feature_names = prepare_features_and_target(df, target_column)
            
            # Check if target is degenerate in this sample (single class or too imbalanced)
            unique_vals = np.unique(y)
            if len(unique_vals) < 2:
                logger.warning(f"Skipping: Target has only {len(unique_vals)} unique value(s) in sample")
                continue
            
            # For classification, check if classes are too imbalanced for CV
            if len(unique_vals) <= 10:  # Likely classification
                class_counts = np.bincount(y.astype(int))
                min_class_count = class_counts[class_counts > 0].min()
                if min_class_count < 2:
                    logger.warning(f"Skipping: Smallest class has only {min_class_count} sample(s) (too few for CV)")
                    continue
            
            # Train and evaluate
            model_scores, importance = train_and_evaluate_models(
                X, y, feature_names, model_families, multi_model_config
            )
            
            if model_scores:
                all_model_scores.append(model_scores)
                all_importances.append(importance)
                
                scores_str = ", ".join([f"{k}={v:.3f}" for k, v in model_scores.items()])
                logger.info(f"Scores: {scores_str}, importance={importance:.2f}")
            
        except Exception as e:
            logger.warning(f"Failed: {e}")
            continue
    
    if not all_model_scores:
        logger.warning(f"No successful evaluations for {target_name} (skipping)")
        return TargetPredictabilityScore(
            target_name=target_name,
            target_column=target_column,
            mean_r2=-999.0,  # Flag for degenerate/failed targets
            std_r2=1.0,
            mean_importance=0.0,
            consistency=0.0,
            n_models=0,
            model_scores={}
        )
    
    # Aggregate across symbols and models (skip NaN scores)
    all_scores_by_model = defaultdict(list)
    for scores_dict in all_model_scores:
        for model_name, score in scores_dict.items():
            if not (np.isnan(score) if isinstance(score, (float, np.floating)) else False):
                all_scores_by_model[model_name].append(score)
    
    # Calculate statistics (only from models that succeeded)
    model_means = {model: np.mean(scores) for model, scores in all_scores_by_model.items() if scores}
    if not model_means:
        logger.warning(f"No successful model evaluations for {target_name}")
        return TargetPredictabilityScore(
            target_name=target_name,
            target_column=target_column,
            mean_r2=-999.0,
            std_r2=1.0,
            mean_importance=0.0,
            consistency=0.0,
            n_models=0,
            model_scores={}
        )
    
    mean_r2 = np.mean(list(model_means.values()))
    std_r2 = np.std(list(model_means.values())) if len(model_means) > 1 else 0.0
    mean_importance = np.mean(all_importances)
    consistency = 1.0 - (std_r2 / (abs(mean_r2) + 1e-6))
    
    # Composite score
    composite = calculate_composite_score(
        mean_r2, std_r2, mean_importance, len(all_scores_by_model)
    )
    
    result = TargetPredictabilityScore(
        target_name=target_name,
        target_column=target_column,
        mean_r2=mean_r2,
        std_r2=std_r2,
        mean_importance=mean_importance,
        consistency=consistency,
        n_models=len(all_scores_by_model),
        model_scores=model_means,
        composite_score=composite
    )
    
    logger.info(f"Summary: R²={mean_r2:.3f}±{std_r2:.3f}, "
               f"importance={mean_importance:.2f}, composite={composite:.3f}")
    
    return result


def save_rankings(
    results: List[TargetPredictabilityScore],
    output_dir: Path
):
    """Save target predictability rankings"""
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Sort by composite score
    results = sorted(results, key=lambda x: x.composite_score, reverse=True)
    
    # Create DataFrame
    df = pd.DataFrame([{
        'rank': i + 1,
        'target_name': r.target_name,
        'target_column': r.target_column,
        'composite_score': r.composite_score,
        'mean_r2': r.mean_r2,
        'std_r2': r.std_r2,
        'mean_importance': r.mean_importance,
        'consistency': r.consistency,
        'n_models': r.n_models,
        **{f'{model}_r2': score for model, score in r.model_scores.items()},
        'recommendation': _get_recommendation(r)
    } for i, r in enumerate(results)])
    
    # Save CSV
    df.to_csv(output_dir / "target_predictability_rankings.csv", index=False)
    logger.info(f"\nSaved rankings to target_predictability_rankings.csv")
    
    # Save YAML with recommendations
    yaml_data = {
        'target_rankings': [
            {
                'rank': i + 1,
                'target': r.target_name,
                'composite_score': float(r.composite_score),
                'mean_r2': float(r.mean_r2),
                'recommendation': _get_recommendation(r)
            }
            for i, r in enumerate(results)
        ]
    }
    
    with open(output_dir / "target_predictability_rankings.yaml", 'w') as f:
        yaml.dump(yaml_data, f, default_flow_style=False)
    
    logger.info(f"Saved YAML to target_predictability_rankings.yaml")


def _get_recommendation(score: TargetPredictabilityScore) -> str:
    """Get recommendation based on predictability score"""
    if score.composite_score >= 0.7:
        return "PRIORITIZE - Strong predictive signal"
    elif score.composite_score >= 0.5:
        return "ENABLE - Good predictive signal"
    elif score.composite_score >= 0.3:
        return "TEST - Moderate signal, worth exploring"
    else:
        return "DEPRIORITIZE - Weak signal, low ROI"


def main():
    parser = argparse.ArgumentParser(
        description="Rank target predictability across model families"
    )
    parser.add_argument("--symbols", type=str, default="AAPL,MSFT,GOOGL,TSLA,JPM",
                       help="Symbols to test on (default: 5 representative stocks)")
    parser.add_argument("--data-dir", type=Path,
                       default=_REPO_ROOT / "data/data_labeled/interval=5m")
    parser.add_argument("--output-dir", type=Path,
                       default=_REPO_ROOT / "results/target_rankings")
    parser.add_argument("--targets", type=str,
                       help="Specific targets to evaluate (comma-separated), default: all enabled")
    parser.add_argument("--discover-all", action="store_true",
                       help="Auto-discover and rank ALL targets from data (ignores config)")
    parser.add_argument("--model-families", type=str,
                       default=None,
                       help="Model families to use (default: use all enabled from multi_model_feature_selection.yaml)")
    parser.add_argument("--multi-model-config", type=Path,
                       default=None,
                       help="Path to multi-model config (default: CONFIG/multi_model_feature_selection.yaml)")
    
    args = parser.parse_args()
    
    # Parse inputs
    symbols = [s.strip() for s in args.symbols.split(',')]
    
    # Load multi-model config
    multi_model_config = None
    if args.multi_model_config:
        multi_model_config = load_multi_model_config(args.multi_model_config)
    else:
        multi_model_config = load_multi_model_config()  # Try default path
    
    # Determine model families
    if args.model_families:
        model_families = [m.strip() for m in args.model_families.split(',')]
    elif multi_model_config:
        # Use enabled models from config
        model_families = [
            name for name, config in multi_model_config.get('model_families', {}).items()
            if config.get('enabled', False)
        ]
        logger.info(f"Using {len(model_families)} model families from config: {', '.join(model_families)}")
    else:
        # Default fallback
        model_families = ['lightgbm', 'random_forest', 'neural_network']
        logger.info(f"Using default model families: {', '.join(model_families)}")
    
    logger.info("="*80)
    logger.info("Target Predictability Ranking")
    logger.info("="*80)
    logger.info(f"Test symbols: {', '.join(symbols)}")
    logger.info(f"Model families: {', '.join(model_families)}")
    
    # Discover or load targets
    if args.discover_all:
        logger.info("Auto-discovering ALL targets from data...")
        targets_to_eval = discover_all_targets(symbols[0], args.data_dir)
        logger.info(f"Found {len(targets_to_eval)} valid targets\n")
    else:
        # Load target configs
        target_configs = load_target_configs()
        
        # Filter targets
        if args.targets:
            requested = [t.strip() for t in args.targets.split(',')]
            targets_to_eval = {k: v for k, v in target_configs.items() if k in requested}
        else:
            # Only evaluate enabled targets
            targets_to_eval = {k: v for k, v in target_configs.items() if v.get('enabled', False)}
        
        logger.info(f"Evaluating {len(targets_to_eval)} targets\n")
    
    # Evaluate each target
    results = []
    for target_name, target_config in targets_to_eval.items():
        result = evaluate_target_predictability(
            target_name, target_config, symbols, args.data_dir, model_families, multi_model_config
        )
        # Skip degenerate targets (marked with mean_r2 = -999)
        if result.mean_r2 != -999.0:
            results.append(result)
    
    # Save rankings
    save_rankings(results, args.output_dir)
    
    # Print summary
    logger.info("="*80)
    logger.info("TARGET PREDICTABILITY RANKINGS")
    logger.info("="*80)
    
    results = sorted(results, key=lambda x: x.composite_score, reverse=True)
    
    for i, result in enumerate(results, 1):
        logger.info(f"\n{i:2d}. {result.target_name:25s} | Score: {result.composite_score:.3f}")
        logger.info(f"    R²: {result.mean_r2:.3f} ± {result.std_r2:.3f}")
        logger.info(f"    Importance: {result.mean_importance:.2f}")
        logger.info(f"    Recommendation: {_get_recommendation(result)}")
    
    logger.info("\n" + "="*80)
    logger.info("✅ Target ranking complete!")
    logger.info(f"Results saved to: {args.output_dir}")
    logger.info("="*80)
    
    return 0


if __name__ == "__main__":
    sys.exit(main())

