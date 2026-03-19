"""
Visualization Module.

Functions for creating charts and plots.
Supports CRISP-DM phases 2 (Data Understanding) and 5 (Evaluation).

Author: Jose Marcel Lopez Pino
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


# Default style configuration
FIGURE_SIZE = (10, 6)
STYLE = "seaborn-v0_8-whitegrid"
PALETTE = "Set2"
DPI = 150


def setup_style():
    """Configure default matplotlib/seaborn style."""
    plt.style.use(STYLE)
    sns.set_palette(PALETTE)
    plt.rcParams["figure.figsize"] = FIGURE_SIZE
    plt.rcParams["figure.dpi"] = DPI


def save_figure(fig, filename: str, folder: str = "reports/figures"):
    """Save figure to reports/figures directory.

    Args:
        fig: Matplotlib figure object.
        filename: Name for the saved file (without extension).
        folder: Target folder path.
    """
    filepath = f"{folder}/{filename}.png"
    fig.savefig(filepath, bbox_inches="tight", dpi=DPI)
    print(f"Figure saved: {filepath}")
