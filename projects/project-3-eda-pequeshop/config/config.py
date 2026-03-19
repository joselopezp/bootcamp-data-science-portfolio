"""
Project Configuration.

Centralized settings for paths, parameters, and constants.
"""

from pathlib import Path

# Project paths
PROJECT_ROOT = Path(__file__).parent.parent
DATA_RAW = PROJECT_ROOT / "data" / "raw"
DATA_PROCESSED = PROJECT_ROOT / "data" / "processed"
DATA_FINAL = PROJECT_ROOT / "data" / "final"
REPORTS = PROJECT_ROOT / "reports"
FIGURES = REPORTS / "figures"

# Analysis parameters (adjust per project)
RANDOM_STATE = 42
TEST_SIZE = 0.2
