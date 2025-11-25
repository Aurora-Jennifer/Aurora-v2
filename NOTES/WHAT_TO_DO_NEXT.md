# What To Do Next: Clear Action Plan

You have all the tools - here's your step-by-step workflow:

---

## Step 1: Rank Features by IC and Predictive Power

**This is your main feature selection script** - it combines:
- IC (correlation with targets) - simple, interpretable
- Predictive power (model importance) - what actually works
- Uses your target rankings - focuses on best targets

### Run It:

```bash
conda activate trader_env
cd /home/Jennifer/trader

python scripts/rank_features_by_ic_and_predictive.py \
  --symbols AAPL,MSFT,GOOGL,TSLA,JPM \
  --output-dir results/feature_selection
```

**What it does**:
- Automatically uses your top 10 targets from `results/final_clean/target_predictability_rankings.yaml`
- Ranks features by IC (correlation) and predictive power (model importance)
- Combines both metrics into a final ranking
- Weights features by target quality (better targets = more weight)

**Output**: `results/feature_selection/feature_rankings_ic_predictive.csv`

---

## Step 2: Review the Rankings

Open the CSV file and look for:

### Top Features (Keep These!)
- **Combined score > 0.5**: Excellent features
- **IC (abs) > 0.1**: Good correlation with targets
- **Predictive > 0.3**: Models find them useful

### What to Do:
1. **Select top 50-100 features** with highest combined score
2. **Check redundancy**: If two features have similar names and both rank high, pick one
3. **Verify target**: Make sure the "Best Target" column shows a good target (R² > 0.1)

---

## Step 3: Use Selected Features

### Option A: Update Your Feature Config

Create a feature list file:

```bash
# Extract top 50 features
python -c "
import pandas as pd
df = pd.read_csv('results/feature_selection/feature_rankings_ic_predictive.csv')
top_features = df.head(50)['feature_name'].tolist()
print('\n'.join(top_features))
" > CONFIG/selected_features.txt
```

### Option B: Use in Multi-Model Feature Selection

Run multi-model selection on your best target:

```bash
python scripts/multi_model_feature_selection.py \
  --target y_will_peak_60m_0.8 \
  --symbols AAPL,MSFT,GOOGL,TSLA,JPM \
  --output-dir results/peak_60m_multi_model
```

This gives you detailed model-specific rankings.

---

## Step 4: Build Your Strategy

### With Your Top Features:

1. **Train models** using top 50-100 features
2. **Backtest** on historical data
3. **Validate** on out-of-sample data
4. **Paper trade** before going live

---

## Quick Reference: All Your Scripts

### 1. Target Ranking (Already Done )
```bash
python scripts/rank_target_predictability.py --discover-all
```
**Purpose**: Find which targets are most predictable

**Output**: `results/final_clean/target_predictability_rankings.yaml`

---

### 2. Feature Ranking by IC + Predictive (DO THIS NEXT )
```bash
python scripts/rank_features_by_ic_and_predictive.py
```
**Purpose**: Find best features for your best targets

**Output**: `results/feature_selection/feature_rankings_ic_predictive.csv`

---

### 3. Multi-Model Feature Selection (Optional)
```bash
python scripts/multi_model_feature_selection.py --target <TARGET>
```
**Purpose**: Detailed model-specific feature importance

**Output**: `results/<target>_multi_model/`

---

### 4. Comprehensive Feature Ranking (Optional)
```bash
python scripts/rank_features_comprehensive.py --target <TARGET>
```
**Purpose**: Quality audit + predictive power + redundancy detection

**Output**: `results/feature_rankings_comprehensive/`

---

## Recommended Workflow

```
1.  Rank Targets (DONE)
   └─> Found best targets (peak_60m, valley_60m, etc.)

2.  Rank Features by IC + Predictive (DO THIS)
   └─> Find best features for your best targets

3. Select Top 50-100 Features
   └─> Use the CSV to pick your feature set

4. Train Models
   └─> Use selected features to train your models

5. Backtest & Validate
   └─> Test on historical data

6. Deploy
   └─> Paper trade → Live trade
```

---

## Understanding the Metrics

### IC (Information Coefficient)
- **What it is**: Correlation between feature and target
- **Range**: -1 to +1 (use absolute value)
- **Good value**: > 0.1 (10% correlation)
- **Interpretation**: Feature moves with target

### Predictive Power
- **What it is**: Model-based feature importance
- **Range**: 0 to 1 (normalized)
- **Good value**: > 0.3
- **Interpretation**: Models actually use this feature

### Combined Score
- **What it is**: Weighted combination (40% IC + 60% Predictive)
- **Range**: 0 to 1
- **Good value**: > 0.5
- **Interpretation**: Best overall features

---

## Troubleshooting

### "No targets found"
**Fix**: Make sure `results/final_clean/target_predictability_rankings.yaml` exists

### "All features have low scores"
**Possible causes**:
- Targets are hard to predict (check target R²)
- Features are not predictive (try different features)
- Data quality issues (check missing rates)

**Fix**: Review target rankings - if target R² < 0.1, that target may not be predictable

### "Script is slow"
**Fix**: Reduce `--max-samples` (default 50000) or use fewer symbols

---

## Next Steps Summary

1. **Run feature ranking**:
   ```bash
   python scripts/rank_features_by_ic_and_predictive.py
   ```

2. **Review top 50 features** in the CSV

3. **Select your feature set** (50-100 features)

4. **Train models** with selected features

5. **Backtest and validate**

---

## You're Not Lost!

You have:
- Best targets identified (from target ranking)
- Feature ranking script (IC + predictive)
- Multi-model selection (detailed analysis)
- Comprehensive ranking (quality audit)

**Just run the feature ranking script and use the top features!**

The script automatically:
- Uses your best targets
- Combines IC and predictive power
- Gives you a clear ranking

**Start here**: `python scripts/rank_features_by_ic_and_predictive.py`

