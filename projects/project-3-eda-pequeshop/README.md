# PequeShop: Exploratory Data Analysis for Commercial Decisions

> **CRISP-DM Cycle 2 — Diagnostic Analytics** | Module 4: Análisis Exploratorio de Datos

---

## Project Overview

This project applies Exploratory Data Analysis (EDA) techniques on PequeShop's e-commerce dataset to uncover customer behavior patterns and support strategic decisions on retention, pricing, and channel optimization.

**This is CRISP-DM Cycle 2**, building directly on [Project 2 (Module 3 — Data Preparation)](../Module_3_Data_Preparation/), which completed the first three CRISP-DM phases: Business Understanding, Data Understanding, and Data Preparation. Project 3 picks up with clean datasets and advances through Modeling, Evaluation, and Deployment — demonstrating how real data science projects evolve iteratively.

```
CRISP-DM Iterative Cycles — PequeShop

Cycle 1 (Project 2, M3):  Business Understanding → Data Understanding → Data Preparation
                           Output: Clean datasets + KPIs + Customer segmentation

Cycle 2 (Project 3, M4):  Modeling → Evaluation → Deployment
                           Output: Statistical insights + Visualizations + Recommendations

Cycle 3 (Future, M6):     Predictive modeling (ML supervised)
Cycle 4 (Future, M7):     RFM + K-Means customer segmentation
Cycle 5 (Future, Post):   BG/NBD probabilistic models (CLV)
```

---

## Business Context

**PequeShop** is a Chilean e-commerce specializing in children's clothing and accessories (ages 4-10), operating on two platforms: MercadoLibre and Shopify. The Dirección de Análisis Estratégico needs to understand historical customer data to make evidence-based decisions.

**Key Business Questions:**
- What drives revenue? Which variables are the strongest predictors?
- What is the customer retention health? How severe is churn?
- Are there actionable patterns in customer behavior across platforms?
- Which correlations are meaningful vs. spurious?

---

## Key Results

| KPI | Value | Context |
|-----|-------|---------|
| Total Revenue | $37.5M CLP | 1,192 transactions |
| Active Customers | 392 | Out of 500 registered (108 never purchased) |
| Average Ticket | $31,500 CLP | Right-skewed: Pareto pattern |
| NPS Score | 30.2 | 47% response rate (53% no response — bias) |
| Churn Rate | 41.4% | 207 Dormant / 500 total customers |

### Regression Models (statsmodels OLS)

| Metric | Simple Regression | Multiple Regression |
|--------|-------------------|---------------------|
| R² | 0.362 | **0.992** |
| RMSE | $16,845 | **$1,856** |
| MAE | $12,334 | **$1,295** |
| Predictors | quantity | quantity + unit_price |

### Key Correlations (Pearson)

| Relationship | r | Classification |
|---|---|---|
| quantity → total_amount | 0.602 | Meaningful |
| unit_price → total_amount | 0.610 | Meaningful |
| subtotal → total_amount | 0.997 | Spurious (structural) |
| shipping → total_amount | -0.548 | Investigate |
| NPS → revenue | 0.12 | Weak (53% non-response bias) |

---

## Project Structure

```
project-3-eda-pequeshop/
├── data/
│   ├── raw/                         # Symlink to Project 2 outputs
│   ├── processed/                   # Datasets from Project 2 ETL
│   │   ├── transactions_final.csv   # 1,192 rows × 15 columns
│   │   └── customers_final.csv      # 392 rows × 12 columns
│   └── final/                       # Analysis outputs
├── notebooks/
│   ├── 01_business_understanding.ipynb   # → Links to Project 2 (M3 L1-L2)
│   ├── 02_data_understanding.ipynb       # → Links to Project 2 (M3 L2-L3)
│   ├── 03_data_preparation.ipynb         # → Links to Project 2 (M3 L4-L6)
│   ├── 04_modeling.ipynb                 # EDA + Stats + Correlations + Regression
│   ├── 05_evaluation.ipynb               # Seaborn + Matplotlib visualizations
│   └── 06_deployment.ipynb               # Insights + Recommendations + Export
├── reports/
│   ├── figures/                     # 16 exported PNG visualizations
│   └── pequeshop_eda_informe_tecnico.pptx
├── src/
│   ├── analysis.py
│   └── visualization.py
├── docs/
│   └── data_dictionary.md
└── README.md
```

### CRISP-DM Phase Mapping

| Notebook | CRISP-DM Phase | Scope | Source |
|----------|----------------|-------|--------|
| 01_business_understanding | Business Understanding | Problem definition, KPIs | **Project 2** |
| 02_data_understanding | Data Understanding | Data extraction, IDA | **Project 2** |
| 03_data_preparation | Data Preparation | ETL, cleaning, feature engineering | **Project 2** |
| 04_modeling | Modeling | EDA, descriptive stats, correlations, regression | **This project** |
| 05_evaluation | Evaluation | Advanced visualization (Seaborn + Matplotlib) | **This project** |
| 06_deployment | Deployment | Insights, recommendations, export | **This project** |

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.12 | Core language |
| Pandas | Data manipulation |
| NumPy | Numerical operations |
| Statsmodels | OLS regression, statistical tests |
| Seaborn | Statistical visualizations (pairplot, violinplot, heatmap, FacetGrid) |
| Matplotlib | Custom visualizations, subplots, export |
| SciPy | Statistical functions |
| Scikit-learn | Metrics (MSE, MAE) |

---

## Lessons Covered (Module 4)

| Lesson | Topic | Key Deliverables |
|--------|-------|-----------------|
| L1 | Análisis Exploratorio de Datos | Variable classification, IDA, EDA vs IDA distinction |
| L2 | Estadística Descriptiva | Mean, median, mode, variance, std, quartiles, histograms, boxplots |
| L3 | Correlación | Pearson coefficient, scatterplots, correlation matrix, spurious detection |
| L4 | Regresiones Lineales | OLS with statsmodels, R², MSE, MAE, predictor significance |
| L5 | Análisis Visual (Seaborn) | pairplot, violinplot, jointplot, heatmap, FacetGrid |
| L6 | Matplotlib | Subplots, annotations, custom styling, PNG export, technical report |

---

## Strategic Recommendations

| Priority | Action | Expected Impact |
|----------|--------|-----------------|
| **HIGH** | Reactivation campaign for 207 Dormant customers | Reduce churn from 41.4% to <30% |
| **HIGH** | Cross-sell/upsell strategy (dual levers: quantity + unit_price) | Increase avg ticket by 15-20% |
| MEDIUM | Improve NPS response rate (current: 47%) | Reliable satisfaction data |
| MEDIUM | Investigate Shopify underperformance (25% vs MercadoLibre 75%) | Optimize channel investment |
| LOW | Analyze negative shipping correlation → free shipping threshold | Revenue uplift |

---

## How to Run

```bash
# Clone the repository
git clone https://github.com/joselopezp/bootcamp-data-science-portfolio.git
cd Projects/project-3-eda-pequeshop

# Activate virtual environment
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # Linux/Mac

# Run notebooks in order
# Open 04_modeling.ipynb → 05_evaluation.ipynb → 06_deployment.ipynb
```

---

## Deliverables

- [x] Notebooks L1-L6 in VS Code (Jupyter)
- [x] 16 exported figures (PNG) in `reports/figures/`
- [x] Technical presentation (3-slide PPTX)
- [x] Commented source code (PEP 8, Google-style docstrings)
- [x] Final document with insights and recommendations
- [x] GitHub repository

---

## CRISP-DM Evolution Roadmap

| Level | Question | PequeShop Cycle | Module | Status |
|-------|----------|-----------------|--------|--------|
| Descriptive | What happened? | Project 2 (ETL + KPIs) | M3 | ✅ Done |
| Diagnostic | Why did it happen? | Project 3 (EDA + Regression) | M4 | ✅ Current |
| Predictive | What will happen? | Churn classification (ML) | M6 | ⏳ Next |
| Segmentation | Natural groups? | RFM + K-Means + NPS cross-analysis | M7 | 📋 Planned |
| Prescriptive | What should we do? | BG/NBD (CLV) + Earned Growth Rate (EGR) | Post | 🔮 Future |

---

*Framework: CRISP-DM + Lean | Methodology: Project-Based Learning (PBL)*

**Jose Marcel Lopez Pino**  
Industrial Engineer (Business + Operations) | Data Science & Business Analytics  
Bootcamp: Fundamentos de Ciencia de Datos - SENCE/Alkemy (2025-2026)

*Industrial Engineering in Chile encompasses finance, marketing, economics, and operations management — enabling a unique business + analytics perspective.*
