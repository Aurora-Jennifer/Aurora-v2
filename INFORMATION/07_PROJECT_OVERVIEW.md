# Project Overview

**High-level overview of the complete trading ML pipeline.**

---

## Purpose

Build machine learning models to predict short-term market movements for systematic trading strategies.

**Focus:** Intraday prediction (5m-2h horizons) using barrier labels and excess returns.

---

## Architecture

```
Raw Market Data
    ↓
DATA_PROCESSING → Features + Targets
    ↓
TRAINING → Trained Models
    ↓
Strategies (Future) → Trading Signals
    ↓
Execution (Future) → Orders
```

---

## Directory Structure

```
trader/
│
├── CONFIG/                        # Centralized configurations
│   ├── model_config/             # Model hyperparameters (17 models)
│   ├── training_config/          # Training workflows
│   └── config_loader.py          # Config loading utility
│
├── DATA_PROCESSING/              # Data pipeline
│   ├── features/                 # Feature engineering
│   ├── targets/                  # Target generation
│   ├── pipeline/                 # Processing workflows
│   ├── utils/                    # Utilities
│   └── data/                     # Data storage
│
├── TRAINING/                     # Model training
│   ├── model_fun/                # 17+ model trainers
│   ├── strategies/               # Training strategies
│   ├── walkforward/              # Walk-forward validation
│   ├── memory/                   # Memory management
│   └── EXPERIMENTS/              # Experimental workflows
│
├── INFORMATION/                  # Documentation
│   ├── 01_QUICK_START.md        # Config quick start
│   ├── 02_CONFIG_REFERENCE.md   # Config reference
│   ├── 03_MIGRATION_NOTES.md    # Migration details
│   ├── 04_DATA_PIPELINE.md      # Data workflow
│   ├── 05_MODEL_TRAINING.md     # Training guide
│   ├── 06_COLUMN_REFERENCE.md   # Column docs
│   └── 07_PROJECT_OVERVIEW.md   # This file
│
└── data/                         # Primary data directory
    └── data_labeled/             # Labeled datasets
        └── interval=5m/          # 5-minute bars
            ├── A.parquet
            ├── AAPL.parquet
            └── ...
```

---

## Workflow

### 1. Data Acquisition
**Input:** Raw OHLCV data (5-minute bars, NYSE RTH)  
**Output:** Cleaned, normalized session data

```
data/data_labeled/interval=5m/*.parquet
    ↓
[Normalize session]
    ↓
DATA_PROCESSING/data/raw/
```

### 2. Feature Engineering
**Input:** Normalized OHLCV  
**Output:** 200+ engineered features

```
[Feature builders]
    ↓
Returns, volatility, momentum, technical indicators
    ↓
DATA_PROCESSING/data/processed/
```

### 3. Target Generation
**Input:** Processed features  
**Output:** Prediction labels

```
[Target generators]
    ↓
Barrier labels, excess returns, HFT forward returns
    ↓
DATA_PROCESSING/data/labeled/
```

### 4. Model Training
**Input:** Labeled datasets  
**Output:** Trained models

```
[Training strategies]
    ↓
LightGBM, XGBoost, Ensemble, MultiTask, Deep Learning
    ↓
models/*.pkl + configs
```

### 5. Evaluation
**Input:** Trained models  
**Output:** Performance metrics

```
[Walk-forward validation]
    ↓
Sharpe, drawdown, hit rate, profit factor
    ↓
results/
```

---

## Key Components

### CONFIG (Centralized Configuration)
**Purpose:** No more hardcoded settings!

**Features:**
- 17 model configs with 3 variants each (conservative/balanced/aggressive)
- Runtime overrides
- Environment variable support
- Version control friendly

**Usage:**
```python
from CONFIG.config_loader import load_model_config

config = load_model_config("lightgbm", variant="conservative")
trainer = LightGBMTrainer(config)
```

### DATA_PROCESSING (ETL Pipeline)
**Purpose:** Transform raw data into ML-ready features

**Modules:**
- **features/**: 3 feature builders (simple, comprehensive, streaming)
- **targets/**: 3 target types (barrier, excess returns, HFT)
- **pipeline/**: End-to-end workflows (normalization, batch processing)
- **utils/**: Memory management, logging, validation

**Usage:**
```python
from DATA_PROCESSING.features import ComprehensiveFeatureBuilder
from DATA_PROCESSING.targets import compute_barrier_targets

builder = ComprehensiveFeatureBuilder(config_path="config/features.yaml")
features = builder.build_features(input_paths, output_dir, universe_config)

targets = compute_barrier_targets(prices=df['close'], horizon_minutes=15)
```

### TRAINING (Model Training)
**Purpose:** Train 17+ models on labeled data

**Available Models:**
- **Core:** LightGBM, XGBoost, Ensemble, MultiTask
- **Deep Learning:** MLP, Transformer, LSTM, CNN1D
- **Feature Engineering:** VAE, GAN, GMMRegime
- **Probabilistic:** NGBoost, QuantileLightGBM
- **Advanced:** ChangePoint, FTRL, RewardBased, MetaLearning

**Training Strategies:**
- **SingleTask:** One model per target
- **MultiTask:** Shared model for correlated targets
- **Cascade:** Sequential dependencies

**Usage:**
```python
from TRAINING.model_fun import LightGBMTrainer
from CONFIG.config_loader import load_model_config

config = load_model_config("lightgbm", variant="conservative")
trainer = LightGBMTrainer(config)
trainer.train(X_train, y_train, X_val, y_val)
```

---

## Configuration Philosophy

### Centralized vs Hardcoded

**Before (Bad):**
```python
class LightGBMTrainer:
    def __init__(self):
        self.n_estimators = 1500  # Hardcoded!
        self.learning_rate = 0.03  # Hardcoded!
        self.max_depth = 5         # Hardcoded!
```

**After (Good):**
```python
class LightGBMTrainer:
    def __init__(self, config=None):
        if config is None:
            config = load_model_config("lightgbm")  # Loads from CONFIG/
        self.config = config
```

**Benefits:**
- ✅ Change configs without editing code
- ✅ Version control configs separately
- ✅ Easy experimentation
- ✅ Reproducibility

---

## Data Schema

### Labeled Dataset Structure

**OHLCV (6 columns):**
- `ts`, `open`, `high`, `low`, `close`, `volume`

**Features (~200 columns):**
- Returns: `ret_1m`, `ret_5m`, ...
- Volatility: `vol_5m`, `vol_15m`, ...
- Technical: `sma_*`, `ema_*`, `rsi_*`, ...
- Custom: Cross-sectional, interactions

**Targets (~20+ columns):**
- Barrier: `y_will_peak`, `y_will_valley`, `y_first_touch`
- Probabilities: `p_up`, `p_down`
- Excess Returns: `excess_ret_5d`, `y_class`
- HFT: `fwd_ret_15m`, `fwd_ret_30m`, ...

See `06_COLUMN_REFERENCE.md` for complete documentation.

---

## Training Philosophy

### Prevent Overfitting
1. **High regularization** (conservative variant)
2. **Early stopping** (monitor validation)
3. **Feature selection** (top 50-60 features)
4. **Walk-forward validation** (simulate real trading)

### Model Selection
1. **Start simple** - LightGBM/XGBoost first
2. **Ensemble** - Combine diverse models
3. **Deep learning** - For sequential patterns
4. **Specialized** - NGBoost for uncertainty, VAE for features

### Hyperparameter Tuning
1. **Use variants** - Conservative/Balanced/Aggressive presets
2. **Manual tuning** - Edit YAML configs
3. **Grid search** - If needed (expensive)

---

## Best Practices

### Data Processing
1. ✅ Always normalize sessions (RTH only, grid-aligned)
2. ✅ Validate schema before processing
3. ✅ Use streaming builder for large datasets
4. ✅ Check memory usage regularly
5. ✅ Save intermediate stages (raw → processed → labeled)

### Training
1. ✅ Load configs from CONFIG/
2. ✅ Enable early stopping
3. ✅ Track feature importance
4. ✅ Use walk-forward validation
5. ✅ Save model + config together

### Experimentation
1. ✅ Create custom variants in CONFIG files
2. ✅ Use runtime overrides for quick tests
3. ✅ Log all experiments
4. ✅ Compare metrics systematically

---

## Common Tasks

### Add New Feature
1. Edit `DATA_PROCESSING/features/simple_features.py`
2. Add to feature definitions dict
3. Rerun feature builder
4. Validate output

### Add New Target
1. Edit `DATA_PROCESSING/targets/barrier.py` (or create new)
2. Define target function
3. Update `targets/__init__.py`
4. Rerun target generation

### Add New Model
1. Create trainer in `TRAINING/model_fun/`
2. Create config in `CONFIG/model_config/`
3. Update `TRAINING/model_fun/__init__.py`
4. Test with small dataset

### Run Experiment
1. Create variant in config YAML
2. Load config with variant name
3. Train model
4. Compare metrics to baseline

---

## Performance Metrics

### Model Evaluation
- **MSE/RMSE** - Regression error
- **R²** - Variance explained
- **Classification metrics** - Accuracy, precision, recall, F1

### Trading Simulation
- **Sharpe Ratio** - Risk-adjusted returns
- **Max Drawdown** - Worst decline
- **Hit Rate** - % correct predictions
- **Profit Factor** - Gross profit / loss
- **Win/Loss Ratio** - Avg win / avg loss

---

## Next Steps for Fresh Start

### 1. Verify Data Setup
```bash
# Check data directory
ls data/data_labeled/interval=5m/

# Verify schema
python -c "import polars as pl; df = pl.read_parquet('data/data_labeled/interval=5m/AAPL.parquet'); print(df.columns)"
```

### 2. Run Data Pipeline
```bash
# Normalize and build features
python DATA_PROCESSING/features/comprehensive_builder.py \
    --config config/features.yaml \
    --output-dir DATA_PROCESSING/data/processed/

# Generate targets
python DATA_PROCESSING/pipeline/barrier_pipeline.py \
    --input-dir data/data_labeled/interval=5m/ \
    --output-dir DATA_PROCESSING/data/labeled/
```

### 3. Train First Model
```python
from TRAINING.model_fun import LightGBMTrainer
from CONFIG.config_loader import load_model_config
import polars as pl

# Load data
df = pl.read_parquet("DATA_PROCESSING/data/labeled/AAPL_labeled.parquet")

# Prepare features and targets
feature_cols = [col for col in df.columns if not col.startswith('y_') and col not in ['ts', 'symbol']]
X = df[feature_cols].to_pandas()
y = df['y_will_peak'].to_pandas()

# Load conservative config
config = load_model_config("lightgbm", variant="conservative")

# Train
trainer = LightGBMTrainer(config)
trainer.train(X, y)

# Evaluate
importance = trainer.get_feature_importance()
print(importance.head(20))
```

### 4. Validate with Walk-Forward
```python
from TRAINING.walkforward import WalkForwardEngine

engine = WalkForwardEngine(
    data=df,
    train_days=252,
    test_days=63,
    step_days=21
)

results = engine.run(
    model_name="lightgbm",
    config=config,
    metrics=["sharpe", "max_drawdown", "hit_rate"]
)
```

---

## Documentation Navigation

- **01_QUICK_START.md** - Quick config reference
- **02_CONFIG_REFERENCE.md** - Complete config API
- **03_MIGRATION_NOTES.md** - Migration details
- **04_DATA_PIPELINE.md** - Data processing workflow
- **05_MODEL_TRAINING.md** - Training guide
- **06_COLUMN_REFERENCE.md** - Column documentation
- **07_PROJECT_OVERVIEW.md** - This file

---

## Support

For questions or issues:
1. Check relevant INFORMATION/ docs
2. Review CONFIG/ for configuration options
3. Examine DATA_PROCESSING/ or TRAINING/ code
4. Check existing experiments in TRAINING/EXPERIMENTS/

---

**Project Status:** ✅ Production-ready pipeline with centralized configs

**Last Updated:** November 13, 2025

