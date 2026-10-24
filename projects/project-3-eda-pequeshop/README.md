# PequeShop: Exploratory Data Analysis for Business Decisions

> **CRISP-DM Cycle 2 — Diagnostic Analytics** | Module 4: Análisis Exploratorio de Datos

![Python](https://img.shields.io/badge/Python-3.12.10-3776AB?logo=python&logoColor=white)
![Framework](https://img.shields.io/badge/Framework-CRISP--DM%20%2B%20LEAN-2E86AB)
![Type](https://img.shields.io/badge/Type-Diagnostic%20Analytics%20%7C%20EDA-blueviolet)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## Table of Contents

- [Project Overview](#project-overview)
- [Business Context](#business-context)
- [Key Results](#key-results)
- [Project Structure](#project-structure)
- [Tech Stack](#tech-stack)
- [Lessons Covered](#lessons-covered-module-4)
- [How to Run](#how-to-run)
- [Strategic Recommendations](#strategic-recommendations)
- [Deliverables](#deliverables)
- [Post-Evaluation Enhancements and Corrections](#post-evaluation-enhancements-and-corrections)
- [CRISP-DM Evolution Roadmap](#crisp-dm-evolution-roadmap)
- [Credits](#credits)
- [License](#license)

---

## Project Overview

This project applies Exploratory Data Analysis (EDA) techniques on PequeShop's e-commerce dataset to uncover customer behavior patterns and support strategic decisions on retention, pricing, and channel optimization.

**This is CRISP-DM Cycle 2**, building directly on [Project 2 (Module 3 — Data Preparation)](../Module_3_Data_Preparation/), which completed the first three CRISP-DM phases: Business Understanding, Data Understanding, and Data Preparation. Project 3 picks up with clean datasets and advances through Modeling, Evaluation, and Deployment — demonstrating how real data science projects evolve iteratively.

**What I learned:** Applying OLS regression with statsmodels to quantify variable relationships, distinguishing meaningful from spurious correlations, and translating statistical outputs (R², p-values, RMSE) into actionable business language for non-technical stakeholders.

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
| Buyers | 392 | Out of 500 registered (108 never purchased) |
| Average Ticket | $31,500 CLP | Right-skewed: Pareto pattern |
| NPS Score | 30.2 | 60% response rate among buyers (235 of 392); margin of error ±6.3 points at 95% confidence. Simulated survey: responses were assigned at random, so NPS carries no information about behavior in this dataset |
| Dormant Rate (180+ days) | 52.8% | 207 Dormant / 392 buyers |

### Regression Models (statsmodels OLS)

| Metric | Simple Regression | Multiple Regression |
|--------|-------------------|---------------------|
| R² | 0.362 | **0.772** |
| RMSE | $17,352 | **$10,378** |
| MAE | $12,041 | **$6,160** |
| Predictors | quantity | quantity + unit_price |

### Key Correlations (Pearson)

| Relationship | r | Classification |
|---|---|---|
| quantity → total_amount | 0.602 | Meaningful |
| unit_price → total_amount | 0.610 | Meaningful |
| subtotal → total_amount | 0.997 | Spurious (structural) |
| shipping → total_amount | -0.548 | Investigate |
| NPS → revenue | 0.12 | Weak (simulated survey, independent of behavior by design) |

---

## Project Structure

```
project-3-eda-pequeshop/
├── data/
│   ├── raw/                         # Symlink to Project 2 outputs
│   ├── processed/                   # Datasets from Project 2 ETL
│   │   ├── transactions_final.csv   # 1,192 rows × 19 columns
│   │   └── customers_final.csv      # 500 rows × 16 columns
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
├── LICENSE
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

**Skills Demonstrated:**
`Python` · `Pandas` · `NumPy` · `Statsmodels` · `Seaborn` · `Matplotlib` · `EDA` ·
`OLS Regression` · `Pearson Correlation` · `Statistical Analysis` · `Data Visualization` ·
`Business Analytics` · `CRISP-DM` · `Customer Churn Analysis` · `KPI Design`

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

## How to Run

```bash
# 1. Clone the repository
git clone https://github.com/joselopezp/bootcamp-data-science-portfolio.git
cd Projects/project-3-eda-pequeshop

# 2. Create and activate virtual environment
python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # Linux/Mac

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run notebooks in order
# Notebooks 01-03 reference Project 2 outputs (already in data/processed/)
# Start analysis from:
jupyter notebook notebooks/04_modeling.ipynb
```

> ⚠️ Raw data is excluded via `.gitignore`. Processed datasets from Project 2
> are available in `data/processed/` and are ready to use without additional setup.

---

## Strategic Recommendations

| Priority | Action | Expected Impact |
|----------|--------|-----------------|
| **HIGH** | Reactivation campaign for 207 Dormant customers. Success metric: share of the 207 who purchase within 90 days of contact, measured against a randomly held-out control group (target to be set after a pilot) | Scenario, not a forecast: each 10% reactivated ≈ 21 customers ≈ $0.68M CLP (one purchase each at the average Dormant ticket of $32,413). The 10% is illustrative, not an industry benchmark |
| **HIGH** | Cross-sell/upsell strategy (dual levers: quantity + unit_price) | Increase avg ticket by 15-20% |
| MEDIUM | Survey all buyers and improve the NPS response rate (current: 60% of buyers, assuming all 392 were invited) | Reliable satisfaction data: about 277 responses (71% of buyers) give a ±5-point margin at 95% confidence, assuming a 50/30/20 promoter/passive/detractor mix |
| MEDIUM | Investigate Shopify underperformance (25% vs MercadoLibre 75%) | Optimize channel investment |
| LOW | Analyze negative shipping correlation → free shipping threshold | Revenue uplift |

---

## Deliverables

- [x] Notebooks L1-L6 in VS Code (Jupyter)
- [x] 16 exported figures (PNG) in `reports/figures/`
- [x] Technical presentation (3-slide PPTX)
- [x] Commented source code (PEP 8, Google-style docstrings)
- [x] Final document with insights and recommendations
- [x] GitHub repository

---

## Post-Evaluation Enhancements and Corrections

After initial project evaluation, the following corrections and enhancements were made to this project.

| Type | Change | Description | Impact |
|------|--------|-------------|--------|
| Correction | Churn denominator | Dormant rate recalculated over the 392 customers with purchases (207 of 392 = 52.8%); previously 41.4% over 500 registered customers, which included 108 who never purchased | Rate now matches the segmentation in notebook 05 |
| Correction | NPS response rate | 235 responses over the 392 buyers (60%); previously 47% over 500 registered. The survey is simulated: responses were assigned at random among buyers | Buyers are the correct base; NPS carries no information about behavior in this dataset |
| Correction | NPS text in notebooks | Notebooks 04–06 stated 53% non-response over 500 registered customers; corrected to 40% non-response over the 392 buyers. One saved output in notebook 04 was edited to match its hard-coded print | Text now matches the README; no code or calculation changed |
| Correction | Unsourced target removed | The "<30%" churn target had no verified source. Replaced by a success metric (share of Dormant customers who purchase within 90 days of contact, against a random control group) and a labeled scenario | Target to be set after a pilot |
| Correction | Regression metrics | Multiple regression reported R² 0.992, RMSE $1,856 and MAE $1,295; the executed notebook gives R² 0.772, RMSE $10,378 and MAE $6,160. Simple regression RMSE and MAE aligned too ($17,352 and $12,041) | README now matches the executed notebook |
| Correction | File dimensions | `customers_final.csv` has 500 rows × 16 columns and `transactions_final.csv` 1,192 × 19 (previously 392 × 12 and 1,192 × 15) | Project structure matches the data |
| Correction | KPI panel labels | The KPI panel in notebook 05 labelled 392 as "Active Customers" and 52.8% as "Churn Rate"; the setup cell and the key insights also called all buyers "active". 392 is the number of buyers (the Active segment has 97) and 52.8% is the Dormant rate, a churn proxy. Labels and wording corrected and the figure regenerated; the README KPI table uses the same terms | Panel, segmentation table, insights and README now use the same definitions |
| Correction | "Active" wording in notebooks 04 and 06 | Notebook 04 ("active customers only") and notebook 06 ("52.8% de clientes activos están Dormidos") used "active" for all 392 buyers; the Active segment has 97. Changed to buyers, with the 207 of 392 denominator in notebook 06 | Same definition across notebooks 04 to 06 and the README |
| Enhancement | Business Understanding | Notebook 01 now documents the Problem Statement Canvas, the KPI definitions (with denominators) and a decisions log for this cycle | Success criteria are defined in phase 1, before the recommendations that use them |

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

## Credits

**Data:** PequeShop is a fictional Chilean e-commerce business created for
educational purposes within the Alkemy / SENCE Data Science Bootcamp (2025–2026).
The dataset was designed and generated by Jose Marcel Lopez Pino to simulate
realistic e-commerce operations.

**Methodology References:**
- CRISP-DM: [Chapman et al. (2000)](https://www.the-modeling-agency.com/crisp-dm.pdf) — Cross-Industry Standard Process for Data Mining
- Lean Thinking: Womack & Jones (1996) — applied to analytical workflow design
- OLS Regression: [Statsmodels Documentation](https://www.statsmodels.org/)
- NPS Framework: Reichheld, F. (2003) — *The One Number You Need to Grow*, Harvard Business Review

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

*Thesis: Volatility Forecasting of IPSA Stock Returns (Chilean Stock Exchange)
using a GJR-GARCH Model.*

[![GitHub](https://img.shields.io/badge/GitHub-joselopezp-181717?style=flat&logo=github)](https://github.com/joselopezp)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-jose--lopez--pino-0077B5?style=flat&logo=linkedin)](https://www.linkedin.com/in/jose-lopez-pino/)
