# Dimensional Reduction for Client Segmentation — VisionData

![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![Framework](https://img.shields.io/badge/Framework-CRISP--DM%20%2B%20LEAN-2E86AB)
![Type](https://img.shields.io/badge/Type-CBL%20Case-orange)
![Module](https://img.shields.io/badge/Module-M7%20Unsupervised%20ML-blueviolet)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## Executive Summary

VisionData's survey datasets (60 variables per client) were degrading predictive model performance and producing unreadable executive visualizations. This case applies **PCA** and **t-SNE** to reduce dimensionality to 2D, compares their suitability for two distinct business use cases, and delivers a justified dual recommendation: PCA for ML pipelines, t-SNE for executive presentations.

**Key result:** PCA explains 16.83% of variance in 2 components — confirming the problem is structural. t-SNE (KL divergence: 1.89) reveals three clearly separated client segments invisible to linear projection.

---

## Table of Contents

1. [Business Objective](#business-objective)
2. [Problem Statement Canvas](#problem-statement-canvas)
3. [Solution Overview](#solution-overview)
4. [Repository Structure](#repository-structure)
5. [CRISP-DM Phases](#crisp-dm-phases)
6. [Key Insights](#key-insights)
7. [Business Recommendations](#business-recommendations)
8. [Limitations](#limitations)
9. [Next Steps](#next-steps)
10. [How to Run](#how-to-run)

---

## Business Objective

**Problem:** Survey datasets with 60+ variables per client cause model degradation and unreadable executive visualizations at VisionData.

**Why it matters:** Marketing campaigns designed without clear segment insight waste budget on undifferentiated audiences. Unscalable pipelines block the analytics team as client base grows.

**Decision to support:** Which dimensionality reduction technique should VisionData adopt for (a) ML preprocessing pipelines and (b) executive client segment presentations?

**Expected impact:** Faster model training, improved predictive performance, and marketing visualizations that reveal three actionable client segments.

---

## Problem Statement Canvas

| Element | Description |
|---|---|
| **Business Problem** | 60-variable survey datasets degrade model performance and make client segmentation invisible to decision-makers |
| **Business Impact** | Undifferentiated marketing spend; slow model training; erosion of trust in analytics function |
| **Decision to Support** | PCA vs t-SNE selection for two distinct use cases: ML pipeline vs executive presentation |
| **Analytical Question** | Do PCA and t-SNE reveal natural client clusters, and which is more suitable for each use case? |
| **Success Metrics** | PCA: explained variance ratio quantified. t-SNE: visually distinct clusters without requiring labels |
| **Proposed Approach** | Apply both techniques; compare 2D visualizations; deliver justified dual recommendation |

---

## Solution Overview

| | |
|---|---|
| **Type** | Unsupervised ML — Dimensionality Reduction |
| **Techniques** | PCA (linear) + t-SNE (non-linear) |
| **End Users** | Marketing Director, Head of Sales, ML Engineering team |
| **Output Format** | 2D visualizations + comparative analysis + business recommendation |
| **Dataset** | Synthetic survey dataset — 1,000 clients × 60 variables (15 demographic, 25 consumption, 20 digital) |
| **Key Libraries** | scikit-learn 1.8.0 · matplotlib 3.10.8 · seaborn 0.13.2 · numpy 2.4.1 · pandas 3.0.0 |

---

## Repository Structure

```
case-pca-tsne-dimensionality-reduction/
│
├── README.md
├── notebooks/
│   └── dimensionality_reduction_analysis.ipynb
├── data/
│   └── (no files — synthetic dataset generated in-notebook)
└── reports/
    ├── executive_summary.md
    ├── fig_00_correlation_heatmap.png
    ├── fig_01_pca_scree_plot.png
    ├── fig_02_pca_2d.png
    ├── fig_03_tsne_2d.png
    └── fig_04_comparison_pca_tsne.png
```

---

## CRISP-DM Phases

| Phase | Scope | Key Output |
|---|---|---|
| **Business Understanding** | ✅ Implemented | Problem Statement Canvas — dual use case framing |
| **Data Understanding** | ✅ Implemented | Correlation heatmap confirming inter-feature redundancy |
| **Data Preparation** | ✅ Implemented | StandardScaler applied; 0 missing values confirmed |
| **Modeling** | ✅ Implemented | PCA (full spectrum + 2D) · t-SNE (perplexity=40, max_iter=1000) |
| **Evaluation** | ✅ Implemented | 8-criterion comparison table · dual recommendation · UMAP roadmap |
| **Deployment** | ⬜ Out of scope | CBL learning case — not a production pipeline |

---

## Key Insights

### Insight 1 — 16.83% variance in 2D confirms the problem is structural

**Context:** VisionData suspected high dimensionality was hurting models but lacked quantification.
**Analysis:** PCA's first 2 components explain only 16.83% of total variance (PC1: 8.81%, PC2: 8.02%). Reaching 80% requires 35+ components.
**Insight:** No 2D linear projection can adequately summarize 60 correlated survey variables. This is a structural problem — not solvable by feature selection alone.
**Possible Decision:** Redesign the survey instrument to eliminate redundant variables before the next data collection cycle; target 30–40 high-information variables.

### Insight 2 — t-SNE reveals three actionable segments invisible to PCA

**Context:** Marketing needed readable client groupings to personalize campaign strategy.
**Analysis:** t-SNE (perplexity=40, KL divergence=1.89) produces clearly separated clusters — Digital Natives, Traditional Buyers, High-Value Spenders. PCA shows the same segments with significant overlap.
**Insight:** The segments are real and separable — but only a non-linear technique reveals them visually. Overlap in PCA does not mean segments don't exist; it means linear assumptions are insufficient for this data structure.
**Possible Decision:** Use t-SNE visualizations in the quarterly marketing review to align budget allocation across three distinct client profiles.

### Insight 3 — PCA → t-SNE hybrid resolves the scalability trade-off

**Context:** t-SNE's O(n²) complexity makes it impractical as VisionData's client base grows beyond 50,000 records.
**Analysis:** Applying PCA first (retaining 80% variance) then running t-SNE on the compressed output reduces computational cost ~70% while preserving embedding quality.
**Insight:** The choice between PCA and t-SNE is a false dilemma in production. The industry-standard pattern is PCA for compression, t-SNE (or UMAP) for visualization.
**Possible Decision:** Implement the hybrid pipeline as the standard preprocessing step for all future survey datasets.

---

## Business Recommendations

| Priority | Recommendation | Expected Impact | Effort |
|---|---|---|---|
| 🔴 High | Adopt t-SNE for executive segment visualizations | Marketing gains actionable client maps for campaign design | Low |
| 🔴 High | Implement PCA (80% variance threshold) as ML preprocessing standard | Reduces training time; improves model generalization | Low |
| 🟡 Medium | Deploy hybrid PCA → t-SNE pipeline for production | Eliminates t-SNE bottleneck at scale (50,000+ clients) | Medium |
| 🟢 Low | Evaluate UMAP as long-term t-SNE replacement | Faster O(n log n), reproducible, preserves local + global structure | Medium |

---

## Limitations

**Data:** Synthetic dataset — results are indicative, not confirmatory. Real survey data may have missing values, non-normal distributions, and categorical variables requiring additional preprocessing.

**Model:** t-SNE is stochastic — results vary between runs without fixed seed. KL divergence of 1.89 indicates acceptable but imperfect preservation of high-dimensional structure. No silhouette score computed in this version.

**Scope:** Segment labels derived from ground truth, not from unsupervised discovery. Next iteration should apply KMeans post-reduction and validate with silhouette analysis.

---

## Next Steps

| Horizon | Action |
|---|---|
| **Immediate** | Present `fig_04_comparison_pca_tsne.png` to Marketing with dual-recommendation framing |
| **Short-term** | Add silhouette score; test perplexity sensitivity (20, 30, 40, 50); implement hybrid PCA → t-SNE |
| **Long-term** | Implement UMAP for production scalability; connect with KMeans clustering to complete the unsupervised segmentation arc |

---

## How to Run

```powershell
# From portfolio root — activate shared virtual environment
.venv\Scripts\Activate.ps1

# Navigate to case
cd cases\case-pca-tsne-dimensionality-reduction

# Launch notebook
jupyter lab notebooks\dimensionality_reduction_analysis.ipynb
```

> No additional dependencies required — all libraries are available in the shared `.venv` at portfolio root.

---

*Framework: CRISP-DM + LEAN | Methodology: Case-Based Learning (CBL)*

**Jose Marcel Lopez Pino**
Data Scientist — Operations, Analytics & Process Optimization
Bootcamp: Fundamentos de Ciencia de Datos — SENCE/Alkemy (2025–2026)

*Industrial Engineering in Chile (Academic degree: Bachelor of Science in Industrial Engineering — 5.5-year program, comparable to a U.S. M.S.) encompasses business strategy, finance, marketing, economics, operations management, and technology management — backed by a rigorous scientific foundation in calculus, linear algebra, probability and statistics, physics, and optimization — enabling a unique business + analytics perspective.*

[![GitHub](https://img.shields.io/badge/GitHub-joselopezp-181717?style=flat&logo=github)](https://github.com/joselopezp)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-jose--lopez--pino-0077B5?style=flat&logo=linkedin)](https://www.linkedin.com/in/jose-lopez-pino/)
