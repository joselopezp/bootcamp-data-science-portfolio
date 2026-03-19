"""
analysis.py — Dimensionality reduction and clustering utilities.

Purpose
-------
Implements the modeling pipeline for CRISP-DM Phase 4. Each function wraps
a specific algorithm with consistent return signatures so the evaluation
notebook (Phase 5) can compare results uniformly across methods.

Business context
----------------
The goal is customer behavioral segmentation for Auto Industry Insights S.A.
Dimensionality reduction (PCA, t-SNE) serves two purposes: visualization
of high-dimensional customer data in 2D, and noise reduction before
applying clustering algorithms.

Algorithm selection rationale (recorded in docs/decisions_log.md)
------------------------------------------------------------------
- KMeans: baseline; fast, interpretable, works well on normalized data.
- DBSCAN: detects arbitrary-shaped clusters and flags noise (outlier
  customers that do not belong to any segment).
- Hierarchical: produces a dendrogram that helps visually confirm the
  optimal number of clusters before committing to k.
- PCA: linear reduction; preserves global variance structure.
- t-SNE: non-linear reduction; preserves local neighborhood structure,
  better for revealing cluster separation visually.
"""

# === Scientific computing — numerical operations ===
import numpy as np

# === Machine learning — clustering algorithms (specialized) ===
from sklearn.cluster import AgglomerativeClustering, DBSCAN, KMeans

# === Machine learning — dimensionality reduction (specialized) ===
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

# === Machine learning — cluster quality evaluation (specialized) ===
from sklearn.metrics import silhouette_score


# ---------------------------------------------------------------------------
# Dimensionality reduction
# ---------------------------------------------------------------------------


def run_pca(
    X: np.ndarray,
    n_components: int = 2,
    random_state: int = 42,
) -> tuple[np.ndarray, PCA]:
    """Reduce feature matrix dimensionality using Principal Component Analysis.

    PCA finds the directions of maximum variance in the data (principal
    components) and projects all observations onto those axes. Used here for:
    1. 2D visualization of the customer feature space.
    2. Noise reduction before t-SNE (applying PCA first improves t-SNE
       stability on high-dimensional data — see run_tsne docstring).

    The fitted PCA object is returned to allow inspection of explained
    variance ratios and component loadings in the evaluation notebook.

    Args:
        X: Scaled feature matrix of shape (n_samples, n_features).
           Must be StandardScaler-normalized before calling this function.
        n_components: Number of principal components to retain.
                      Use 2 for 2D visualization; use higher values
                      (e.g., 10-50) as input to t-SNE.
        random_state: Seed for reproducibility of randomized SVD solver.

    Returns:
        Tuple of:
            - X_pca: Transformed array of shape (n_samples, n_components).
            - pca: Fitted PCA object. Access pca.explained_variance_ratio_
                   to inspect how much variance each component captures.

    Example:
        >>> X_pca, pca = run_pca(X, n_components=2)
        >>> print(f"Variance explained: {pca.explained_variance_ratio_.sum():.1%}")
    """
    pca = PCA(n_components=n_components, random_state=random_state)
    X_pca = pca.fit_transform(X)

    return X_pca, pca


def run_tsne(
    X: np.ndarray,
    n_components: int = 2,
    perplexity: float = 30.0,
    random_state: int = 42,
) -> np.ndarray:
    """Reduce dimensionality using t-Distributed Stochastic Neighbor Embedding.

    t-SNE is a non-linear technique that preserves local neighborhood
    structure. Unlike PCA (which preserves global variance), t-SNE is
    optimized for 2D/3D visualization and reveals cluster separation
    that PCA may miss.

    Important: t-SNE distances between clusters are NOT interpretable.
    Only the presence of distinct groups matters. Do not infer that
    clusters far apart in t-SNE space are more different than close ones.

    Recommended practice applied here: run PCA first (to 10-50 components)
    and pass the PCA output to t-SNE. This reduces noise, speeds up
    computation, and improves embedding stability on high-dim retail data.

    Args:
        X: Feature matrix input. For best results, pass PCA-reduced data
           (n_components=10-50) rather than the full scaled matrix.
        n_components: Number of output dimensions. Use 2 for scatter plots.
        perplexity: Controls the effective number of neighbors considered
                    per point. Typical range: 5-50. Larger datasets benefit
                    from higher perplexity (30-50).
        random_state: Seed for reproducibility. t-SNE is stochastic;
                      fixing the seed is essential for consistent outputs.

    Returns:
        Transformed array of shape (n_samples, n_components).

    Example:
        >>> X_pca, _ = run_pca(X, n_components=10)
        >>> X_tsne = run_tsne(X_pca, perplexity=30.0)
    """
    tsne = TSNE(
        n_components=n_components,
        perplexity=perplexity,
        random_state=random_state,
    )
    return tsne.fit_transform(X)


# ---------------------------------------------------------------------------
# Cluster count selection
# ---------------------------------------------------------------------------


def elbow_method(
    X: np.ndarray,
    k_range: range,
    random_state: int = 42,
) -> dict[int, float]:
    """Compute KMeans inertia for a range of k values (elbow curve data).

    Inertia measures the total within-cluster sum of squared distances to
    centroids. As k increases, inertia decreases monotonically. The optimal k
    is at the elbow: the point where additional clusters yield diminishing
    returns in inertia reduction.

    Business framing: choosing k is equivalent to deciding how many distinct
    customer personas the marketing team can realistically act upon. More
    clusters = more tailored campaigns but higher operational complexity.

    Args:
        X: Scaled feature matrix of shape (n_samples, n_features).
        k_range: Range of k values to evaluate (e.g., range(2, 11)).
                 Minimum k=2 is required for silhouette score calculation.
        random_state: Seed for KMeans centroid initialization.

    Returns:
        Dictionary mapping each k to its inertia value.
        Pass this directly to visualization.plot_elbow().

    Example:
        >>> inertia = elbow_method(X, k_range=range(2, 11))
        >>> plot_elbow(inertia, save_path=REPORTS_FIGURES / "elbow.png")
    """
    return {
        k: KMeans(
            n_clusters=k,
            random_state=random_state,
            n_init=10,  # Run 10 initializations; keep best result
        )
        .fit(X)
        .inertia_
        for k in k_range
    }


# ---------------------------------------------------------------------------
# Clustering algorithms
# ---------------------------------------------------------------------------


def run_kmeans(
    X: np.ndarray,
    n_clusters: int,
    random_state: int = 42,
) -> tuple[np.ndarray, float]:
    """Fit KMeans clustering and return cluster labels with silhouette score.

    KMeans partitions n_samples into k clusters by minimizing within-cluster
    variance (inertia). It assumes clusters are convex and roughly equal in
    size — a reasonable starting assumption for customer segmentation.

    Used as the primary algorithm here because it is fast, interpretable,
    and its cluster centroids directly map to customer persona profiles
    (mean feature values per cluster).

    Args:
        X: Scaled feature matrix of shape (n_samples, n_features).
        n_clusters: Number of clusters. Determine from elbow_method() output.
        random_state: Seed for centroid initialization reproducibility.

    Returns:
        Tuple of:
            - labels: Integer cluster assignment per sample, shape (n_samples,).
            - silhouette: Float in [-1, 1]. Values above 0.35 indicate
                          reasonable cluster separation for retail data.

    Example:
        >>> labels, score = run_kmeans(X, n_clusters=4)
        >>> print(f"Silhouette: {score:.3f}")
    """
    km = KMeans(
        n_clusters=n_clusters,
        random_state=random_state,
        n_init=10,  # Multiple restarts prevent poor local minima
    )
    labels = km.fit_predict(X)

    # Silhouette score: mean distance to own cluster vs. nearest other cluster
    silhouette = silhouette_score(X, labels)

    return labels, silhouette


def run_dbscan(
    X: np.ndarray,
    eps: float = 0.5,
    min_samples: int = 5,
) -> tuple[np.ndarray, float | None]:
    """Fit DBSCAN density-based clustering and return labels with silhouette score.

    DBSCAN groups points that are densely connected (within eps distance of
    at least min_samples neighbors). Unlike KMeans, it does not require
    specifying k in advance and can detect arbitrarily shaped clusters.

    Key output difference from KMeans: label -1 indicates noise points --
    customers that do not belong to any dense cluster. These may represent
    truly unusual customers worth separate investigation.

    Limitation: DBSCAN is sensitive to eps and min_samples. Apply on
    PCA-reduced data (not the full feature matrix) to mitigate the curse
    of dimensionality, which inflates all pairwise distances uniformly
    and makes eps calibration unreliable in high dimensions.

    Args:
        X: Scaled feature matrix. Prefer PCA-reduced (2-10 components)
           over the full matrix for eps stability.
        eps: Maximum distance between two points to be considered neighbors.
             Start with 0.5 on PCA-reduced data; adjust based on results.
        min_samples: Minimum neighbors required to form a core point.
                     Rule of thumb: n_features * 2, minimum 5.

    Returns:
        Tuple of:
            - labels: Cluster assignments. Label -1 = noise point.
            - silhouette: Float silhouette score, or None if fewer than
                          2 clusters are found (score is undefined).

    Example:
        >>> labels, score = run_dbscan(X_pca, eps=0.5, min_samples=5)
        >>> n_noise = (labels == -1).sum()
        >>> print(f"Noise points: {n_noise} | Score: {score}")
    """
    db = DBSCAN(eps=eps, min_samples=min_samples)
    labels = db.fit_predict(X)

    # Count valid clusters, excluding noise label (-1)
    n_clusters = len(set(labels)) - (1 if -1 in labels else 0)

    # Silhouette score requires at least 2 clusters to be meaningful
    silhouette = silhouette_score(X, labels) if n_clusters > 1 else None

    return labels, silhouette


def run_hierarchical(
    X: np.ndarray,
    n_clusters: int,
    linkage: str = "ward",
) -> tuple[np.ndarray, float]:
    """Fit Agglomerative Hierarchical Clustering and return labels with silhouette.

    Hierarchical clustering builds a tree (dendrogram) by iteratively merging
    the most similar pairs of clusters. The dendrogram is visualized in
    visualization.plot_dendrogram() to visually confirm the optimal k before
    committing to a partition.

    Ward linkage chosen as default: it minimizes the total within-cluster
    variance at each merge step, making it consistent with KMeans objective
    and therefore a fair comparison baseline.

    Args:
        X: Scaled feature matrix of shape (n_samples, n_features).
        n_clusters: Number of clusters for the final partition.
                    Should match the k used in run_kmeans() for comparability.
        linkage: Merge criterion. Options:
                 'ward'     -- minimizes within-cluster variance (default).
                 'complete' -- maximizes distance between cluster extremes.
                 'average'  -- uses mean pairwise distance between clusters.

    Returns:
        Tuple of:
            - labels: Integer cluster assignment per sample, shape (n_samples,).
            - silhouette: Float silhouette score for this partition.

    Example:
        >>> labels, score = run_hierarchical(X, n_clusters=4, linkage="ward")
        >>> print(f"Hierarchical silhouette: {score:.3f}")
    """
    hc = AgglomerativeClustering(n_clusters=n_clusters, linkage=linkage)
    labels = hc.fit_predict(X)

    silhouette = silhouette_score(X, labels)

    return labels, silhouette
