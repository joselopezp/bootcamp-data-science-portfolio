"""
Project 6 — Module 7: Customer Segmentation (Unsupervised ML)
Global configuration: paths and reproducibility seed.
"""
from pathlib import Path

# ── Paths ──────────────────────────────────────────────────────────────────
PROJECT_ROOT     = Path(__file__).resolve().parent.parent
DATA_RAW         = PROJECT_ROOT / "data" / "raw"
DATA_PROCESSED   = PROJECT_ROOT / "data" / "processed"
DATA_FINAL       = PROJECT_ROOT / "data" / "final"
REPORTS_FIGURES  = PROJECT_ROOT / "reports" / "figures"
REPORTS_EXEC     = PROJECT_ROOT / "reports" / "executive"

# Create output dirs if missing
for _p in [REPORTS_FIGURES, REPORTS_EXEC]:
    _p.mkdir(parents=True, exist_ok=True)

# ── Reproducibility ────────────────────────────────────────────────────────
RANDOM_STATE = 42

# ── Modeling defaults ──────────────────────────────────────────────────────
KMEANS_K_RANGE  = range(2, 11)   # k values to evaluate in elbow method
TSNE_PERPLEXITY = 30.0
PCA_N_COMPONENTS = 2
