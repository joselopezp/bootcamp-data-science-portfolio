# 426x Faster: Real-Time Mining Equity Metrics with NumPy
### Portfolio Analytics — BHP, FCX, RIO, VALE, SCCO | CRISP-DM + LEAN

![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![Framework](https://img.shields.io/badge/Framework-CRISP--DM%20%2B%20LEAN-2E86AB)
![Type](https://img.shields.io/badge/Type-Case--Based%20Learning-blueviolet)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## Business Problem

A financial analytics firm processing mining equity data relies on unstructured formats
and loop-based Python pipelines, causing performance bottlenecks when computing real-time
metrics for portfolio management decisions.

## Context

| | |
|---|---|
| **Industry** | Financial Services — Mining Equities |
| **Data** | Real closing prices via yfinance — BHP, FCX, RIO, VALE, SCCO |
| **Scope** | 5 equities × 5 trading days (5×5 NumPy matrix) |
| **Module** | M3 — Data Acquisition and Preparation |
| **Bootcamp** | Fundamentos de Ciencia de Datos — SENCE / Alkemy |

## Objective

Demonstrate that NumPy vectorized operations can replace loop-based Python pipelines
for financial metric computation — reducing code complexity while improving performance
at scale.

## Methodology

- **Ingestion** — Real closing prices downloaded via `yfinance` for 5 mining equities
- **Structuring** — DataFrame converted to a 5×5 NumPy matrix (rows = equities, columns = days)
- **Transformation** — Descriptive statistics, daily returns, log returns, min-max normalization, z-scores, base-100 price index — all via broadcasting, zero explicit loops
- **Comparison** — NumPy vectorized vs Python loops benchmark at scale (500 equities × 252 days)

## Key Findings

- All required financial metrics computed correctly using only NumPy vectorized operations
- NumPy delivered a measurable speedup over loop-based Python at realistic data scale
- Broadcasting with `keepdims=True` eliminates the need for manual reshaping in per-equity operations
- GARCH is the industry standard for volatility modeling on these assets; LSTM is a valid exploratory alternative given sufficient historical data (12+ months minimum)

## Business Impact

- **Better decisions** — Real-time metrics enable faster portfolio management responses in volatile markets
- **Risk reduction** — Vectorized operations eliminate accumulator errors common in manual loop implementations
- **Process optimization** — Code reduction from ~6 lines of nested loops to a single readable NumPy expression per metric

## Tech Stack

- Python 3.12
- NumPy 2.4.1
- yfinance
- pandas 3.0.0
- matplotlib 3.10.8

## How to Run
```bash
# 1. Clone the repository
git clone https://github.com/joselopezp/bootcamp-data-science-portfolio.git
cd bootcamp-data-science-portfolio

# 2. Activate the shared virtual environment
.venv\Scripts\Activate.ps1        # Windows
source .venv/bin/activate          # macOS / Linux

# 3. Navigate to the case
cd cases/case-numpy-financial-analysis

# 4. Launch Jupyter
jupyter lab
```

Open `notebooks/case_numpy_financial_analysis.ipynb` and run all cells.
Requires internet connection for `yfinance` data download.

---

*Framework: CRISP-DM + LEAN | Methodology: Case-Based Learning (CBL)*

**Jose Marcel Lopez Pino**
Industrial Engineer (Operations, Analytics & Process Optimization) | Data Science & Business Analytics
Bootcamp: Fundamentos de Ciencia de Datos — SENCE/Alkemy (2025–2026)

[![GitHub](https://img.shields.io/badge/GitHub-joselopezp-181717?style=flat&logo=github)](https://github.com/joselopezp)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-jose--lopez--pino-0077B5?style=flat&logo=linkedin)](https://www.linkedin.com/in/jose-lopez-pino/)
