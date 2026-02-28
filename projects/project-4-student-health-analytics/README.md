# Project 4 — Statistical Inference over Student Habits

Statistical hypothesis testing on 1,000 university students to identify
which lifestyle habits (sleep, exercise, diet) significantly impact academic
performance — and translate findings into actionable wellness interventions.

![Python](https://img.shields.io/badge/Python-3.12.10-3776AB?logo=python&logoColor=white)
![Framework](https://img.shields.io/badge/Framework-CRISP--DM%20%2B%20LEAN-2E86AB)
![Type](https://img.shields.io/badge/Type-Statistical%20Inference-blueviolet)
![Dataset](https://img.shields.io/badge/Dataset-Kaggle-20BEFF?logo=kaggle&logoColor=white)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## Table of Contents

1. [Business Context](#business-context)
2. [Research Questions & Hypotheses](#research-questions--hypotheses)
3. [Key Results](#key-results)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Project Structure](#project-structure)
7. [Tech Stack & Skills Demonstrated](#tech-stack--skills-demonstrated)
8. [Strategic Recommendations](#strategic-recommendations)
9. [Deliverables](#deliverables)
10. [CRISP-DM Roadmap](#crisp-dm-roadmap)
11. [Known Improvements](#known-improvements)
12. [Data Source](#data-source)
13. [Credits](#credits)
14. [License](#license)

---

## Business Context

**Problem:** University health departments allocate wellness budgets without
statistical evidence of which student habits most affect academic outcomes.
Interventions are often designed on assumptions rather than data.

**Goal:** Identify which lifestyle variables (sleep, exercise, diet quality)
have a statistically significant relationship with exam scores, and prioritize
interventions based on effect size, population reach, and cost.

**Why this matters:** A data-driven wellness strategy maximizes ROI on
student support programs — consistent with Lean principles of eliminating
waste and targeting the highest-leverage intervention first.

**What I learned:** Hypothesis formulation must be grounded in exploratory
data analysis. When H₁ is defined before data exploration, the direction of
the test may not match the actual data — requiring CRISP-DM iteration and
transparent documentation of the revision process (see Section 5b in
`06_deployment.ipynb`).

---

## Research Questions & Hypotheses

| ID | Research Question | H₀ | H₁ | Test |
|----|------------------|----|----|------|
| H1 | Do students sleep less than the WHO 7h benchmark? | μ_sleep = 7h | μ_sleep < 7h | One-sample t-test (left) |
| H2 | Do active students score higher than sedentary students? | μ_active = μ_sedentary | μ_active > μ_sedentary | Welch t-test (right) |
| H3 | Is sedentarism significantly different from 50% prevalence? | p_sedentary = 0.50 | p_sedentary < 0.50 | Proportion z-test (left) |
| H4 | Does diet quality affect exam scores across groups? | μ_poor = μ_fair = μ_good | At least one group differs | One-way ANOVA + Bonferroni |

> **Note on H3:** Originally formulated as H₁: p > 0.50 (majority sedentary).
> After execution, p̂ = 41.2% — below 50%. H₁ was revised to H₁: p < 0.50
> following CRISP-DM iterative principles. The revision is documented in
> `06_deployment.ipynb` Section 5b as a methodological transparency note.

---

## Key Results

### Hypothesis Test Summary

| Hypothesis | Test | Decision | Effect Size | Business Signal |
|------------|------|----------|-------------|-----------------|
| H1 — Sleep vs 7h | One-sample t-test | ✅ **Reject H₀** | Cohen's d = −0.43 (Small–Medium) | Mean sleep significantly below WHO benchmark |
| H2 — Exercise vs Scores | Welch t-test | ✅ **Reject H₀** | Cohen's d = 0.23 (Small) | Active students score measurably higher |
| H3 — Sedentary prevalence | Proportion z-test | ✅ **Reject H₀** | Cohen's h = −0.18 | 41.2% sedentary — significantly below 50% |
| H4 — Diet quality | One-way ANOVA | ❌ Fail to reject H₀ | η² = 0.003 (Negligible) | No significant diet effect in this dataset |

All tests: α = 0.05 · 4 mandatory outputs per test: statistic, p-value, effect size, 95% CI.

### Notable Findings

- **Sleep deprivation** affects the majority of students and is the primary risk factor
  for academic underperformance (1.5–2× higher probability of academic risk when sleep < 7h)
- **Active students** (≥ 3 days/week exercise) score an average of ~3.5 points higher
  on exams — a small but statistically significant and practically actionable difference
- **Sedentarism** (41.2%) is a minority behavior, not majority — intervention should
  target the at-risk subgroup rather than a campus-wide campaign
- **Diet quality** showed no statistically significant effect on exam scores in this
  sample — a valid negative finding that informs resource allocation

---

## Installation

```bash
# Clone the repository
git clone https://github.com/joselopezp/bootcamp-data-science-portfolio.git
cd bootcamp-data-science-portfolio/projects/project-4-statistical-inference

# Create virtual environment
python -m venv .venv
source .venv/bin/activate        # Mac/Linux
.venv\Scripts\activate           # Windows

# Install dependencies
pip install -r requirements.txt
```

---

## Usage

> ⚠️ Raw data is excluded via `.gitignore`. Download the dataset before running
> notebooks (see [Data Source](#data-source)).

Run notebooks in CRISP-DM order:

```
01_business_understanding.ipynb   → Define hypotheses, study design, PICO framework
02_data_understanding.ipynb       → Probability foundations, data quality, sampling
03_data_preparation.ipynb         → Distribution fitting (Normal, Poisson, Binomial)
04_modeling.ipynb                 → CLT empirical verification, SE = σ/√n
05_evaluation.ipynb               → Confidence intervals (90%, 95%, 99%)
06_deployment.ipynb               → Hypothesis tests, ANOVA, prescriptive analysis
```

> **Recommended:** Use `Kernel → Restart & Run All` on each notebook to ensure
> all variables are defined before dependent cells execute.

---

## Project Structure

```
project-4-statistical-inference/
├── README.md
├── requirements.txt
├── .gitignore
├── data/
│   ├── raw/                          # student_habits_performance.csv (excluded)
│   └── README.md                     # Data source instructions
├── notebooks/
│   ├── 01_business_understanding.ipynb   # CRISP-DM Phase 1
│   ├── 02_data_understanding.ipynb       # CRISP-DM Phase 2
│   ├── 03_data_preparation.ipynb         # CRISP-DM Phase 3
│   ├── 04_modeling.ipynb                 # CRISP-DM Phase 4
│   ├── 05_evaluation.ipynb               # CRISP-DM Phase 5
│   └── 06_deployment.ipynb               # CRISP-DM Phase 6
├── reports/
│   ├── figures/                      # All generated plots (PNG)
│   └── presentation/
│       └── Project4_Statistical_Inference.pptx
└── docs/
    └── lean_retrospective.md
```

### CRISP-DM Phase Mapping

| Phase | Notebook | Key Output |
|-------|----------|------------|
| 1 — Business Understanding | `01` | 4 hypotheses, PICO framework, study design |
| 2 — Data Understanding | `02` | Probability foundations, P(A), P(B\|A), data quality |
| 3 — Data Preparation | `03` | Distribution fitting: Normal, Poisson, Binomial |
| 4 — Modeling | `04` | CLT empirical verification, SE = σ/√n across n=5→1000 |
| 5 — Evaluation | `05` | CI at 90%, 95%, 99% — benchmark inclusion/exclusion check |
| 6 — Deployment | `06` | 4 hypothesis tests + ANOVA diagnostics + prescriptive analysis |

---

## Tech Stack & Skills Demonstrated

| Category | Tools / Libraries |
|----------|------------------|
| Language | Python 3.12.10 |
| Data manipulation | Pandas, NumPy |
| Statistical testing | SciPy (`ttest_1samp`, `ttest_ind`, `f_oneway`, `levene`, `shapiro`), Statsmodels (`proportions_ztest`) |
| Visualization | Matplotlib, Seaborn |
| Environment | VS Code, Jupyter, venv |
| Version control | Git, GitHub |
| Methodology | CRISP-DM, Lean Thinking, PBL |

**Skills demonstrated:**

`Python` · `Statistical Inference` · `Hypothesis Testing` · `One-sample t-test` · `Welch t-test` · `Proportion z-test` · `One-way ANOVA` · `Post-hoc Bonferroni` · `Cohen's d` · `eta-squared` · `Confidence Intervals` · `CLT` · `CRISP-DM` · `Lean Thinking` · `Business Analytics` · `Prescriptive Analysis` · `Pandas` · `SciPy` · `Statsmodels` · `Matplotlib` · `Seaborn`

---

## Strategic Recommendations

Based on statistical evidence (α = 0.05), ordered by intervention priority
using Lean logic: maximum impact per unit of investment.

| Priority | Intervention | Evidence | Population | Est. Reach | Cost |
|----------|-------------|----------|------------|------------|------|
| 🔴 HIGH | Sleep Hygiene Program | H1 ✅ rejected · d = −0.43 | ~65% students | ~250 students | Low |
| 🔴 HIGH | Anti-Sedentarism Campaign | H2 ✅ rejected · d = 0.23 | 41.2% sedentary | ~12 students | Low–Med |
| 🟡 MEDIUM | Nutrition Program | H4 ❌ not significant · η² = 0.003 | Poor diet subgroup | TBD | Medium |

**Implementation order:** Sleep → Activity → Nutrition

**Rationale (Lean):** Sleep program delivers the highest ROI — largest affected
population, lowest intervention cost, strongest statistical evidence.
The nutrition program, while worth monitoring, showed no significant effect
in this dataset and should be deprioritized pending further evidence.

> **Personal perspective:** Framing student habits as a process system
> (Habits = Inputs · Exam Score = Output) allows applying Value Stream Mapping
> logic to identify the primary bottleneck. Sleep deprivation is the dominant
> constraint — the Lean-optimal move is to address it first before investing in
> downstream variables.

---

## Deliverables

| Deliverable | Audience | Format | Status |
|-------------|----------|--------|--------|
| `01_business_understanding.ipynb` | Data team | Jupyter (EN) | ✅ |
| `02_data_understanding.ipynb` | Data team | Jupyter (EN) | ✅ |
| `03_data_preparation.ipynb` | Data team | Jupyter (EN) | ✅ |
| `04_modeling.ipynb` | Data team | Jupyter (EN) | ✅ |
| `05_evaluation.ipynb` | Data team | Jupyter (EN) | ✅ |
| `06_deployment.ipynb` | Data team | Jupyter (EN) | ✅ |
| Figures (`reports/figures/`) | All | PNG | ✅ |
| Executive Summary | Health Director | PDF/PPTX (ES) | ⏳ |

> See [`docs/lean_retrospective.md`](docs/lean_retrospective.md) for full methodology retrospective.

---

## CRISP-DM Roadmap

This project covers the full CRISP-DM cycle within Module 5 (Statistical Inference).
Future analytical phases are planned as the bootcamp progresses:

| Phase | Module | Technique | Status |
|-------|--------|-----------|--------|
| Descriptive (L1–L3) | 5 | Probability, distributions | ✅ Complete |
| Diagnostic (L4–L5) | 5 | CLT, confidence intervals | ✅ Complete |
| Inferential (L6) | 5 | Hypothesis testing, ANOVA | ✅ Complete |
| Predictive | 6 | Supervised ML (regression/classification) | ⏳ Module 6 |
| Unsupervised | 7 | Clustering, RFM + KMeans | ⏳ Module 7 |
| Prescriptive (advanced) | Post-bootcamp | BG/NBD, survival analysis | ⏳ Planned |

---

## Known Improvements

| # | Improvement | Priority | Notes |
|---|-------------|----------|-------|
| 1 | **Notebook pipeline chaining** | Medium | Each notebook currently loads raw CSV independently. Correct flow: `02` saves `data/processed/02_output.csv` → `03` loads it → etc. Eliminates redundant loading, ensures each phase consumes verified outputs from the previous one. |
| 2 | **H3 hypothesis pre-registration** | Low | H₁ was formulated before EDA, assuming p_sedentary > 0.50. Actual data: p̂ = 41.2%. Best practice: quick descriptive pass before committing to hypothesis direction. Fully documented in `06_deployment.ipynb` Section 5b. |

---

## Data Source

| Field | Details |
|-------|---------|
| **Dataset** | [Student Habits vs Academic Performance](https://www.kaggle.com/datasets/jayaantanaath/student-habits-vs-academic-performance) |
| **Provider** | Kaggle |
| **Author** | jayaantanaath |
| **License** | CC0 (Public Domain) |
| **Records** | 1,000 rows × 16 columns |
| **Accessed** | February 2026 |

### How to Reproduce

> ⚠️ Raw data is excluded from this repository via `.gitignore`.

**Option 1 — kagglehub (used in notebooks):**
```python
import kagglehub
path = kagglehub.dataset_download("jayaantanaath/student-habits-vs-academic-performance")
```

**Option 2 — Kaggle CLI:**
```bash
kaggle datasets download -d jayaantanaath/student-habits-vs-academic-performance \
  -p data/raw/ --unzip
```

**Option 3 — Manual download:**
1. Visit the Kaggle URL above
2. Download `student_habits_performance.csv`
3. Place in `data/raw/`
4. Run notebooks in order: `01` → `02` → ... → `06`

---

## Credits

### Methodology
- CRISP-DM: Chapman et al. (2000). *CRISP-DM 1.0: Step-by-step data mining guide*
- Cohen's d interpretation: Cohen, J. (1988). *Statistical Power Analysis for the Behavioral Sciences* (2nd ed.)
- η² interpretation: Cohen, J. (1988) — small = 0.01, medium = 0.06, large = 0.14
- Lean Thinking: Womack & Jones (1996). *Lean Thinking*

### Libraries
See [Tech Stack](#tech-stack--skills-demonstrated).

### Bootcamp
Alkemy / SENCE — Fundamentos de Ciencia de Datos (2025–2026)

---

## License

This project is licensed under the [MIT License](LICENSE).

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
