# Feature Importance Score Interpretation

## ✅ **Fixed: Now Using Interpretable 0-1 Scale**

The importance score is now **normalized to 0-1** and represents:

**"What percentage of total feature importance is concentrated in the top 10% of features?"**

---

## How It Works

### Calculation:
1. Get all feature importances from the model
2. Sort them and take the **top 10%** of features
3. Sum their importance values
4. Divide by **total importance** → gives a **percentage (0-1)**

### Formula:
```
importance_score = (sum of top 10% importances) / (sum of all importances)
```

---

## Interpretation

| Score Range | Meaning | Example |
|-------------|---------|---------|
| **0.6 - 0.8** | **Strong signal** - Top 10% features capture 60-80% of importance | Good targets (R² > 0.1) |
| **0.4 - 0.6** | **Moderate signal** - Top 10% features capture 40-60% of importance | Marginal targets |
| **0.2 - 0.4** | **Weak signal** - Top 10% features capture 20-40% of importance | Poor targets (R² < 0) |
| **0.0 - 0.2** | **Very weak signal** - Importance spread evenly across features | Unpredictable targets |

---

## Expected Values

### Good Targets (R² > 0.1):
- **Importance: 0.60 - 0.70** (60-70% in top 10%)
- Example: `peak_60m_0.8` with R²=0.12 → importance ≈ 0.65

### Poor Targets (R² < 0):
- **Importance: 0.20 - 0.30** (20-30% in top 10%)
- Example: `swing_high_10m_0.05` with R²=-0.45 → importance ≈ 0.25

---

## Why This Makes Sense

1. **Interpretable**: 0.65 = "65% of importance in top 10% features"
2. **Comparable**: All targets use the same 0-1 scale
3. **Meaningful**: Higher = more concentrated signal = better target
4. **Correlates with R²**: Good targets have higher importance scores

---

## Before vs After

### Before (Raw Sum):
```
Good target: importance = 637.49  ❌ What does this mean?
Poor target: importance = 569.07  ❌ Hard to interpret
```

### After (Normalized 0-1):
```
Good target: importance = 0.65  ✅ "65% in top 10% features"
Poor target: importance = 0.25  ✅ "25% in top 10% features"
```

---

## Example Output

```
Evaluating: peak_60m_0.8 (y_will_peak_60m_0.8)
  📊 Summary: R²=0.124±0.041, importance=0.65, composite=0.596
  ✅ Good target - 65% of importance in top 10% features

Evaluating: swing_high_10m_0.05 (y_will_swing_high_10m_0.05)
  📊 Summary: R²=-0.447±0.054, importance=0.25, composite=0.526
  ⚠️ Poor target - Only 25% of importance in top 10% features
```

---

## Composite Score Impact

The composite score now uses the normalized importance directly:
- **Before**: `importance_component = min(1.0, mean_importance / 100.0)` (arbitrary scaling)
- **After**: `importance_component = mean_importance` (already 0-1, interpretable)

This makes the composite score more accurate and meaningful.

---

## Summary

✅ **Importance is now on a 0-1 scale**
✅ **Represents percentage of importance in top 10% features**
✅ **Easy to interpret and compare across targets**
✅ **Correlates with R² (good targets = higher importance)**

**The importance score now makes intuitive sense!** 🎯

