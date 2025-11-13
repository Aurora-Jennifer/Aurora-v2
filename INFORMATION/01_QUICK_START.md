# Quick Start: Centralized Configurations

**All 17 production trainers now auto-load configs from `CONFIG/model_config/` - no more hardcoded settings!**

---

## Basic Usage

### Option 1: Auto-Load (Simplest)
```python
trainer = LightGBMTrainer()  # Automatically loads CONFIG/model_config/lightgbm.yaml
trainer.train(X, y)
```

### Option 2: Use Variant
```python
from CONFIG.config_loader import load_model_config

config = load_model_config("xgboost", variant="conservative")
trainer = XGBoostTrainer(config)
```

### Option 3: Override Parameters
```python
config = load_model_config("mlp", overrides={"epochs": 100, "learning_rate": 0.0001})
trainer = MLPTrainer(config)
```

---

## Available Models

**Core (Spec 1/2/3):** `lightgbm`, `xgboost`, `ensemble`, `multi_task`  
**Deep Learning:** `mlp`, `transformer`, `lstm`, `cnn1d`  
**Feature Engineering:** `vae`, `gan`, `gmm_regime`  
**Probabilistic:** `ngboost`, `quantile_lightgbm`  
**Advanced:** `change_point`, `ftrl_proximal`, `reward_based`, `meta_learning`

---

## Configuration Variants

Each model has 3 variants:
- **`conservative`** - Highest regularization, least overfitting
- **`balanced`** - Default, good starting point
- **`aggressive`** - Faster training, lower regularization

```python
config = load_model_config("lightgbm", variant="conservative")
```

---

## Common Overrides

### Tree Models
```python
config = load_model_config("lightgbm", overrides={
    "n_estimators": 2000,
    "learning_rate": 0.01,
    "max_depth": 5
})
```

### Neural Networks
```python
config = load_model_config("mlp", overrides={
    "epochs": 100,
    "batch_size": 256,
    "dropout": 0.3
})
```

---

## Config Files Location

All configs: **`CONFIG/model_config/`**

To change settings, just edit the YAML file - no Python code changes needed!

---

## Troubleshooting

```python
# Check available configs
from CONFIG.config_loader import get_available_model_configs
print(get_available_model_configs())

# See current config
trainer = LightGBMTrainer()
print(trainer.config)
```

