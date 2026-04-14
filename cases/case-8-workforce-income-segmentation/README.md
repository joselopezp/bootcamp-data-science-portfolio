# Identifying High-Value Profiles at Scale: Income Classification & Segmentation with PySpark MLlib
### Workforce Socioeconomic Segmentation — UCI Adult Census 1994 · AUC = 0.9028 | CRISP-DM + LEAN

![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![PySpark](https://img.shields.io/badge/PySpark-4.1.1-E25A1C?logo=apachespark&logoColor=white)
![Framework](https://img.shields.io/badge/Framework-CRISP--DM%20%2B%20LEAN-2E86AB)
![Type](https://img.shields.io/badge/Type-Predictive%20Analytics-blueviolet)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow)

End-to-end scalable MLlib pipeline to identify high-value customer profiles and enable data-driven behavioral segmentation.

The model uses income classification as a proxy for customer value (Logistic Regression, AUC = 0.9028 after CrossValidator optimization) and identifies 4 distinct segments (KMeans, validated via Elbow Method).

Built on the UCI Adult Census dataset, this solution is directly applicable to e-commerce environments for customer targeting, campaign optimization, and personalized experiences.

---

## Table of Contents

1. [Description](#description)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Key Results](#key-results)
5. [Model Card](#model-card)
6. [Model Performance](#model-performance)
7. [MLOps Checklist](#mlops-checklist)
8. [Project Structure](#project-structure)
9. [Tech Stack & Skills Demonstrated](#tech-stack--skills-demonstrated)
10. [Strategic Recommendations](#strategic-recommendations)
11. [Business Impact Estimation](#business-impact-estimation)
12. [Deliverables](#deliverables)
13. [CRISP-DM Roadmap](#crisp-dm-roadmap)
14. [Credits](#credits)
15. [License](#license)

---

## Description

**What does this project do?**
Applies PySpark MLlib to build a supervised classification model (Logistic Regression)
and an unsupervised segmentation model (KMeans k=4), integrated in an end-to-end
MLlib Pipeline with preprocessing, feature engineering, evaluation, and hyperparameter optimization.

**Why was it built?**
To demonstrate Big Data ML capabilities on a real-world dataset using distributed
computing — a skill gap between traditional data scientists and those who can scale
to production-grade data volumes.

**What problem does it solve?**
This project uses the UCI Adult Census dataset as a proxy to simulate customer value modeling.

The pipeline answers two key business questions:
1. Can we identify high-value customer profiles using income classification as a proxy? (Supervised)
2. What distinct behavioral segments exist within the customer base? (Unsupervised)

These are core problems in customer analytics:
- Identifying high-value customers for targeted campaigns
- Segmenting users into actionable groups for personalization
- Prioritizing marketing spend based on predicted customer value

This pipeline demonstrates how to operationalize these capabilities using scalable ML infrastructure.

**What did I learn?**
- End-to-end MLlib Pipeline architecture (StringIndexer → OHE → VectorAssembler → Scaler → Model)
- Diagnosing and resolving PySpark worker serialization failures (`EOFException`)
- Extracting ROC curve data directly from MLlib model summary
- Creating Spark SQL temp views without Python serialization bottlenecks
- CrossValidator with ParamGridBuilder for systematic hyperparameter tuning
- Elbow Method for KMeans k selection in distributed computing context

---

## Installation

```bash
# Clone the portfolio repository
git clone https://github.com/joselopezp/bootcamp-data-science-portfolio.git
cd bootcamp-data-science-portfolio

# Activate the shared virtual environment
.venv\Scripts\activate          # Windows
source .venv/bin/activate       # macOS / Linux

# Install case dependencies
pip install -r cases/case-7-customer-purchase-prediction-spark-mllib/requirements.txt
```

**Java requirement:** Java 17 (Temurin recommended) must be installed and `JAVA_HOME` set.

---

## Usage

> Raw data excluded via `.gitignore`. Download before running.

**Download dataset:**
```powershell
Invoke-WebRequest `
    -Uri "https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data" `
    -OutFile "cases\case-7-customer-purchase-prediction-spark-mllib\data\raw\adult.data"
```

**Run notebook:**
```
notebooks/01_customer_purchase_prediction_pipeline.ipynb
```
Execute all cells in order (Run All Cells). The notebook is self-contained —
all preprocessing, modeling, evaluation, hyperparameter optimization, and SQL practice run sequentially.

---

## Key Results

| Model | Metric | Value | Baseline |
|---|---|---|---|
| Logistic Regression | AUC-ROC (after CV) | **0.9028** | 0.50 (random) |
| Logistic Regression | AUC-ROC (before CV) | 0.9005 | 0.50 (random) |
| Logistic Regression | Accuracy (after CV) | **0.8472** | 0.75 (majority) |
| Logistic Regression | Best regParam | 0.001 | — |
| Logistic Regression | Best elasticNetParam | 0.5 (ElasticNet L1+L2) | — |
| KMeans k=4 | WSSSE | 906,189 | — |
| KMeans k=4 | k validation | Elbow Method k=2..8 | No dominant inflection — k=4 justified by business interpretability |

**Key finding:** CrossValidator (5-fold, 12 parameter combinations) improved AUC by +0.0023
over the Lean MVP baseline — confirming the original model was already well-calibrated.
Elbow Method shows no dominant geometric inflection point, validating k=4 as a
business-driven choice.

---

## Model Card

### Supervised Model

| Field | Details |
|---|---|
| **Model type** | Logistic Regression |
| **Task** | Binary Classification |
| **Training data** | UCI Adult Census Income · 30,162 records (after cleaning) · 1994 US Census |
| **Features used** | 9 features: `age`, `education_num`, `capital_gain`, `capital_loss`, `hours_per_week`, `workclass`, `marital_status`, `occupation`, `sex` |
| **Target variable** | `income` — binary: `<=50K` (0) / `>50K` (1) — used as proxy for customer value |
| **Framework** | PySpark MLlib 4.1.1 |
| **Hyperparameters (optimized)** | `maxIter=20`, `regParam=0.001`, `elasticNetParam=0.5` |
| **Optimization** | CrossValidator 5-fold · 12 param combinations (4 regParam x 3 elasticNetParam) |
| **Training date** | 2026-03 |

### Unsupervised Model

| Field | Details |
|---|---|
| **Model type** | KMeans |
| **Task** | Clustering — customer behavioral segmentation |
| **Training data** | UCI Adult Census Income · 30,162 records |
| **Features used** | Same 9 features as supervised model |
| **k** | 4 clusters — business interpretability criterion, validated by Elbow Method (k=2..8) |
| **Framework** | PySpark MLlib 4.1.1 |
| **Hyperparameters** | `k=4`, `maxIter=20`, `seed=42` |
| **Training date** | 2026-03 |

---

## Model Performance

### Logistic Regression

| Metric | Before CV | After CV | Change |
|---|---|---|---|
| AUC-ROC | 0.9005 | **0.9028** | +0.0023 |
| Accuracy | 0.8407 | **0.8472** | +0.0065 |
| regParam | 0.01 | 0.001 | Refined |
| elasticNetParam | 0.0 | 0.5 | ElasticNet L1+L2 |
| Baseline (majority) | 0.75 | — | — |

> **Primary metric:** AUC-ROC — chosen over Accuracy because the customer base is
> imbalanced (~75% low-value, ~25% high-value profiles). Accuracy alone would be misleading.
>
> **Lean note:** CV improvement = +0.0023 AUC — below 0.005 threshold.
> Original MVP model was already well-calibrated. Optimization confirms, not replaces.

### KMeans k=4

| Metric | Value |
|---|---|
| WSSSE (k=4) | 906,189 |
| k validation | Elbow Method k=2..8 — no dominant inflection point |
| k selection rationale | Business interpretability — 4 actionable customer segments |

**Elbow Method results:**

| k | WSSSE |
|---|---|
| 2 | 976,381 |
| 3 | 939,049 |
| **4** | **906,189** (chosen) |
| 5 | 883,191 |
| 6 | 855,060 |
| 7 | 826,978 |
| 8 | 792,378 |

---

## MLOps Checklist

### Reproducibility
- [x] Random seed fixed (`seed=42`)
- [x] Requirements pinned (`requirements.txt` with exact versions)
- [x] Data download command documented (PowerShell `Invoke-WebRequest`)
- [ ] Model artifact saved — deferred, not required for case scope

### Model Versioning
- [x] Training parameters logged in Decisions Log (notebook Section 8)
- [x] Hyperparameter optimization documented (Section 11 — CrossValidator results)
- [ ] Model artifact saved to `models/` folder — deferred post-bootcamp

### Monitoring (awareness level)
- [x] Data limitations documented — 1994 US Census, not representative of current customer behavior
- [x] Model limitations documented — trained on historical data, retraining needed for current use
- [x] Retraining trigger defined — significant shift in income distribution or customer behavior patterns
- [x] Fairness note — `sex` included as feature; fairness audit required before production deployment

---

## Project Structure

```
case-7-customer-purchase-prediction-spark-mllib/
├── data/
│   └── raw/
│       └── adult.data              # UCI Adult Census Income (excluded from Git)
├── notebooks/
│   └── 01_customer_purchase_prediction_pipeline.ipynb
├── reports/
│   ├── executive_summary.md
│   └── figures/
│       ├── model_performance_summary.png
│       ├── roc_curve.png
│       └── elbow_method.png
├── requirements.txt
└── README.md
```

| Notebook | CRISP-DM Phase | Content |
|---|---|---|
| `01_customer_purchase_prediction_pipeline.ipynb` | Phase 2–5 | Data Understanding → Preparation → Modeling → Evaluation → Optimization |

---

## Tech Stack & Skills Demonstrated

| Category | Tool | Version |
|---|---|---|
| Language | Python | 3.12 |
| Big Data | PySpark MLlib | 4.1.1 |
| Runtime | Java Temurin | 17 |
| Visualization | Matplotlib | 3.10.8 |
| Data | NumPy / Pandas | 2.4.1 / 3.0.0 |
| IDE | VS Code + Jupyter | — |

**Skills demonstrated:**

`PySpark` · `MLlib` · `Logistic Regression` · `KMeans` · `ML Pipeline` · `Spark SQL`
`Binary Classification` · `Clustering` · `Feature Engineering` · `OneHotEncoding`
`CrossValidator` · `ParamGridBuilder` · `Elbow Method` · `ROC Curve` · `AUC-ROC`
`Silhouette Score` · `CRISP-DM` · `Lean Analytics` · `Big Data` · `Distributed Computing`
`Business Analytics` · `Customer Segmentation` · `Customer Value Modeling`

---

## Strategic Recommendations

This pipeline demonstrates a scalable, decision-oriented framework for value-based customer segmentation and prioritization.

Organizations that could apply this framework include:

1. **Retail / E-commerce** — Prioritize high-value customers to maximize conversion, retention, and marketing ROI through targeted acquisition and personalization strategies.

2. **Banking / Insurance** — Score customers by value profile to optimize risk-adjusted returns, pricing strategies, and product allocation.

3. **Public Policy / HR Analytics** — Segment workforce populations to improve compensation strategies, target training investments, and support data-driven equity decisions.

**Feature insight:** `capital_gain`, `education_num`, and `occupation` are the
strongest value discriminators in this dataset — available in most CRM,
HR, and census-derived data sources.

---

## Business Impact Estimation

| Scenario | Without Model | With Model | Estimated Gain |
|---|---|---|---|
| Customer value classification | Rule-based or no scoring | AUC = 0.9028 — 90% discrimination | Significant reduction in misclassification vs majority baseline |
| Customer base segmentation | Homogeneous — 1 group | 4 differentiated customer segments | Enables differentiated strategies per segment |
| Feature-based filtering | No systematic approach | Top predictors identified (education, occupation, capital_gain) | Lightweight proxy for scoring without full model deployment |
| Decision workflow | Manual spreadsheet-based analysis, static reporting | Automated, scalable ML pipeline with continuous scoring and segmentation | Shorter decision cycles, reduced manual effort, improved scalability |

> **Note:** Estimates are illustrative. Production impact depends on organization size,
> current baseline, and data recency. The 1994 Census dataset serves as a
> methodology proof-of-concept — retrain on current data before deployment.

---

## Deliverables

- [x] `01_customer_purchase_prediction_pipeline.ipynb` — end-to-end MLlib pipeline with optimization
- [x] `reports/executive_summary.md` — business-facing summary
- [x] `reports/figures/model_performance_summary.png` — visual metrics summary
- [x] `reports/figures/roc_curve.png` — ROC Curve with AUC annotation
- [x] `reports/figures/elbow_method.png` — Elbow Method k=2..8
- [x] `requirements.txt` — pinned dependencies
- [x] `README.md` — this document with Model Card and MLOps Checklist

---

## CRISP-DM Roadmap

| Phase | Status | Notebook Section |
|---|---|---|
| 1 — Business Understanding | ✅ | Header + Executive Summary |
| 2 — Data Understanding | ✅ | Section 1–2 |
| 3 — Data Preparation | ✅ | Section 2–3 |
| 4 — Modeling | ✅ | Section 4–5 |
| 5 — Evaluation | ✅ | Section 6 + Section 11 |
| 6 — Deployment | ⚠️ Partial | README + figures (model artifact deferred) |

---

## Credits

### Data Source
UCI Machine Learning Repository — Adult Census Income Dataset
Kohavi, R. (1996). Scaling Up the Accuracy of Naive-Bayes Classifiers: A Decision-Tree Hybrid.
Available at: https://archive.ics.uci.edu/dataset/2/adult

### Methodology
- Chapman, P. et al. (2000). CRISP-DM 1.0: Step-by-step data mining guide. SPSS Inc.
- Womack, J. & Jones, D. (1996). Lean Thinking. Simon & Schuster.

### Libraries
See Tech Stack section.

---

## License

MIT License © 2026 Jose Marcel Lopez Pino
