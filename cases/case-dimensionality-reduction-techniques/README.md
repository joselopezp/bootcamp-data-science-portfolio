# Case: Dimensionality Reduction Techniques
## DataMed Analytics — Clinical Dataset Dimensionality Reduction

![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![Framework](https://img.shields.io/badge/Framework-CRISP--DM%20%2B%20LEAN-2E86AB)
![Type](https://img.shields.io/badge/Type-CBL%20Case-orange)
![Module](https://img.shields.io/badge/Module-M7%20Unsupervised%20ML-blueviolet)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## Executive Summary

DataMed Analytics faces overfitting and low interpretability when training classification models on a 100+ variable neurological clinical dataset. This case applies PCA and t-SNE to the Wisconsin Breast Cancer dataset (569 patients, 30 features) as a clinically analogous proxy, delivering a technique selection recommendation. **Key result:** PCA reduces 30 features to 10 components retaining 95% of variance (66% dimension reduction); t-SNE achieves superior visual cluster separation (KL divergence = 0.9658). Recommendation: PCA for predictive pipelines, t-SNE for exploratory visualization.

---

## Table of Contents

1. [Business Objective](#business-objective)
2. [Problem Statement Canvas](#problem-statement-canvas)
3. [Solution Overview](#solution-overview)
4. [Repository Structure](#repository-structure)
5. [Key Insights](#key-insights)
6. [Business Recommendations](#business-recommendations)
7. [Limitations](#limitations)
8. [Next Steps](#next-steps)
9. [How to Run](#how-to-run)

---

## Business Objective

**Problem:** Clinical ML models trained on 100+ variable datasets suffer from overfitting, slow processing times, and low interpretability — blocking early diagnosis of neurodegenerative diseases.

**Why it matters:** Delayed early diagnosis increases patient risk and clinical costs. The center expects a functional model in under two weeks.

**Decision to support:** Select the dimensionality reduction technique to integrate into the clinical classification pipeline.

**Expected impact:** Reduced training time, improved model generalization, and actionable visualizations for the clinical team.

---

## Problem Statement Canvas

| Element | Description |
|---|---|
| **Business Problem** | 100+ variable clinical dataset causes overfitting, slow processing, and low model interpretability |
| **Business Impact** | Delayed early diagnosis of neurodegenerative diseases; increased clinical risk |
| **Decision to Support** | Choose between PCA and t-SNE for the DataMed Analytics classification pipeline |
| **Analytical Question** | Which technique best separates diagnostic classes while enabling downstream predictive modeling? |
| **Success Metrics** | PCA: ≥95% variance retained with minimum components. t-SNE: KL divergence < 1.0 |
| **Proposed Approach** | Apply both techniques to a clinically analogous dataset; comparative analysis drives selection |

---

## Solution Overview

| | |
|---|---|
| **Type** | Comparative dimensionality reduction analysis (PCA vs t-SNE) |
| **Dataset** | Wisconsin Breast Cancer — UCI / sklearn (569 patients, 30 numerical features, binary target) |
| **Proxy rationale** | Clinically analogous: high-dimensional numerical features, binary classification, no missing values |
| **End users** | DataMed Analytics data science team; clinical visualization team |
| **Output** | Technique selection recommendation + 5 publication-ready visualizations |
| **Dependencies** | Shared `.venv` at portfolio root — scikit-learn 1.8.0, numpy 2.4.1, pandas 3.0.0, matplotlib 3.10.8, seaborn 0.13.2 |

---

## Repository Structure

```
case-dimensionality-reduction-techniques/
├── README.md                          # This document
├── notebooks/
│   └── case_dimensionality_reduction_techniques.ipynb
├── data/                              # Not used — dataset loaded from sklearn
├── reports/
│   └── executive_summary.md
└── figures/                           # Generated on notebook execution
    ├── fig1_pca_variance.png
    ├── fig2_pca_2d.png
    ├── fig3_tsne_2d.png
    ├── fig4_comparison.png
    └── fig5_pca_loadings.png
```

---

## Key Insights

### Insight 1 — PCA captures 44.3% of variance in a single component

- **Context:** The clinical dataset has 30 correlated numerical features (cell nucleus measurements). High multicollinearity is expected in clinical data.
- **Analysis:** PC1 alone explains 44.3% of total variance; PC1+PC2 together explain 63.2%. The scree plot shows a sharp elbow after PC3, confirming strong underlying structure.
- **Insight:** The dataset is highly compressible — most variance is concentrated in a few directions, which is typical of clinical measurement batteries where features are biologically correlated.
- **Possible Decision:** A DataMed analyst can confidently reduce 30 features to 10 components (95% variance retained) without meaningful information loss before training any classifier.

### Insight 2 — 10 components retain 95% of variance — a 66% dimension reduction

- **Context:** The team needed to know how many components to retain before building the classification pipeline.
- **Analysis:** Cumulative explained variance reaches 95% at exactly 10 components, reducing the feature space from 30 to 10 dimensions (33% of original size).
- **Insight:** A 66% reduction in dimensionality directly translates to faster training, lower memory usage, and reduced overfitting risk — addressing all three pain points identified by the DataMed team.
- **Possible Decision:** Set `PCA(n_components=10)` as the first step in the sklearn Pipeline for the neurodegenerative classification model.

### Insight 3 — t-SNE delivers tighter cluster separation but cannot be used in predictive pipelines

- **Context:** The visualization team needed to inspect whether malignant and benign cases form separable clusters before committing to a classification approach.
- **Analysis:** t-SNE achieves a KL divergence of 0.9658 (< 1.0 threshold), producing visually tight, well-separated clusters. PCA shows a clear linear boundary but with more overlap in the 2D projection.
- **Insight:** t-SNE is superior for exploratory visualization and communicating separability to clinical stakeholders — but its stochastic nature and lack of a `transform()` method make it incompatible with sklearn Pipeline objects for production use.
- **Possible Decision:** Use t-SNE for stakeholder presentations and data quality validation; use PCA for the production pipeline.

---

## Business Recommendations

| Priority | Recommendation | Expected Impact | Effort |
|---|---|---|---|
| 🔴 High | Integrate `PCA(n_components=10)` as first step in the classification pipeline | 66% dimension reduction → faster training, reduced overfitting | Low |
| 🟡 Medium | Use t-SNE visualizations in clinical stakeholder presentations to validate class separability | Builds trust with medical team before model deployment | Low |
| 🟢 Low | Evaluate UMAP as a future alternative to t-SNE | Faster, supports `transform()`, better global structure preservation | Medium |

---

## Limitations

- **Data:** Wisconsin Breast Cancer is a proxy dataset — results must be validated on the actual neurological dataset (100+ features) before production deployment.
- **Model:** This case covers dimensionality reduction only — no downstream classifier trained or evaluated.
- **Scope:** t-SNE results are stochastic; visualizations may vary slightly across runs despite `random_state=42`.
- **t-SNE scalability:** With 100+ features and potentially thousands of patients, t-SNE computational cost (O(n²)) becomes prohibitive — UMAP should be evaluated at that scale.

---

## Next Steps

| Horizon | Action |
|---|---|
| **Immediate** | Apply `PCA(n_components=10)` as preprocessing step in a LogReg or SVM classification pipeline on this dataset |
| **Short-term** | Evaluate UMAP as a modern alternative — faster, supports `transform()`, better preserves global structure |
| **Long-term** | Apply validated pipeline to the actual DataMed neurological dataset (100+ features); validate cluster coherence with clinical labels |

---

## How to Run

```powershell
# From portfolio root — activate shared virtual environment
.venv\Scripts\Activate.ps1

# Navigate to case
cd cases\case-dimensionality-reduction-techniques

# Launch notebook
jupyter lab notebooks\case_dimensionality_reduction_techniques.ipynb
```

> No additional dependencies required — all packages are available in the shared `.venv`.

---

*Framework: CRISP-DM + LEAN | Methodology: Case-Based Learning (CBL)*

**Jose Marcel Lopez Pino**
Data Scientist — Operations, Analytics & Process Optimization | Data Science & Business Analytics
Bootcamp: Fundamentos de Ciencia de Datos — SENCE/Alkemy (2025–2026)

*Industrial Engineering in Chile (Academic degree: Bachelor of Science in Industrial Engineering — 5.5-year program, comparable to a U.S. M.S.) encompasses business strategy, finance, marketing, economics, operations management, and technology management — backed by a rigorous scientific foundation in calculus, linear algebra, probability and statistics, physics, and optimization — enabling a unique business + analytics perspective.*

[![GitHub](https://img.shields.io/badge/GitHub-joselopezp-181717?style=flat&logo=github)](https://github.com/joselopezp)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-jose--lopez--pino-0077B5?style=flat&logo=linkedin)](https://www.linkedin.com/in/jose-lopez-pino/)
