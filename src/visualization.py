"""
visualization.py — Plotting utilities for clustering and dimensionality reduction.

Purpose
-------
Centralizes all visualization logic for CRISP-DM Phase 4 (Modeling) and
Phase 5 (Evaluation). Every function saves figures to reports/figures/
and displays them inline in Jupyter, following the dual-output convention.

Design principles applied here
-------------------------------
- Each function produces one focused chart. No multi-purpose plots.
- All figures saved at 150 DPI for report quality without excessive file size.
- Color palette: 'Blues_d' for single-variable charts; 'tab10' for cluster
  labels (up to 10 distinct colors, colorblind-aware).
- Noise points from DBSCAN (label -1) are always rendered in gray and
  labeled "Noise" to distinguish them from valid clusters.
- save_path is always optional: functions work in interactive mode without it.
"""

# === Standard library ===
from pathlib import Path

# === Scientific computing — numerical operations ===
import numpy as np

# === Visualization — base plotting (universal) ===
import matplotlib.pyplot as plt

# === Visualization — statistical plotting (specialized) ===
import seaborn as sns

# === Scientific computing — hierarchical clustering for dendrogram (specialized) ===
from scipy.cluster.hierarchy import dendrogram, linkage


# ---------------------------------------------------------------------------
# KMeans elbow curve
# ---------------------------------------------------------------------------


def plot_elbow(
    inertia_dict: dict[int, float],
    save_path: Path | None = None,
) -> None:
    """Plot the KMeans elbow curve to support optimal k selection.

    Inertia (within-cluster SSE) is plotted against k. The analyst selects
    the k at the inflection point where marginal inertia reduction becomes
    small -- analogous to a diminishing returns curve in process optimization.

    Args:
        inertia_dict: Dict {k: inertia} returned by analysis.elbow_method().
                      Keys are k values; values are inertia floats.
        save_path: Optional path to save the figure as PNG.
                   If None, figure is displayed but not saved.

    Example:
        >>> plot_elbow(inertia_dict, save_path=REPORTS_FIGURES / "elbow.png")
    """
    ks = list(inertia_dict.keys())
    inertias = list(inertia_dict.values())

    fig, ax = plt.subplots(figsize=(8, 5))

    ax.plot(ks, inertias, marker="o", color="steelblue", linewidth=2, markersize=7)
    ax.set_xlabel("Number of Clusters (k)", fontsize=12)
    ax.set_ylabel("Inertia (Within-cluster SSE)", fontsize=12)
    ax.set_title("Elbow Method — Optimal k Selection", fontsize=14)

    # Show integer ticks only for cleaner x-axis
    ax.set_xticks(ks)

    plt.tight_layout()

    if save_path:
        fig.savefig(save_path, dpi=150, bbox_inches="tight")

    plt.show()


# ---------------------------------------------------------------------------
# 2D cluster scatter plots (PCA or t-SNE)
# ---------------------------------------------------------------------------


def plot_clusters_2d(
    X_2d: np.ndarray,
    labels: np.ndarray,
    title: str,
    method: str = "PCA",
    save_path: Path | None = None,
) -> None:
    """Scatter plot of 2D-reduced customer data colored by cluster assignment.

    Used for both PCA and t-SNE embeddings. DBSCAN noise points (label -1)
    are rendered in gray and labeled separately to avoid confusion with
    valid clusters.

    Args:
        X_2d: 2D array of shape (n_samples, 2) from run_pca() or run_tsne().
        labels: Cluster assignment array of shape (n_samples,).
                Value -1 indicates DBSCAN noise points.
        title: Chart title. Should include algorithm name and embedding type
               (e.g., "KMeans (k=4) — t-SNE").
        method: Reduction method used, for axis labels. Either "PCA" or "t-SNE".
        save_path: Optional path to save the figure as PNG.

    Example:
        >>> plot_clusters_2d(X_pca, km_labels, "KMeans (k=4) — PCA",
        ...                  method="PCA", save_path=REPORTS_FIGURES / "km_pca.png")
    """
    unique_labels = sorted(set(labels))

    # tab10 palette supports up to 10 distinct cluster colors
    palette = sns.color_palette("tab10", n_colors=max(len(unique_labels), 1))

    fig, ax = plt.subplots(figsize=(9, 6))

    for i, label in enumerate(unique_labels):
        mask = labels == label

        # DBSCAN noise points rendered separately in gray
        display_label = "Noise" if label == -1 else f"Cluster {label}"
        color = "gray" if label == -1 else palette[i]

        ax.scatter(
            X_2d[mask, 0],
            X_2d[mask, 1],
            label=display_label,
            alpha=0.7,
            s=40,
            color=color,
        )

    ax.set_xlabel(f"{method} Component 1", fontsize=12)
    ax.set_ylabel(f"{method} Component 2", fontsize=12)
    ax.set_title(title, fontsize=14)
    ax.legend(loc="best", fontsize=10)

    plt.tight_layout()

    if save_path:
        fig.savefig(save_path, dpi=150, bbox_inches="tight")

    plt.show()


# ---------------------------------------------------------------------------
# Hierarchical clustering dendrogram
# ---------------------------------------------------------------------------


def plot_dendrogram(
    X: np.ndarray,
    method: str = "ward",
    truncate_p: int = 12,
    save_path: Path | None = None,
) -> None:
    """Plot a hierarchical clustering dendrogram from the feature matrix.

    The dendrogram reveals the natural cluster structure before specifying k.
    Large vertical gaps between merges indicate strong cluster boundaries --
    the optimal k corresponds to the level where the largest gaps appear.

    Truncation is applied for readability: only the last `truncate_p` merges
    are shown, with leaf labels indicating the number of samples in each
    collapsed subtree.

    Args:
        X: Scaled feature matrix of shape (n_samples, n_features).
           The linkage matrix is computed internally from X.
           For large datasets (n > 5000), pass PCA-reduced X to reduce
           computation time.
        method: Linkage method. Should match the linkage used in
                run_hierarchical() for consistency. Options: 'ward',
                'complete', 'average', 'single'.
        truncate_p: Number of final merges to display. Lower values produce
                    a cleaner chart; higher values show more detail.
        save_path: Optional path to save the figure as PNG.

    Example:
        >>> plot_dendrogram(X_pca, method="ward", truncate_p=12,
        ...                 save_path=REPORTS_FIGURES / "dendrogram.png")
    """
    # Compute linkage matrix from the feature matrix
    linked = linkage(X, method=method)

    fig, ax = plt.subplots(figsize=(12, 6))

    dendrogram(
        linked,
        truncate_mode="lastp",  # Show only the last p merges
        p=truncate_p,
        leaf_rotation=45,
        ax=ax,
    )

    ax.set_title(
        f"Hierarchical Clustering Dendrogram (linkage='{method}')", fontsize=14
    )
    ax.set_xlabel("Customer Index / Cluster Size (n)", fontsize=12)
    ax.set_ylabel("Merge Distance", fontsize=12)

    plt.tight_layout()

    if save_path:
        fig.savefig(save_path, dpi=150, bbox_inches="tight")

    plt.show()


# ---------------------------------------------------------------------------
# Algorithm comparison chart
# ---------------------------------------------------------------------------


def plot_silhouette_comparison(
    scores: dict[str, float | None],
    save_path: Path | None = None,
) -> None:
    """Bar chart comparing silhouette scores across clustering algorithms.

    Silhouette score ranges from -1 (poor) to +1 (perfect separation).
    A horizontal reference line at 0.35 marks the minimum acceptable
    threshold for commercially interpretable retail customer segments.

    Algorithms with None scores (e.g., DBSCAN with only 1 cluster found)
    are excluded from the chart but logged to the console.

    Args:
        scores: Dict mapping algorithm name to silhouette score or None.
                Example: {"KMeans": 0.42, "DBSCAN": None, "Hierarchical": 0.38}
        save_path: Optional path to save the figure as PNG.

    Example:
        >>> plot_silhouette_comparison(scores,
        ...     save_path=REPORTS_FIGURES / "silhouette_comparison.png")
    """
    # Exclude None scores (algorithm produced fewer than 2 clusters)
    valid_scores = {k: v for k, v in scores.items() if v is not None}
    excluded = [k for k, v in scores.items() if v is None]

    if excluded:
        print(f"Excluded from chart (score undefined): {excluded}")

    colors = sns.color_palette("Blues_d", n_colors=len(valid_scores))

    fig, ax = plt.subplots(figsize=(7, 5))

    bars = ax.bar(
        valid_scores.keys(),
        valid_scores.values(),
        color=colors,
        edgecolor="white",
        width=0.5,
    )

    # Annotate each bar with its exact score value
    ax.bar_label(bars, fmt="%.3f", padding=4, fontsize=11)

    # Reference line: minimum acceptable silhouette for business interpretability
    ax.axhline(
        0.35,
        color="red",
        linestyle="--",
        linewidth=1.2,
        label="Minimum target (0.35)",
    )

    ax.set_ylim(0, 1)
    ax.set_ylabel("Silhouette Score", fontsize=12)
    ax.set_title("Algorithm Comparison — Silhouette Score", fontsize=14)
    ax.legend(fontsize=10)

    plt.tight_layout()

    if save_path:
        fig.savefig(save_path, dpi=150, bbox_inches="tight")

    plt.show()
