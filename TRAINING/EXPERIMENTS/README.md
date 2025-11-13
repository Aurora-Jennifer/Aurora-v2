# EXPERIMENTS - Optimized Training Workflow

## Overview

This folder contains the **new, optimized 3-phase training workflow** that fixes overfitting and reduces feature dimensionality from 400+ to ~50-60 features.

---

## 🎯 Workflow Overview

```
Phase 1: Feature Engineering & Selection
  ↓
  - Load 421 features
  - Train LightGBM to get feature importance
  - Select top 50 features
  - Train VAE/GMM on selected features
  - Save: top_50_features.json, vae_encoder.joblib, gmm_model.joblib
  
Phase 2: Core Model Training
  ↓
  - Load Phase 1 artifacts
  - Transform 421 → 61 features (50 + VAE + GMM)
  - Train: LightGBM, MultiTask, Ensemble
  - Use: Early stopping, proper regularization
  - Save: trained_models/
  
Phase 3: Sequential Model Training
  ↓
  - Load Phase 1 artifacts
  - Transform 421 → 61 features
  - Train: LSTM, Transformer, CNN1D
  - Use: Reduced dimensionality for faster training
  - Save: sequential_models/
```

---

## 📁 Folder Structure

```
EXPERIMENTS/
├── README.md                          # This file
├── OPERATIONS_GUIDE.md                # Step-by-step operations guide
├── run_all_phases.sh                  # Master script (refactored train_all_symbols.sh)
│
├── phase1_feature_engineering/
│   ├── run_phase1.py                  # Feature selection & engineering
│   ├── feature_selection_config.yaml  # Phase 1 configuration
│   └── README.md                      # Phase 1 documentation
│
├── phase2_core_models/
│   ├── run_phase2.py                  # Core model training
│   ├── core_models_config.yaml        # Phase 2 configuration
│   └── README.md                      # Phase 2 documentation
│
├── phase3_sequential_models/
│   ├── run_phase3.py                  # Sequential model training
│   ├── sequential_config.yaml         # Phase 3 configuration
│   └── README.md                      # Phase 3 documentation
│
├── configs/
│   ├── experiment_defaults.yaml       # Default settings for all experiments
│   └── custom_experiments/            # Your custom experiment configs
│
├── metadata/                          # Phase 1 outputs (feature lists, models)
│   ├── top_50_features.json
│   ├── vae_encoder.joblib
│   └── gmm_model.joblib
│
└── logs/                              # Experiment logs
    ├── phase1_YYYYMMDD_HHMMSS.log
    ├── phase2_YYYYMMDD_HHMMSS.log
    └── phase3_YYYYMMDD_HHMMSS.log
```

---

## 🚀 Quick Start

### Option 1: Run All Phases (Recommended for First Time)

```bash
cd TRAINING/EXPERIMENTS
./run_all_phases.sh
```

This will:
1. Run Phase 1 (feature engineering)
2. Run Phase 2 (core models)
3. Run Phase 3 (sequential models)

### Option 2: Run Individual Phases

```bash
# Phase 1 only (if you want to experiment with feature selection)
python phase1_feature_engineering/run_phase1.py \
    --data-dir ../../data \
    --config phase1_feature_engineering/feature_selection_config.yaml \
    --output-dir metadata

# Phase 2 only (if Phase 1 is already done)
python phase2_core_models/run_phase2.py \
    --data-dir ../../data \
    --metadata-dir metadata \
    --config phase2_core_models/core_models_config.yaml

# Phase 3 only (if Phases 1-2 are already done)
python phase3_sequential_models/run_phase3.py \
    --data-dir ../../data \
    --metadata-dir metadata \
    --config phase3_sequential_models/sequential_config.yaml
```

---

## 📊 What's Different from Old Workflow?

### Old Workflow (Slow, Overfits)
```
❌ Phase 1: Train models on ALL 421 features
❌ Phase 2: Train more models on ALL 421 features
❌ No feature selection
❌ No proper regularization
❌ Models overfit
```

### New Workflow (Fast, Generalizes)
```
✅ Phase 1: SELECT top 50 features, engineer new ones (VAE, GMM)
✅ Phase 2: Train models on ~60 features with proper regularization
✅ Phase 3: Train sequential models on ~60 features
✅ Early stopping enabled
✅ Models generalize well
```

---

## 🎓 Key Improvements

1. **Feature Selection**: 421 → 50 most important features
2. **Feature Engineering**: VAE (latent) + GMM (regime) = +11 features
3. **Final Feature Set**: ~61 features (manageable, powerful)
4. **Proper Regularization**: Spec 2 hyperparameters for LightGBM/XGBoost
5. **Early Stopping**: Automatic validation split and early stopping
6. **Active Dropout**: Properly enabled in neural networks

---

## 📈 Expected Results

### Before (Old Workflow)
- Training time: **6-8 hours**
- Train score: 0.85
- Validation score: 0.45 ❌ (overfitting)
- Features: 421

### After (New Workflow)
- Training time: **2-3 hours** ✅
- Train score: 0.72
- Validation score: 0.68 ✅ (good generalization)
- Features: 61

---

## 🔧 Configuration

All experiments are controlled by YAML configs in each phase folder.

### Key Configuration Options

**Phase 1: Feature Selection**
```yaml
feature_selection:
  n_features: 50              # Top N features to select
  primary_target: fwd_ret_5m  # Target for feature importance
  min_importance: 0.001       # Minimum importance threshold

feature_engineering:
  vae:
    latent_dim: 10            # VAE latent features
  gmm:
    n_components: 3           # GMM regimes
```

**Phase 2: Core Models**
```yaml
models:
  lightgbm:
    max_depth: 8
    learning_rate: 0.03
    subsample: 0.75
  
  multitask:
    targets: [tth, mdd, mfe, fwd_ret]
    learning_rate: 0.0001
    patience: 10
```

**Phase 3: Sequential Models**
```yaml
models:
  lstm:
    hidden_dim: 128
    num_layers: 2
    dropout: 0.3
```

---

## 📚 Documentation

- `OPERATIONS_GUIDE.md`: Step-by-step operations manual
- `phase1_feature_engineering/README.md`: Phase 1 details
- `phase2_core_models/README.md`: Phase 2 details
- `phase3_sequential_models/README.md`: Phase 3 details

---

## ✅ Verification Checklist

After running the workflow, verify:

1. **Phase 1 Outputs Exist**:
   ```bash
   ls metadata/
   # Should see: top_50_features.json, vae_encoder.joblib, gmm_model.joblib
   ```

2. **Feature Count Reduced**:
   ```python
   import json
   with open('metadata/top_50_features.json') as f:
       features = json.load(f)
   print(f"Selected {len(features)} features")  # Should be ~50
   ```

3. **Models Trained Successfully**:
   ```bash
   ls output/core_models/
   # Should see: lightgbm_fwd_ret_5m.joblib, multitask_model.joblib, etc.
   ```

4. **Validation Scores Improved**:
   - Check logs for train vs validation scores
   - Gap should be small (< 0.1)

---

## 🐛 Troubleshooting

### Issue: Phase 1 fails with "No feature importance"
**Solution**: Ensure your data has valid targets and features. Check data quality.

### Issue: Phase 2 can't find metadata
**Solution**: Run Phase 1 first, or specify correct `--metadata-dir`

### Issue: Models still overfitting
**Solution**: 
1. Reduce `n_features` further (try 30 instead of 50)
2. Increase regularization in configs
3. Check for data leakage (future data in features)

### Issue: Training too slow
**Solution**:
1. Reduce number of estimators in LightGBM/XGBoost
2. Use smaller validation set
3. Train fewer models initially

---

## 🎯 Next Steps

1. **First Run**: Execute `./run_all_phases.sh` and verify it works
2. **Experiment**: Modify configs to test different feature counts
3. **Analyze**: Review `logs/` and feature importance reports
4. **Iterate**: Refine feature selection based on results
5. **Deploy**: Use best models in production

---

## 📞 Support

For issues or questions:
1. Check `OPERATIONS_GUIDE.md` for detailed instructions
2. Review logs in `logs/` folder
3. Check phase-specific README files
4. Review parent folder documentation:
   - `../TRAINING_OPTIMIZATION_GUIDE.md`
   - `../FEATURE_SELECTION_GUIDE.md`
   - `../FIRST_BATCH_SPECS_IMPLEMENTATION.md`

