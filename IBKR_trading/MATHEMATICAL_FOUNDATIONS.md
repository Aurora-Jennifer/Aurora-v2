# Mathematical Foundations for IBKR Cost-Aware Ensemble Trading

## 🎯 **Purpose**
This document contains all mathematical equations and formulas used in the IBKR trading system, with descriptions of where they're applied and why they're necessary for cost-aware intraday trading.

## 📊 **1. Standardization & Calibration**

### **Z-Score Standardization**
```
s_{m,h} = clip((r̂_{m,h} - μ_{m,h}) / σ_{m,h}, -3, 3)
```

**Where:**
- `s_{m,h}` = standardized score for model m, horizon h
- `r̂_{m,h}` = raw prediction from model m for horizon h
- `μ_{m,h}` = rolling mean of predictions (N≈5-10 trading days)
- `σ_{m,h}` = rolling standard deviation of predictions
- `clip(-3, 3)` = prevents extreme outliers from dominating

**Used in:** `ZooBalancer.standardize()`
**Why:** Every model family scales differently. Short horizons demand calibrated, comparable signals. Standardization ensures fair comparison across different model types.

### **Confidence Calculation**
```
c_{m,h} = IC_{m,h} × freshness × capacity × stability
```

**Where:**
- `IC_{m,h}^{(τ)} = Spearman(r̂_{m,h}^{t-1}, r_h^{t})` = Information Coefficient
- `freshness = e^{-Δt/τ_h}` with `τ_{5m}=150s`, `τ_{10m}=300s`
- `capacity = min(1, κ × ADV / planned_dollars)`
- `stability = 1 / (rolling_RMSE_of_calibration)`

**Used in:** `ZooBalancer` confidence weighting
**Why:** Short horizons need freshness checks. Stale data or low-capacity situations should reduce model confidence.

### **Calibrated Score**
```
s̃_{m,h} = s_{m,h} × c_{m,h}
```

**Used in:** Final model score after confidence adjustment
**Why:** Combines standardized prediction with confidence to get realistic signal strength.

## 🎯 **2. Within-Horizon Ensemble Blending**

### **Net IC After Costs**
```
μ_{m,h} = IC_{m,h} - λ_c × cost_share_{m,h}
```

**Where:**
- `IC_{m,h}` = Information Coefficient for model m, horizon h
- `λ_c` = cost penalty parameter (typically 0.5)
- `cost_share_{m,h}` = expected_cost / expected_|alpha|

**Used in:** `ZooBalancer.weights()` target vector
**Why:** Penalizes models with high cost-to-alpha ratios. Prevents expensive models from dominating the ensemble.

### **Ridge Risk-Parity Weights**
```
w_h ∝ (Σ_h + λI)^{-1} μ_h
w_h ← clip(w_h, 0, ∞)
∑w_h = 1
```

**Where:**
- `Σ_h` = correlation matrix of standardized scores across families
- `λ` = ridge regularization parameter (typically 0.15)
- `μ_h` = target vector of net IC after costs
- `I` = identity matrix

**Used in:** `ZooBalancer.weights()` for correlation-aware weighting
**Why:** Ridge regression prevents overfitting to correlated models. Risk parity ensures no single model dominates.

### **Temperature Compression**
```
w_h^{(T)} ∝ w_h^{1/T}
T_{5m} = 0.75, T_{10m} = 0.85
```

**Used in:** `ZooBalancer.weights()` for short horizon compression
**Why:** Short horizons (5m, 10m) need more conservative weighting. Temperature compression reduces extreme weights.

### **Horizon Alpha**
```
α_h = ∑_m w_{m,h}^{(T)} × s̃_{m,h}
```

**Used in:** Final blended prediction per horizon
**Why:** Combines all model predictions within a horizon using optimized weights.

## 🌐 **3. Across-Horizon Arbitration**

### **Net Score Calculation**
```
net_h = α_h - k₁ × spread_bps - k₂ × σ × √(h/5) - k₃ × impact(q)
```

**Where:**
- `α_h` = horizon alpha from ensemble
- `k₁` = spread penalty coefficient (typically 1.0)
- `k₂` = volatility timing penalty (typically 0.15)
- `k₃` = market impact penalty (typically 1.0)
- `spread_bps` = bid-ask spread in basis points
- `σ` = volatility estimate
- `h` = horizon in minutes
- `impact(q)` = market impact function of order size

**Used in:** `HorizonArbiter.net_score()` for cost-aware horizon selection
**Why:** Accounts for all trading costs when selecting optimal horizon. Penalizes longer horizons for timing risk.

### **Horizon Score with Penalty**
```
score_h = net_h / √(h/5)
```

**Used in:** `HorizonArbiter.choose()` for horizon selection
**Why:** Penalizes longer horizons when deciding entries in a 5m loop. Favors shorter horizons for intraday trading.

### **Trade/No-Trade Gate**
```
score_{h*} ≥ θ_enter
θ_enter = cost_bps + reserve_bps
```

**Where:**
- `reserve_bps` = 0.5-1.0× spread for 5m, 0.3-0.7× spread for 10m
- `cost_bps` = estimated trading costs

**Used in:** `HorizonArbiter.choose()` trade decision
**Why:** Only trade when expected alpha exceeds all costs plus safety margin.

## 🚧 **4. Barrier Target Gating**

### **Long Entry Blocking**
```
Block if: P(will_peak_5m) > 0.6 OR P(y_will_peak_5m) > 0.6
```

**Used in:** `BarrierGates.allow_long_entry()`
**Why:** Prevents buying into local tops when barrier models predict peak probability > 60%.

### **Long Entry Preference**
```
Prefer if: P(will_valley_5m) > 0.55 AND ΔP > 0
```

**Used in:** `BarrierGates.allow_long_entry()` for valley bounce detection
**Why:** Favors entries after valleys when price is turning up.

### **Position Size Reduction**
```
size_reduction = (1 - P(peak))
```

**Used in:** `BarrierGates` for risk-adjusted position sizing
**Why:** Reduces position size when peak probability is high but not blocking.

### **Long Exit Signal**
```
Exit if: P(will_peak_5m) > 0.65 OR α_{5m} < 0
```

**Used in:** `BarrierGates.long_exit_signal()`
**Why:** Exit when peak probability is very high or alpha turns negative.

## 🎰 **5. Online Bandit Weight Updates**

### **Exp3-IX Algorithm**
```
u_i ← u_i × exp(η × r̂_i)
r̂_i = r_i / p_i
```

**Where:**
- `u_i` = weight for arm i (model, horizon)
- `η` = learning rate (typically min(0.07, √(ln K / (K T))))
- `r_i` = observed reward (net P&L bps)
- `p_i` = probability of selecting arm i
- `K` = number of arms
- `T` = total time steps

**Used in:** `EnsembleWeightOptimizer` for online weight updates
**Why:** Adapts model weights based on actual performance. Exp3-IX is robust to adversarial environments.

### **Reward Calculation**
```
r_i = net_realized_PnL_bps - fees - slippage
```

**Used in:** Bandit reward function
**Why:** Uses net P&L after all costs to ensure weights reflect actual profitability.

### **Probability Selection**
```
p_i ∝ (1-γ) × (u_i / ∑u) + γ / K
```

**Where:**
- `γ` = exploration parameter (typically 0.05)
- `K` = total number of arms

**Used in:** `EnsembleWeightOptimizer` for arm selection
**Why:** Balances exploitation of good models with exploration of new ones.

## ⚡ **6. Short-Horizon Execution Policy**

### **Initial Limit Price**
```
px₀ = mid_px + tick × 0  # Start at mid
```

**Used in:** `ShortHorizonExecutionPolicy.plan()` initial order
**Why:** Start passive to minimize market impact.

### **Step-Up Price**
```
px₁ = mid_px + tick × 1  # One tick more aggressive
```

**Used in:** `ShortHorizonExecutionPolicy.plan()` step-up order
**Why:** Gradually increase aggression if initial order doesn't fill.

### **Fill Rate Check**
```
if fill_rate < 0.4 by half_TIF:
    step_up_aggression()
```

**Used in:** `ShortHorizonExecutionPolicy` execution logic
**Why:** Only step up if initial order isn't filling fast enough.

### **Position Size Calculation**
```
size = min(β × ADV_1m, risk_based_cap)
β_{5m} = 0.08
```

**Where:**
- `ADV_1m` = average daily volume over 1 minute
- `β` = participation rate
- `risk_based_cap` = maximum position from risk management

**Used in:** `ShortHorizonExecutionPolicy` for order sizing
**Why:** Limits position size to avoid market impact while respecting risk constraints.

## 🛡️ **7. Risk Management Gates**

### **Spread Gate**
```
if spread_bps > spread_max_bps:
    HOLD
```

**Where:** `spread_max_bps` = 8-12 bps typically

**Used in:** `IBKRBrokerAdapter` pre-trade checks
**Why:** Avoid trading in wide spreads where costs are too high.

### **Quote Age Gate**
```
if quote_age_ms > 200:
    REJECT
```

**Used in:** `IBKRBrokerAdapter` data freshness checks
**Why:** Reject stale data to prevent bad decisions.

### **Latency Gate**
```
if t_infer_to_order > 2s:
    WARN
if t_infer_to_order > 1s:
    LOG_WARNING
```

**Used in:** Performance monitoring
**Why:** Ensure decisions are made quickly enough for intraday trading.

### **Cost Sanity Gate**
```
if estimated_slippage > 0.6 × spread:
    HOLD
```

**Used in:** `CostModel` validation
**Why:** Prevent trades when estimated costs are too high relative to spread.

## 📈 **8. Performance Metrics**

### **Information Coefficient**
```
IC = Spearman(predictions, actual_returns)
```

**Used in:** Model performance evaluation
**Why:** Measures predictive power of models.

### **Net Alpha After Costs**
```
net_alpha = gross_alpha - slippage - fees - taxes
```

**Used in:** Performance evaluation
**Why:** True measure of trading profitability.

### **Sharpe Ratio**
```
Sharpe = (mean_returns - risk_free_rate) / std_returns
```

**Used in:** Risk-adjusted performance evaluation
**Why:** Standard measure of risk-adjusted returns.

### **Maximum Drawdown**
```
MDD = max(peak - trough) / peak
```

**Used in:** Risk management
**Why:** Measures worst-case loss from peak to trough.

## 🔧 **9. Configuration Parameters**

### **Temperature Parameters**
```yaml
temp:
  "5m": 0.75    # More conservative for shortest horizon
  "10m": 0.85   # Slightly less conservative
  "15m": 0.90   # Standard temperature
  "30m": 1.0    # No compression
  "60m": 1.0    # No compression
```

### **Cost Thresholds**
```yaml
cost_thresholds:
  "5m": 0.002   # 0.2% maximum costs
  "10m": 0.003  # 0.3% maximum costs
  "15m": 0.004  # 0.4% maximum costs
  "30m": 0.005  # 0.5% maximum costs
  "60m": 0.006  # 0.6% maximum costs
```

### **Confidence Thresholds**
```yaml
confidence_thresholds:
  "5m": 0.8     # 80% confidence required
  "10m": 0.75   # 75% confidence required
  "15m": 0.7    # 70% confidence required
  "30m": 0.65   # 65% confidence required
  "60m": 0.6    # 60% confidence required
```

### **Bandit Parameters**
```yaml
bandit:
  gamma: 0.05   # 5% exploration
  eta: 0.05     # Learning rate
  algo: "exp3ix" # Algorithm choice
```

## 🎯 **10. Key Design Principles**

### **Cost-Aware Decision Making**
Every equation includes cost considerations to ensure profitable trading after all expenses.

### **Short Horizon Focus**
Temperature compression and confidence thresholds favor shorter horizons (5m, 10m) for intraday trading.

### **Barrier Target Integration**
Uses `will_peak`, `will_valley`, and `y_*` models to prevent entries into local tops/bottoms.

### **Online Learning**
Exp3-IX bandit algorithm continuously adapts model weights based on actual performance.

### **Risk Management**
Multiple gates prevent trading in adverse conditions (wide spreads, stale data, high costs).

### **Execution Realism**
TIF + staged aggression matches the reality of 5-10m holding periods.

This mathematical foundation ensures the IBKR trading system operates as a disciplined desk for short intraday trading while preserving all existing risk gates and adding sophisticated cost-aware decision making.
