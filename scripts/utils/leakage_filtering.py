"""
Target-Aware Leakage Filtering

Filters out features that would leak information about the target being predicted.
Uses temporal awareness: features computed at time t cannot use information from
time t+horizon or later.
"""

import re
from typing import List, Set, Optional
import logging

logger = logging.getLogger(__name__)


def filter_features_for_target(
    all_columns: List[str],
    target_column: str,
    verbose: bool = False
) -> List[str]:
    """
    Filter features that would leak information about the target.
    
    Uses target-aware filtering:
    - For forward return targets (fwd_ret_*), exclude features computed from
      future returns or overlapping time windows
    - For barrier targets (y_will_*), exclude features that know about barrier
      hits (tth_*, mfe_share_*, hit_direction_*, etc.)
    
    Args:
        all_columns: List of all column names in the dataset
        target_column: Name of the target column being predicted
        verbose: If True, log excluded features
    
    Returns:
        List of safe feature column names
    """
    # Start with all columns except the target itself
    safe_columns = [c for c in all_columns if c != target_column]
    
    # Get target metadata
    target_type = _classify_target_type(target_column)
    target_horizon = _extract_horizon(target_column)
    
    # Apply target-specific filtering rules
    if target_type == 'forward_return':
        safe_columns = _filter_for_forward_return_target(
            safe_columns, target_column, target_horizon, verbose
        )
    elif target_type == 'barrier':
        safe_columns = _filter_for_barrier_target(
            safe_columns, target_column, target_horizon, verbose
        )
    elif target_type == 'first_touch':
        # First touch targets are already leaked (correlated with hit_direction)
        # But we still filter features
        safe_columns = _filter_for_barrier_target(
            safe_columns, target_column, target_horizon, verbose
        )
    
    # Always exclude these leaking features regardless of target type
    always_exclude = _get_always_excluded_features()
    excluded = [c for c in safe_columns if _matches_any_pattern(c, always_exclude)]
    safe_columns = [c for c in safe_columns if c not in excluded]
    
    if verbose and excluded:
        logger.info(f"  Excluded {len(excluded)} always-leaked features")
    
    return safe_columns


def _classify_target_type(target_column: str) -> str:
    """Classify target type from column name"""
    if target_column.startswith('fwd_ret_'):
        return 'forward_return'
    elif target_column.startswith('y_will_'):
        return 'barrier'
    elif 'first_touch' in target_column:
        return 'first_touch'
    else:
        return 'unknown'


def _extract_horizon(target_column: str) -> Optional[int]:
    """
    Extract horizon from target column name (in minutes)
    
    Examples:
        fwd_ret_60m -> 60
        y_will_peak_15m_0.8 -> 15
        fwd_ret_1d -> 1440 (assuming 1d = 1440 minutes)
    """
    # Pattern: number followed by 'm', 'h', or 'd'
    patterns = [
        (r'(\d+)m', lambda x: int(x)),  # minutes
        (r'(\d+)h', lambda x: int(x) * 60),  # hours -> minutes
        (r'(\d+)d', lambda x: int(x) * 1440),  # days -> minutes
    ]
    
    for pattern, converter in patterns:
        match = re.search(pattern, target_column)
        if match:
            return converter(match.group(1))
    
    return None


def _filter_for_forward_return_target(
    columns: List[str],
    target_column: str,
    target_horizon: Optional[int],
    verbose: bool
) -> List[str]:
    """
    Filter features for forward return targets.
    
    Excludes:
    - Features computed from future returns (overlapping windows)
    - Features that use information beyond the target horizon
    """
    excluded = []
    safe = []
    
    for col in columns:
        should_exclude = False
        
        # Exclude forward returns with overlapping or longer horizons
        if col.startswith('fwd_ret_'):
            col_horizon = _extract_horizon(col)
            if col_horizon is not None and target_horizon is not None:
                # Exclude if feature horizon >= target horizon (overlaps)
                if col_horizon >= target_horizon:
                    should_exclude = True
                    excluded.append((col, "overlapping forward return"))
        
        # Exclude features computed from future paths
        if any(col.startswith(prefix) for prefix in [
            'tth_',  # time-to-hit (knows when barrier will be hit)
            'mfe_share_',  # fraction of time in profit (requires future path)
            'time_in_profit_',  # duration in profit (requires future path)
            'flipcount_',  # number of flips (requires future path)
        ]):
            should_exclude = True
            excluded.append((col, "future path feature"))
        
        # Exclude barrier hit features (they're targets, not features)
        if col.startswith('y_will_') or col.startswith('y_first_touch'):
            should_exclude = True
            excluded.append((col, "barrier target (not a feature)"))
        
        if not should_exclude:
            safe.append(col)
    
    if verbose and excluded:
        logger.info(f"  Excluded {len(excluded)} features for forward return target:")
        for col, reason in excluded[:10]:  # Show first 10
            logger.info(f"    - {col}: {reason}")
        if len(excluded) > 10:
            logger.info(f"    ... and {len(excluded) - 10} more")
    
    return safe


def _filter_for_barrier_target(
    columns: List[str],
    target_column: str,
    target_horizon: Optional[int],
    verbose: bool
) -> List[str]:
    """
    Filter features for barrier targets (y_will_peak, y_will_valley, etc.).
    
    Excludes:
    - Features that know about barrier hits (tth_*, hit_direction_*, etc.)
    - Features computed from future paths
    - First touch targets (they're leaked)
    """
    excluded = []
    safe = []
    
    for col in columns:
        should_exclude = False
        
        # Exclude features that know about barrier hits
        if any(col.startswith(prefix) for prefix in [
            'tth_',  # time-to-hit
            'tth_abs_',  # absolute time-to-hit
            'hit_direction_',  # which barrier hits first (correlated with first_touch)
            'hit_asym_',  # asymmetric barrier hit
        ]):
            should_exclude = True
            excluded.append((col, "barrier hit feature"))
        
        # Exclude first touch targets (they're leaked - correlated with hit_direction)
        if 'first_touch' in col and col.startswith('y_'):
            should_exclude = True
            excluded.append((col, "first_touch target (leaked)"))
        
        # Exclude features computed from future paths
        if any(col.startswith(prefix) for prefix in [
            'mfe_share_',  # fraction of time in profit
            'time_in_profit_',  # duration in profit
            'flipcount_',  # number of flips
        ]):
            should_exclude = True
            excluded.append((col, "future path feature"))
        
        # Exclude other barrier targets (they're targets, not features)
        if col.startswith('y_will_') and col != target_column:
            should_exclude = True
            excluded.append((col, "other barrier target"))
        
        if not should_exclude:
            safe.append(col)
    
    if verbose and excluded:
        logger.info(f"  Excluded {len(excluded)} features for barrier target:")
        for col, reason in excluded[:10]:  # Show first 10
            logger.info(f"    - {col}: {reason}")
        if len(excluded) > 10:
            logger.info(f"    ... and {len(excluded) - 10} more")
    
    return safe


def _get_always_excluded_features() -> List[str]:
    """
    Get patterns for features that should always be excluded (regardless of target).
    
    These are features that leak information by definition.
    """
    return [
        r'^tth_',  # time-to-hit
        r'^tth_abs_',  # absolute time-to-hit
        r'^mfe_share_',  # max favorable excursion share
        r'^time_in_profit_',  # time in profit
        r'^flipcount_',  # flip count
        r'^hit_direction_',  # hit direction (correlated with first_touch)
        r'^hit_asym_',  # asymmetric hit
        r'^y_first_touch',  # first touch (leaked)
    ]


def _matches_any_pattern(text: str, patterns: List[str]) -> bool:
    """Check if text matches any regex pattern"""
    import re
    for pattern in patterns:
        if re.match(pattern, text):
            return True
    return False
