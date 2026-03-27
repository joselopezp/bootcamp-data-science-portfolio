"""
config.py -- Project-wide configuration: paths and constants.

Centralizes all path definitions so notebooks never use hardcoded paths.
Import from notebooks as:
    from config.config import DATA_RAW, RANDOM_STATE
"""

# === Standard library ===
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

PROJECT_ROOT     = Path(__file__).resolve().parent.parent
DATA_RAW         = PROJECT_ROOT / "data" / "raw"
DATA_PROCESSED   = PROJECT_ROOT / "data" / "processed"
DATA_FINAL       = PROJECT_ROOT / "data" / "final"
REPORTS_FIGURES  = PROJECT_ROOT / "reports" / "figures"
REPORTS_EXEC     = PROJECT_ROOT / "reports" / "executive"

# Create output directories if they do not exist yet
for _p in [REPORTS_FIGURES, REPORTS_EXEC]:
    _p.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------------------------
# Reproducibility
# ---------------------------------------------------------------------------

# Fixed seed used across all stochastic operations (train/test splits,
# KMeans initialization, t-SNE, etc.) to ensure reproducible results.
RANDOM_STATE = 42
