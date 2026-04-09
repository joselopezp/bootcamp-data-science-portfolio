# RetailMax: Retail Analytics Pipeline

> **CRISP-DM + LEAN — PBL Project** | Module 9: Fundamentos de Big Data

![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![Framework](https://img.shields.io/badge/Framework-CRISP--DM%20%2B%20LEAN-2E86AB)
![Type](https://img.shields.io/badge/Type-Big%20Data%20%2B%20ML-blueviolet)
![PySpark](https://img.shields.io/badge/PySpark-4.1.1-E25A1C?logo=apachespark&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## Table of Contents

- [Project Overview](#project-overview)
- [Business Context](#business-context)
- [Problem Statement Canvas](#problem-statement-canvas)
- [Key Results](#key-results)
- [Customer Segments](#customer-segments)
- [Project Structure](#project-structure)
- [CRISP-DM Phase Mapping](#crisp-dm-phase-mapping)
- [Tech Stack](#tech-stack)
- [How to Run](#how-to-run)
- [Strategic Recommendations](#strategic-recommendations)
- [Business Impact Estimation](#business-impact-estimation)
- [Model Card](#model-card)
- [Limitations](#limitations)
- [Deliverables](#deliverables)
- [Data Source](#data-source)
- [Cloud Validation Roadmap](#cloud-validation-roadmap)
- [BI Integration Roadmap](#bi-integration-roadmap)
- [Next Steps](#next-steps)
- [Credits](#credits)
- [License](#license)

---

## Project Overview

End-to-end Big Data analytics pipeline for RetailMax, an e-commerce platform
processing over 2 million records. The pipeline ingests structured and
unstructured data, applies distributed transformations with Apache Spark,
generates business metrics via Spark SQL, and builds scalable ML models
(Logistic Regression + K-Means) to classify and segment customers for
targeted marketing.

**Why it was built:** To demonstrate the ability to design and implement a
complete Big Data pipeline — from raw data ingestion through ML-driven
business insights — using industry-standard tools at scale.

**What problem it solves:** RetailMax's fragmented analytics process prevented
the marketing team from identifying high-value customers and creating targeted
campaigns. This pipeline unifies 10 data sources into a single analytical
framework with actionable customer segments.

**What I learned:** Distributed computing with PySpark, RDD/DataFrame duality,
Spark SQL optimization, MLlib pipeline construction, Parquet storage benefits,
and how to translate ML outputs into business recommendations.

---

## Business Context

**RetailMax** is a large-scale e-commerce platform with fragmented analytics —
data stored across multiple systems, traditional ML tools unable to scale to
full transaction volume. Marketing decisions rely on sampled data, missing
patterns in long-tail customer segments.

**Key Business Questions:**
- Which customers should receive personalized retention offers vs. standard promotions?
- What natural customer segments exist, and what marketing action fits each?
- Can we process the full dataset (not samples) to uncover patterns invisible at smaller scale?

---

## Problem Statement Canvas

| Element | Description |
|---|---|
| **Business Problem** | Analytics process is slow and fragmented — marketing decisions based on sampled data |
| **Business Impact** | 15–25% waste in retention budget; 19% of high-ticket customers dissatisfied (review 2.1/5) |
| **Decision to Support** | Which customers get retention offers vs. standard promotions; which segments to prioritize |
| **Analytical Question** | Can we classify customers as High/Low Value and segment them at scale using transaction + review + browsing data? |
| **Success Metrics** | AUC-ROC ≥ 0.75; Silhouette ≥ 0.40; pipeline processes 2M+ records |
| **Proposed Approach** | PySpark pipeline: Olist data + synthetic clickstream → RDD transformations → Spark SQL → MLlib (LogReg + K-Means) |

---

## Key Results

| Metric | Value | Target | Status |
|---|---|---|---|
| AUC-ROC (Logistic Regression) | **0.9506** | ≥ 0.75 | ✅ PASS |
| Accuracy | **0.9506** | — | — |
| Precision (weighted) | **0.9539** | — | — |
| Recall (weighted) | **0.9506** | — | — |
| F1 Score | **0.9505** | — | — |
| Silhouette Score (K-Means, K=4) | **0.5855** | ≥ 0.40 | ✅ PASS |
| Total records processed | **2,055,860** | > 100K | ✅ PASS |

---

## Customer Segments

| Cluster | Name | Size | Avg Ticket | Avg Review | Marketing Action |
|---|---|---|---|---|---|
| 0 | **One-time Satisfied** | 72,013 (77%) | $112 | 4.6 | Reactivation campaign — 2nd purchase offer at 30 days |
| 1 | **Loyal Repeaters** | 703 (0.8%) | $128 | 4.3 | VIP program — free shipping, early access, rewards |
| 2 | **Multi-item Buyers** | 2,769 (3%) | $116 | 4.0 | Bundle cross-sell — volume discounts on 3+ items |
| 3 | **High-ticket Critics** | 17,911 (19%) | $290 | 2.1 | Service recovery — follow-up within 48h for low reviews |

---

## Project Structure

```
project-8-retailmax-big-data/
├── README.md
├── project.yaml
├── .gitignore
├── data/
│   ├── raw/                  # Olist CSVs (9 files, ~120 MB)
│   ├── processed/            # Parquet intermediate files
│   └── final/                # ML outputs (predictions, clusters)
├── notebooks/
│   ├── 01_business_understanding.ipynb
│   ├── 02_data_understanding.ipynb
│   ├── 03_data_preparation.ipynb
│   ├── 04_modeling.ipynb
│   ├── 05_evaluation.ipynb
│   └── 06_deployment.ipynb
├── src/
│   └── __init__.py
├── reports/
│   ├── figures/                      # Visualizations (PNG)
│   ├── executive_summary.md          # Spanish version
│   └── executive_summary_en.md       # English version
└── docs/
    ├── architecture.md
    ├── decisions_log.md
    └── lean_retrospective.md
```

---

## CRISP-DM Phase Mapping

| Notebook | CRISP-DM Phase | Consigna Lesson | Key Output |
|---|---|---|---|
| 01 | Business Understanding | L1: Big Data Fundamentals | Problem Statement Canvas, 5V analysis, architecture diagram |
| 02 | Data Understanding | L2: Spark Intro + Config | SparkSession, 9 Olist tables + 500K clickstream loaded |
| 03 | Data Preparation | L3: RDD Transformations | map/filter/flatMap/distinct/sortBy, Pair RDDs, cache, DAG |
| 04 | Modeling | L4: Spark SQL + L5: MLlib | SQL metrics, Parquet output, LogReg + K-Means pipeline |
| 05 | Evaluation | L5: MLlib (cont.) | Metrics validation, cluster interpretation, marketing report |
| 06 | Deployment | Integration | Consigna compliance, model card, retrospective |

---

## Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.12 | Core language |
| PySpark 4.1.1 | Distributed processing engine |
| Spark MLlib | Scalable ML (LogReg, K-Means) |
| Java 17 (Temurin) | JVM runtime for Spark |
| Apache Parquet | Columnar storage (~60% compression vs CSV) |
| Spark SQL | Business metrics and aggregations |
| Matplotlib + Seaborn | Visualizations |
| Pandas + NumPy | Local data manipulation |

**Skills Demonstrated:**
`PySpark` · `Spark SQL` · `MLlib` · `RDD` · `DataFrame` · `Parquet` · `Big Data` · `K-Means` · `Logistic Regression` · `Pipeline` · `CRISP-DM` · `Business Analytics`

---

## How to Run

```powershell
# From portfolio root — activate shared virtual environment
.venv\Scripts\Activate.ps1

# Navigate to project
cd projects\project-8-retailmax-big-data

# Download dataset (requires Kaggle API)
kaggle datasets download -d olistbr/brazilian-ecommerce -p data/raw/ --unzip

# Launch notebooks
jupyter lab notebooks\01_business_understanding.ipynb
```

> ⚠️ Raw data excluded via `.gitignore`. Download from Kaggle before running.
> Requires: PySpark 4.1.1, Java 17 (Temurin), and `HADOOP_HOME` configured
> with `winutils.exe` for Windows Parquet write support.

---

## Strategic Recommendations

| Priority | Segment | Action | Expected Impact |
|---|---|---|---|
| 🔴 HIGH | High-ticket Critics (19%) | Service recovery — follow-up within 48h for reviews ≤ 2 | Mitigate ~$5.2M churn risk |
| 🔴 HIGH | One-time Satisfied (77%) | Reactivation — personalized 2nd-purchase offer at 30 days | ~$400K additional revenue |
| 🟡 MEDIUM | Multi-item Buyers (3%) | Bundle offers — volume discounts on 3+ item orders | +22% basket size ($370→$450) |
| 🟢 LOW | Loyal Repeaters (0.8%) | VIP program — free shipping, early access, birthday rewards | 95%+ retention of best segment |

---

## Business Impact Estimation

| Scenario | Current State | Target | Estimated Impact |
|---|---|---|---|
| Reactivate One-time Satisfied (5%) | 72,013 single-purchase | 3,600 repeat | ~$400K additional revenue |
| Recover High-ticket Critics | 17,911 dissatisfied, $290 avg | Review 2.1→3.5 | ~$5.2M churn risk mitigated |
| Expand Loyal Repeaters | 703 customers (0.8%) | Double to 1.5% | ~$200K incremental revenue |

> **Methodology:** Revenue estimates based on segment avg_ticket × projected conversion.
> **Assumptions:** 5% reactivation rate (conservative — industry avg 10–15%); churn prevention assumes 50% of dissatisfied critics would not return.

---

## Model Card

### Logistic Regression — High Value Classification

| Field | Details |
|---|---|
| **Model type** | Logistic Regression (binary) |
| **Task** | Classify customers as High Value (1) vs Low Value (0) |
| **Training data** | Olist, 93,396 customers |
| **Features** | 5: order_count, total_spent, avg_ticket, items_purchased, avg_review_score |
| **Target** | high_value (1 if avg_ticket > median) |
| **Framework** | Spark MLlib (PySpark 4.1.1) |
| **AUC-ROC** | 0.9506 |

### K-Means — Customer Segmentation

| Field | Details |
|---|---|
| **Model type** | K-Means Clustering |
| **Task** | Segment customers for targeted marketing |
| **K** | 4 (optimal K=3 by Silhouette; K=4 for richer segmentation) |
| **Features** | 5 (scaled with StandardScaler) |
| **Silhouette** | 0.5855 (K=4) / 0.8451 (K=3) |

---

## Limitations

- **Data:** Olist dataset is from 2016–2018 — customer behavior may differ in 2026
- **Model:** LogReg assumes linear feature-probability relationship — GBT could improve AUC
- **Scope:** Clickstream is synthetic — real data would improve features. Local mode only — cloud validation roadmap below
- **Target:** High Value threshold (median) should be validated against actual CLV data

---

## Deliverables

- [x] Notebooks (01–06) with PySpark development per lesson
- [x] Generated files (Parquet, visualizations)
- [x] Final report with results, metrics, and analysis
- [x] Functional MLlib pipeline documented
- [x] GitHub repository
- [x] Executive summary (EN + ES)

---

## Data Source

| Field | Details |
|---|---|
| **Dataset** | [Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) |
| **Provider** | Kaggle |
| **License** | CC BY-NC-SA 4.0 |
| **Records** | ~100K orders, 9 interrelated CSV tables |
| **Period** | 2016–2018 |
| **Accessed** | April 2026 |

### How to Reproduce

> ⚠️ Raw data excluded via `.gitignore`.

```bash
kaggle datasets download -d olistbr/brazilian-ecommerce -p data/raw/ --unzip
```

Synthetic clickstream (500K events) is generated within NB 02 using `spark.range()`.

---

## Cloud Validation Roadmap

The pipeline is designed for distributed execution. The local implementation
is the baseline; cloud validation demonstrates production-ready scalability.

| Platform | Status | Target Date | Purpose |
|---|---|---|---|
| 🟢 **Local (PySpark 4.1.1)** | ✅ Complete | April 2026 | Full pipeline development and testing |
| 🟡 **Google Colab** | ⏳ Planned | April 10, 2026 | Free cloud validation — proof that pipeline runs outside local environment |
| 🔵 **AWS EMR Serverless** | ⏳ Planned | Post-certification | Production-grade validation on industry-standard cloud platform (~$2–5 USD one-time cost) |
| 🟣 **Databricks Community** | Optional | TBD | Alternative cloud validation — recognized Spark platform |

**Why multiple platforms?** Different target markets value different cloud
certifications. AWS EMR is the strongest signal for USA/Canada roles.
Databricks is preferred for Data Engineering positions globally. Colab
provides the fastest no-cost validation.

---

## BI Integration Roadmap

The ML outputs (customer segments, classification predictions) are saved as
Parquet files — ready for direct consumption by business intelligence tools.

| Tool | Status | Purpose |
|---|---|---|
| 🟡 **Power BI** | ⏳ Planned (post-certification) | Interactive dashboard for marketing team — segment explorer, KPI tracker, campaign ROI simulator |
| 🟣 **Tableau** | Optional | Alternative BI layer |

**Planned Power BI dashboard:**
- **Page 1 — Segment Overview:** Customer count per segment, avg ticket, avg review, revenue contribution
- **Page 2 — High-Value Classifier:** Distribution of high-value predictions by state, category, payment method
- **Page 3 — Marketing Action Tracker:** Priority matrix (effort vs impact), expected ROI per action
- **Page 4 — What-If Analysis:** Slider controls to simulate reactivation rates, churn recovery scenarios

**Data pipeline to Power BI:**
```
PySpark (MLlib output) → Parquet → Power BI Desktop (DirectQuery or Import)
                                  OR
                                  → CSV export → Power BI Service (scheduled refresh)
```

This completes the full analytical stack: **Big Data ingestion → ML modeling → BI visualization → business decision**.

---

## Next Steps

| Horizon | Action |
|---|---|
| **Immediate** | Deliver segment report to marketing for Q2 2026 campaign design |
| **Short-term** | Validate pipeline on Google Colab (cloud environment) by April 10, 2026 |
| **Post-certification** | AWS EMR Serverless validation + Power BI interactive dashboard |
| **Long-term** | Integrate real clickstream data + BG/NBD lifetime value model |

> See [`docs/lean_retrospective.md`](docs/lean_retrospective.md) for full methodology retrospective.

---

## Credits

**Data:** [Olist Brazilian E-Commerce Dataset](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) (CC BY-NC-SA 4.0)

**Methodology References:**
- CRISP-DM: [Chapman et al. (2000)](https://www.the-modeling-agency.com/crisp-dm.pdf)
- Lean Thinking: Womack & Jones (1996)
- Apache Spark: [Official Documentation](https://spark.apache.org/docs/latest/)

**Tools & Libraries:** See [Tech Stack](#tech-stack) section.

---

## License

This project is licensed under the [MIT License](LICENSE).

© 2026 Jose Marcel Lopez Pino

---

*Framework: CRISP-DM + Lean | Methodology: Project-Based Learning (PBL)*

**Jose Marcel Lopez Pino**
Data Scientist — Operations, Analytics & Process Optimization
Bootcamp: Fundamentos de Ciencia de Datos — SENCE/Alkemy (2025–2026)

*Industrial Engineering in Chile (Academic degree: Bachelor of Science in
Industrial Engineering — 5.5-year program, comparable to a U.S. M.S.) encompasses
business strategy, finance, marketing, economics, operations management, and
technology management — backed by a rigorous scientific foundation in calculus,
linear algebra, probability and statistics, physics, and optimization — enabling
a unique business + analytics perspective.*

[![GitHub](https://img.shields.io/badge/GitHub-joselopezp-181717?style=flat&logo=github)](https://github.com/joselopezp)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-jose--lopez--pino-0077B5?style=flat&logo=linkedin)](https://www.linkedin.com/in/jose-lopez-pino/)
