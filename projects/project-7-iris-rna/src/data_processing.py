"""
data_processing.py -- Data ingestion, cleaning, and feature scaling utilities.

Purpose
-------
Centralizes all data preparation logic so that notebooks remain focused on
business narrative and CRISP-DM documentation. Every function corresponds
to a specific step in Phase 3 (Data Preparation) of the CRISP-DM framework.

Business context
----------------
TBD -- fill in after Phase 1 (Business Understanding) is complete.

Design decisions recorded here
-------------------------------
TBD -- document algorithm/library choices with rationale as they are made.
"""

# === Standard library ===
from pathlib import Path

# === Scientific computing -- core data structures ===
import numpy as np
import pandas as pd

# === Machine learning -- preprocessing (specialized) ===
from sklearn.preprocessing import StandardScaler


# ---------------------------------------------------------------------------
# Data ingestion
# ---------------------------------------------------------------------------


def load_raw_data(filepath: Path) -> pd.DataFrame:
    """Load the raw dataset from a CSV file.

    Kept intentionally simple: no parsing or type coercion at load time.
    All transformations happen in dedicated functions so each step is
    traceable in the Decisions Log.

    Args:
        filepath: Absolute or relative path to the raw CSV file.

    Returns:
        Raw DataFrame with original dtypes and all columns intact.
    """
    return pd.read_csv(filepath)
