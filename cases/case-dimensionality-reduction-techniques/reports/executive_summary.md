# Executive Summary — Dimensionality Reduction Techniques
## DataMed Analytics — Clinical Dataset Analysis

**Author:** Jose Marcel Lopez Pino
**Role:** Data Scientist — Operations, Analytics & Process Optimization
**Framework:** CRISP-DM + LEAN | Case-Based Learning (CBL)
**Date:** April 2026
**Status:** ![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

---

## 1. Business Context

| | |
|---|---|
| **Industry** | Healthcare / Clinical Analytics |
| **Business Unit** | Data Science — Neurological Studies |
| **Stakeholder** | Data Science Lead / Clinical Visualization Team |
| **Decision to Support** | Select the dimensionality reduction technique to integrate into the early diagnosis classification pipeline |

> **Situation:** DataMed Analytics is developing a classification model for early diagnosis of neurodegenerative diseases using a clinical dataset with 100+ variables per patient. The data science team has identified three critical problems: model overfitting, slow training times, and low interpretability. Dimensionality reduction is required before the clinical center's two-week delivery deadline.

---

## 2. Problem Statement

> Which dimensionality reduction technique — PCA or t-SNE — best addresses the DataMed Analytics pipeline requirements: maximum variance retention, class separability, and compatibility with downstream predictive modeling?

**Business Impact if Unresolved:**
- Classification models trained on 100+ correlated features will overfit, producing unreliable early diagnoses and increasing clinical risk.
- Without dimensionality reduction, training time and memory costs scale quadratically — blocking the two-week delivery commitment.

---

## 3. Analytical Approach

> Non-technical summary — what was done, not how.

| Step | Description |
|---|---|
| **Data** | Wisconsin Breast Cancer dataset (UCI / sklearn) — 569 patients, 30 numerical features, binary clinical target (Malignant / Benign). Clinically analogous proxy for the neurological dataset. |
| **Method** | StandardScaler normalization → PCA (variance analysis + 2D projection + feature loadings) → t-SNE (cluster visualization) → comparative analysis |
| **Tools** | Python · scikit-learn 1.8.0 · NumPy · pandas · Matplotlib · Seaborn |
| **Validation** | PCA: cumulative explained variance curve. t-SNE: KL divergence (< 1.0 threshold). Visual inspection of class separation in 2D projections. |

---

## 4. Key Findings

### Finding 1 — PCA compresses 30 features to 10 components retaining 95% of information

- **Context:** The clinical dataset has 30 correlated numerical features derived from cell nucleus measurements. High multicollinearity is expected in clinical measurement batteries.
- **Analysis:** PC1 alone explains 44.3% of total variance; PC1+PC2 together explain 63.2%. Exactly 10 components are needed to retain 95% of total variance — a 66% reduction from 30 to 10 dimensions.
- **Insight:** The dataset is highly compressible. The sharp scree plot elbow after PC3 confirms strong latent structure — typical of clinical datasets where biological correlations dominate feature relationships.
- **Possible Decision:** Set `PCA(n_components=10)` as the mandatory first step in the classification pipeline, before any classifier training.

### Finding 2 — Cell shape and size features are the primary drivers of PC1

- **Context:** The clinical team needs to understand which original variables the PCA transformation preserves most, to validate biological coherence of the reduction.
- **Analysis:** The top 5 PC1 contributors are: mean concave points (0.261), mean concavity (0.258), worst concave points (0.251), mean compactness (0.239), and worst perimeter (0.237). All relate to cell shape irregularity.
- **Insight:** PC1 captures the biological signal most associated with malignancy — irregular, concave cell shapes. The PCA reduction is not just mathematical compression; it preserves clinically meaningful structure.
- **Possible Decision:** Share the loadings heatmap with the clinical team to validate that the reduced representation aligns with known diagnostic markers.

### Finding 3 — t-SNE achieves superior visual separation but is incompatible with production pipelines

- **Context:** The visualization team required evidence of class separability before committing to a classification strategy.
- **Analysis:** t-SNE produces tight, visually distinct clusters for Malignant and Benign cases (KL divergence = 0.9658, below the 1.0 quality threshold). PCA shows a clear linear boundary but with more overlap in the 2D projection.
- **Insight:** t-SNE is the better tool for communicating separability to clinical stakeholders — but its stochastic nature and absence of a `transform()` method make it structurally incompatible with sklearn Pipeline objects required for production deployment.
- **Possible Decision:** Use t-SNE exclusively for exploratory analysis and stakeholder presentations; use PCA for all pipeline and modeling steps.

---

## 5. Business Recommendations

| Priority | Recommendation | Expected Impact | Effort |
|---|---|---|---|
| 🔴 High | Integrate `PCA(n_components=10)` as first step in the classification pipeline | 66% dimension reduction → faster training, reduced overfitting, lower memory cost | Low |
| 🟡 Medium | Present t-SNE visualizations to the clinical team to validate class separability before model deployment | Builds clinical stakeholder trust; validates the classification approach early | Low |
| 🟢 Low | Evaluate UMAP as a future replacement for t-SNE at scale | Faster than t-SNE (O(n log n) vs O(n²)), supports `transform()`, better preserves global structure | Medium |

---

## 6. Limitations

- **Data:** Wisconsin Breast Cancer is a clinically analogous proxy — all results must be re-validated on the actual DataMed neurological dataset (100+ features) before production use.
- **Model:** This analysis covers dimensionality reduction only. No downstream classifier was trained or evaluated in this case.
- **Scope:** t-SNE is stochastic; despite `random_state=42`, results may vary across library versions or hardware. Not suitable for reproducible production pipelines.
- **Scale:** t-SNE computational cost (O(n²)) becomes prohibitive with thousands of patients and 100+ features — UMAP should be evaluated at that scale.

---

## 7. Next Steps

| Horizon | Action |
|---|---|
| **Immediate** | Apply `PCA(n_components=10)` in a full sklearn Pipeline with LogReg or SVM classifier on this dataset; measure classification performance gain vs. raw features |
| **Short-term** | Benchmark UMAP vs t-SNE on the Wisconsin dataset — compare cluster quality (KL divergence equivalent) and runtime |
| **Long-term** | Apply the validated PCA pipeline to the actual DataMed neurological dataset (100+ features); validate cluster coherence against clinical diagnostic labels |

---

*Framework: CRISP-DM + LEAN | Methodology: Case-Based Learning (CBL)*

**Jose Marcel Lopez Pino**
Data Scientist — Operations, Analytics & Process Optimization | Data Science & Business Analytics
Bootcamp: Fundamentos de Ciencia de Datos — SENCE/Alkemy (2025–2026)

[![GitHub](https://img.shields.io/badge/GitHub-joselopezp-181717?style=flat&logo=github)](https://github.com/joselopezp)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-jose--lopez--pino-0077B5?style=flat&logo=linkedin)](https://www.linkedin.com/in/jose-lopez-pino/)
