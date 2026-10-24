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
- [Post-Evaluation Enhancements and Corrections](#post-evaluation-enhancements-and-corrections)
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
across MercadoLibre and Shopify in Chile. The dataset contains 500 registered customers (392 buyers)
and 1,192 transactions generated to simulate realistic retail behavior.

**Key Business Questions:**

- Is PequeShop's average ticket aligned with the Chilean e-commerce benchmark
  of $25,000 CLP?
- Do customers spend differently on MercadoLibre vs Shopify?
- Is PequeShop's churn rate statistically above the 30% reference value (assumed, no verified source)?
- Does NPS segment (Promoter / Passive / Detractor) predict spending behavior?

---

## Key Results

| Hypothesis | Test | Statistic | p-value | Effect Size | Decision |
|------------|------|-----------|---------|-------------|----------|
| H1 — avg_ticket vs $25,000 CLP | One-sample t | t = 7.80 | < 0.001 | Cohen's d = 0.394 | **Reject H0** |
| H2 — MercadoLibre vs Shopify | Welch t | t = 2.27 | 0.024 | Cohen's d = 0.262 | **Reject H0** |
| H3 — Dormant rate (churn proxy) vs 30% (assumed) | Proportion z | z = 9.05 | < 0.001 | Cohen's h = 0.468 | **Reject H0** |
| H4 — avg_ticket by NPS segment | One-way ANOVA | F = 0.25 | 0.780 | eta-sq = 0.002 | **Fail to reject H0** |

> All tests: α = 0.05

**Summary:** Three of four hypotheses rejected. PequeShop's avg_ticket,
platform difference, and Dormant rate all deviate significantly from their reference values (the 30% Dormant reference is an assumption with no verified source).
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
| **HIGH** | H3 — Churn | Dormant rate (52.8%, 207 of 392 buyers) exceeds the assumed 30% reference value (z=9.05, p<0.001) | Launch retention campaign targeting Dormant segment immediately |
| **HIGH** | H1 — Pricing | avg_ticket significantly differs from $25,000 CLP benchmark (t=7.80, p<0.001) | Review pricing strategy vs Chilean e-commerce market |
| **MEDIUM** | H2 — Channel | MercadoLibre and Shopify tickets differ significantly (t=2.27, p=0.024) | Develop differentiated pricing and promotion strategy per channel |
| **LOW / HOLD** | H4 — NPS | No significant relationship between NPS and spending (F=0.25, p=0.780) | Do not invest in NPS-based pricing segmentation — no statistical justification |

> **Lean rule applied:** Resources concentrated on confirmed signals only.
> H4 result prevents investment in a segmentation strategy with no evidence base.

> **Catalog expansion note:** Expanding the product catalog (more SKUs, categories)
> may increase avg_ticket and reduce churn by giving customers more reasons to return.
> However, H3 results show the Dormant rate already exceeds the assumed 30% reference value significantly.
> Lean logic applies: retain existing customers before investing in catalog growth.
> A retained customer generates more lifetime value than a new customer acquired
> through a broader catalog without solving the underlying retention problem.

---

## Business Impact Estimation

| Scenario | Current State | Target | Estimated Impact |
|----------|--------------|--------|-----------------|
| Churn reduction (H3) | 52.8% Dormant rate (207 of 392 buyers) | Reduce toward the assumed 30% reference value | Not estimated (the 30% target has no verified source) |
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
> are not stored in this repository; copy them from `projects/project-2-pequeshop-analytics/data/processed/` into `data/processed/`.
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
| **Records** | 500 customers (392 buyers) · 1,192 transactions |
| **Columns** | customers: 16 · transactions: 19 |
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
- CRISP-DM: Chapman et al. (2000). *CRISP-DM 1.0: Step-by-step data mining guide*. SPSS Inc.
- Provost, F. & Fawcett, T. (2013). *Data Science for Business: What You Need to Know about Data Mining and Data-Analytic Thinking* (1st ed.). O'Reilly Media.
- Lean Thinking: Womack, J. & Jones, D. (1996). *Lean Thinking*. Simon & Schuster.
- Cohen, J. (1988). *Statistical Power Analysis for the Behavioral Sciences* (2nd ed.). Lawrence Erlbaum.
- Montgomery, D.C. (2017). *Design and Analysis of Experiments* (9th ed.). Wiley.

**Tools & Libraries:** See [Tech Stack](#tech-stack) section.

---

## Post-Evaluation Enhancements and Corrections

| # | Date | Type | Where | What changed | Reason |
|---|------|------|-------|--------------|--------|
| 1 | 2026-10-24 | Correction | Notebooks 03, 05, 06 + 3 figures | Dormant rate computed over the 392 buyers (207/392 = 52.8%) instead of the 500 registered customers (41.4%). H3: z 5.18 → 9.05, Cohen's h 0.239 → 0.468, 95% CI (0.4786, 0.5775). H1 and H4 unchanged. | The 108 customers who never purchased have no segment and cannot be Dormant |
| 2 | 2026-10-24 | Correction | README, notebooks 01, 02, 03 | Figures aligned with notebooks 03/05/06 (e.g. Binomial p = 0.414 → 0.528 in notebook 03); "active customers" → "buyers"; "At-Risk" → "At Risk" (the label in the data); customers columns 15 → 16 | Text and labels did not match the data |
| 2b | 2026-10-24 | Correction | Notebook 02 | Sample space restricted to the 392 buyers (`dropna` on `retargeting_segment`); previously 500 rows, and the `'At-Risk'` filter matched nothing | Probabilities were computed over the wrong denominator. Saved outputs of notebook 02 now show Omega = 392 (Active 97, At Risk 88, Dormant 207). |
| 3 | 2026-10-24 | Correction | README, notebooks 01, 02, 05, 06 | 30% benchmark relabelled as assumed reference value (no verified source); "statistically confirmed emergency" and "~45 customers retained" claims removed | Not supported by any notebook or source |
| 4 | 2026-10-24 | Correction | README | License link fixed (`../../LICENSE`); How to Run no longer says the CSVs are included (they are not versioned: copy them from project-2) | Link was broken; instruction was false |
| 5 | 2026-10-24 | Correction | `notebooks/README.md` | Duplicate, older README removed | Two READMEs disagreed |
| 6 | 2026-10-24 | Enhancement | `requirements.txt` | Added (versions used to run notebooks 01-06, Python 3.12) | Notebooks could not run without installing libraries by trial and error |
| 7 | 2026-10-24 | Enhancement | Notebooks 01-06 | Executed end to end (Restart & Run All) with `requirements.txt` and saved with outputs; notebook 02 had none | Every figure in this README can be traced to a saved cell output |
| 8 | 2026-10-24 | Enhancement | README | Date column added to this table | Shows when each change was made after the original delivery (2026-03) |

## License

This project is licensed under the [MIT License](../../LICENSE).

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
