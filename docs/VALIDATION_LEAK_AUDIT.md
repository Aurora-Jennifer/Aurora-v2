# Validation Split Leak Audit

**Date**: 2025-11-23  
**Status**: 🔴 **CRITICAL LEAKS FOUND**

## Summary

Found **6 locations** using standard K-Fold or TimeSeriesSplit without purge gap, causing temporal leakage in financial ML.

## Leak Locations

### ✅ FIXED
1. **`scripts/rank_target_predictability.py`** (line 565)
   - ✅ Now uses `PurgedTimeSeriesSplit` with horizon-based purge_overlap
   - ✅ Calculates purge from target horizon (e.g., 60m target → 17 bars purge)

### ❌ CRITICAL LEAKS (Need Fix)

2. **`scripts/rank_features_by_ic_and_predictive.py`** (line 731-733)
   - ❌ Uses `LogisticRegressionCV(cv=3)` and `LassoCV(cv=3)`
   - **Problem**: Standard K-Fold (cv=3) shuffles data randomly
   - **Impact**: HIGH - Used for feature ranking
   - **Fix**: Pass `PurgedTimeSeriesSplit` to `cv` parameter

3. **`scripts/multi_model_feature_selection.py`** (line 549-551)
   - ❌ Uses `LogisticRegressionCV(cv=3)` and `LassoCV(cv=3)`
   - **Problem**: Standard K-Fold (cv=3) shuffles data randomly
   - **Impact**: HIGH - Used for feature selection
   - **Fix**: Pass `PurgedTimeSeriesSplit` to `cv` parameter

4. **`TRAINING/unified_training_interface.py`** (line 185)
   - ❌ Uses `cross_val_score(..., cv=n_splits)`
   - **Problem**: Standard K-Fold (no purge)
   - **Impact**: HIGH - Main training interface
   - **Fix**: Use `PurgedTimeSeriesSplit` instead

5. **`TRAINING/model_fun/ensemble_trainer.py`** (line 163)
   - ❌ Uses `train_test_split(..., shuffle=False)`
   - **Problem**: No purge gap between train/test
   - **Impact**: MEDIUM - Ensemble training
   - **Fix**: Add purge gap manually or use PurgedTimeSeriesSplit

6. **`TRAINING/processing/cross_sectional.py`** (line 106)
   - ❌ Uses `GroupKFold(n_splits=n_splits)`
   - **Problem**: No purge gap for temporal data
   - **Impact**: MEDIUM - Cross-sectional validation
   - **Fix**: Need custom GroupKFold with purge (or use PurgedTimeSeriesSplit if timestamps are sequential)

### ⚠️ LOW PRIORITY (Diagnostic Tools)

7. **`scripts/diagnose_leakage.py`** (line 201)
   - ⚠️ Uses `TimeSeriesSplit` (not purged)
   - **Problem**: Diagnostic tool, not production code
   - **Impact**: LOW - Only used for debugging
   - **Fix**: Optional - can update for consistency

## Visual Explanation

### ❌ Standard K-Fold (LEAKS):
```
Fold 1: [Train] [Test]  ← Train and Test touch (leak!)
Fold 2: [Train] [Test]  ← Train and Test touch (leak!)
```

### ✅ PurgedTimeSeriesSplit (SAFE):
```
Fold 1: [Train] [GAP] [Test]  ← Gap = target horizon (safe!)
Fold 2: [Train] [GAP] [Test]  ← Gap = target horizon (safe!)
```

## Fix Priority

1. **HIGH**: Fix `rank_features_by_ic_and_predictive.py` and `multi_model_feature_selection.py`
   - These are used for feature ranking/selection
   - Leakage here affects all downstream models

2. **HIGH**: Fix `TRAINING/unified_training_interface.py`
   - Main training interface
   - All training goes through this

3. **MEDIUM**: Fix `ensemble_trainer.py` and `cross_sectional.py`
   - Used in production training
   - Less critical but still important

4. **LOW**: Fix `diagnose_leakage.py`
   - Diagnostic tool only
   - Can update for consistency

## Next Steps

1. Fix all HIGH priority leaks
2. Test that scores drop (expected - previous scores were inflated)
3. Verify purge_overlap is calculated correctly for each target
4. Update documentation

