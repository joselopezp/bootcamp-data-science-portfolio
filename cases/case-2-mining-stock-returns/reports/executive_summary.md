# 426x Faster: Real-Time Mining Equity Metrics with NumPy
### Portfolio Analytics — BHP, FCX, RIO, VALE, SCCO | CRISP-DM + LEAN

**Author:** Jose Marcel Lopez Pino
**Role:** Data Scientist — Operations, Analytics & Process Optimization
**Framework:** CRISP-DM + LEAN | Case-Based Learning (CBL)
**Date:** April 2026
**Status:** ![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

---

## 1. Business Context

| | |
|---|---|
| **Industry** | Financial Services — Mining Equities |
| **Business Unit** | Asset Management / Portfolio Analytics |
| **Stakeholder** | Portfolio Manager |
| **Decision to Support** | Should the analytics pipeline migrate from loop-based Python to NumPy vectorized operations? |

> **Situation:** A financial analytics firm monitoring mining equity portfolios relies on
> unstructured data formats and loop-based Python pipelines. As data volume grows, this
> approach creates performance bottlenecks that delay real-time metric computation —
> directly impacting portfolio management response times in volatile markets.

---

## 2. Problem Statement

> Can NumPy vectorized operations replace loop-based Python for financial metric computation
> while reducing code complexity and delivering measurable performance gains?

**Business Impact if Unresolved:**
- Delayed metrics increase decision latency for portfolio managers — in volatile markets, minutes matter
- Loop-based pipelines do not scale: adding equities or extending time windows compounds the performance problem linearly

---

## 3. Analytical Approach

> Non-technical summary — what was done, not how.

| Step | Description |
|---|---|
| **Data** | Real closing prices via yfinance — BHP, FCX, RIO, VALE, SCCO — 5 trading days (2026-03-26 → 2026-04-01) |
| **Method** | Descriptive statistics, daily returns, log returns, min-max normalization, z-scores, and base-100 price index — all via NumPy broadcasting, zero explicit loops |
| **Tool** | Python 3.12 · NumPy 2.4.1 · yfinance · matplotlib |
| **Validation** | NumPy results cross-checked against loop-based Python baseline using `np.allclose()` — results identical |

---

## 4. Key Findings

> Three findings following: **Context → Analysis → Insight → Decision**

### Finding 1 — SCCO was the strongest performer across the week
- **Context:** Five copper-linked mining equities were monitored over 5 consecutive trading days.
- **Analysis:** SCCO delivered the highest single-day return (+8.024%, Day 3→4) and the highest 5-day cumulative return (+11.799%). FCX recorded the worst single-day return (-2.827%, Day 2→3).
- **Insight:** SCCO showed both the highest upside and the highest intraday volatility — a pattern consistent with its higher beta relative to copper price movements.
- **Possible Decision:** A portfolio manager could review SCCO position sizing given its amplified response to commodity price shifts during the observed period.

### Finding 2 — All equities recovered strongly on Day 3→4
- **Context:** Day 2→3 showed mixed or negative returns across most equities (FCX -2.827%, SCCO -1.721%, BHP -0.691%).
- **Analysis:** Day 3→4 reversed the trend sharply — all five equities posted their strongest single-day gains of the week: SCCO +8.024%, FCX +7.557%, RIO +5.033%, BHP +5.390%, VALE +5.364%.
- **Insight:** The synchronized recovery across all five equities suggests a sector-wide catalyst (e.g., commodity price movement or macro news) rather than company-specific drivers.
- **Possible Decision:** Monitor sector-level macro triggers as leading indicators for rebalancing decisions across correlated mining positions.

### Finding 3 — NumPy delivers a 426x speedup over loop-based Python
- **Context:** The current pipeline uses nested Python loops for metric computation. At 5×5 scale the difference is invisible — but the firm's real portfolio operates at 500+ equities × 252 trading days.
- **Analysis:** Benchmarked at realistic scale (500 equities × 252 days, 1,000 runs): Python loops averaged 33.31 ms per call; NumPy averaged 0.08 ms per call — a **426x speedup**. Code reduced from 6 lines of nested loops to 1 readable expression.
- **Insight:** The performance gap is not marginal — it is structural. NumPy's vectorized C backend eliminates Python interpreter overhead entirely for array operations.
- **Possible Decision:** Migrate the analytics pipeline to NumPy immediately. Zero infrastructure change required — NumPy is already available in every standard Python data environment.

---

## 5. Business Recommendations

| Priority | Recommendation | Expected Impact | Effort |
|---|---|---|---|
| 🔴 High | Migrate loop-based metric computation to NumPy vectorized operations | 426x faster execution; real-time metrics at full portfolio scale | Low — drop-in replacement, no new infrastructure |
| 🟡 Medium | Extend the analysis window to 30 days to enable rolling volatility (std) and trend detection | More robust signals for rebalancing decisions | Medium — data pipeline extension |
| 🟢 Low | Model copper-linked equity volatility (FCX, SCCO, VALE) using GARCH — the industry-standard econometric approach for heteroskedastic financial time series | Quantified volatility estimates for risk management | High — requires econometric modeling expertise |

---

## 6. Limitations

- **Data:** 5-day window is insufficient for trend or volatility conclusions — extend to 30+ days minimum for strategic decisions
- **Model:** Descriptive analysis only — no predictive or causal component in this version
- **Scope:** Adjusted closing prices only — does not account for intraday volatility, bid-ask spreads, or trading volume

---

## 7. Next Steps

| Horizon | Action |
|---|---|
| **Immediate** | Apply these NumPy patterns as the foundation for the M3 pandas module |
| **Short-term** | Extend to 30-day window for rolling volatility analysis (`np.std` with sliding window) |
| **Long-term** | Model copper-linked equity volatility (FCX, SCCO, VALE) using GARCH — industry standard for heteroskedastic financial time series. LSTM is a valid exploratory alternative if sufficient historical data is available (12+ months minimum), as it can capture non-linear temporal patterns that GARCH may miss — but at the cost of interpretability and data volume. |

---

*Framework: CRISP-DM + LEAN | Methodology: Case-Based Learning (CBL)*

**Jose Marcel Lopez Pino**
Industrial Engineer (Operations, Analytics & Process Optimization) | Data Science & Business Analytics
Bootcamp: Fundamentos de Ciencia de Datos — SENCE/Alkemy (2025–2026)

[![GitHub](https://img.shields.io/badge/GitHub-joselopezp-181717?style=flat&logo=github)](https://github.com/joselopezp)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-jose--lopez--pino-0077B5?style=flat&logo=linkedin)](https://www.linkedin.com/in/jose-lopez-pino/)
