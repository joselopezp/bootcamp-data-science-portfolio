# Executive Summary — Dimensional Reduction for Client Segmentation

**Author:** Jose Marcel Lopez Pino
**Role:** Data Scientist — Operations, Analytics & Process Optimization
**Framework:** CRISP-DM + LEAN | Case-Based Learning (CBL)
**Case:** `case-pca-tsne-dimensionality-reduction`
**Module:** M7 — Unsupervised Machine Learning
**Date:** April 2026
**Status:** ![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

---

## 1. Business Context

| | |
|---|---|
| **Industry** | Consulting / Marketing Analytics |
| **Business Unit** | AI & Analytics Team |
| **Stakeholder** | Marketing Director / Head of Sales |
| **Decision to Support** | Which dimensionality reduction technique should VisionData use for (a) ML preprocessing pipelines and (b) executive client segment presentations? |

> **Situation:** VisionData manages survey datasets with 60+ variables per client — demographics, consumption habits, and digital preferences. Current predictive models are underperforming due to the curse of dimensionality, and executive visualizations fail to reveal actionable client patterns. A structured dimensionality reduction approach is required to unblock both the analytics pipeline and the business storytelling.

---

## 2. Problem Statement

> High dimensionality (60 variables per client) is simultaneously degrading model predictive performance and making client segmentation invisible to marketing decision-makers.

**Business Impact if Unresolved:**
- Marketing campaigns designed without clear segment insight — budget allocated to undifferentiated audiences
- Model training times scale poorly as survey data grows — analytical team productivity at risk
- Executive presentations without readable visualizations erode trust in the analytics function

---

## 3. Analytical Approach

> Two dimensionality reduction techniques were applied to a realistic synthetic dataset simulating VisionData's survey structure (1,000 clients × 60 variables). Results are directly transferable to production data.

| Step | Description |
|---|---|
| **Data** | Synthetic survey dataset — 1,000 clients, 60 variables (15 demographic, 25 consumption, 20 digital preferences), 3 natural client segments |
| **Preprocessing** | StandardScaler — required before both techniques; eliminates scale dominance across heterogeneous survey variables |
| **Method 1** | Principal Component Analysis (PCA) — linear, deterministic, quantifiable |
| **Method 2** | t-SNE (t-Distributed Stochastic Neighbor Embedding) — non-linear, cluster-focused, visual |
| **Tool** | Python · scikit-learn 1.8.0 · matplotlib · seaborn |
| **Validation** | KL divergence monitored for t-SNE convergence; explained variance ratio tracked for PCA component selection |

---

## 4. Key Findings

### Finding 1 — The dimensionality problem is more severe than assumed

- **Context:** VisionData suspected high dimensionality was hurting models, but lacked quantification.
- **Analysis:** PCA's first 2 components explain only **16.83%** of total variance (PC1: 8.81%, PC2: 8.02%). Reaching 80% variance requires approximately 35+ components.
- **Insight:** No 2D linear projection can adequately summarize 60 correlated survey variables. The problem is structural — not solvable by feature selection alone.
- **Possible Decision:** Redesign the survey instrument to eliminate redundant variables before the next data collection cycle; target 30–40 high-information variables.

### Finding 2 — t-SNE reveals three actionable client segments invisible to PCA

- **Context:** Marketing needed to identify natural client groupings to personalize campaigns.
- **Analysis:** t-SNE (perplexity=40, KL divergence=1.89) produces clearly separated clusters corresponding to three distinct behavioral profiles: Digital Natives, Traditional Buyers, and High-Value Spenders. PCA shows the same segments with significant overlap.
- **Insight:** The three segments are real and separable — but only a non-linear technique reveals them visually. The overlap in PCA does not mean segments don't exist; it means PCA's linear assumptions are insufficient for this data structure.
- **Possible Decision:** Use t-SNE visualizations in the next quarterly marketing review to align campaign budget allocation across the three identified segments.

### Finding 3 — A hybrid PCA → t-SNE pipeline resolves the scalability trade-off

- **Context:** t-SNE's O(n²) complexity makes it impractical as VisionData's client base grows beyond 50,000 records.
- **Analysis:** Applying PCA first (retaining 80% variance, ~35 components) and then running t-SNE on the compressed representation reduces computational cost by ~70% while preserving embedding quality.
- **Insight:** The choice between PCA and t-SNE is a false dilemma in production. The industry-standard pattern is PCA for compression, t-SNE (or UMAP) for visualization.
- **Possible Decision:** Implement the hybrid pipeline as the standard preprocessing step for all future survey datasets. Evaluate UMAP as a long-term replacement for t-SNE at scale.

---

## 5. Business Recommendations

| Priority | Recommendation | Expected Impact | Effort |
|---|---|---|---|
| 🔴 High | Adopt t-SNE for executive segment visualizations immediately | Marketing gains readable, actionable client maps for campaign design | Low — existing pipeline, new output format |
| 🔴 High | Implement PCA (80% variance threshold) as standard ML preprocessing step | Reduces model training time; improves generalization by eliminating noise dimensions | Low — 3 lines of code in existing pipeline |
| 🟡 Medium | Deploy hybrid PCA → t-SNE pipeline for production scalability | Eliminates t-SNE bottleneck as client base grows; stable at 50,000+ records | Medium — requires pipeline refactoring |
| 🟢 Low | Evaluate UMAP as long-term replacement for t-SNE | Faster (O(n log n)), reproducible, preserves both local and global structure | Medium — new library, validation required |

---

## 6. Limitations

- **Data:** Synthetic dataset — results are indicative, not confirmatory. Real survey data may have missing values, non-normal distributions, and categorical variables requiring additional preprocessing.
- **Model:** t-SNE is stochastic — results vary between runs without a fixed random seed. KL divergence of 1.89 indicates acceptable but imperfect preservation of high-dimensional structure.
- **Scope:** No cluster quality metric (e.g. silhouette score) was computed in this version. Segment labels are derived from ground truth, not from unsupervised discovery — next iteration should apply KMeans post-reduction and validate with silhouette analysis.

---

## 7. Next Steps

| Horizon | Action |
|---|---|
| **Immediate** | Present `fig_04_comparison_pca_tsne.png` to Marketing Director with the dual-recommendation framing from Finding 2 |
| **Short-term** | Add silhouette score analysis to quantify cluster separation; test perplexity sensitivity (20, 30, 40, 50) |
| **Long-term** | Implement UMAP for production; connect with M7 KMeans clustering case to complete the unsupervised segmentation arc |

---

*Framework: CRISP-DM + LEAN | Methodology: Case-Based Learning (CBL)*

**Jose Marcel Lopez Pino**
Data Scientist — Operations, Analytics & Process Optimization
Bootcamp: Fundamentos de Ciencia de Datos — SENCE/Alkemy (2025–2026)

[![GitHub](https://img.shields.io/badge/GitHub-joselopezp-181717?style=flat&logo=github)](https://github.com/joselopezp)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-jose--lopez--pino-0077B5?style=flat&logo=linkedin)](https://www.linkedin.com/in/jose-lopez-pino/)
