# Feature Selection Config Quick Reference

## Files Overview

| File | Purpose | Edit When |
|------|---------|-----------|
| `CONFIG/feature_selection_config.yaml` | LightGBM params, defaults, paths | Change training behavior |
| `CONFIG/target_configs.yaml` | Target definitions, enable/disable | Add/remove prediction targets |
| `CONFIG/feature_groups.yaml` | Feature family definitions | Group new feature types |

## Common Tasks

### Quick Test (Faster Training)
```yaml
# Edit CONFIG/feature_selection_config.yaml
lightgbm:
  n_estimators: 100      # ↓ from 500
  learning_rate: 0.1     # ↑ from 0.05
```

### Production (More Stable)
```yaml
# Edit CONFIG/feature_selection_config.yaml
lightgbm:
  n_estimators: 1000     # ↑ from 500
  learning_rate: 0.03    # ↓ from 0.05
  subsample: 0.7         # ↓ from 0.8
```

### Change Default Target
```yaml
# Edit CONFIG/feature_selection_config.yaml
defaults:
  target_column: "y_will_valley_60m_0.8"  # was peak, now valley
```

### Enable/Disable Targets
```yaml
# Edit CONFIG/target_configs.yaml
targets:
  peak_30m:
    enabled: true     # Turn on
  
  swing_high_15m:
    enabled: false    # Turn off
```

### Add New Target
```yaml
# Edit CONFIG/target_configs.yaml
targets:
  my_new_target:
    target_column: "y_my_prediction"
    description: "What it predicts"
    use_case: "When to use it"
    top_n: 60
    method: "mean"
    enabled: true
```

### Change Feature Count
```yaml
# Edit CONFIG/feature_selection_config.yaml
defaults:
  top_n: 100    # was 60
```

### Use Custom Config
```bash
# Copy and edit
cp CONFIG/feature_selection_config.yaml my_config.yaml
vim my_config.yaml

# Use it
python scripts/select_features.py --config my_config.yaml
```

## Override from CLI (Quick Test)

```bash
# Override single values without editing config
python scripts/select_features.py --top-n 100
python scripts/select_features.py --num-workers 4
python scripts/select_features.py --method median
python scripts/select_features.py --target-column y_will_valley_60m_0.8
```

## Key Parameters Explained

| Parameter | Default | Fast | Stable | Purpose |
|-----------|---------|------|--------|---------|
| `n_estimators` | 500 | 100 | 1000 | Training iterations |
| `learning_rate` | 0.05 | 0.1 | 0.03 | Step size |
| `subsample` | 0.8 | 0.5 | 0.7 | Row sampling |
| `top_n` | 60 | 30 | 100 | Features to select |

## See Also
- `INFORMATION/08_FEATURE_SELECTION.md` - Full guide
- `CONFIG/README.md` - Config usage
- `CONFIG/feature_selection_config.yaml` - Main config (well commented)

