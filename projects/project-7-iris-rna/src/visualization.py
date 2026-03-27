"""
visualization.py -- Plotting utilities for analysis results.

Purpose
-------
Centralizes all visualization logic for CRISP-DM Phase 4 (Modeling) and
Phase 5 (Evaluation). Every function saves figures to reports/figures/
and displays them inline in Jupyter.

Design principles
-----------------
- Each function produces one focused chart. No multi-purpose plots.
- All figures saved at 150 DPI for report quality.
- save_path is always optional: functions work in interactive mode without it.
"""

# === Standard library ===
from pathlib import Path

# === Scientific computing -- numerical operations ===
import numpy as np

# === Visualization -- base plotting ===
import matplotlib.pyplot as plt

# === Visualization -- statistical plotting (specialized) ===
import seaborn as sns
