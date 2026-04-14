# From 6-Hour Weekly Cleanup to 5-Minute Automated Pipeline
### Mining Operations Data Consolidation — CSV, Excel & HTML Sources | CRISP-DM + LEAN

**Author:** Jose Marcel Lopez Pino
**Role:** Data Scientist — Operations, Analytics & Process Optimization
**Framework:** CRISP-DM + LEAN | Case-Based Learning (CBL)
**Date:** April 2026
**Status:** ![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

---

## 1. Business Context

| | |
|---|---|
| **Industry** | Mining — Copper Operations |
| **Business Unit** | Operations & Maintenance |
| **Stakeholder** | Operations Director / Maintenance Manager |
| **Decision to Support** | Can daily KPI reporting (availability, production, maintenance cost) be automated without manual data preparation? |

> **Situation:** A mid-size copper mining company consolidates operational data from three
> unintegrated source systems: a CMMS exporting maintenance records as CSV, an ERP exporting
> daily production reports as Excel, and public web tables providing industry benchmarks.
> Each source arrives weekly with quality issues that require 4–6 hours of manual cleaning
> before any reporting can begin — blocking operational decisions by up to one business day.

---

## 2. Problem Statement

> Can a Pandas ingestion pipeline automatically load, clean, and standardize data from three
> heterogeneous sources to enable daily automated operational reporting?

**Business Impact if Unresolved:**
- 4–6 hours/week of analyst time consumed by manual data preparation (~$10–15k/year in labor cost)
- KPI dashboards delayed by up to 1 business day — maintenance decisions made on stale data
- Duplicate production records inflate reported tonnage figures, distorting performance metrics
- No reproducibility — manual cleaning steps are undocumented and operator-dependent

---

## 3. Analytical Approach

> Non-technical summary — what was done, not how.

| Step | Description |
|---|---|
| **Data** | Three simulated sources mirroring real mine-site architecture: 120 maintenance records (CSV), 90 daily production records (Excel), 8-mine industry reference table (HTML) |
| **Method** | CRISP-DM Phase 3 pipeline: load → audit → clean → transform → export |
| **Tool** | Python · pandas 3.0.0 · openpyxl · lxml |
| **Validation** | `assert` statements validate completeness, duplicate count, and data types at each cleaning step before proceeding |

---

## 4. Key Findings

### Finding 1 — Structural inconsistency is the dominant quality problem
- **Context:** Three sources were loaded and audited before any cleaning was applied.
- **Analysis:** Of the total quality issues found, type errors and naming inconsistencies (column names with special characters, mixed-type columns, inconsistent casing) outnumbered null values. The Excel source had 7 duplicate rows (~8%) and 3 columns with names containing spaces and parentheses that broke automated joins.
- **Insight:** The root cause is upstream — inconsistent export configurations in the CMMS and ERP, not data entry errors. Fixing the export settings would eliminate most downstream cleaning work.
- **Possible Decision:** Operations IT should standardize CMMS and ERP export templates to enforce consistent column naming and eliminate duplicate-export behavior at the source.

### Finding 2 — Median imputation preserves 15% of maintenance records at acceptable cost
- **Context:** The `maintenance_cost` column had ~15% null values — a level too high to drop without losing statistical reliability.
- **Analysis:** Cost distribution was right-skewed (range: $500–$15,000 USD). Median imputation ($4,823 USD) was chosen over mean to avoid inflating central tendency estimates due to high-cost outlier events.
- **Insight:** Imputed records are flagged implicitly by the pipeline — any downstream analysis should treat imputed cost values as estimates, not actuals. A confidence interval on cost KPIs should reflect this uncertainty.
- **Possible Decision:** Maintenance team should enforce cost entry as a mandatory field in the CMMS work order closure workflow to eliminate nulls at the source within 60 days.

### Finding 3 — Pipeline reduces preparation time from hours to minutes
- **Context:** Manual cleaning currently takes 4–6 hours per week across three sources.
- **Analysis:** The full pipeline — load, audit, clean, transform, export — executes in under 5 minutes on a standard laptop, with `assert`-validated output quality at each step.
- **Insight:** The pipeline is reproducible and operator-independent. The same input always produces the same output, eliminating the undocumented manual steps that currently create version-control and auditability problems.
- **Possible Decision:** Schedule the pipeline for daily automated execution (cron / Airflow) to deliver analysis-ready datasets to the BI layer each morning before the operations shift review.

---

## 5. Business Recommendations

| Priority | Recommendation | Expected Impact | Effort |
|---|---|---|---|
| 🔴 High | Schedule pipeline for daily automated execution | Eliminates 4–6 h/week manual prep; enables same-day KPI reporting | Low |
| 🔴 High | Enforce mandatory `maintenance_cost` entry in CMMS work order closure | Eliminates ~15% null rate; improves cost KPI reliability | Low |
| 🟡 Medium | Standardize ERP and CMMS export templates (column names, no duplicates) | Removes structural inconsistency at source; reduces pipeline complexity | Medium |
| 🟢 Low | Extend pipeline with a `merge` step joining maintenance and production on `faena` | Enables integrated availability + cost analysis in a single dataset | Low |

---

## 6. Limitations

- **Data:** Simulated datasets — real production volumes and costs will differ; pipeline logic is validated but business metrics require real data before decision use
- **Method:** Ingestion and preparation only — no predictive or diagnostic analysis in this version
- **Scope:** `maintenance_cost` nulls imputed with median — imputed values should be treated as estimates in cost KPI calculations, not as actuals

---

## 7. Next Steps

| Horizon | Action |
|---|---|
| **Immediate** | Use `equipment_maintenance_clean.csv` as input for M3 EDA case (failure type frequency, cost by equipment type) |
| **Short-term** | Add merge step joining production and maintenance on `faena` for integrated availability + cost dashboard |
| **Long-term** | Schedule pipeline for daily automated execution via cron or Apache Airflow in production environment |

---

*Framework: CRISP-DM + LEAN | Methodology: Case-Based Learning (CBL)*

**Jose Marcel Lopez Pino**
Data Scientist — Operations, Analytics & Process Optimization | Data Science & Business Analytics
Bootcamp: Fundamentos de Ciencia de Datos — SENCE/Alkemy (2025–2026)

[![GitHub](https://img.shields.io/badge/GitHub-joselopezp-181717?style=flat&logo=github)](https://github.com/joselopezp)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-jose--lopez--pino-0077B5?style=flat&logo=linkedin)](https://www.linkedin.com/in/jose-lopez-pino/)
