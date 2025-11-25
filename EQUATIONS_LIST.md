# Complete List of Equations in Repository

This document contains all mathematical equations and formulas found across the codebase.

## **1. Standardization & Calibration (IBKR Trading)**

### Z-Score Standardization
```
s_{m,h} = clip((r̂_{m,h} - μ_{m,h}) / σ_{m,h}, -3, 3)
```
- `s_{m,h}` = standardized score for model m, horizon h
- `r̂_{m,h}` = raw prediction from model m for horizon h
- `μ_{m,h}` = rolling mean of predictions (N≈5-10 trading days)
- `σ_{m,h}` = rolling standard deviation of predictions
- **File:** `IBKR_trading/MATHEMATICAL_FOUNDATIONS.md`
- **Used in:** `ZooBalancer.standardize()`

### Confidence Calculation
```
c_{m,h} = IC_{m,h} × freshness × capacity × stability
```
- `IC_{m,h}^{(τ)} = Spearman(r̂_{m,h}^{t-1}, r_h^{t})` = Information Coefficient
- `freshness = e^{-Δt/τ_h}` with `τ_{5m}=150s`, `τ_{10m}=300s`
- `capacity = min(1, κ × ADV / planned_dollars)`
- `stability = 1 / (rolling_RMSE_of_calibration)`
- **File:** `IBKR_trading/MATHEMATICAL_FOUNDATIONS.md`

### Calibrated Score
```
s̃_{m,h} = s_{m,h} × c_{m,h}
```
- **File:** `IBKR_trading/MATHEMATICAL_FOUNDATIONS.md`

## **2. Ensemble Blending (IBKR Trading)**

### Net IC After Costs
```
μ_{m,h} = IC_{m,h} - λ_c × cost_share_{m,h}
```
- `IC_{m,h}` = Information Coefficient for model m, horizon h
- `λ_c` = cost penalty parameter (typically 0.5)
- `cost_share_{m,h}` = expected_cost / expected_|alpha|
- **File:** `IBKR_trading/MATHEMATICAL_FOUNDATIONS.md`

### Ridge Risk-Parity Weights
```
w_h ∝ (Σ_h + λI)^{-1} μ_h
w_h ← clip(w_h, 0, ∞)
∑w_h = 1
```
- `Σ_h` = correlation matrix of standardized scores across families
- `λ` = ridge regularization parameter (typically 0.15)
- `μ_h` = target vector of net IC after costs
- `I` = identity matrix
- **File:** `IBKR_trading/MATHEMATICAL_FOUNDATIONS.md`
- **C++ Implementation:** `w = λ * (Σ + λI)^(-1) * z` (from `C++_INTEGRATION_SUMMARY.md`)

### Temperature Compression
```
w_h^{(T)} ∝ w_h^{1/T}
T_{5m} = 0.75, T_{10m} = 0.85
```
- **File:** `IBKR_trading/MATHEMATICAL_FOUNDATIONS.md`

### Horizon Alpha
```
α_h = ∑_m w_{m,h}^{(T)} × s̃_{m,h}
```
- **File:** `IBKR_trading/MATHEMATICAL_FOUNDATIONS.md`

## **3. Horizon Arbitration (IBKR Trading)**

### Net Score Calculation
```
net_h = α_h - k₁ × spread_bps - k₂ × σ × √(h/5) - k₃ × impact(q)
```
- `α_h` = horizon alpha from ensemble
- `k₁` = spread penalty coefficient (typically 1.0)
- `k₂` = volatility timing penalty (typically 0.15)
- `k₃` = market impact penalty (typically 1.0)
- `spread_bps` = bid-ask spread in basis points
- `σ` = volatility estimate
- `h` = horizon in minutes
- `impact(q)` = market impact function of order size
- **File:** `IBKR_trading/MATHEMATICAL_FOUNDATIONS.md`

### Horizon Score with Penalty
```
score_h = net_h / √(h/5)
```
- **File:** `IBKR_trading/MATHEMATICAL_FOUNDATIONS.md`

### Trade/No-Trade Gate
```
score_{h*} ≥ θ_enter
θ_enter = cost_bps + reserve_bps
```
- `reserve_bps` = 0.5-1.0× spread for 5m, 0.3-0.7× spread for 10m
- **File:** `IBKR_trading/MATHEMATICAL_FOUNDATIONS.md`

## **4. Barrier Target Gating (IBKR Trading)**

### Barrier Gate Formula
```
g = max(g_min, (1 - p_peak)^gamma * (0.5 + 0.5 * p_valley)^delta)
```
- `g_min` = minimum gate value
- `gamma`, `delta` = power parameters
- **File:** `IBKR_trading/live_trading/C++_INTEGRATION_SUMMARY.md`
- **Implementation:** `IBKR_trading/live_trading/barrier_gate.py`

### Long Entry Blocking
```
Block if: P(will_peak_5m) > 0.6 OR P(y_will_peak_5m) > 0.6
```
- **File:** `IBKR_trading/MATHEMATICAL_FOUNDATIONS.md`

### Long Entry Preference
```
Prefer if: P(will_valley_5m) > 0.55 AND ΔP > 0
```
- **File:** `IBKR_trading/MATHEMATICAL_FOUNDATIONS.md`

### Position Size Reduction
```
size_reduction = (1 - P(peak))
```
- **File:** `IBKR_trading/MATHEMATICAL_FOUNDATIONS.md`

### Long Exit Signal
```
Exit if: P(will_peak_5m) > 0.65 OR α_{5m} < 0
```
- **File:** `IBKR_trading/MATHEMATICAL_FOUNDATIONS.md`

## **5. Online Bandit Learning (IBKR Trading)**

### Exp3-IX Algorithm
```
u_i ← u_i × exp(η × r̂_i)
r̂_i = r_i / p_i
```
- `u_i` = weight for arm i (model, horizon)
- `η` = learning rate (typically min(0.07, √(ln K / (K T))))
- `r_i` = observed reward (net P&L bps)
- `p_i` = probability of selecting arm i
- `K` = number of arms
- `T` = total time steps
- **File:** `IBKR_trading/MATHEMATICAL_FOUNDATIONS.md`

### Reward Calculation
```
r_i = net_realized_PnL_bps - fees - slippage
```
- **File:** `IBKR_trading/MATHEMATICAL_FOUNDATIONS.md`

### Probability Selection
```
p_i ∝ (1-γ) × (u_i / ∑u) + γ / K
```
- `γ` = exploration parameter (typically 0.05)
- **File:** `IBKR_trading/MATHEMATICAL_FOUNDATIONS.md`

## **6. Execution Policy (IBKR Trading)**

### Initial Limit Price
```
px₀ = mid_px + tick × 0
```
- **File:** `IBKR_trading/MATHEMATICAL_FOUNDATIONS.md`

### Step-Up Price
```
px₁ = mid_px + tick × 1
```
- **File:** `IBKR_trading/MATHEMATICAL_FOUNDATIONS.md`

### Position Size Calculation
```
size = min(β × ADV_1m, risk_based_cap)
β_{5m} = 0.08
```
- **File:** `IBKR_trading/MATHEMATICAL_FOUNDATIONS.md`

## **7. Cost Estimation (IBKR Trading)**

### Cost Formula
```
c_h = k1 × spread + k2 × vol × sqrt(h/5) + k3 × participation^0.6
```
- `k1` = spread coefficient (default: 0.5)
- `k2` = volatility coefficient (default: 0.3)
- `k3` = participation coefficient (default: 0.2)
- `h` = horizon in minutes
- **File:** `IBKR_trading/live_trading/cost_arbitrator.py`

## **8. Optimization Objective (IBKR Trading)**

### QP/LP Solver Objective
```
maximize: z^T w - λ w^T Σ w - γ |C(w - w_cur)|_1
subject to:
  - Σ w_i = 1 (weights sum to 1)
  - w_i ≤ w_max (per-name caps)
  - Σ |w_i| ≤ G_max (gross exposure)
  - |Σ w_i| ≤ N_max (net exposure)
  - Σ |w_i - w_cur,i| ≤ T_max (turnover)
  - |β^T w| ≤ β_tol (beta neutrality)
  - Σ w_i * s_i ≤ S_max (sector caps)
```
- `z` = Risk-scaled scores
- `Σ` = Correlation matrix (shrunk)
- `C` = Per-name cost vector
- `β` = Beta exposures
- `s` = Sector exposures
- **File:** `IBKR_trading/CS_DOCS/OPTIMIZATION_ARCHITECTURE.md`

### Simplified Objective (Greedy)
```
max_w z^T w - λ w^T Σ w - γ |C(w - w_cur)|_1
```
- **File:** `IBKR_trading/OPTIMIZATION_ENGINE_ANALYSIS.md`

## **9. Performance Metrics**

### R² (Coefficient of Determination)
```
R² = 1 - (SS_res / SS_tot)
SS_res = Σ(y_true - y_pred)²
SS_tot = Σ(y_true - mean(y_true))²
```
- **File:** `scripts/utils/task_metrics.py` (lines 46-49)

### Information Coefficient (IC)
```
IC = corrcoef(predictions, actual_returns)
IC = Spearman(predictions, actual_returns)  # Alternative definition
```
- **File:** `scripts/utils/task_metrics.py` (line 59)
- **File:** `IBKR_trading/MATHEMATICAL_FOUNDATIONS.md` (line 294)

### MSE (Mean Squared Error)
```
MSE = mean((y_true - y_pred)²)
```
- **File:** `scripts/utils/task_metrics.py` (line 54)

### MAE (Mean Absolute Error)
```
MAE = mean(|y_true - y_pred|)
```
- **File:** `scripts/utils/task_metrics.py` (line 67)

### Sharpe Ratio
```
Sharpe = (mean_returns - risk_free_rate) / std_returns
```
- **File:** `IBKR_trading/MATHEMATICAL_FOUNDATIONS.md` (line 310)

### Maximum Drawdown
```
MDD = max(peak - trough) / peak
```
- **File:** `IBKR_trading/MATHEMATICAL_FOUNDATIONS.md` (line 318)

### Net Alpha After Costs
```
net_alpha = gross_alpha - slippage - fees - taxes
```
- **File:** `IBKR_trading/MATHEMATICAL_FOUNDATIONS.md` (line 302)

## **10. Composite Scoring (Target Ranking)**

### Regression Composite Score
```
composite = 0.7 × IC + 0.3 × R²_normalized
```
- R²_normalized: Clamped to [-10, 1] range
- **File:** `scripts/utils/task_metrics.py` (line 242)

### Binary Classification Composite Score
```
composite = 0.6 × AUC + 0.3 × accuracy + 0.1 × logloss_penalty
logloss_penalty = max(0.0, 1.0 - logloss)
```
- **File:** `scripts/utils/task_metrics.py` (line 253)

### Multiclass Classification Composite Score
```
composite = 0.5 × accuracy + 0.3 × macro_F1 + 0.2 × ce_penalty
ce_penalty = max(0.0, 1.0 - cross_entropy)
```
- **File:** `scripts/utils/task_metrics.py` (line 264)

### Predictability Composite Score
```
score_component = max(0, mean_score)  # For regression: clamp negative R² to 0
consistency_component = 1.0 / (1.0 + std_score)
importance_component = mean_importance × (1.0 + mean_score)  # If mean_score > 0
importance_component = mean_importance × max(0.5, 1.0 - |mean_score| × 0.67)  # If mean_score < 0
model_agreement = min(1.0, n_models / 5.0)

composite = 0.4 × score_component + 0.3 × consistency_component + 0.2 × importance_component + 0.1 × model_agreement
```
- **File:** `scripts/rank_target_predictability.py` (lines 2000-2035)

## **11. Risk Management Gates**

### Spread Gate
```
if spread_bps > spread_max_bps: HOLD
```
- `spread_max_bps` = 8-12 bps typically
- **File:** `IBKR_trading/MATHEMATICAL_FOUNDATIONS.md`

### Quote Age Gate
```
if quote_age_ms > 200: REJECT
```
- **File:** `IBKR_trading/MATHEMATICAL_FOUNDATIONS.md`

### Cost Sanity Gate
```
if estimated_slippage > 0.6 × spread: HOLD
```
- **File:** `IBKR_trading/MATHEMATICAL_FOUNDATIONS.md`

## **12. Feature Pruning**

### Cumulative Importance Threshold
```
Drop features where: cumulative_importance < 0.01%
Keep at least: min_features = 50
```
- **File:** `scripts/utils/feature_pruning.py`

## **13. Panel Data Purging**

### Time-Based Purge Calculation
```
cutoff_time = test_start_time - purge_overlap_time
train_stop_idx = searchsorted(time_vals, cutoff_time, side='right')
```
- **File:** `scripts/utils/purged_time_series_split.py` (lines 178-189)

### Purge Time Calculation
```
purge_time = target_horizon + purge_buffer
purge_buffer = purge_buffer_bars × data_interval_minutes
```
- **File:** `scripts/rank_target_predictability.py` (lines 743-744)

## **14. Data Interval Detection**

### Median Time Difference
```
median_diff_minutes = median(time_diffs).total_seconds() / 60.0
detected_interval = argmin(|common_intervals - median_diff_minutes|)
```
- Common intervals: [1, 5, 15, 30, 60] minutes
- **File:** `scripts/rank_target_predictability.py` (lines 692-721)

## **Summary**

**Total Equations Found:** 40+

**Categories:**
- **IBKR Trading System:** 25+ equations (standardization, blending, arbitration, costs, optimization)
- **Target Ranking System:** 8+ equations (metrics, composite scores, purging)
- **Performance Metrics:** 6+ equations (R², IC, Sharpe, MDD, etc.)
- **Risk Management:** 3+ equations (gates, thresholds)

**Primary Documentation:**
- `IBKR_trading/MATHEMATICAL_FOUNDATIONS.md` - Complete IBKR trading equations
- `IBKR_trading/CS_DOCS/OPTIMIZATION_ARCHITECTURE.md` - Optimization objective
- `scripts/utils/task_metrics.py` - Metric calculations
- `scripts/rank_target_predictability.py` - Composite scoring

