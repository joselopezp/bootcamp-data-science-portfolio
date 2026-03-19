"""
data_processing.py — Data ingestion, cleaning, and feature scaling utilities.

Purpose
-------
Centralizes all data preparation logic so that notebooks remain focused on
business narrative and CRISP-DM documentation. Every function here corresponds
to a specific step in Phase 3 (Data Preparation) of the CRISP-DM framework.

Business context
----------------
Raw customer data from Retail Insights S.A. contains mixed types (numeric,
ordinal, nominal), missing values, and outliers. These functions transform
the raw input into a clean, normalized feature matrix ready for distance-based
clustering algorithms (KMeans, DBSCAN, Hierarchical).

Design decisions recorded here
-------------------------------
- IQR chosen over Z-score: more robust when outliers are already present.
- StandardScaler chosen over MinMaxScaler: distance-based algorithms require
  zero mean and unit variance; MinMaxScaler is sensitive to extreme values.
- Median imputation (not mean): preserves central tendency under skew.
"""

# === Standard library ===
from pathlib import Path

# === Scientific computing — core data structures ===
import numpy as np
import pandas as pd

# === Machine learning — preprocessing (specialized) ===
from sklearn.preprocessing import StandardScaler


# ---------------------------------------------------------------------------
# Data ingestion
# ---------------------------------------------------------------------------


def load_raw_data(filepath: Path) -> pd.DataFrame:
    """Load the raw customer dataset from a CSV file.

    Kept intentionally simple: no parsing or type coercion at load time.
    All transformations happen in dedicated functions so each step is
    traceable in the Decisions Log.

    Args:
        filepath: Absolute or relative path to the raw CSV file.
                  Expected location: data/raw/Train.csv.

    Returns:
        Raw DataFrame with original dtypes and all columns intact,
        including the held-out 'Segmentation' label column.

    Example:
        >>> df = load_raw_data(DATA_RAW / "Train.csv")
        >>> df.shape
        (8068, 11)
    """
    return pd.read_csv(filepath)


# ---------------------------------------------------------------------------
# Outlier removal
# ---------------------------------------------------------------------------


def remove_outliers_iqr(
    df: pd.DataFrame,
    columns: list[str],
    factor: float = 1.5,
) -> pd.DataFrame:
    """Remove rows where any specified column falls outside the IQR fence.

    Uses the Tukey fences method: values outside [Q1 - factor*IQR,
    Q3 + factor*IQR] are considered outliers. A factor of 1.5 is the
    standard conservative threshold; use 3.0 only for extreme outlier
    detection.

    Why IQR over Z-score: Z-score assumes normality and is distorted by
    the very outliers it tries to detect. IQR is non-parametric and robust
    to skewed distributions common in retail customer data (e.g., age,
    work experience).

    Business impact: removes noisy records that would distort cluster
    centroids and inflate within-cluster variance — analogous to removing
    measurement errors before process capability analysis.

    Args:
        df: Input DataFrame. Must contain all columns listed in `columns`.
        columns: Numeric columns to apply the IQR filter to.
                 Non-numeric columns are unaffected.
        factor: IQR multiplier that controls fence width.
                1.5 (default) = standard outlier removal.
                3.0 = extreme outlier removal only.

    Returns:
        Filtered DataFrame with outlier rows removed and index reset.
        Original DataFrame is not modified.

    Example:
        >>> df_clean = remove_outliers_iqr(df, ["Age", "Work_Experience"])
        >>> print(f"Removed: {len(df) - len(df_clean)} rows")
    """
    # Start with all rows included; progressively narrow the mask
    # by intersecting conditions across each column.
    mask = pd.Series(True, index=df.index)

    for col in columns:
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        iqr = q3 - q1

        lower_fence = q1 - factor * iqr
        upper_fence = q3 + factor * iqr

        # Intersect: row survives only if it passes ALL column filters
        mask &= df[col].between(lower_fence, upper_fence)

    return df[mask].reset_index(drop=True)


# ---------------------------------------------------------------------------
# Feature scaling
# ---------------------------------------------------------------------------


def normalize_features(
    df: pd.DataFrame,
    columns: list[str],
) -> tuple[pd.DataFrame, StandardScaler]:
    """Standardize selected columns to zero mean and unit variance.

    Applies sklearn's StandardScaler: each value is transformed as
    z = (x - mean) / std. This is mandatory for distance-based algorithms
    (KMeans, DBSCAN, Hierarchical) because unscaled features with larger
    numeric ranges would dominate the distance metric unfairly.

    Why StandardScaler over MinMaxScaler: MinMaxScaler maps values to
    [0, 1] but is sensitive to outliers that survive IQR removal.
    StandardScaler is more stable and is the industry default for clustering.

    The fitted scaler object is returned alongside the scaled DataFrame
    so it can be serialized (joblib.dump) and reused on new customer data
    at deployment time — enabling the scalable pipeline requirement.

    Args:
        df: Input DataFrame after encoding and outlier removal.
        columns: Columns to standardize. Typically all numeric features
                 after one-hot encoding. Non-listed columns are preserved
                 unchanged.

    Returns:
        Tuple of:
            - df_scaled: Copy of df with specified columns standardized.
            - scaler: Fitted StandardScaler instance, ready for
                      joblib serialization and inference-time reuse.

    Example:
        >>> df_scaled, scaler = normalize_features(df_encoded, feature_cols)
        >>> joblib.dump(scaler, DATA_PROCESSED / "scaler.pkl")
    """
    scaler = StandardScaler()

    # Work on a copy to preserve the original DataFrame for audit purposes
    df_scaled = df.copy()
    df_scaled[columns] = scaler.fit_transform(df[columns])

    return df_scaled, scaler
