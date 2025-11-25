"""
Target/Label Generation Module

Provides target generation for different trading strategies:
- barrier: Barrier/first-passage labels (will_peak, will_valley)
- excess_returns: Excess return labels and neutral band classification
- hft_forward: HFT forward return targets for short horizons
"""

from .barrier import (
    compute_barrier_targets,
    add_barrier_targets_to_dataframe,
    add_zigzag_targets_to_dataframe,
    add_mfe_mdd_targets_to_dataframe,
    add_enhanced_targets_to_dataframe
)
from .excess_returns import (
    rolling_beta,
    future_excess_return,
    compute_neutral_band,
    classify_excess_return
)

__all__ = [
    # Barrier targets
    "compute_barrier_targets",
    "add_barrier_targets_to_dataframe",
    "add_zigzag_targets_to_dataframe",
    "add_mfe_mdd_targets_to_dataframe",
    "add_enhanced_targets_to_dataframe",
    # Excess return targets
    "rolling_beta",
    "future_excess_return",
    "compute_neutral_band",
    "classify_excess_return",
]

