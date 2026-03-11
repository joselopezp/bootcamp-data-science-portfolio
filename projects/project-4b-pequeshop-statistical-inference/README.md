# PequeShop Statistical Inference: Testing Business Hypotheses with Python

> **PequeShop Analytics Cycle 3 — Statistical Inference** | Module 5: Fundamentos de Ciencia de Datos

![Python](https://img.shields.io/badge/Python-3.12.10-3776AB?logo=python&logoColor=white)
![Framework](https://img.shields.io/badge/Framework-CRISP--DM%20%2B%20LEAN-2E86AB)
![Type](https://img.shields.io/badge/Type-Statistical%20Inference-blueviolet)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## Table of Contents

- [Project Overview](#project-overview)
- [Business Context](#business-context)
- [Key Results](#key-results)
- [Strategic Recommendations](#strategic-recommendations)
- [Business Impact Estimation](#business-impact-estimation)
- [Project Structure](#project-structure)
- [Tech Stack](#tech-stack)
- [How to Run](#how-to-run)
- [Deliverables](#deliverables)
- [CRISP-DM Roadmap](#crisp-dm-roadmap)
- [Data Source](#data-source)
- [Credits](#credits)
- [License](#license)

---

## Project Overview

This project applies statistical inference to validate four business hypotheses
for PequeShop, a Chilean children's clothing e-commerce business. Using
hypothesis testing, confidence intervals, and the Central Limit Theorem, it
answers whether observed KPI deviations are statistically significant — or just
noise.

The analysis moves beyond descriptive statistics (covered in project-3) to
formal statistical decisions: are these patterns real enough to justify
business investment?

**What I learned:** One-sample t-test, Welch t-test, proportion z-test,
one-way ANOVA, effect size interpretation (Cohen's d, Cohen's h, eta-squared),
confidence interval construction, CLT empirical verification, and translating
statistical results into prioritized business recommendations.

---

## Business Context

**PequeShop** is a synthetic children's clothing e-commerce operation selling
across MercadoLibre and Shopify in Chile. The dataset contains 392 customers
and 1,192 transactions generated to simulate realistic retail behavior.

**Key Business Questions:**

- Is PequeShop's average ticket aligned with the Chilean e-commerce benchmark
  of $25,000 CLP?
- Do customers spend differently on MercadoLibre vs Shopify?
- Is PequeShop's churn rate statistically above the 30% industry benchmark?
- Does NPS segment (Promoter / Passive / Detractor) predict spending behavior?

---

## Key Results

| Hypothesis | Test | Statistic | p-value | Effect Size | Decision |
|------------|------|-----------|---------|-------------|----------|
| H1 — avg_ticket vs $25,000 CLP | One-sample t | t = 7.80 | < 0.001 | Cohen's d = 0.394 | **Reject H0** |
| H2 — MercadoLibre vs Shopify | Welch t | t = 2.27 | 0.024 | Cohen's d = 0.262 | **Reject H0** |
| H3 — Churn rate vs 30% | Proportion z | z = 5.18 | < 0.001 | Cohen's h = 0.239 | **Reject H0** |
| H4 — avg_ticket by NPS segment | One-way ANOVA | F = 0.25 | 0.780 | eta-sq = 0.002 | **Fail to reject H0** |

> All tests: α = 0.05

**Summary:** Three of four hypotheses rejected. PequeShop's avg_ticket,
platform difference, and churn rate all deviate significantly from benchmarks.
NPS segment does not predict spending — pricing segmentation by NPS is not
statistically justified.

> **Limitation:** Dataset is synthetic (n=392). Effect sizes are small
> (Cohen's d ~ 0.26–0.39). With real-world data at higher volume, effects
> may be more pronounced and H4 could reveal an NPS–ticket relationship
> not detectable here.

---

## Strategic Recommendations

| Priority | Hypothesis | Finding | Recommended Action |
|----------|-----------|---------|-------------------|
| **HIGH** | H3 — Churn | Churn significantly exceeds 30% benchmark (z=5.18, p<0.001) | Launch retention campaign targeting Dormant segment immediately |
| **HIGH** | H1 — Pricing | avg_ticket significantly differs from $25,000 CLP benchmark (t=7.80, p<0.001) | Review pricing strategy vs Chilean e-commerce market |
| **MEDIUM** | H2 — Channel | MercadoLibre and Shopify tickets differ significantly (t=2.27, p=0.024) | Develop differentiated pricing and promotion strategy per channel |
| **LOW / HOLD** | H4 — NPS | No significant relationship between NPS and spending (F=0.25, p=0.780) | Do not invest in NPS-based pricing segmentation — no statistical justification |

> **Lean rule applied:** Resources concentrated on confirmed signals only.
> H4 result prevents investment in a segmentation strategy with no evidence base.

> **Catalog expansion note:** Expanding the product catalog (more SKUs, categories)
> may increase avg_ticket and reduce churn by giving customers more reasons to return.
> However, H3 results show churn already exceeds the 30% benchmark significantly.
> Lean logic applies: retain existing customers before investing in catalog growth.
> A retained customer generates more lifetime value than a new customer acquired
> through a broader catalog without solving the underlying retention problem.

---

## Business Impact Estimation

| Scenario | Current State | Target | Estimated Impact |
|----------|--------------|--------|-----------------|
| Churn reduction (H3) | ~41% churn rate | Reduce to 30% benchmark | ~45 customers retained per cycle |
| Channel optimization (H2) | Undifferentiated pricing | Platform-specific promotions | Potential avg_ticket uplift on lower-performing channel |
| Pricing alignment (H1) | Significant deviation from $25k benchmark | Align or justify deviation | Informed pricing decision vs market |

> **Methodology:** Estimates based on n=392 synthetic customers.
> **Assumptions:** Linear retention response; no cross-channel cannibalization.
> **Data source:** PequeShop synthetic dataset — see Data Source section.

---

## Project Structure

```
project-4b-pequeshop-statistical-inference/
├── data/
│   ├── raw/                    # Original data (never modify)
│   ├── processed/              # customers_final.csv, transactions_final.csv
│   └── final/
├── notebooks/
│   ├── 01_business_understanding.ipynb   # CRISP-DM Phase 1 — 4 hypotheses, PICO
│   ├── 02_data_understanding.ipynb       # CRISP-DM Phase 2 — probability, sample space
│   ├── 03_data_preparation.ipynb         # CRISP-DM Phase 3 — distribution fitting
│   ├── 04_modeling.ipynb                 # CRISP-DM Phase 4 — CLT empirical verification
│   ├── 05_evaluation.ipynb               # CRISP-DM Phase 5 — confidence intervals
│   └── 06_deployment.ipynb               # CRISP-DM Phase 6 — hypothesis tests + recommendations
├── reports/
│   ├── figures/                # All generated visualizations
│   └── executive/
├── docs/
│   ├── METHODOLOGY.md
│   ├── data_dictionary.md
│   ├── decisions_log.md
│   └── lean_retrospective.md
├── src/
├── requirements.txt
├── .gitignore
└── README.md
```

### CRISP-DM Phase Mapping

| Notebook | CRISP-DM Phase | Scope |
|----------|----------------|-------|
| 01 | Business Understanding | Problem definition, 4 hypotheses (PICO), study design |
| 02 | Data Understanding | Sample space, probability events, conditional probability, sampling design |
| 03 | Data Preparation | Distribution fitting — Normal, Poisson, Binomial |
| 04 | Modeling | CLT empirical verification, SE = σ/√n convergence |
| 05 | Evaluation | Confidence intervals 90/95/99% for avg_ticket and churn rate |
| 06 | Deployment | H1–H4 hypothesis tests, effect sizes, business recommendations |

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.12 | Core language |
| Pandas | Data manipulation and groupby aggregations |
| NumPy | Numerical operations, bootstrap simulation |
| SciPy | Statistical tests (t-test, z-test, ANOVA, distribution fitting) |
| Statsmodels | Proportion z-test, post-hoc Bonferroni |
| Matplotlib | Custom visualizations |
| Seaborn | Boxplots, distribution plots |

**Skills Demonstrated:**
`Python` · `Statistical Inference` · `Hypothesis Testing` · `Confidence Intervals` · `ANOVA` · `Effect Size` · `CLT` · `Pandas` · `SciPy` · `Statsmodels` · `CRISP-DM` · `Lean Thinking` · `Business Analytics`

---

## How to Run

```bash
git clone https://github.com/joselopezp/bootcamp-data-science-portfolio.git
cd projects/project-4b-pequeshop-statistical-inference
python -m venv .venv
.venv\Scripts\activate          # Windows
pip install -r requirements.txt
jupyter notebook notebooks/01_business_understanding.ipynb
```

> ⚠️ Dataset is synthetic — `customers_final.csv` and `transactions_final.csv`
> are included in `data/processed/`. No external download required.
> Run notebooks in order: 01 → 02 → 03 → 04 → 05 → 06.

---

## Deliverables

- [x] 6 notebooks following CRISP-DM + Lean structure (01–06)
- [x] Hypothesis test results with effect sizes and confidence intervals
- [x] CLT empirical verification with bootstrap simulation
- [x] Confidence intervals at 90%, 95%, 99% for key KPIs
- [x] Visualizations in `reports/figures/`
- [x] Prioritized business recommendations (Lean priority order)
- [x] Decisions log and methodology documentation

---

## CRISP-DM Roadmap

| Level | Question | Cycle | Module | Status |
|-------|----------|-------|--------|--------|
| Descriptive | What happened? | project-2-pequeshop-analytics | M3 — ETL | ✅ Complete |
| Diagnostic | Why did it happen? | project-3-eda-pequeshop | M4 — EDA | ✅ Complete |
| Inferential | Are the patterns statistically real? | **project-4b** (this project) | M5 — Statistical Inference | ✅ Complete |
| Predictive | What will happen? | project-5-ecommerce-spend-prediction | M6 — ML | 🔲 Pending |

---

## Data Source

| Field | Details |
|-------|---------|
| **Dataset** | PequeShop synthetic e-commerce dataset |
| **Origin** | Generated via project-2-pequeshop-analytics (CRISP-DM Cycle 1) |
| **Records** | 392 customers · 1,192 transactions |
| **Columns** | customers: 15 · transactions: 19 |
| **Accessed** | March 2026 |

### How to Reproduce

> ⚠️ Data is synthetic — generated in project-2 and copied to `data/processed/`.
> No external source required. Full generation methodology documented in
> `project-2-pequeshop-analytics/`.

---

## Credits

**Data:** Synthetic dataset designed and generated by Jose Marcel Lopez Pino
as part of the PequeShop Analytics continuous case study.

**Methodology References:**
- CRISP-DM: [Chapman et al. (2000)](https://www.the-modeling-agency.com/crisp-dm.pdf)
- Lean Thinking: Womack & Jones (1996)
- Cohen, J. (1988). *Statistical Power Analysis for the Behavioral Sciences* (2nd ed.)
- Montgomery, D.C. (2017). *Design and Analysis of Experiments* (9th ed.)

**Tools & Libraries:** See [Tech Stack](#tech-stack) section.

---

## License

MIT License — see [LICENSE](../../LICENSE) for details.

---

*Framework: CRISP-DM + Lean | Module 5 — Statistical Inference*
*Jose Marcel Lopez Pino — Bootcamp Fundamentos de Ciencia de Datos, SENCE/Alkemy 2025-2026*
