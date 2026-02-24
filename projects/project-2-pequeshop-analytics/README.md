# PequeShop: Data Preparation Pipeline

> **CRISP-DM Cycle 1 — Data Preparation** | Module 3: Preparación de Datos

![Python](https://img.shields.io/badge/Python-3.12.10-3776AB?logo=python&logoColor=white)
![Framework](https://img.shields.io/badge/Framework-CRISP--DM%20%2B%20LEAN-2E86AB)
![Type](https://img.shields.io/badge/Type-ETL%20Pipeline%20%7C%20Data%20Preparation-blueviolet)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## Table of Contents

- [Project Overview](#project-overview)
- [Business Context](#business-context)
- [Methodology: CRISP-DM + Lean](#methodology-crisp-dm--lean)
- [ETL Pipeline Architecture](#etl-pipeline-architecture)
- [KPI Summary](#kpi-summary-final-results)
- [Business Value](#business-value)
- [Pricing Insights](#pricing-insights-conceptual-extension)
- [KPI Framework](#kpi-framework)
- [Project Structure](#project-structure)
- [Tech Stack](#tech-stack)
- [Lessons / Pipeline Stages](#lessons--pipeline-stages)
- [Data Quality Report](#data-quality-report)
- [Key Outputs](#key-outputs)
- [Post-Evaluation Enhancements](#post-evaluation-enhancements)
- [How to Run](#how-to-run)
- [Credits](#credits)
- [License](#license)

---

## Project Overview

End-to-end ETL data preparation pipeline for PequeShop, a Chilean children's
e-commerce. Consolidates fragmented data from MercadoLibre, Shopify, and
marketing platforms into clean, analytics-ready datasets with business KPIs,
customer segmentation, and NPS integration.

**This is CRISP-DM Cycle 1**, covering phases 1–3 (Business Understanding,
Data Understanding, Data Preparation). Clean outputs feed directly into
[Project 3 (Module 4 — EDA)](../project-3-eda-pequeshop/), which continues
with Modeling, Evaluation, and Deployment.

**What I learned:** Designing multi-source ETL pipelines with schema
harmonization, applying hybrid outlier treatment (business rules + statistical
methods), and translating data quality decisions into documented business
rationale — not just technical fixes.

---

## Business Context

**PequeShop** is a Chilean e-commerce specializing in children's clothing and
accessories (ages 4–10). The company's growth journey:

| Phase | Period | Platform | Challenge |
|-------|--------|----------|-----------|
| Launch | 2023 | MercadoLibre | Market validation |
| Migration | 2024 | Shopify | Own storefront, reduce fees |
| Growth | 2024–2025 | Multi-channel | Facebook/Instagram Ads integration |

**Business Problem:** Data is fragmented across multiple platforms with
inconsistent formats, missing values, and outliers that prevent unified
analytics and decision-making.

**Business Decision Enabled:** Clean, consolidated data enables Customer
Lifetime Value (CLTV) analysis, Customer Acquisition Cost (CAC) optimization,
Net Promoter Score (NPS) segmentation, and marketing attribution modeling.

---

## Methodology: CRISP-DM + Lean

This project follows **CRISP-DM** for structured data science work, combined
with **Lean principles** for iterative validation and value generation over
excessive complexity.

**Lean principles applied:**
- **Eliminate waste:** Early identification of `customer_id` mapping ensured
  data traceability across platforms, avoiding rework in later phases.
- **Build-Measure-Learn:** NPS integration was discovered during exploratory
  analysis and incorporated iteratively, enhancing customer segmentation
  without delaying the pipeline.
- **Value focus:** Every transformation decision (outlier treatment, feature
  engineering) was evaluated against business impact, not just technical
  correctness.

### Project Scope: CRISP-DM Phases

| CRISP-DM Phase | Lean Principle Applied | ETL Stage | Lessons |
|----------------|------------------------|-----------|---------|
| ✅ Business Understanding | Value focus | — | Problem definition, KPIs |
| ✅ Data Understanding | Eliminate waste | **Extract** | L1–L3: Early `customer_id` mapping |
| ✅ Data Preparation | Build-Measure-Learn | **Transform** | L4–L5: NPS discovered & integrated iteratively |
| ✅ Data Preparation | Continuous improvement | **Load** | L6: Aggregation, KPIs, export |
| ⏳ Modeling | — | — | *Project 3 (M4)* |
| ⏳ Evaluation | — | — | *Project 3 (M4)* |
| ⏳ Deployment | — | — | *Project 3 (M4)* |

> See [`docs/lean_retrospective.md`](docs/lean_retrospective.md) for full
> methodology retrospective.

---

## ETL Pipeline Architecture

```
┌──────────────────────────────────────────────────────────────────┐
│                         EXTRACT                                   │
├──────────────────────────────────────────────────────────────────┤
│  📄 CSV     → MercadoLibre historical transactions               │
│  📊 Excel   → Shopify orders (different schema)                  │
│  🌐 Web     → Marketing campaign metrics (HTML table)            │
└──────────────────────────────────────────────────────────────────┘
                              ↓
┌──────────────────────────────────────────────────────────────────┐
│                        TRANSFORM                                  │
├──────────────────────────────────────────────────────────────────┤
│  🔧 Schema harmonization (column mapping)                        │
│  📅 Date format standardization                                  │
│  🏷️  Categorical encoding (products, regions)                    │
│  🚫 Missing value imputation (median/mode)                       │
│  📊 Outlier detection (IQR + Z-score hybrid)                     │
│  ✨ Feature engineering (time, customer metrics)                 │
│  🎯 NPS integration and classification                           │
│  🔄 Retargeting segment creation                                 │
└──────────────────────────────────────────────────────────────────┘
                              ↓
┌──────────────────────────────────────────────────────────────────┐
│                          LOAD                                     │
├──────────────────────────────────────────────────────────────────┤
│  💾 CSV  → Clean datasets for analysis                           │
│  📊 Excel → Business-ready workbook for stakeholders             │
│  📈 KPI Dashboard → Executive summary metrics                    │
└──────────────────────────────────────────────────────────────────┘
```

---

## KPI Summary (Final Results)

| Category | Metric | Value |
|----------|--------|-------|
| 📊 Customer Health | NPS Score | 30.2 |
| 📊 Customer Health | Churn Rate | 41.4% |
| 📊 Customer Health | At-Risk Rate | 17.6% |
| 💰 Revenue | Total Revenue | $37.8M CLP (~$44K USD) |
| 💰 Revenue | Transactions | 1,192 |
| 💰 Revenue | Average Ticket | $31,689 CLP (~$37 USD) |
| 🎯 Customers | Registered | 500 |
| 🎯 Customers | Active (with purchases) | 392 |
| 🎯 Acquisition | Overall CAC | $23,771 CLP (~$28 USD) |

*Exchange rate: 1 USD ≈ 860 CLP (Feb 2026)*

---

## Business Value

### Problem Solved

Fragmented data across multiple platforms prevented PequeShop from
understanding customer behavior and making data-driven decisions. This
pipeline consolidates and cleans data to enable actionable analytics.

### Decisions Enabled

| Analysis | Business Decision |
|----------|-------------------|
| NPS by segment | Prioritize customer service resources |
| CAC by channel | Optimize marketing budget allocation |
| Customer Churn | Trigger retention campaigns |
| Revenue Churn | Forecast and stabilize cash flow |
| Retargeting segments | Personalized marketing actions |

### Retargeting Segments Created

| Segment | Criteria | Action |
|---------|----------|--------|
| Active | Purchased within 90 days | Upsell campaigns |
| At Risk | No purchase 90–180 days | Retention offers |
| Dormant | No purchase 180+ days | Win-back campaigns |

*Note: Thresholds adjusted for children's clothing retail cycle
(kids outgrow clothes every 3–6 months).*

### ROI Potential

- **Reduce churn** by identifying at-risk customers early
- **Lower CAC** by focusing on high-performing channels
- **Increase CLTV** through targeted retention actions
- **Improve NPS** by addressing detractor feedback

---

## Pricing Insights (Conceptual Extension)

### Price Elasticity Model

**Method:** Log-Log regression (industry standard)

```
ln(Q) = α + β·ln(P)
```

Where β represents price elasticity of demand directly.

### Elasticity by NPS Segment

| Segment | β (Elasticity) | Interpretation | Strategy |
|---------|----------------|----------------|----------|
| Promoters (9–10) | -0.6 | Inelastic | Premium pricing potential |
| Passives (7–8) | -1.1 | Unit elastic | Maintain current pricing |
| Detractors (0–6) | -1.8 | Elastic | Discount-driven retention |

> "In a hypothetical scenario (e.g., β ≈ -0.6), high NPS customers may exhibit
> lower price sensitivity, opening the door for future price optimization
> analysis without sacrificing customer loyalty."

---

## KPI Framework

See [KPI Framework](docs/kpi_framework.md) for complete metrics documentation.

### KPI Tree (Executive Level)

```
                         ┌─────────────────┐
                         │     REVENUE     │
                         └────────┬────────┘
            ┌────────────────────┼────────────────────┐
            ▼                    ▼                    ▼
    ┌──────────────┐    ┌──────────────┐    ┌──────────────┐
    │    Traffic   │    │  Conversion  │    │     AOV      │
    └──────────────┘    └──────────────┘    └──────────────┘

                       ┌─────────────────┐
                       │  PROFITABILITY  │
                       └────────┬────────┘
            ┌────────────────────┼────────────────────┐
            ▼                    ▼                    ▼
    ┌──────────────┐    ┌──────────────┐    ┌──────────────┐
    │     CAC      │    │Revenue Churn │    │  Elasticity  │
    └──────────────┘    └──────────────┘    └──────────────┘
```

---

## Project Structure

```
project-2-pequeshop-analytics/
├── data/
│   ├── raw/                        # Original & intermediate data
│   │   ├── *.npy                   # NumPy arrays (synthetic generation)
│   │   ├── shopify_orders_2024.xlsx
│   │   ├── marketing_metrics.html
│   │   ├── marketing_metrics.csv
│   │   ├── transactions_*.csv      # Pipeline stages
│   │   ├── customers_*.csv
│   │   └── nps_surveys.csv
│   └── processed/                  # Final clean datasets
│       ├── transactions_final.csv
│       ├── customers_final.csv
│       └── pequeshop_analytics.xlsx
├── notebooks/
│   └── data_preparation.ipynb      # Main ETL pipeline (L1–L6)
├── docs/
│   ├── pricing_playbook.md
│   ├── kpi_framework.md
│   └── lean_retrospective.md
├── LICENSE
└── README.md
```

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.12 | Core language |
| NumPy | Numerical operations, synthetic data generation |
| Pandas | Data manipulation, ETL pipeline |
| SciPy | Statistical methods (Z-score outlier detection) |
| openpyxl | Excel read/write |
| lxml | HTML parsing (web data extraction) |

**Skills Demonstrated:**
`Python` · `Pandas` · `NumPy` · `SciPy` · `ETL Pipeline` · `Data Cleaning` ·
`Feature Engineering` · `Outlier Detection` · `NPS Analysis` · `Customer Segmentation` ·
`CRISP-DM` · `Business Analytics` · `KPI Design` · `E-commerce Analytics`

---

## Lessons / Pipeline Stages

| Stage | CRISP-DM | ETL | Description | Status |
|-------|----------|-----|-------------|--------|
| L1 | Data Understanding | — | Synthetic data generation (NumPy) | ✅ |
| L2 | Data Understanding | Extract | DataFrame creation (Pandas) | ✅ |
| L3 | Data Understanding | Extract | Multi-source ingestion (CSV, Excel, Web) | ✅ |
| L4 | Data Preparation | Transform | Missing values & outliers | ✅ |
| L5 | Data Preparation | Transform | Data wrangling, NPS, feature engineering | ✅ |
| L6 | Data Preparation | Load | Aggregation, KPIs, pivot & export | ✅ |

---

## Data Quality Report

### Before Cleaning
- Initial generation: 2,000 transactions (L1)
- After consolidation: 1,192 transactions (892 MercadoLibre + 300 Shopify)
- Null values: Present in Shopify data
- Outliers: Extreme prices, bulk quantities

### After Cleaning
- Null values: 0 (imputed with median/mode)
- Outliers: Capped or flagged
- New features: 15+ engineered columns
- Data integrity: 100%
- Final transactions: 1,192
- Active customers: 392

### Cleaning Decisions Documented

| Issue | Decision | Rationale |
|-------|----------|-----------|
| Missing prices | Impute with median | Robust to outliers |
| Price > 100k CLP | Cap at P99 | Likely data entry error (hybrid approach) |
| Quantity > 20 | Flag, don't remove | Valid bulk orders exist |
| Negative values | Remove row | Invalid transaction |

**Outlier Treatment Strategy:**
- Detection: Business rule (>100,000 CLP = likely data entry error)
- Capping: P99 percentile to preserve realistic price distribution
- Hybrid approach: domain knowledge for detection + statistical methods
  for replacement.

---

## Key Outputs

### Files Generated

| File | Records | Purpose |
|------|---------|---------|
| transactions_final.csv | 1,192 | Clean transaction data with time features |
| customers_final.csv | 392 | Active customers with NPS, metrics, segments |
| nps_surveys.csv | ~235 | NPS survey responses (60% of active customers) |
| pequeshop_analytics.xlsx | 6 sheets | Business-ready workbook |

### Features Engineered

**Time Features:**
- year, month, quarter, season, day_of_week, is_weekend

**Customer Features:**
- total_transactions, total_revenue, avg_ticket
- days_since_last_purchase, tenure_days
- nps_score, nps_category
- retargeting_segment, is_high_value, priority_winback

---

## Post-Evaluation Enhancements

After initial project evaluation, the following improvements were implemented
in the `post-evaluation-enhancements` branch:

| Enhancement | Description | Impact |
|-------------|-------------|--------|
| Customer ID consistency | Shopify transactions now use existing customer IDs from pool | Data integrity improved |
| Retargeting thresholds | Adjusted from 60/90 to 90/180 days | More realistic for children's clothing retail |
| Variable naming | Standardized `df_treated` throughout L5–L6 | Code consistency |
| KPI accuracy | Recalculated with corrected data | More reliable metrics |

### Future Roadmap

| Enhancement | Description | Priority |
|-------------|-------------|----------|
| RFM Segmentation | Recency, Frequency, Monetary analysis | Medium |
| Earned Growth Rate (EGR) | Referral tracking, Net Revenue Retention | Medium |
| Fader & Hardie Model (sBG) | Cohort-based churn projection | Advanced |
| CLTV Modeling | Customer Lifetime Value prediction | High |

---

## How to Run

```bash
# 1. Clone repository
git clone https://github.com/joselopezp/bootcamp-data-science-portfolio.git

# 2. Navigate to project
cd projects/project-2-pequeshop-analytics

# 3. Create and activate virtual environment
python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # Linux/Mac

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run notebook
jupyter notebook notebooks/data_preparation.ipynb
```

> ⚠️ Raw data is generated synthetically in L1 of the notebook —
> no external dataset download required.

---

## Credits

**Data:** PequeShop is a fictional Chilean e-commerce business created for
educational purposes within the Alkemy / SENCE Data Science Bootcamp (2025–2026).
The dataset was designed and generated synthetically by Jose Marcel Lopez Pino
using NumPy to simulate realistic multi-platform e-commerce operations.

**Methodology References:**
- CRISP-DM: [Chapman et al. (2000)](https://www.the-modeling-agency.com/crisp-dm.pdf) — Cross-Industry Standard Process for Data Mining
- Lean Thinking: Womack & Jones (1996) — applied to analytical workflow design
- NPS Framework: Reichheld, F. (2003) — *The One Number You Need to Grow*, Harvard Business Review
- Price Elasticity: Varian, H. (1992) — *Microeconomic Analysis*, applied to NPS segmentation

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

*Industrial Engineering in Chile encompasses finance, marketing, economics,
and operations management — enabling a unique business + analytics perspective.*

[![GitHub](https://img.shields.io/badge/GitHub-joselopezp-181717?style=flat&logo=github)](https://github.com/joselopezp)
