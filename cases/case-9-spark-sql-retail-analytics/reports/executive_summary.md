# 1 Million Transactions Queried in Seconds: Spark SQL for Retail Decision-Making
### Distributed Sales Analytics — RetailMax · ~USD 500M Revenue Dataset | CRISP-DM + LEAN

**Author:** Jose Marcel Lopez Pino
**Role:** Industrial Engineer (Operations, Analytics & Process Optimization)
**Framework:** CRISP-DM + LEAN | Case-Based Learning (CBL)
**Date:** April 2026
**Status:** ![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

---

## 1. Business Context

| | |
|---|---|
| **Industry** | Retail |
| **Business Unit** | Sales Analytics & Operations |
| **Stakeholder** | Commercial Director / Operations Manager |
| **Decision to Support** | Where to allocate inventory and marketing budget across product categories and branches |

> **Situation:** RetailMax operates a multi-branch retail network with over 1 million
> sales transactions in the current period. Without distributed query capability,
> analytical questions about category mix, branch performance, and high-value transactions
> require manual sampling or off-line aggregation — limiting decision speed and accuracy.

---

## 2. Problem Statement

> How can RetailMax answer operational questions over its full transactional history
> (millions of records) in seconds, using a query interface that scales to cloud-scale
> data without rewrites?

**Business Impact if Unresolved:**
- Decisions on inventory and marketing are made on partial samples or stale aggregates
- ~1M transactions per period exceed the practical limit of single-machine pandas analysis
- Inability to drill into high-value transaction patterns delays restocking decisions

---

## 3. Analytical Approach

> Non-technical summary — what was done, not how.

| Step | Description |
|---|---|
| **Data** | 1,000,000 RetailMax sales transactions · 4 categories · 2025 |
| **Method** | Three Spark SQL queries — filter, aggregation, top-N — on a registered temporary view |
| **Tool** | Python · PySpark 4.1.1 · Spark SQL · Catalyst Optimizer |
| **Validation** | Inspected Catalyst execution plan (`explain(True)`) to confirm predicate pushdown and projection pruning |

---

## 4. Key Findings

> Three findings following: **Context → Analysis → Insight → Decision**

### Finding 1 — Technology dominates revenue mix (40%)
- **Context:** Four product categories operate across the branch network; mix is unknown at the executive level.
- **Analysis:** `Tecnologia` generates **CLP 190,436M** (40% of total), followed by `Oficina` (CLP 142,972M / 30%), `Utiles` (CLP 94,521M / 20%), and `Accesorios` (CLP 47,749M / 10%) — a textbook Pareto distribution.
- **Insight:** Revenue concentration in Technology is structural, not anomalous. The 40-30-20-10 split is consistent enough to anchor budget planning.
- **Possible Decision:** Allocate marketing and inventory budget proportionally to revenue contribution as a baseline, then test growth investments in lower-share categories.

### Finding 2 — Volume drives revenue, not price
- **Context:** Conventional retail wisdom assumes high-revenue categories command premium pricing.
- **Analysis:** Average ticket across all four categories is nearly identical: Tecnologia CLP 475,452 · Oficina CLP 476,326 · Utiles CLP 475,090 · Accesorios CLP 475,825 — a spread of only **0.3%**.
- **Insight:** RetailMax's revenue mix is purely a function of **transaction count**, not pricing. The Tecnologia advantage comes from selling 4x as many transactions as Accesorios at essentially the same average ticket.
- **Possible Decision:** Reframe the marketing question from *"can we raise prices in Tec?"* to *"can we drive transaction volume in Accesorios and Utiles?"*. Prioritize traffic-generating campaigns over premium-pricing initiatives.

### Finding 3 — High-value Technology segment is large enough to manage as its own line
- **Context:** Premium-priced transactions (>CLP 300K) are typically a minority worth special restocking attention.
- **Analysis:** **274,143 Technology transactions** exceed CLP 300K — approximately **27% of all Technology sales** and **27%** of total transactions in the dataset.
- **Insight:** This is not a niche segment. High-value Tech sales are large enough to justify dedicated inventory tracking, separate restocking cadence, and supplier-specific terms.
- **Possible Decision:** Establish a dedicated SKU-level dashboard for Tech transactions >CLP 300K with weekly restocking review, distinct from general inventory operations.

---

## 5. Business Recommendations

| Priority | Recommendation | Expected Impact | Effort |
|---|---|---|---|
| 🔴 High | Establish dedicated restocking process for Tech transactions >CLP 300K (~274K transactions) | Reduced stockouts in highest-margin segment | Medium |
| 🟡 Medium | Reallocate marketing investment toward volume-driving campaigns in Utiles and Accesorios | Closes 20–30 pp revenue-share gap vs Tec | Medium |
| 🟢 Low | Convert sales data to Parquet format for 10x faster recurring analytics queries | Faster decision cycles; lower compute cost | Low |

---

## 6. Limitations

- **Data:** Single-period synthetic dataset — no year-over-year comparison or seasonality analysis.
- **Scope:** Three query patterns (filter, aggregation, top-N) demonstrate core capability but do not include window functions, temporal aggregations, or joins.
- **Branch context:** Branch IDs are anonymized — geographic or demographic enrichment would strengthen the top-5 finding.

---

## 7. Next Steps

| Horizon | Action |
|---|---|
| **Immediate** | Convert `ventas.csv` to Parquet; expected ~10x query speedup for repeated analytics |
| **Short-term** | Add window functions and temporal queries (`MONTH(fecha)`, `YEAR(fecha)`) for seasonality and per-branch ranking |
| **Long-term** | Migrate to AWS EMR Serverless + S3 — same SQL code, distributed execution at production scale |

---

*Framework: CRISP-DM + LEAN | Methodology: Case-Based Learning (CBL)*

**Jose Marcel Lopez Pino**
Industrial Engineer (Operations, Analytics & Process Optimization) | Data Science & Business Analytics
Bootcamp: Fundamentos de Ciencia de Datos — SENCE/Alkemy (2025–2026)

[![GitHub](https://img.shields.io/badge/GitHub-joselopezp-181717?style=flat&logo=github)](https://github.com/joselopezp)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-jose--lopez--pino-0077B5?style=flat&logo=linkedin)](https://www.linkedin.com/in/jose-lopez-pino/)
