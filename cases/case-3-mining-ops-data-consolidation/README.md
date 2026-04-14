# From 6-Hour Weekly Cleanup to 5-Minute Automated Pipeline
### Mining Operations Data Consolidation — CSV, Excel & HTML Sources | CRISP-DM + LEAN

![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![Framework](https://img.shields.io/badge/Framework-CRISP--DM%20%2B%20LEAN-2E86AB)
![Type](https://img.shields.io/badge/Type-Case--Based%20Learning-blueviolet)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## Business Problem

A copper mining company consolidates operational data from three unintegrated source
systems — a CMMS exporting maintenance records as CSV, an ERP exporting production
reports as Excel, and a public web table providing industry benchmarks. Quality issues
across all three sources (nulls, duplicates, incorrect types, inconsistent casing)
require 4–6 hours of manual preparation per week, blocking automated KPI reporting
and delaying operational decisions by up to one business day.

## Context

| | |
|---|---|
| **Industry** | Mining — Copper Operations |
| **Data** | Simulated — 120 maintenance records (CSV), 90 production records (Excel), 8-mine reference table (HTML) |
| **Scope** | Three heterogeneous sources → single automated ingestion pipeline |
| **Module** | M3 — Data Acquisition and Preparation |
| **Bootcamp** | Fundamentos de Ciencia de Datos — SENCE / Alkemy |

## Objective

Demonstrate a structured Pandas ingestion pipeline that loads, cleans, transforms,
and exports data from three heterogeneous sources — reducing manual preparation from
4–6 hours/week to under 5 minutes per execution, with `assert`-validated output
quality at each step.

## Methodology

- **Ingestion** — CSV loaded with `read_csv()`, Excel with `read_excel()`, HTML table with `read_html()` (simulated in-memory for reproducibility)
- **Audit** — `quality_audit()` function diagnoses completeness, nulls, and duplicates across all three sources before any transformation
- **Cleaning** — Median imputation for skewed cost nulls, `errors='coerce'` for mixed-type columns, duplicate removal, datetime conversion, casing standardization
- **Transformation** — Column selection, snake_case renaming via regex, chronological sorting, derived metric (`cost_per_downtime_hour`)
- **Export** — Analysis-ready outputs to `data/processed/` as CSV and Excel; `assert` validation at each step

## Key Findings

- Structural inconsistency (column naming, mixed types, casing) was the dominant quality problem — not missing values
- `maintenance_cost` nulls (~15%) imputed with median to preserve record integrity; dropping would have caused unacceptable KPI distortion
- `read_html()` API is identical whether reading from a live URL or an in-memory HTML string — simulation is fully production-equivalent
- Root cause of most quality issues is upstream: inconsistent CMMS/ERP export configurations, not data entry errors

## Business Impact

- **Better decisions** — Daily KPI reporting enabled without manual intervention; operations team receives analysis-ready data each morning
- **Risk reduction** — `assert`-validated pipeline eliminates undocumented manual steps and version-control problems
- **Process optimization** — Pipeline reduces data preparation from 4–6 hours/week to under 5 minutes per execution (~50× improvement)

## Tech Stack

- Python 3.12
- pandas 3.0.0
- NumPy 2.4.1
- openpyxl
- lxml

## How to Run

```bash
# 1. Clone the repository
git clone https://github.com/joselopezp/bootcamp-data-science-portfolio.git
cd bootcamp-data-science-portfolio

# 2. Activate the shared virtual environment
.venv\Scripts\Activate.ps1        # Windows
source .venv/bin/activate          # macOS / Linux

# 3. Install case dependencies
pip install openpyxl lxml

# 4. Navigate to the case
cd cases/case-pandas-file-ingestion

# 5. Launch Jupyter
jupyter lab
```

Open `notebooks/case-pandas-file-ingestion.ipynb` and run all cells top to bottom.
No internet connection required — all data is generated synthetically by the notebook.

---

*Framework: CRISP-DM + LEAN | Methodology: Case-Based Learning (CBL)*

**Jose Marcel Lopez Pino**
Data Scientist — Operations, Analytics & Process Optimization | Data Science & Business Analytics
Bootcamp: Fundamentos de Ciencia de Datos — SENCE/Alkemy (2025–2026)

[![GitHub](https://img.shields.io/badge/GitHub-joselopezp-181717?style=flat&logo=github)](https://github.com/joselopezp)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-jose--lopez--pino-0077B5?style=flat&logo=linkedin)](https://www.linkedin.com/in/jose-lopez-pino/)
