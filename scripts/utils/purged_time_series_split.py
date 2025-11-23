"""
Purged Time Series Split for Financial ML

This CV splitter prevents temporal leakage by enforcing a "purge" gap
between training and test sets equal to the target horizon.

Critical for financial ML where standard K-Fold would leak future information.
"""

import numpy as np
from sklearn.model_selection._split import _BaseKFold
from sklearn.utils import indexable

try:
    from sklearn.utils.validation import _num_samples
except ImportError:
    # Fallback for older sklearn versions
    def _num_samples(x):
        """Get number of samples in array-like object"""
        if hasattr(x, '__len__'):
            return len(x)
        elif hasattr(x, 'shape'):
            return x.shape[0]
        else:
            raise TypeError(f"Cannot determine number of samples in {type(x)}")


class PurgedTimeSeriesSplit(_BaseKFold):
    """
    Time Series Split with an Embargo/Purge to prevent overlap leakage.
    
    This is CRITICAL for financial ML. Standard K-Fold shuffles data randomly,
    which destroys time patterns and allows training on future data to predict past data.
    
    The purge ensures there's a gap between train and test sets equal to the target horizon,
    preventing any temporal leakage from overlapping time windows.
    
    Args:
        n_splits: Number of folds (default: 5)
        purge_overlap: Number of rows to drop between Train and Test.
                      Set this >= your Target Horizon (e.g., if target is 60m, set to 60+).
                      Default: 0 (no purge, but still respects time order)
    
    Example:
        # For a 60-minute target with 5-minute bars:
        # purge_overlap = 60 / 5 = 12 bars, plus 5 for safety = 17
        cv = PurgedTimeSeriesSplit(n_splits=5, purge_overlap=17)
        scores = cross_val_score(model, X, y, cv=cv, scoring='r2')
    """
    
    def __init__(self, n_splits=5, purge_overlap=0):
        super().__init__(n_splits, shuffle=False, random_state=None)
        self.purge_overlap = purge_overlap
    
    def split(self, X, y=None, groups=None):
        """
        Generate indices to split data into training and test set.
        
        Args:
            X: Feature matrix
            y: Target vector (optional)
            groups: Group labels (optional, not used but required by interface)
        
        Yields:
            (train_indices, test_indices) tuples
        """
        X, y, groups = indexable(X, y, groups)
        n_samples = _num_samples(X)
        indices = np.arange(n_samples)
        
        # Calculate fold sizes (distribute samples evenly across folds)
        fold_sizes = np.full(self.n_splits, n_samples // self.n_splits, dtype=int)
        fold_sizes[:n_samples % self.n_splits] += 1
        
        current = 0
        
        for fold_idx, fold_size in enumerate(fold_sizes):
            start, stop = current, current + fold_size
            test_indices = indices[start:stop]
            
            # The 'Train' set is everything BEFORE the test set
            # BUT we must cut off the end of the training set to prevent leakage
            train_stop = start - self.purge_overlap
            
            if train_stop > 0:
                train_indices = indices[:train_stop]
                yield train_indices, test_indices
            else:
                # If purge eats the whole train set (early folds), skip this fold
                # This can happen if purge_overlap is too large relative to data size
                # Log a warning but continue to next fold
                import warnings
                warnings.warn(
                    f"Fold {fold_idx + 1}: purge_overlap={self.purge_overlap} is too large. "
                    f"Train set would be empty (start={start}, train_stop={train_stop}). "
                    f"Skipping this fold."
                )
            
            current = stop
    
    def get_n_splits(self, X=None, y=None, groups=None):
        """Returns the number of splitting iterations in the cross-validator"""
        return self.n_splits

