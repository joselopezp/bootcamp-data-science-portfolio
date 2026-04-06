# Case: Dimensionality Reduction Techniques
## Customer Personality Analysis — PCA vs t-SNE

![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![Framework](https://img.shields.io/badge/Framework-CRISP--DM%20%2B%20LEAN-2E86AB)
![Type](https://img.shields.io/badge/Type-CBL%20Case-orange)
![Module](https://img.shields.io/badge/Module-M7%20Unsupervised%20ML-blueviolet)
![License](https://img.shields.io/badge/License-MIT-yellow)

> **VisionData** needs to compress a 100+ variable customer survey dataset into 2D to reveal natural segments for marketing campaign targeting. This case applies PCA and t-SNE to a real customer personality dataset (2,240 customers × 30 engineered features), compares their ability to expose cluster structure, and produces a justified two-track technique recommendation. **Key result:** PCA retains 28.8% variance in 2D (95% at 24 components); t-SNE achieves superior cluster separation with KL divergence = 0.8887.

---

## Table of Contents

1. [Business Objective](#1-business-objective)
2. [Problem Statement Canvas](#2-problem-statement-canvas)
3. [Dataset](#3-dataset)
4. [Repository Structure](#4-repository-structure)
5. [CRISP-DM Scope](#5-crisp-dm-scope)
6. [Key Findings](#6-key-findings)
7. [Business Recommendations](#7-business-recommendations)
8. [Limitations](#8-limitations)
9. [Next Steps](#9-next-steps)
10. [How to Run](#10-how-to-run)

---

## 1. Business Objective

**Problem:** Customer survey datasets with 100+ variables cause slow ML model training and produce unreadable executive visualisations — preventing the marketing team from identifying actionable customer segments.

**Why it matters:** Without visible segment structure, all customers receive the same campaign — wasting budget and reducing ROI.

**Decision to support:** Select the dimensionality reduction technique that best reveals natural customer clusters for differentiated campaign targeting.

**Expected impact:** Enables segment-specific marketing campaigns; reduces ML training dimensionality from 30 to 24 features (20% reduction) while retaining 95% of information.

---

## 2. Problem Statement Canvas

| # | Element | Content |
|---|---------|---------|
| 1 | **Business Problem** | Survey datasets with 100+ variables make ML models slow and executive visualisations unreadable |
| 2 | **Business Impact** | Marketing campaigns cannot be differentiated — all customers treated equally despite distinct behaviour |
| 3 | **Decision to Support** | Which dimensionality reduction technique best reveals natural customer clusters for campaign targeting? |
| 4 | **Analytical Question** | Can PCA or t-SNE compress 30 engineered customer features into 2D while preserving segment structure? |
| 5 | **Success Metrics** | PCA: cumulative variance retained. t-SNE: KL divergence < 1.0. Justified recommendation with documented trade-offs |
| 6 | **Proposed Approach** | Apply both techniques to real customer data; comparative analysis drives technique selection |

---

## 3. Dataset

| Field | Detail |
|-------|--------|
| **Source** | [Customer Personality Analysis — Kaggle (imakash3011)](https://www.kaggle.com/datasets/imakash3011/customer-personality-analysis) |
| **File** | `marketing_campaign.csv` (tab-separated) |
| **Raw dimensions** | 2,240 customers × 29 variables |
| **Engineered features** | 30 features after preparation |
| **Feature groups** | Demographics · Spend by category · Purchase channel · Campaign acceptance · Encoded marital status |

**Final feature list (30):**

| Group | Features |
|-------|----------|
| Demographics | `Education` (ordinal) · `Income` · `Kidhome` · `Teenhome` · `Age` · `Seniority_Days` |
| Spend | `MntWines` · `MntFruits` · `MntMeatProducts` · `MntFishProducts` · `MntSweetProducts` · `MntGoldProds` |
| Channel | `NumDealsPurchases` · `NumWebPurchases` · `NumCatalogPurchases` · `NumStorePurchases` · `NumWebVisitsMonth` |
| Campaigns | `AcceptedCmp1` · `AcceptedCmp2` · `AcceptedCmp3` · `AcceptedCmp4` · `AcceptedCmp5` |
| Marital Status | `Alone` · `Divorced` · `Married` · `Single` · `Together` · `Widow` · `YOLO` (dummy encoded) |

**Preparation decisions:**
- `Income`: 24 nulls (1.1%) → median imputation applied first, before any transformation
- `Age`: engineered from `Year_Birth` (`2024 - Year_Birth`)
- `Seniority_Days`: days since `Dt_Customer` relative to most recent enrollment date
- Removed: `ID`, `Z_CostContact`, `Z_Revenue` (non-informative) · `Response`, `Complain` (target-like)
- Scaling: `StandardScaler` — mandatory for distance-based techniques

---

## 4. Repository Structure

```
case-pca-tsne-dimensionality-reduction/
│
├── README.md                          # This file
├── notebooks/
│   └── case_pca_tsne_dimensionality_reduction.ipynb   # Main analysis notebook
├── data/
│   ├── raw/
│   │   └── marketing_campaign.csv     # Original dataset (Kaggle)
│   ├── processed/
│   │   └── marketing_scaled.csv       # StandardScaler output (30 features)
│   └── final/
└── reports/
    ├── executive_summary.md           # 1-page business summary
    └── figures/
        ├── fig1_spend_distributions.png
        ├── fig2_pca_explained_variance.png
        ├── fig3_pca_2d.png
        ├── fig4_tsne_2d.png
        └── fig5_comparison.png
```

---

## 5. CRISP-DM Scope

| Phase | Status | Key Output |
|-------|--------|------------|
| 1. Business Understanding | ✅ Complete | Problem Statement Canvas · LEAN Value Statement |
| 2. Data Understanding | ✅ Complete | Shape profiling · missing values · spend distribution (Fig 1) |
| 3. Data Preparation | ✅ Complete | Feature engineering · encoding · imputation · StandardScaler |
| 4. Modeling | ✅ Complete | PCA (Fig 2, 3) · t-SNE with PCA pre-reduction (Fig 4) |
| 5. Evaluation | ✅ Complete | Side-by-side comparison (Fig 5) · justified two-track recommendation |
| 6. Deployment | ⚠️ Out of scope | CBL case — technique selection only, not production integration |

---

## 6. Key Findings

### Finding 1 — PCA retains only 28.8% variance in 2D
- **Context:** Marketing needs a 2D visualisation for executive presentations.
- **Analysis:** PC1 = 21.5%, PC2 = 7.3% → combined 28.8% variance retained. Reaching 80% requires 16 components; 95% requires 24.
- **Insight:** A 2D PCA projection loses over 70% of information — insufficient for clear cluster visualisation, though PC1 is driven by spend variables (interpretable axis).
- **Possible Decision:** Use PCA at 24 components as ML preprocessing — not as the primary visualisation tool.

### Finding 2 — t-SNE reveals compact, well-separated customer clusters
- **Context:** Same 2,240 customers projected via t-SNE (perplexity=40, PCA pre-reduction to 24 components).
- **Analysis:** KL divergence = **0.8887** — below the 1.0 quality threshold. Visually distinct cluster structures emerged that were invisible in PCA 2D.
- **Insight:** t-SNE successfully reveals natural customer groupings — directly actionable for the marketing team without requiring statistical expertise to interpret.
- **Possible Decision:** Use t-SNE 2D output as the basis for customer segment maps in marketing decks.

### Finding 3 — The two techniques are complementary, not competing
- **Context:** Marketing needs both executive visualisation and a preprocessing step for predictive models.
- **Analysis:** t-SNE has no `transform()` method — cannot score new customers or integrate into sklearn pipelines. PCA does.
- **Insight:** Each technique solves a different problem. A single-tool recommendation would create either an analytically limited or operationally incomplete solution.
- **Possible Decision:** Adopt a two-track approach — t-SNE for exploration and presentation; PCA (24 components) for all ML pipeline preprocessing.

---

## 7. Business Recommendations

| Priority | Recommendation | Expected Impact | Effort |
|---|---|---|---|
| 🔴 High | Deploy t-SNE visualisation for marketing segment presentation | Enables differentiated campaign targeting across identified clusters | Low |
| 🔴 High | Apply PCA (24 components) as preprocessing for all downstream ML models | Reduces dimensionality 30→24 retaining 95% variance; faster training | Low |
| 🟡 Medium | Overlay KMeans cluster labels on t-SNE plot for actionable segment profiles | Quantifies segment size and behaviour for budget allocation | Medium |
| 🟢 Low | Evaluate UMAP as long-term replacement for t-SNE | Faster at scale, supports `transform()`, better global structure preservation | Medium |

---

## 8. Limitations

- **Data:** Single snapshot — no temporal behaviour. Segments may shift seasonally.
- **Model:** t-SNE axes carry no meaning — inter-cluster distances are not reliable. Cluster quality not formally validated (silhouette score is a recommended next step).
- **Marital Status:** `YOLO` category present in raw data — retained as-is; may reflect data quality issues in the original survey.
- **Scope:** Deployment phase out of scope — no production pipeline integration in this CBL case.

---

## 9. Next Steps

| Horizon | Action |
|---------|--------|
| **Immediate** | Apply PCA (24 components) as preprocessing before KMeans — validate cluster quality with silhouette score |
| **Short-term** | Overlay KMeans cluster labels on t-SNE plot — produce colour-coded segment map for marketing presentation |
| **Long-term** | Evaluate UMAP for production scale (>50k customers) — supports `transform()` for real-time customer scoring |

---

## 10. How to Run

```powershell
# From portfolio root — activate shared virtual environment
.venv\Scripts\Activate.ps1

# Navigate to case
cd cases\case-pca-tsne-dimensionality-reduction

# Launch notebook
jupyter lab notebooks\case_pca_tsne_dimensionality_reduction.ipynb
```

> **Dataset:** Download `marketing_campaign.csv` from [Kaggle](https://www.kaggle.com/datasets/imakash3011/customer-personality-analysis) and place in `data/raw/`.

---

*Framework: CRISP-DM + LEAN | Methodology: Case-Based Learning (CBL)*

**Jose Marcel Lopez Pino**
Data Scientist — Operations, Analytics & Process Optimization | Data Science & Business Analytics
Bootcamp: Fundamentos de Ciencia de Datos — SENCE/Alkemy (2025–2026)

*Industrial Engineering in Chile (Academic degree: Bachelor of Science in
Industrial Engineering — 5.5-year program, comparable to a U.S. M.S.) encompasses
business strategy, finance, marketing, economics, operations management, and
technology management — backed by a rigorous scientific foundation in calculus,
linear algebra, probability and statistics, physics, and optimization — enabling
a unique business + analytics perspective.*

[![GitHub](https://img.shields.io/badge/GitHub-joselopezp-181717?style=flat&logo=github)](https://github.com/joselopezp)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-jose--lopez--pino-0077B5?style=flat&logo=linkedin)](https://www.linkedin.com/in/jose-lopez-pino/)
