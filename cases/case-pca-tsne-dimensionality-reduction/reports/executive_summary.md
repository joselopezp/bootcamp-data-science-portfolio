# Executive Summary — Dimensionality Reduction: PCA vs t-SNE

**Author:** Jose Marcel Lopez Pino
**Role:** Data Scientist — Operations, Analytics & Process Optimization
**Framework:** CRISP-DM + LEAN | Case-Based Learning (CBL)
**Module:** M7 — Unsupervised Machine Learning
**Date:** April 2026
**Status:** ![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

---

## 1. Business Context

| | |
|---|---|
| **Industry** | Customer Analytics / Marketing Consulting |
| **Business Unit** | Analytics & Visualisation |
| **Stakeholder** | Marketing Director — VisionData |
| **Decision to Support** | Which dimensionality reduction technique should be used to reveal natural customer segments for campaign targeting? |

> **Situation:** VisionData received a customer survey dataset with 100+ variables per customer — demographics, consumption habits, and digital preferences. Current ML models are underperforming due to high dimensionality, and executive visualisations fail to communicate clear customer patterns to the marketing team.

---

## 2. Problem Statement

> How can we compress a high-dimensional customer dataset into 2D while preserving enough structure to reveal natural segments for differentiated marketing campaigns?

**Business Impact if Unresolved:**
- All customers treated equally — no differentiated campaign targeting
- ML model training times remain prohibitive at full dimensionality
- Marketing team cannot act on unreadable 100-variable visualisations

---

## 3. Analytical Approach

> Non-technical summary — what was done, not how.

| Step | Description |
|---|---|
| **Data** | Customer Personality Analysis (Kaggle) — 2,240 customers × 29 variables. Engineered to 30 features: age, seniority, spend by category, channel behaviour, campaign response, encoded demographics |
| **Method** | Two dimensionality reduction techniques applied and compared: PCA (linear, global) and t-SNE (non-linear, local). PCA pre-reduction to 24 components (95% variance) applied before t-SNE as industry best practice |
| **Tool** | Python · scikit-learn · matplotlib |
| **Validation** | PCA: cumulative explained variance curve. t-SNE: KL divergence minimisation (final = 0.8887, below 1.0 threshold) |

---

## 4. Key Findings

### Finding 1 — PCA retains limited variance in 2D
- **Context:** Marketing needs a 2D visualisation to present customer segments in executive meetings.
- **Analysis:** PCA compressed 30 features into 2 components retaining only **28.8%** of total variance (PC1 = 21.5%, PC2 = 7.3%). Reaching 80% variance requires 16 components; 95% requires 24.
- **Insight:** A 2D PCA projection loses over 70% of information — insufficient to reveal clear customer clusters visually, though axes remain interpretable (PC1 driven by spend variables).
- **Possible Decision:** Use PCA at 24 components as a preprocessing step before ML models — not as the primary visualisation tool for marketing presentations.

### Finding 2 — t-SNE reveals compact, well-separated customer clusters
- **Context:** The same 2,240 customers projected onto 2D using t-SNE (perplexity=40, 1,000 iterations).
- **Analysis:** t-SNE achieved a KL divergence of **0.8887** — below the 1.0 quality threshold — with visually distinct cluster structures not visible in PCA.
- **Insight:** t-SNE successfully reveals natural customer groupings that PCA cannot expose in 2D, making it directly actionable for the marketing team.
- **Possible Decision:** Use t-SNE 2D output as the basis for customer segment maps in marketing presentations. Combine with KMeans labels in the next analysis step.

### Finding 3 — No single technique serves both use cases
- **Context:** The marketing team needs both executive visualisations (exploration) and a preprocessing step for predictive models (pipeline).
- **Analysis:** t-SNE has no `transform()` method — it cannot score new customers or integrate into sklearn pipelines. PCA does.
- **Insight:** The two techniques are complementary, not competing. Using only one would be either analytically limiting (PCA only) or operationally incomplete (t-SNE only).
- **Possible Decision:** Adopt a two-track approach: t-SNE for segment discovery and presentation; PCA (24 components) for all ML pipeline preprocessing.

---

## 5. Business Recommendations

| Priority | Recommendation | Expected Impact | Effort |
|---|---|---|---|
| 🔴 High | Deploy t-SNE visualisation for marketing segment presentation | Enables differentiated campaign targeting across identified clusters | Low |
| 🔴 High | Apply PCA (24 components, 95% variance) as preprocessing for all downstream ML models | Reduces training time; eliminates noise from 30 → 24 dimensions | Low |
| 🟡 Medium | Combine t-SNE clusters with KMeans labels for actionable segment profiles | Quantifies segment size and characteristics for budget allocation | Medium |
| 🟢 Low | Evaluate UMAP as long-term replacement for t-SNE | Faster at scale, supports `transform()`, better global structure preservation | Medium |

---

## 6. Limitations

- **Data:** Dataset covers a single snapshot — no temporal behaviour. Customer segments may shift over time.
- **Model:** t-SNE axes carry no meaning — inter-cluster distances are not reliable. Cluster quality not formally validated (silhouette score pending).
- **Scope:** Deployment phase out of scope for this CBL case — no production pipeline integration.

---

## 7. Next Steps

| Horizon | Action |
|---|---|
| **Immediate** | Apply PCA (24 components) as preprocessing step before KMeans — validate cluster quality with silhouette score |
| **Short-term** | Overlay KMeans cluster labels on t-SNE plot — produce colour-coded segment map for marketing presentation |
| **Long-term** | Evaluate UMAP for production scale (>50k customers) — supports `transform()` for real-time customer scoring |

---

*Framework: CRISP-DM + LEAN | Methodology: Case-Based Learning (CBL)*

**Jose Marcel Lopez Pino**
Data Scientist — Operations, Analytics & Process Optimization | Data Science & Business Analytics
Bootcamp: Fundamentos de Ciencia de Datos — SENCE/Alkemy (2025–2026)

[![GitHub](https://img.shields.io/badge/GitHub-joselopezp-181717?style=flat&logo=github)](https://github.com/joselopezp)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-jose--lopez--pino-0077B5?style=flat&logo=linkedin)](https://www.linkedin.com/in/jose-lopez-pino/)
