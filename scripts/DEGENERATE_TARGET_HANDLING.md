# Degenerate Target Handling - All Ranking Scripts

## ✅ Updated Scripts

All ranking scripts now have **consistent, robust handling** of degenerate targets:

1. **`rank_target_predictability.py`** ✅
2. **`rank_features_by_ic_and_predictive.py`** ✅
3. **`rank_features_comprehensive.py`** ✅
4. **`multi_model_feature_selection.py`** ✅

## 🛡️ Protection Mechanisms

### 1. Pre-Training Validation

All scripts now validate targets **before** training models:

- ✅ Check for < 2 unique values (degenerate)
- ✅ Check for classes with < 2 samples (too imbalanced for CV)
- ✅ Early return if target is invalid

### 2. Error Handling in Model Training

All models now handle degenerate targets gracefully:

- ✅ **LightGBM**: Catches "invalid classes" errors
- ✅ **XGBoost**: Catches "Invalid classes" / "Expected" errors
- ✅ **Neural Network**: Catches "least populated class" errors
- ✅ **Random Forest**: Handles degenerate cases

### 3. Cross-Validation Safety

- ✅ All `cross_val_score` calls use `error_score='nan'`
- ✅ Failed CV folds return NaN instead of crashing
- ✅ Aggregation skips NaN scores

### 4. Shared Validation Utility

Created `scripts/utils/target_validation.py` with:
- `validate_target()` - Pre-training validation
- `check_cv_compatibility()` - CV compatibility check
- `safe_cross_val_score()` - Safe CV wrapper

## 📊 What This Fixes

### Before:
- ❌ Scripts crashed on degenerate targets
- ❌ Neural Network failed with "least populated class" errors
- ❌ XGBoost failed with "Invalid classes" errors
- ❌ Warnings flooded the output

### After:
- ✅ Scripts skip degenerate targets gracefully
- ✅ Models return NaN for failed evaluations
- ✅ Aggregation only uses successful models
- ✅ Clean output with minimal warnings

## 🎯 Result

All ranking scripts now:
1. **Validate targets** before training
2. **Handle errors gracefully** during training
3. **Skip NaN scores** when aggregating
4. **Complete successfully** even with problematic targets

---

## Example: What Happens Now

### Degenerate Target in Some Symbols

**Before**: Script crashes or floods warnings

**After**:
```
2025-11-13 18:34:23 - INFO -   AAPL...
2025-11-13 18:34:23 - WARNING -     ⚠️  Skipping: Target has only 1 unique value in sample
2025-11-13 18:34:24 - INFO -   MSFT...
2025-11-13 18:34:30 - INFO -     ✓ Scores: lightgbm=0.168, random_forest=0.121, importance=6.87
```

**Result**: Script continues, uses valid symbols only

---

## Technical Details

### Validation Checks

```python
# Check 1: Minimum samples
if len(y_clean) < 10:
    return False, "Too few samples"

# Check 2: Multiple unique values
if len(unique_vals) < 2:
    return False, "Only 1 unique value (degenerate)"

# Check 3: Class balance (for classification)
if min_class_count < 2:
    return False, "Smallest class has only 1 sample (too few for CV)"
```

### Error Handling Pattern

```python
try:
    model.fit(X, y)
    # ... get importance ...
except (ValueError, TypeError) as e:
    error_str = str(e).lower()
    if any(kw in error_str for kw in ['invalid classes', 'too few', 'least populated']):
        logger.debug(f"    {model_name}: Target degenerate")
        return {}  # or NaN
    raise
```

---

## Status: ✅ ALL SCRIPTS UPDATED

All ranking scripts now have consistent, robust degenerate target handling!

