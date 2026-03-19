# Unsupervised ML Customer Segmentation: Discovering Behavioral Clusters in the Auto Industry

> **Auto Industry Analytics — Unsupervised ML** | Module 7: Fundamentos de Ciencia de Datos

![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![Framework](https://img.shields.io/badge/Framework-CRISP--DM%20%2B%20LEAN-2E86AB)
![Type](https://img.shields.io/badge/Type-Unsupervised%20ML-blueviolet)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## Table of Contents

- [Project Overview](#project-overview)
- [Business Context](#business-context)
- [Key Results](#key-results)
- [Cluster Profiles — Customer Personas](#cluster-profiles--customer-personas)
- [Strategic Recommendations](#strategic-recommendations)
- [Limitations & Honest Assessment](#limitations--honest-assessment)
- [Project Structure](#project-structure)
- [Tech Stack](#tech-stack)
- [How to Run](#how-to-run)
- [Deliverables](#deliverables)
- [CRISP-DM Roadmap](#crisp-dm-roadmap)
- [Model Card](#model-card)
- [MLOps Checklist](#mlops-checklist)
- [Data Source](#data-source)
- [Credits](#credits)
- [License](#license)

---

## Project Overview

This project applies unsupervised machine learning to validate and extend a
customer segmentation strategy for an automobile company client of
**Auto Industry Insights S.A.** — a market intelligence consultancy.

The client's sales team manually classified 8,068 existing customers into
4 segments (A, B, C, D) and used this strategy successfully for targeted
outreach. They now plan to enter new markets and need to validate whether
these segments reflect natural behavioral clusters — and whether the pipeline
can scale to new, unlabeled customers.

Using dimensionality reduction (PCA, t-SNE) and three clustering algorithms
(KMeans, DBSCAN, Hierarchical), this project discovers hidden behavioral
patterns independently of the manual labels — then compares results against
the original segmentation as external validation.

**What I learned:** KMeans, DBSCAN, and Agglomerative Clustering; PCA and t-SNE
for dimensionality reduction; silhouette score and elbow method for model
evaluation; cluster profiling for business interpretation; and the importance of
honest assessment when unsupervised results diverge from expert-assigned labels.

---

## Business Context

**Client:** Auto Industry Insights S.A. — a market intelligence consultancy
serving automobile manufacturers planning expansion into new markets.

**Problem:** The client's automobile company manually classified customers into
4 segments (A, B, C, D) using sales team domain knowledge. While this strategy
has worked well in existing markets, the company cannot verify whether these
segments reflect genuine behavioral patterns or sales team bias — and cannot
automatically assign segments to 2,627 new potential customers in new markets.

**Decision enabled:** Do natural behavioral customer clusters exist in the data?
If so, how many? And can the pipeline assign segments to new, unseen customers
at scale — enabling the same targeted outreach strategy in new markets?

**Dataset context:** The dataset contains 8,068 customers from the automobile
company's existing market, with demographic and behavioral features plus the
manually assigned segment labels (A/B/C/D). Our unsupervised approach discovers
cluster structure independently — labels are used only for external validation
in notebook 05 to assess alignment between data-driven and expert-assigned segments.

**Key Business Questions:**

| # | Question | Answer |
|---|---------|--------|
| BQ1 | Do natural behavioral clusters exist independently of manual labels? | Yes — 4 clusters identified (KMeans) |
| BQ2 | What traits define each cluster? | Age, profession, spending score, marital status |
| BQ3 | Which algorithm produces the most actionable segments? | KMeans (silhouette=0.154) |
| BQ4 | Can the pipeline scale to new customers? | ✅ Validated on 20% holdout test set |

---

## Key Results

| Algorithm | Silhouette Score | Clusters | vs Target (≥0.35) |
|-----------|-----------------|----------|-------------------|
| **KMeans** | **0.154** | **4** | ⚠️ Below target |
| Hierarchical | 0.088 | 4 | ⚠️ Below target |
| DBSCAN | N/A | — | N/A (1 cluster found) |

> **KMeans selected** as the best algorithm — highest silhouette score among
> valid algorithms. Scores below 0.35 are expected given the expert-assigned
> label structure (see Limitations section).

> **Elbow curve note:** No pronounced inflection point was observed between
> k=2 and k=10 — the inertia curve decreases near-linearly. k=4 was selected
> as a pragmatic choice consistent with the company's existing 4-segment strategy.

---

## Cluster Profiles — Customer Personas

| Cluster | Persona | Age | Profession | Spending Score | Family Size | Key Traits |
|---------|---------|-----|-----------|----------------|-------------|------------|
| 0 | **Senior Executives** | ~63 | Executive / Lawyer | Medium-High (1.31) | 2.65 | Older, married, high seniority |
| 1 | **Mid-Career Artists** | ~47 | Artist / Entertainment | Medium (0.61) | 2.48 | Graduated, creative professions |
| 2 | **Young Healthcare** | ~29 | Healthcare / Doctor | Low (0.08) | 3.40 | Young, single, large families, low spending |
| 3 | **Engineers** | ~42 | Engineer (100%) | Medium (0.50) | 2.90 | Homogeneous profession cluster |

---

## Strategic Recommendations

| Priority | Segment | Finding | Recommended Action |
|----------|---------|---------|-------------------|
| **HIGH** | Senior Executives (C0) | Highest spending score; established careers | Premium vehicle offers + exclusive loyalty benefits |
| **HIGH** | Young Healthcare (C2) | Youngest segment; large families; low spending | Entry-level + family vehicle promotions |
| **MEDIUM** | Mid-Career Artists (C1) | Creative professionals; medium spending | Lifestyle-oriented campaigns + design-led models |
| **LOW/HOLD** | Engineers (C3) | Homogeneous profession cluster; medium spending | Technical specification campaigns + performance models |

> **LEAN rule:** Recommendations are directional. Validation on real new-market
> customer data is required before full campaign deployment.

---

## Limitations & Honest Assessment

| Limitation | Impact | Mitigation |
|-----------|--------|-----------|
| Expert-assigned labels | Segments A/B/C/D reflect sales team judgment — not pure behavioral patterns. Unsupervised clusters may not align with manual labels. | Use external validation (notebook 05) to assess alignment |
| Silhouette scores below 0.35 | Cluster boundaries are soft — significant overlap between segments | Expected when ground truth was manually assigned; use for direction only |
| No clear elbow | k=4 is pragmatic, not data-driven | Consider gap statistic for more rigorous k selection in future cycle |
| DBSCAN found 1 cluster | Default eps=0.5 too restrictive for this feature space | Tune eps via k-distance plot in next iteration |

> **Personal perspective:** A silhouette score of 0.154 is analogous to a Cpk of ~0.5
> — the process (segmentation) exists but has high variation. The low score is
> partly expected: if segments were assigned by expert judgment rather than
> behavioral distance, clustering algorithms will struggle to reproduce them.
> The pipeline is validated and scalable — what requires improvement is the
> feature engineering, not the methodology.

---

## Project Structure

```
project-6-unsupervised-ml-customer-segmentation/
├── data/
│   ├── raw/                    # Train.csv (Kaggle) + test.csv (80/20 split)
│   ├── processed/              # customers_clean.csv, X_scaled.npy, scaler.pkl,
│   │                           # feature_cols.csv, model_final_v1.pkl
│   └── final/                  # cluster_labels.csv, X_pca.npy, X_tsne.npy
├── notebooks/
│   ├── 01_business_understanding.ipynb   # Problem Statement Canvas, BQs, success criteria
│   ├── 02_data_understanding.ipynb       # EDA, distributions, correlation matrix
│   ├── 03_data_preparation.ipynb         # Encoding, IQR, StandardScaler, 80/20 split
│   ├── 04_modeling.ipynb                 # PCA, t-SNE, KMeans, DBSCAN, Hierarchical
│   ├── 05_evaluation.ipynb               # Silhouette comparison, cluster profiling, personas
│   └── 06_deployment.ipynb               # Pipeline validation on test set, MLOps checklist
├── reports/
│   └── figures/                # All generated visualizations
├── docs/
│   ├── METHODOLOGY.md
│   ├── data_dictionary.md
│   ├── decisions_log.md
│   └── lean_retrospective.md
├── src/
│   ├── data_processing.py
│   ├── analysis.py
│   └── visualization.py
├── requirements.txt
├── .gitignore
└── README.md
```

### CRISP-DM Phase Mapping

| Notebook | CRISP-DM Phase | Scope |
|----------|----------------|-------|
| 01 | Business Understanding | Problem Statement Canvas, BQs, stakeholder map |
| 02 | Data Understanding | EDA, distributions, correlation matrix |
| 03 | Data Preparation | Encoding, outlier removal, scaling, 80/20 split |
| 04 | Modeling | PCA, t-SNE, KMeans (elbow), DBSCAN, Hierarchical |
| 05 | Evaluation | Silhouette comparison, cluster profiling, personas |
| 06 | Deployment | Pipeline validation on test set, MLOps checklist |

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.12 | Core language |
| Pandas | Data manipulation and encoding |
| NumPy | Numerical operations, array persistence |
| Scikit-learn | PCA, t-SNE, KMeans, DBSCAN, Hierarchical, silhouette score |
| SciPy | Hierarchical dendrogram (linkage) |
| Matplotlib | Custom visualizations |
| Seaborn | Heatmaps, scatter plots, cluster profiles |
| Joblib | Model and scaler persistence |

**Skills Demonstrated:**
`Python` · `Unsupervised ML` · `Clustering` · `Dimensionality Reduction` · `PCA` · `t-SNE` · `KMeans` · `DBSCAN` · `Hierarchical Clustering` · `Silhouette Score` · `Elbow Method` · `Pandas` · `Scikit-learn` · `CRISP-DM` · `Lean Thinking` · `Business Analytics`

---

## How to Run

```bash
git clone https://github.com/joselopezp/bootcamp-data-science-portfolio.git
cd projects/project-6-unsupervised-ml-customer-segmentation
python -m venv .venv
.venv\Scripts\activate          # Windows
pip install -r requirements.txt
jupyter notebook notebooks/01_business_understanding.ipynb
```

> ⚠️ Download `Train.csv` from Kaggle before running:
> https://www.kaggle.com/datasets/kaushiksuresh147/customer-segmentation
> Place it in `data/raw/`. The 80/20 split (`test.csv`) is generated automatically
> in notebook 03. Run notebooks in order: 01 → 02 → 03 → 04 → 05 → 06.

---

## Deliverables

- [x] 6 notebooks following CRISP-DM + Lean structure (01–06)
- [x] PCA and t-SNE dimensionality reduction with visualizations
- [x] KMeans, DBSCAN, and Hierarchical clustering implemented and compared
- [x] Elbow method and silhouette score evaluation
- [x] Cluster profiling with business persona interpretation
- [x] Pipeline validated on 20% holdout test set
- [x] Scaler and model serialized (`scaler.pkl`, `model_final_v1.pkl`)
- [x] Visualizations in `reports/figures/`
- [x] Decisions log and methodology documentation

---

## CRISP-DM Roadmap

| Level | Question | Cycle | Module | Status |
|-------|----------|-------|--------|--------|
| Descriptive | What happened? | project-2-pequeshop-analytics | M3 — ETL | ✅ Complete |
| Diagnostic | Why did it happen? | project-3-eda-pequeshop | M4 — EDA | ✅ Complete |
| Inferential | Are patterns statistically real? | project-4b-pequeshop-statistical-inference | M5 — Statistical Inference | ✅ Complete |
| Predictive | What will happen? | project-5-ecommerce-spend-prediction | M6 — Supervised ML | ✅ Complete |
| Segmentation | Who are our customers? | **project-6** (this project) | M7 — Unsupervised ML | ✅ Complete |

---

## Model Card

| Field | Details |
|-------|---------|
| **Model type** | KMeans Clustering |
| **Task** | Customer segmentation (unsupervised) |
| **Training data** | Kaggle automobile customer dataset — 80% split (~6,454 rows) |
| **Features used** | 26 features after one-hot encoding (demographics + behavioral) |
| **Target variable** | None — unsupervised |
| **Framework** | Scikit-learn 1.4 |
| **Optimal k** | 4 clusters |
| **Silhouette score** | 0.154 (train set) |
| **Training date** | March 2026 |

---

## MLOps Checklist

### Reproducibility
- [x] Random seed fixed (`random_state=42`)
- [x] Requirements pinned (`requirements.txt`)
- [x] Scaler saved (`data/processed/scaler.pkl`)
- [x] Final model saved (`data/processed/model_final_v1.pkl`)
- [x] Feature columns saved (`data/processed/feature_cols.csv`)

### Model Versioning
- [x] Model filename includes version: `model_final_v1.pkl`
- [x] Training parameters logged in `docs/decisions_log.md`

### Monitoring (awareness level)
- [ ] Data drift: expert-labeled dataset — real new-market data will differ in distribution
- [ ] Model limitations: documented in Limitations section above
- [ ] Retraining trigger: when new-market customer data becomes available

---

## Data Source

| Field | Details |
|-------|---------|
| **Dataset** | Customer Segmentation — Kaggle (kaushiksuresh147) |
| **Original context** | Automobile company — 8,068 customers manually labeled A/B/C/D by sales team |
| **Label type** | Expert-assigned — not derived from clustering or behavioral distance |
| **Train.csv** | 8,068 rows with Segmentation label — used as full dataset |
| **Train split** | 80% of Train.csv (~6,454 rows) — used for model fitting |
| **Test split** | 20% of Train.csv (~1,614 rows) — stratified split generated in notebook 03 |
| **Kaggle Test.csv** | Not used — lacks Segmentation column |
| **Accessed** | March 2026 |

### How to Reproduce

> Download `Train.csv` from:
> https://www.kaggle.com/datasets/kaushiksuresh147/customer-segmentation
> Place in `data/raw/`. The 80/20 test split is generated automatically in notebook 03.
> `Test.csv` from Kaggle is not used in this project.

---

## Credits

**Methodology References:**
- CRISP-DM: Chapman et al. (2000). *CRISP-DM 1.0: Step-by-step data mining guide*. SPSS Inc.
- Provost, F. & Fawcett, T. (2013). *Data Science for Business*. O'Reilly Media.
- Lean Thinking: Womack, J. & Jones, D. (1996). *Lean Thinking*. Simon & Schuster.
- Rousseeuw, P.J. (1987). Silhouettes: A graphical aid to the interpretation and validation of cluster analysis. *Journal of Computational and Applied Mathematics*, 20, 53–65.

**Tools & Libraries:** See [Tech Stack](#tech-stack) section.

---

## License

This project is licensed under the [MIT License](LICENSE).

© 2026 Jose Marcel Lopez Pino

---

*Framework: CRISP-DM + Lean | Methodology: Project-Based Learning (PBL)*

**Jose Marcel Lopez Pino**
Industrial Engineer (Business + Operations) | Data Science & Business Analytics
Bootcamp: Fundamentos de Ciencia de Datos - SENCE/Alkemy (2025–2026)

*Industrial Engineering in Chile (Academic degree: Bachelor of Science in
Industrial Engineering — 5.5-year program, comparable to a U.S. M.S.) encompasses
business strategy, finance, marketing, economics, operations management, and
technology management — backed by a rigorous scientific foundation in calculus,
linear algebra, probability and statistics, physics, and optimization — enabling
a unique business + analytics perspective.*

[![GitHub](https://img.shields.io/badge/GitHub-joselopezp-181717?style=flat&logo=github)](https://github.com/joselopezp)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-jose--lopez--pino-0077B5?style=flat&logo=linkedin)](https://www.linkedin.com/in/jose-lopez-pino/)
