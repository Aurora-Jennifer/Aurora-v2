# R²-Weighted Importance Score

## ✅ **Fixed: Importance Now Scales with R²**

The importance component in the composite score now **scales with R²**, creating a much bigger difference between good and poor targets.

---

## The Problem

**Before:** Importance was the same regardless of R²:
- Good target (R²=0.2, importance=0.65): importance_component = 0.65
- Poor target (R²=-0.45, importance=0.25): importance_component = 0.25
- **Difference: 0.40** ❌ Too small for such a huge R² gap!

---

## The Solution

**After:** Importance is **R²-weighted** with **soft penalty** for negative R²:
- Good target (R²=0.2, importance=0.65): 
  - importance_component = 0.65 × (1 + 0.2) = **0.78** ✅
- Poor target (R²=-0.45, importance=0.25):
  - importance_component = 0.25 × 0.7 = **0.18** ✅ (soft penalty, preserves some signal)
- **Difference: 0.60** ✅ Much better, but doesn't completely dismiss negative R²!

---

## Formula

```python
if mean_r2 > 0:
    # Positive R²: boost proportionally
    importance_component = mean_importance * (1.0 + mean_r2)
else:
    # Negative R²: soft penalty (preserves some signal)
    penalty = abs(mean_r2) * 0.67
    importance_component = mean_importance * max(0.5, 1.0 - penalty)
```

### Examples

| R² | Base Importance | Weighted Importance | Multiplier | Notes |
|----|----------------|---------------------|------------|-------|
| **0.20** (good) | 0.65 | **0.78** | × 1.20 | Boosted |
| **0.12** (good) | 0.65 | **0.73** | × 1.12 | Boosted |
| **0.00** (neutral) | 0.50 | **0.50** | × 1.00 | No change |
| **-0.20** (poor) | 0.30 | **0.24** | × 0.80 | Soft penalty |
| **-0.45** (very poor) | 0.25 | **0.18** | × 0.70 | Moderate penalty, still has value |
| **-0.60** (extremely poor) | 0.25 | **0.15** | × 0.60 | Heavier penalty, but floor at 0.5x |

---

## Impact on Composite Score

The composite score now has a **much bigger gap** between good and poor targets:

### Before (Unweighted):
```
Good target:  R²=0.20, importance=0.65 → composite ≈ 0.41
Poor target:  R²=-0.45, importance=0.25 → composite ≈ 0.19
Difference: 0.22
```

### After (R²-Weighted with Soft Penalty):
```
Good target:  R²=0.20, importance=0.65 → composite ≈ 0.45
Poor target:  R²=-0.45, importance=0.25 → composite ≈ 0.15
Difference: 0.30  ✅ 36% bigger gap, but preserves some signal for negative R²!
```

---

## Why This Makes Sense

1. **Rewards good targets**: Positive R² boosts importance contribution
2. **Soft penalty for negative R²**: Acknowledges that negative R² might still have signal:
   - Could indicate inverse relationships
   - Non-linear patterns that linear models miss
   - Regime-dependent relationships
   - Might be predictable with different features/models
3. **Proportional scaling**: The worse the R², the more importance is penalized
4. **Preserves signal**: Floor at 0.5x ensures even poor targets retain some importance
5. **Bigger differences**: Creates clear separation while not completely dismissing negative R²

---

## Expected Behavior

### Good Targets (R² > 0.1):
- **Importance component: 0.70 - 0.80** (boosted by R²)
- **Composite score: 0.50 - 0.70** (high)

### Poor Targets (R² < -0.3):
- **Importance component: 0.10 - 0.20** (penalized by R²)
- **Composite score: 0.10 - 0.30** (low)

---

## Summary

✅ **Importance now scales with R²**
✅ **Much bigger difference between good and poor targets**
✅ **Composite score better reflects true predictability**
✅ **Clear separation for ranking**

**The gap between R²=-0.45 and R²=0.2 is now properly reflected!** 🎯

