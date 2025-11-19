# Outdated Scripts - Cleanup Guide

## ✅ Current Main Scripts (KEEP)

These are the **active, maintained scripts** you should use:

### Core Scripts
1. **`rank_target_predictability.py`** ⭐
   - **Purpose**: Rank targets by predictability across multiple models
   - **Status**: ✅ UPDATED (now uses all models from config)
   - **Use**: `python scripts/rank_target_predictability.py --discover-all`

2. **`rank_features_by_ic_and_predictive.py`** ⭐
   - **Purpose**: Main feature ranking (IC + predictive power)
   - **Status**: ✅ CURRENT (your main feature selection tool)
   - **Use**: `python scripts/rank_features_by_ic_and_predictive.py`

3. **`multi_model_feature_selection.py`** ⭐
   - **Purpose**: Detailed multi-model feature importance
   - **Status**: ✅ CURRENT (for detailed analysis)
   - **Use**: `python scripts/multi_model_feature_selection.py --target <TARGET>`

4. **`rank_features_comprehensive.py`**
   - **Purpose**: Quality audit + predictive power + redundancy
   - **Status**: ✅ CURRENT (optional, for quality checks)
   - **Use**: `python scripts/rank_features_comprehensive.py`

### Utility Scripts (KEEP)
- **`filter_leaking_features.py`** ✅ - Used by all main scripts (DO NOT DELETE)
- **`list_available_symbols.py`** ✅ - Helper utility
- **`compare_feature_sets.py`** ✅ - Compare different feature sets

---

## 🗑️ Outdated Scripts (CAN DELETE)

These scripts are **no longer needed** or have been **superseded**:

### 1. **`identify_leaking_features.py`** ❌
- **Status**: OUTDATED
- **Reason**: Leakage already identified and fixed. All features are now in `CONFIG/excluded_features.yaml`
- **Replacement**: `filter_leaking_features.py` (which uses the config)
- **Action**: ✅ **SAFE TO DELETE**

### 2. **`test_quick_ranking.py`** ❌
- **Status**: OUTDATED
- **Reason**: Quick test script, no longer needed. Use main scripts instead.
- **Replacement**: Just run `rank_target_predictability.py` with `--discover-all`
- **Action**: ✅ **SAFE TO DELETE**

### 3. **`LEAKAGE_FIX_README.md`** ❌
- **Status**: OUTDATED DOCUMENTATION
- **Reason**: Leakage fix is complete. Info is now in main docs.
- **Action**: ✅ **SAFE TO DELETE** (or move to docs/archive/)

---

## 📝 Documentation Files (OPTIONAL)

These are documentation/helper files. Keep if useful, delete if not:

### Keep (Useful)
- **`EXAMPLE_MULTI_MODEL_WORKFLOW.md`** - Example workflow
- **`MULTI_MODEL_QUICKSTART.sh`** - Quick start helper

### Optional (Helper Scripts)
- **`run_baseline_validation.sh`** - Helper script (keep if you use it)
- **`run_comprehensive_feature_ranking.sh`** - Helper script (keep if you use it)
- **`run_feature_ranking.sh`** - Helper script (keep if you use it)
- **`run_regime_enhancement.sh`** - Helper script (keep if you use it)
- **`run_target_ranking_demo.sh`** - Helper script (can delete if not used)
- **`show_existing_output.sh`** - Helper script (can delete if not used)

---

## 🎯 Recommended Cleanup

### Delete These (Safe):
```bash
cd /home/Jennifer/trader/scripts

# Outdated scripts
rm identify_leaking_features.py
rm test_quick_ranking.py
rm LEAKAGE_FIX_README.md

# Optional: Helper scripts you don't use
rm run_target_ranking_demo.sh  # If you don't use it
rm show_existing_output.sh     # If you don't use it
```

### Keep These (Essential):
- ✅ All main ranking scripts (rank_*.py)
- ✅ `filter_leaking_features.py` (used by main scripts)
- ✅ `multi_model_feature_selection.py`
- ✅ Helper scripts you actually use

---

## 📊 Script Status Summary

| Script | Status | Action |
|--------|--------|--------|
| `rank_target_predictability.py` | ✅ CURRENT | KEEP |
| `rank_features_by_ic_and_predictive.py` | ✅ CURRENT | KEEP |
| `multi_model_feature_selection.py` | ✅ CURRENT | KEEP |
| `rank_features_comprehensive.py` | ✅ CURRENT | KEEP |
| `filter_leaking_features.py` | ✅ UTILITY | KEEP |
| `identify_leaking_features.py` | ❌ OUTDATED | DELETE |
| `test_quick_ranking.py` | ❌ OUTDATED | DELETE |
| `LEAKAGE_FIX_README.md` | ❌ OUTDATED | DELETE |

---

## ⚠️ Note About `select_features.py`

**This script doesn't exist** in your repo, but it's referenced in old documentation:
- `INFORMATION/08_FEATURE_SELECTION.md` mentions it
- `TRAINING/FEATURE_SELECTION_GUIDE.md` mentions it

**Replacement**: Use `rank_features_by_ic_and_predictive.py` instead.

You may want to update those docs to reference the new scripts.

---

## Quick Cleanup Command

```bash
cd /home/Jennifer/trader/scripts

# Delete outdated scripts
rm identify_leaking_features.py test_quick_ranking.py LEAKAGE_FIX_README.md

# Optional: Delete unused helper scripts
# rm run_target_ranking_demo.sh show_existing_output.sh
```

