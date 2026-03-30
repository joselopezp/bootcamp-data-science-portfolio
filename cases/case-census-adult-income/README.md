# Case: Census Adult Income — MLlib Pipeline

![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![PySpark](https://img.shields.io/badge/PySpark-4.1.1-E25A1C?logo=apachespark&logoColor=white)
![Framework](https://img.shields.io/badge/Framework-CRISP--DM%20%2B%20LEAN-2E86AB)
![Type](https://img.shields.io/badge/Type-Predictive%20Analytics-blueviolet)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow)

End-to-end MLlib Pipeline for income prediction and workforce segmentation using PySpark.
Predicts whether a worker earns above USD 50K/year (Logistic Regression, AUC = 0.9005)
and segments socioeconomic profiles into 4 actionable clusters (KMeans).
Built to support RetailMax premium loyalty campaign targeting.

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
MLlib Pipeline with preprocessing, feature engineering, and evaluation.

**Why was it built?**
To demonstrate Big Data ML capabilities on a real-world dataset using distributed
computing — a skill gap between traditional data scientists and those who can scale
to production-grade data volumes.

**What problem does it solve?**
RetailMax cannot identify which customer profiles have high purchasing power.
Treating all customers equally leads to inefficient campaign spend and missed
revenue from high-value segments.

**What did I learn?**
- End-to-end MLlib Pipeline architecture (StringIndexer → OHE → VectorAssembler → Scaler → Model)
- Diagnosing and resolving PySpark worker serialization failures (`EOFException`)
- Extracting ROC curve data directly from MLlib model summary
- Creating Spark SQL temp views without Python serialization bottlenecks

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
pip install -r cases/case-census-adult-income/requirements.txt
```

**Java requirement:** Java 17 (Temurin recommended) must be installed and `JAVA_HOME` set.

---

## Usage

> ⚠️ Raw data excluded via `.gitignore`. Download before running.

**Download dataset:**
```powershell
Invoke-WebRequest `
    -Uri "https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data" `
    -OutFile "cases\case-census-adult-income\data\raw\adult.data"
```

**Run notebook:**
```
notebooks/01_census_adult_income_pipeline.ipynb
```
Execute all cells in order (`Run All Cells`). The notebook is self-contained —
all preprocessing, modeling, evaluation, and SQL practice run sequentially.

---

## Key Results

| Model | Metric | Value | Baseline |
|---|---|---|---|
| Logistic Regression | AUC-ROC | **0.9005** | 0.50 (random) |
| Logistic Regression | Accuracy | **~0.85** | 0.75 (majority) |
| KMeans k=4 | Silhouette Score | reported in notebook | — |
| KMeans k=4 | WSSSE | reported in notebook | — |

**Key finding:** The model achieves AUC = 0.9005 — well above the 0.85 target —
with a simple Logistic Regression and no hyperparameter tuning, validating
the Lean MVP approach.

---

## Model Card

### Supervised Model

| Field | Details |
|---|---|
| **Model type** | Logistic Regression |
| **Task** | Binary Classification |
| **Training data** | UCI Adult Census Income · 30,162 records (after cleaning) · 1994 US Census |
| **Features used** | 9 features: `age`, `education_num`, `capital_gain`, `capital_loss`, `hours_per_week`, `workclass`, `marital_status`, `occupation`, `sex` |
| **Target variable** | `income` — binary: `<=50K` (0) / `>50K` (1) |
| **Framework** | PySpark MLlib 4.1.1 |
| **Hyperparameters** | `maxIter=20`, `regParam=0.01` |
| **Training date** | 2026-03 |

### Unsupervised Model

| Field | Details |
|---|---|
| **Model type** | KMeans |
| **Task** | Clustering — workforce segmentation |
| **Training data** | UCI Adult Census Income · 30,162 records |
| **Features used** | Same 9 features as supervised model |
| **k** | 4 clusters (business interpretability criterion) |
| **Framework** | PySpark MLlib 4.1.1 |
| **Hyperparameters** | `k=4`, `maxIter=20`, `seed=42` |
| **Training date** | 2026-03 |

---

## Model Performance

### Logistic Regression

| Metric | Value |
|---|---|
| AUC-ROC | **0.9005** |
| Accuracy | ~0.85 |
| Baseline (majority class) | 0.75 |
| Improvement over baseline | +~0.10 |

> **Primary metric:** AUC-ROC — chosen over Accuracy because the dataset is
> imbalanced (~75% `<=50K`, ~25% `>50K`). Accuracy alone would be misleading.

### KMeans k=4

| Metric | Value |
|---|---|
| Silhouette Score | See notebook output |
| WSSSE | See notebook output |
| Clusters | 4 — differentiated by age, education, hours worked, capital gain |

---

## MLOps Checklist

### Reproducibility
- [x] Random seed fixed (`seed=42`)
- [x] Requirements pinned (`requirements.txt` with exact versions)
- [x] Data download command documented (PowerShell `Invoke-WebRequest`)
- [ ] Model artifact saved (`spark.save()` — deferred, not required for case scope)

### Model Versioning
- [x] Training parameters logged in Decisions Log (notebook Section 8)
- [ ] Model artifact saved to `models/` folder — deferred post-bootcamp
- [ ] Model filename with version and date — deferred post-bootcamp

### Monitoring (awareness level)
- [x] Data limitations documented — 1994 US Census data, not representative of current labor market
- [x] Model limitations documented — trained on historical data, retraining needed for current use
- [x] Retraining trigger defined — significant shift in income distribution or labor market structure

---

## Project Structure

```
case-census-adult-income/
├── data/
│   └── raw/
│       └── adult.data              # UCI Adult Census Income (excluded from Git)
├── notebooks/
│   └── 01_census_adult_income_pipeline.ipynb
├── reports/
│   └── figures/
│       ├── model_performance_summary.png
│       └── roc_curve.png
├── requirements.txt
└── README.md
```

| Notebook | CRISP-DM Phase | Content |
|---|---|---|
| `01_census_adult_income_pipeline.ipynb` | Phase 2–5 | Data Understanding → Preparation → Modeling → Evaluation |

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
`ROC Curve` · `AUC-ROC` · `Silhouette Score` · `CRISP-DM` · `Lean Analytics`
`Big Data` · `Distributed Computing` · `Business Analytics`

---

## Strategic Recommendations

Based on model results, three actions are recommended for RetailMax:

1. **Premium campaign targeting** — Deploy the Logistic Regression model to score
   the customer database and identify high-income profiles (predicted `>50K`).
   Focus premium loyalty offers on this segment to maximize ROI.

2. **Segment-based personalization** — Use the 4 KMeans clusters as audience
   segments for differentiated messaging: high-education professionals,
   blue-collar workers, management profiles, and entry-level workers each
   respond to different value propositions.

3. **Feature prioritization** — `capital_gain`, `education_num`, and `occupation`
   are the strongest discriminators. Use these as primary filters in CRM
   segmentation rules for campaigns that do not use the ML model directly.

---

## Business Impact Estimation

| Scenario | Current State | Target | Estimated Impact |
|---|---|---|---|
| Premium campaign precision | Untargeted — 100% of base | Top 25% scored by model | 4x reduction in wasted campaign spend |
| High-income segment identification | Manual rule-based | AUC = 0.9005 model | ~10% lift in conversion rate for premium offers |
| Segment-based personalization | 1 message for all | 4 differentiated segments | Estimated +15% engagement rate |

> **Methodology:** Estimates based on industry benchmarks for ML-driven campaign
> targeting (McKinsey: "Analytics-driven marketing delivers 15–20% revenue uplift").
> **Assumptions:** RetailMax has a CRM with >10K customer records; campaign
> conversion baseline is 2–5% (typical retail loyalty program).
> **Data source:** UCI Adult Census Income (1994 US Census) — used as proxy
> for purchasing power profiling.

---

## Deliverables

- [x] `01_census_adult_income_pipeline.ipynb` — end-to-end MLlib pipeline
- [x] `reports/figures/model_performance_summary.png` — visual metrics summary
- [x] `reports/figures/roc_curve.png` — ROC Curve with AUC annotation
- [x] `requirements.txt` — pinned dependencies
- [x] `README.md` — this document with Model Card and MLOps Checklist
- [ ] Executive Summary (Spanish) — `reports/executive/` — deferred

---

## CRISP-DM Roadmap

| Phase | Status | Notebook Section |
|---|---|---|
| 1 — Business Understanding | ✅ | Header + Executive Summary |
| 2 — Data Understanding | ✅ | Section 1–2 |
| 3 — Data Preparation | ✅ | Section 2–3 |
| 4 — Modeling | ✅ | Section 4–5 |
| 5 — Evaluation | ✅ | Section 6 |
| 6 — Deployment | ⚠️ Partial | README + figures (model artifact deferred) |

---

## Credits

### Data Source
UCI Machine Learning Repository — Adult Census Income Dataset
Kohavi, R. (1996). *Scaling Up the Accuracy of Naive-Bayes Classifiers: A Decision-Tree Hybrid.*
Available at: https://archive.ics.uci.edu/dataset/2/adult

### Methodology
- Chapman, P. et al. (2000). *CRISP-DM 1.0: Step-by-step data mining guide.* SPSS Inc.
- Womack, J. & Jones, D. (1996). *Lean Thinking.* Simon & Schuster.

### Libraries
See [Tech Stack](#tech-stack--skills-demonstrated) section.

---

## License

MIT License © 2026 Jose Marcel Lopez Pino
