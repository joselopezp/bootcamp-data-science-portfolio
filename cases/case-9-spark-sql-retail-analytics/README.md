# 1 Million Transactions Queried in Seconds: Spark SQL for Retail Decision-Making
### Distributed Sales Analytics — RetailMax · ~USD 500M Revenue Dataset | CRISP-DM + LEAN

![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![Python](https://img.shields.io/badge/Python-3.12-blue)
![PySpark](https://img.shields.io/badge/PySpark-4.1.1-orange)
![Type](https://img.shields.io/badge/Type-CBL-purple)
![Module](https://img.shields.io/badge/Module-9_Big_Data-red)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

> Distributed analytical queries on 1 million RetailMax sales transactions using
> Spark SQL — filter, aggregation, top-N — with Catalyst optimizer execution plan.

---

## Business Context

RetailMax operates a multi-branch retail network and needs to analyze its full
transactional history to inform inventory allocation, marketing budget assignment,
and branch performance benchmarking. This case demonstrates how Spark SQL enables
distributed queries on large structured datasets — the same query patterns scale
from thousands to billions of records with no code changes.

**Decision to support:** Where to allocate inventory and marketing resources based
on category and branch performance.

---

## Dataset

| | |
|---|---|
| **Source** | Synthetic RetailMax sales transactions |
| **Records** | 1,000,000 |
| **Columns** | 6 — `id_venta`, `id_sucursal`, `producto`, `categoria`, `monto`, `fecha` |
| **Categories** | 4 — Tecnologia, Oficina, Utiles, Accesorios |
| **Period** | 2025 |
| **Format** | CSV |

---

## Methodology

**Framework:** CRISP-DM + LEAN
**Modality:** Case-Based Learning (CBL)

| CRISP-DM Phase | Activity |
|---|---|
| Business Understanding | Define decisions to support — inventory, marketing, branch benchmarking |
| Data Understanding | Load CSV, inspect schema, distinct values, numeric summary |
| Data Preparation | Register temporary SQL view |
| Modeling | Three SQL queries — filter, aggregation, top-N |
| Evaluation | Inspect Catalyst execution plan, synthesize business insights |

---

## Results

| Query | Pattern | Key Result |
|---|---|---|
| **Q1** | Filter (`WHERE`) | 274,143 high-value Technology transactions (>CLP 300K) — 27% of all Tech sales |
| **Q2** | Aggregation (`GROUP BY`) | Tecnologia leads with CLP 190,436M (40% of total revenue) |
| **Q3** | Top-N (`ORDER BY` + `LIMIT`) | Top 5 branches generate CLP 2,650M combined; ticket ~CLP 490K |

**Key insight:** Average ticket is nearly identical across categories
(~CLP 475K — within 0.3% of each other). Revenue differences are driven by
**transaction volume**, not by pricing — directly informing where to focus
marketing spend.

---

## Project Structure

```
case-spark-sql-queries/
├── data/
│   └── raw/
│       └── ventas.csv
├── notebooks/
│   └── 01_spark_sql_queries.ipynb
├── reports/
│   └── executive_summary.md
└── README.md
```

---

## Tech Stack

- **Python 3.12**
- **PySpark 4.1.1** (local mode — `local[*]`)
- **Java 17 Temurin**
- **Spark SQL** (Catalyst optimizer)

---

## Setup

This case uses the shared `.venv` at the portfolio root.

```powershell
# From portfolio root
.venv\Scripts\Activate.ps1
cd cases\case-spark-sql-queries
jupyter notebook notebooks/01_spark_sql_queries.ipynb
```

The notebook resolves `data/raw/ventas.csv` relative to the case folder — no
absolute paths required. If your working directory differs, set the
`PROJECT_ROOT` environment variable to the case root.

---

## Key Learnings

- **Catalyst Optimizer** automatically applies *predicate pushdown* and
  *projection pruning* — the same SQL scales from local CSV to distributed
  cloud storage with no rewrites.
- **Temporary views** (`createOrReplaceTempView`) provide a SQL interface
  to DataFrames without persisting to a catalog — ideal for exploratory
  analysis sessions.
- **Volume vs price** — uniform ticket prices across categories revealed that
  RetailMax's revenue mix is purely a function of transaction count, not
  pricing strategy. This shifts the marketing question from *"raise prices?"*
  to *"drive volume in low-share categories?"*.

---

## Next Steps

- [ ] Convert `ventas.csv` to Parquet for ~10x faster repeated queries
- [ ] Add window functions (`ROW_NUMBER`, `RANK`) for top-N per branch
- [ ] Add temporal queries (`MONTH(fecha)`, `YEAR(fecha)`) for seasonality
- [ ] Migrate to AWS EMR Serverless + S3 for production-scale execution

---

## Author

**Jose Marcel Lopez Pino**
Industrial Engineer (Operations, Analytics & Process Optimization) | Data Science & Business Analytics
Bootcamp: Fundamentos de Ciencia de Datos — SENCE/Alkemy (2025–2026)

[![GitHub](https://img.shields.io/badge/GitHub-joselopezp-181717?style=flat&logo=github)](https://github.com/joselopezp)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-jose--lopez--pino-0077B5?style=flat&logo=linkedin)](https://www.linkedin.com/in/jose-lopez-pino/)
