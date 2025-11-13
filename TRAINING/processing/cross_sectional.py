"""
Cross-Sectional Processing - Mega Script Integration
Implements time-aware cross-sectional normalization and validation.
"""

import numpy as np
import pandas as pd
import logging
from typing import Dict, Any, Tuple, Optional, List
from sklearn.model_selection import GroupKFold
from sklearn.preprocessing import StandardScaler

logger = logging.getLogger(__name__)

class CrossSectionalProcessor:
    """Cross-sectional processing for time-aware machine learning."""
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        self.config = config or {}
        self.normalize_features = self.config.get('normalize_features', True)
        self.normalize_targets = self.config.get('normalize_targets', False)
        self.group_by_time = self.config.get('group_by_time', True)
        self.min_group_size = self.config.get('min_group_size', 10)
        
    def normalize_cross_sectional(self, X: np.ndarray, y: np.ndarray, 
                                timestamps: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        """Apply cross-sectional normalization (mega script approach)."""
        
        logger.info(f"🔧 Applying cross-sectional normalization to {len(X)} samples")
        
        # Group by timestamp for cross-sectional processing
        unique_timestamps = np.unique(timestamps)
        X_normalized = X.copy()
        y_normalized = y.copy()
        
        for timestamp in unique_timestamps:
            # Get indices for this timestamp
            mask = timestamps == timestamp
            if mask.sum() < self.min_group_size:
                continue
                
            # Normalize features cross-sectionally
            if self.normalize_features:
                X_normalized[mask] = self._normalize_group(X[mask])
                
            # Normalize targets cross-sectionally (if enabled)
            if self.normalize_targets:
                y_normalized[mask] = self._normalize_group(y[mask])
        
        logger.info(f"✅ Cross-sectional normalization complete")
        return X_normalized, y_normalized
    
    def _normalize_group(self, data: np.ndarray) -> np.ndarray:
        """Normalize a group of data (cross-sectional)."""
        if len(data) == 0:
            return data
            
        # Z-score normalization
        mean = np.mean(data, axis=0)
        std = np.std(data, axis=0)
        
        # Avoid division by zero
        std = np.where(std == 0, 1.0, std)
        
        return (data - mean) / std
    
    def create_time_aware_splits(self, X: np.ndarray, y: np.ndarray, 
                                timestamps: np.ndarray, 
                                test_size: float = 0.2) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
        """Create time-aware train/validation splits (mega script approach)."""
        
        logger.info(f"🔧 Creating time-aware splits for {len(X)} samples")
        
        # Sort by timestamp to ensure temporal order
        sort_indices = np.argsort(timestamps)
        X_sorted = X[sort_indices]
        y_sorted = y[sort_indices]
        timestamps_sorted = timestamps[sort_indices]
        
        # Find split point that maintains temporal order
        split_idx = int(len(X_sorted) * (1 - test_size))
        
        X_train = X_sorted[:split_idx]
        y_train = y_sorted[:split_idx]
        X_val = X_sorted[split_idx:]
        y_val = y_sorted[split_idx:]
        
        logger.info(f"✅ Time-aware splits: {len(X_train)} train, {len(X_val)} validation")
        return X_train, X_val, y_train, y_val
    
    def create_group_splits(self, X: np.ndarray, y: np.ndarray, 
                           timestamps: np.ndarray, 
                           n_splits: int = 5) -> List[Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]]:
        """Create group-based cross-validation splits (mega script approach)."""
        
        logger.info(f"🔧 Creating group-based CV splits for {len(X)} samples")
        
        # Create groups based on timestamps
        unique_timestamps = np.unique(timestamps)
        groups = np.zeros(len(X), dtype=int)
        
        for i, timestamp in enumerate(unique_timestamps):
            groups[timestamps == timestamp] = i
        
        # Use GroupKFold for time-aware splits
        group_kfold = GroupKFold(n_splits=n_splits)
        splits = []
        
        for train_idx, val_idx in group_kfold.split(X, y, groups):
            X_train, X_val = X[train_idx], X[val_idx]
            y_train, y_val = y[train_idx], y[val_idx]
            splits.append((X_train, X_val, y_train, y_val))
        
        logger.info(f"✅ Created {len(splits)} group-based CV splits")
        return splits
    
    def apply_cross_sectional_validation(self, X: np.ndarray, y: np.ndarray, 
                                       timestamps: np.ndarray,
                                       model, n_splits: int = 5) -> Dict[str, float]:
        """Apply cross-sectional validation (mega script approach)."""
        
        logger.info(f"🔧 Applying cross-sectional validation with {n_splits} splits")
        
        splits = self.create_group_splits(X, y, timestamps, n_splits)
        scores = []
        
        for i, (X_train, X_val, y_train, y_val) in enumerate(splits):
            # Train model on this split
            model.fit(X_train, y_train)
            
            # Evaluate on validation set
            y_pred = model.predict(X_val)
            
            # Calculate score (MSE for regression)
            mse = np.mean((y_val - y_pred) ** 2)
            scores.append(mse)
            
            logger.info(f"Split {i+1}/{n_splits}: MSE = {mse:.6f}")
        
        # Calculate statistics
        mean_score = np.mean(scores)
        std_score = np.std(scores)
        
        results = {
            'mean_score': mean_score,
            'std_score': std_score,
            'scores': scores
        }
        
        logger.info(f"✅ Cross-sectional validation: {mean_score:.6f} ± {std_score:.6f}")
        return results
    
    def get_cross_sectional_stats(self, X: np.ndarray, y: np.ndarray, 
                                 timestamps: np.ndarray) -> Dict[str, Any]:
        """Get cross-sectional statistics."""
        
        unique_timestamps = np.unique(timestamps)
        
        stats = {
            'total_samples': len(X),
            'unique_timestamps': len(unique_timestamps),
            'samples_per_timestamp': len(X) / len(unique_timestamps),
            'timestamp_range': (timestamps.min(), timestamps.max()),
            'feature_stats': {
                'mean': np.mean(X, axis=0),
                'std': np.std(X, axis=0),
                'min': np.min(X, axis=0),
                'max': np.max(X, axis=0)
            },
            'target_stats': {
                'mean': np.mean(y),
                'std': np.std(y),
                'min': np.min(y),
                'max': np.max(y)
            }
        }
        
        return stats
