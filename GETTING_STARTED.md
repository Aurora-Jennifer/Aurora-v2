# Getting Started: Complete Pipeline

**Step-by-step guide to run the complete ML pipeline with centralized configs.**

---

## Prerequisites

1. **Data Setup**
   ```bash
   # Your data should be in:
   data/data_labeled/interval=5m/
   ├── A.parquet
   ├── AAPL.parquet
   └── ... (more symbols)
   ```

2. **Python Environment**
   ```bash
   # Ensure dependencies installed
   pip install polars pandas numpy scikit-learn lightgbm xgboost tensorflow keras
   ```

3. **Verify Structure**
   ```bash
   # Check that new directories exist
   ls -d CONFIG/ DATA_PROCESSING/ TRAINING/ INFORMATION/
   ```

---

## Quick Start (5 Commands)

```bash
# 1. Verify data
python scripts/verify_setup.py

# 2. Build features for one symbol (test)
python scripts/process_single_symbol.py AAPL

# 3. Train first model (test)
python scripts/train_single_model.py AAPL lightgbm

# 4. Run full pipeline (all symbols)
bash scripts/run_full_pipeline.sh

# 5. View results
python scripts/view_results.py
```

---

## Detailed Workflow

### Step 1: Verify Your Setup

**Check data quality:**
```bash
python scripts/verify_setup.py
```

This script checks:
- ✅ Data directory exists
- ✅ Parquet files are readable
- ✅ Required columns present
- ✅ No major data quality issues

**Manual check:**
```bash
# List available symbols
ls data/data_labeled/interval=5m/*.parquet | wc -l

# Check one file
python -c "
import polars as pl
df = pl.read_parquet('data/data_labeled/interval=5m/AAPL.parquet')
print(f'Rows: {len(df):,}')
print(f'Columns: {df.columns}')
print(f'Date range: {df[\"ts\"].min()} to {df[\"ts\"].max()}')
"
```

---

### Step 2: Process Single Symbol (Test Run)

**Test the pipeline on one symbol:**
```bash
python scripts/process_single_symbol.py AAPL --verbose
```

This script:
1. ✅ Loads raw data
2. ✅ Normalizes session (RTH, grid-aligned)
3. ✅ Builds features (200+)
4. ✅ Generates targets (barrier labels)
5. ✅ Saves labeled dataset

**Output location:**
```
DATA_PROCESSING/data/labeled/AAPL_labeled.parquet
```

**Check output:**
```bash
python -c "
import polars as pl
df = pl.read_parquet('DATA_PROCESSING/data/labeled/AAPL_labeled.parquet')
print(f'Rows: {len(df):,}')
print(f'Features: {len([c for c in df.columns if not c.startswith(\"y_\")])}')
print(f'Targets: {len([c for c in df.columns if c.startswith(\"y_\")])}')
"
```

---

### Step 3: Train Single Model (Test Run)

**Train LightGBM on one symbol:**
```bash
python scripts/train_single_model.py AAPL lightgbm --variant conservative
```

This script:
1. ✅ Loads labeled data
2. ✅ Loads config from CONFIG/model_config/lightgbm.yaml
3. ✅ Splits train/validation
4. ✅ Trains with early stopping
5. ✅ Saves model + metrics

**Output location:**
```
models/AAPL_lightgbm_2025-11-13.pkl
models/AAPL_lightgbm_2025-11-13_metrics.json
```

**Check results:**
```bash
python -c "
import json
with open('models/AAPL_lightgbm_2025-11-13_metrics.json') as f:
    metrics = json.load(f)
print('Training Metrics:')
for k, v in metrics.items():
    print(f'  {k}: {v:.4f}')
"
```

---

### Step 4: Run Full Pipeline

**Process all symbols and train models:**
```bash
bash scripts/run_full_pipeline.sh
```

**What it does:**

**Phase 1: Data Processing (Parallel)**
```
For each symbol in data/data_labeled/interval=5m/:
  1. Normalize session
  2. Build features
  3. Generate targets
  → Save to DATA_PROCESSING/data/labeled/
```

**Phase 2: Model Training (Sequential)**
```
For each labeled dataset:
  For each model (lightgbm, xgboost, ensemble):
    1. Load config (conservative variant)
    2. Train with early stopping
    3. Save model + metrics
  → Save to models/
```

**Progress tracking:**
```bash
# Watch progress
tail -f logs/pipeline_2025-11-13.log
```

**Expected runtime:**
- 10 symbols: ~15 minutes
- 50 symbols: ~1 hour
- 500 symbols: ~8-10 hours

---

### Step 5: View Results

**Generate summary report:**
```bash
python scripts/view_results.py
```

**Output:**
```
╔════════════════════════════════════════════╗
║      Model Training Results Summary        ║
╚════════════════════════════════════════════╝

Models Trained: 30 (10 symbols × 3 models)

Performance by Model:
  LightGBM    - Avg Validation R²: 0.234
  XGBoost     - Avg Validation R²: 0.229
  Ensemble    - Avg Validation R²: 0.241

Top 5 Performers:
  1. AAPL + Ensemble    - R²: 0.312
  2. MSFT + LightGBM    - R²: 0.298
  3. NVDA + Ensemble    - R²: 0.287
  4. TSLA + XGBoost     - R²: 0.276
  5. GOOG + LightGBM    - R²: 0.265

Results saved to: results/summary_2025-11-13.csv
```

---

## Configuration Examples

### Use Different Variants

**Conservative (Least Overfitting):**
```bash
python scripts/train_single_model.py AAPL lightgbm --variant conservative
```

**Balanced (Default):**
```bash
python scripts/train_single_model.py AAPL lightgbm --variant balanced
```

**Aggressive (Faster Training):**
```bash
python scripts/train_single_model.py AAPL lightgbm --variant aggressive
```

### Override Specific Parameters

**Python API:**
```python
from CONFIG.config_loader import load_model_config
from TRAINING.model_fun import LightGBMTrainer

config = load_model_config("lightgbm", overrides={
    "n_estimators": 2000,
    "learning_rate": 0.02,
    "max_depth": 6
})

trainer = LightGBMTrainer(config)
```

**Or edit CONFIG/model_config/lightgbm.yaml directly:**
```yaml
variants:
  my_experiment:
    n_estimators: 2000
    learning_rate: 0.02
    max_depth: 6
```

Then use:
```bash
python scripts/train_single_model.py AAPL lightgbm --variant my_experiment
```

---

## Customizing the Pipeline

### Process Different Symbols

**Edit universe config:**
```bash
# Create config/universe.yaml
cat > config/universe.yaml << EOF
symbols:
  - AAPL
  - MSFT
  - GOOGL
  - AMZN
  - TSLA
  - NVDA
  - META
  - NFLX
  - AMD
  - INTC
EOF
```

**Run pipeline:**
```bash
bash scripts/run_full_pipeline.sh --universe config/universe.yaml
```

### Use Different Models

**Train all available models:**
```bash
python scripts/train_all_models.py AAPL
```

**Train specific models:**
```bash
python scripts/train_all_models.py AAPL --models lightgbm,xgboost,mlp,lstm
```

### Different Target Horizons

**Edit feature/target config:**
```python
# In scripts/process_single_symbol.py
targets = compute_barrier_targets(
    prices=df['close'],
    horizon_minutes=30,  # Change from 15 to 30
    barrier_size=0.5
)
```

---

## Advanced Usage

### Walk-Forward Validation

**Test model on historical data:**
```bash
python scripts/run_walkforward.py AAPL lightgbm \
    --train-days 252 \
    --test-days 63 \
    --step-days 21
```

**Output:**
```
Walk-Forward Results for AAPL (LightGBM):
  Folds: 12
  Avg Sharpe: 1.23
  Avg Max Drawdown: -8.4%
  Hit Rate: 54.3%
  Profit Factor: 1.42
```

### Feature Selection

**Select top features:**
```bash
python scripts/select_features.py AAPL \
    --method importance \
    --top-n 60
```

**Retrain with selected features:**
```bash
python scripts/train_single_model.py AAPL lightgbm \
    --feature-file DATA_PROCESSING/data/features/AAPL_top60.txt
```

### Batch Processing

**Process multiple symbols in parallel:**
```bash
parallel -j 4 python scripts/process_single_symbol.py {} ::: AAPL MSFT GOOGL AMZN
```

**Train multiple models in parallel:**
```bash
parallel -j 2 python scripts/train_single_model.py AAPL {} ::: lightgbm xgboost ensemble
```

---

## Monitoring & Logging

### Check Logs

**Pipeline logs:**
```bash
tail -f logs/pipeline_2025-11-13.log
```

**Model training logs:**
```bash
tail -f logs/training_AAPL_lightgbm.log
```

**Memory usage:**
```bash
tail -f logs/memory.log
```

### View Metrics

**TensorBoard (for deep learning models):**
```bash
tensorboard --logdir logs/tensorboard/
```

**MLflow (if configured):**
```bash
mlflow ui --port 5000
```

---

## Troubleshooting

### Data Issues

**Problem:** Missing columns in output
```bash
# Check schema
python scripts/verify_setup.py --check-schema
```

**Problem:** Memory errors
```bash
# Use streaming builder
python scripts/process_single_symbol.py AAPL --streaming
```

### Training Issues

**Problem:** Overfitting (high train, low val accuracy)
```bash
# Use conservative variant
python scripts/train_single_model.py AAPL lightgbm --variant conservative
```

**Problem:** Training too slow
```bash
# Use aggressive variant
python scripts/train_single_model.py AAPL lightgbm --variant aggressive
```

**Problem:** NaN in predictions
```bash
# Check for missing values
python scripts/check_data_quality.py AAPL
```

---

## Directory Layout After Running Pipeline

```
trader/
├── data/
│   └── data_labeled/
│       └── interval=5m/              # Original data
│
├── DATA_PROCESSING/
│   └── data/
│       ├── raw/                      # Normalized data
│       ├── processed/                # With features
│       └── labeled/                  # With targets (ready for training)
│
├── models/                           # Trained models
│   ├── AAPL_lightgbm_2025-11-13.pkl
│   ├── AAPL_xgboost_2025-11-13.pkl
│   └── ...
│
├── results/                          # Performance metrics
│   ├── summary_2025-11-13.csv
│   └── AAPL_lightgbm_metrics.json
│
└── logs/                             # All logs
    ├── pipeline_2025-11-13.log
    ├── training_AAPL_lightgbm.log
    └── memory.log
```

---

## Next Steps

1. **Experiment with variants** - Try conservative/balanced/aggressive
2. **Feature selection** - Reduce from 200+ to 50-60 best features
3. **Walk-forward validation** - Test on historical data
4. **Ensemble models** - Combine multiple model predictions
5. **Deep learning** - Try LSTM/Transformer for sequential patterns

---

## Quick Reference

### Essential Commands
```bash
# Verify setup
python scripts/verify_setup.py

# Test on one symbol
python scripts/process_single_symbol.py AAPL
python scripts/train_single_model.py AAPL lightgbm

# Run full pipeline
bash scripts/run_full_pipeline.sh

# View results
python scripts/view_results.py
```

### Essential Files
- **Configs:** `CONFIG/model_config/*.yaml`
- **Scripts:** `scripts/*.py` and `scripts/*.sh`
- **Logs:** `logs/*.log`
- **Results:** `results/*.csv` and `models/*.pkl`

### Documentation
- **Overview:** `INFORMATION/07_PROJECT_OVERVIEW.md`
- **Data Pipeline:** `INFORMATION/04_DATA_PIPELINE.md`
- **Model Training:** `INFORMATION/05_MODEL_TRAINING.md`
- **Column Reference:** `INFORMATION/06_COLUMN_REFERENCE.md`

---

**Ready to start? Run:** `python scripts/verify_setup.py`

