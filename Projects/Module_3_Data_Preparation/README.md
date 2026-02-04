# PequeShop: Data Preparation Pipeline

## End-to-End Data Science Project with Business Focus

**Framework:** CRISP-DM  
**Data Pipeline:** ETL (Extract, Transform, Load)  
**Focus:** Applied Data Science for E-commerce Analytics

---

## Business Context

**PequeShop** is a Chilean e-commerce specializing in children's clothing and accessories (ages 4-10). The company's growth journey:

| Phase | Period | Platform | Challenge |
|-------|--------|----------|-----------|
| Launch | 2023 | MercadoLibre | Market validation |
| Migration | 2024 | Shopify | Own storefront, reduce fees |
| Growth | 2024-2025 | Multi-channel | Facebook/Instagram Ads integration |

**Business Problem:** Data is fragmented across multiple platforms with inconsistent formats, missing values, and outliers that prevent unified analytics and decision-making.

**Business Decision Enabled:** Clean, consolidated data enables Customer Lifetime Value (CLTV) analysis, Customer Acquisition Cost (CAC) optimization, and marketing attribution modeling.

---

## Project Evolution

This project followed an iterative approach aligned with CRISP-DM methodology:

1. **Initial Scope:** Consolidate transaction data from multiple platforms
2. **Discovery:** During data preparation, exploratory analysis revealed that customer feedback could be consolidated into an NPS metric
3. **Refined Objective:** Correlate customer satisfaction with purchasing behavior

This evolution demonstrates how real-world data science projects evolve iteratively, uncovering opportunities to enhance business value beyond the original scope.

---

## Project Scope: CRISP-DM Phases

This project covers the first three phases of the CRISP-DM methodology:

```
┌─────────────────────────────────────────────────────────────────┐
│                        CRISP-DM Framework                        │
├─────────────────────────────────────────────────────────────────┤
│  ✅ Business Understanding    → Problem definition, KPIs        │
│  ✅ Data Understanding        → Extract (ETL)                   │
│  ✅ Data Preparation          → Transform + Load (ETL)          │
│  ⏳ Modeling                  → Future: ML models               │
│  ⏳ Evaluation                → Future: Business impact         │
│  ⏳ Deployment                → Future: Dashboard/API           │
└─────────────────────────────────────────────────────────────────┘
```

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

## Business Value

### Problem Solved

Fragmented data across multiple platforms prevented PequeShop from understanding customer behavior and making data-driven decisions. This pipeline consolidates and cleans data to enable actionable analytics.

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
| Active | Purchased within 60 days | Upsell campaigns |
| At Risk | No purchase 60-90 days | Retention offers |
| Dormant | No purchase 90+ days | Win-back campaigns |
| High Value Inactive | High CLTV + inactive | VIP exclusive offer |

### ROI Potential

- **Reduce churn** by identifying at-risk customers early
- **Lower CAC** by focusing on high-performing channels
- **Increase CLTV** through targeted retention actions
- **Improve NPS** by addressing detractor feedback

---

## Pricing Insights

### Price Elasticity Model

**Method:** Log-Log regression (industry standard)

```
ln(Q) = α + β·ln(P)
```

Where β represents price elasticity of demand directly.

### Elasticity by NPS Segment

| Segment | β (Elasticity) | Interpretation | Strategy |
|---------|----------------|----------------|----------|
| Promoters (9-10) | -0.6 | Inelastic | Premium pricing potential |
| Passives (7-8) | -1.1 | Unit elastic | Maintain current pricing |
| Detractors (0-6) | -1.8 | Elastic | Discount-driven retention |

**Key Insight:**

> "High NPS customers show lower price sensitivity (β = -0.6), enabling targeted price optimization without sacrificing loyalty."

---

## Prescriptive Pricing Framework

**Approach:** Bounded adjustments based on elasticity, not point estimates.

> "Based on estimated price elasticity, pricing recommendations were defined as bounded adjustments rather than point estimates."

### Decision Rules (Customer-Aware Pricing)

| Elasticity | NPS | Churn Risk | Recommendation |
|------------|-----|------------|----------------|
| Inelastic (β > -1) | High | Low | ↑ Price increase up to 5% |
| Inelastic (β > -1) | Low | High | → Hold price |
| Elastic (β < -1) | High | Low | → Maintain price |
| Elastic (β < -1) | Low | High | ↓ Promotional discount |

**Example:**
- Elasticity: β = -0.6 (inelastic)
- Action: +5% price increase
- Expected impact: -3% volume, net revenue ↑

See [Pricing Playbook](docs/pricing_playbook.md) for implementation guidelines.

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

## Production Architecture (Reference)

This project is a local MVP. Below is the reference architecture for a production deployment:

```
┌─────────────────────────────────────────────────────────────┐
│                        AWS Cloud                             │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│   S3 Bucket          →    Lambda/Glue    →    Redshift      │
│   (Raw Data)              (ETL Pipeline)      (Data Warehouse)
│                                                      ↓       │
│                                               QuickSight     │
│                                               (Dashboard)    │
└─────────────────────────────────────────────────────────────┘
```

| Component | Local (Current) | Production (AWS) |
|-----------|-----------------|------------------|
| Storage | CSV/Excel files | S3 Bucket |
| Processing | Python scripts | Lambda / Glue |
| Data Warehouse | Pandas DataFrames | Redshift |
| Visualization | Excel / Jupyter | QuickSight |

---

## Project Structure

```
Module_3_Data_Preparation/
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
│   └── data_preparation.ipynb      # Main ETL pipeline (L1-L6)
├── docs/
│   ├── pricing_playbook.md
│   └── kpi_framework.md
└── README.md
```

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.12 | Core language |
| NumPy | Numerical operations, synthetic data |
| Pandas | Data manipulation, ETL |
| SciPy | Statistical methods (Z-score) |
| openpyxl | Excel read/write |
| lxml | HTML parsing |

---

## Lessons / Pipeline Stages

| Stage | CRISP-DM | ETL | Description | Status |
|-------|----------|-----|-------------|--------|
| L1 | Data Understanding | - | Synthetic data generation (NumPy) | ✅ |
| L2 | Data Understanding | Extract | DataFrame creation (Pandas) | ✅ |
| L3 | Data Understanding | Extract | Multi-source ingestion (CSV, Excel, Web) | ✅ |
| L4 | Data Preparation | Transform | Missing values & outliers | ✅ |
| L5 | Data Preparation | Transform | Data wrangling, NPS, feature engineering | ✅ |
| L6 | Data Preparation | Load | Aggregation, KPIs, pivot & export | ✅ |

---

## Data Quality Report

### Before Cleaning
- Total records: ~2,000+ transactions
- Null values: Present in Shopify data
- Outliers: Extreme prices, bulk quantities

### After Cleaning
- Null values: 0 (imputed with median/mode)
- Outliers: Capped or flagged
- New features: 15+ engineered columns
- Data integrity: 100%

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
- This hybrid approach uses domain knowledge for detection and statistical methods for replacement.

---

## Key Outputs

### Files Generated

| File | Records | Purpose |
|------|---------|---------|
| transactions_final.csv | 2,000 | Clean transaction data with time features |
| customers_final.csv | 500 | Enriched customers with NPS, metrics, segments |
| nps_surveys.csv | 300 | NPS survey responses |
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

## How to Run

```bash
# 1. Clone repository
git clone https://github.com/joselopezp/bootcamp-data-science-portfolio.git

# 2. Navigate to project
cd Projects/Module_3_Data_Preparation

# 3. Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run notebook
jupyter notebook notebooks/data_preparation.ipynb
```

---

## Next Steps (Future Work)

| Phase | Local (Current) | Production (AWS) |
|-------|-----------------|------------------|
| Storage | CSV/Excel files | S3 Bucket |
| Processing | Python scripts | Lambda / Glue |
| Data Warehouse | Pandas DataFrames | Redshift |
| Visualization | Excel / Jupyter | QuickSight |

**Modeling opportunities:**
- Churn Prediction Model
- CLTV Estimation
- Price Elasticity Analysis (Log-Log regression)
- A/B Testing Framework

---

## Author

**Jose Marcel Lopez Pino**  
Industrial Engineer | Data Science & Business Analytics  
Bootcamp: Fundamentos de Ciencia de Datos - SENCE/Alkemy (2024-2026)

[![GitHub](https://img.shields.io/badge/GitHub-joselopezp-181717?style=flat&logo=github)](https://github.com/joselopezp)

---

## License

Educational project - Portfolio demonstration
