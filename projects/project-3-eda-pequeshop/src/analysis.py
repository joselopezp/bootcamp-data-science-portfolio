"""
Analysis Module.

Functions for statistical analysis and modeling.
Corresponds to CRISP-DM Phase 4: Modeling.

Author: Jose Marcel Lopez Pino
"""

import pandas as pd
import numpy as np


def compute_descriptive_stats(df: pd.DataFrame) -> pd.DataFrame:
    """Compute descriptive statistics for numeric columns.

    Args:
        df: Input DataFrame.

    Returns:
        DataFrame with descriptive statistics.
    """
    return df.describe()


def compute_correlations(df: pd.DataFrame, method: str = "pearson") -> pd.DataFrame:
    """Compute correlation matrix.

    Args:
        df: Input DataFrame.
        method: Correlation method ('pearson', 'spearman', 'kendall').

    Returns:
        Correlation matrix as DataFrame.
    """
    numeric_df = df.select_dtypes(include=[np.number])
    return numeric_df.corr(method=method)
