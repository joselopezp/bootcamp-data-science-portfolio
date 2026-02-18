# [Project Name]

> **One-line description**: [What business problem does this solve?]

**Author**: Jose Marcel Lopez Pino — Industrial Civil Engineer | Data Science  
**Date**: [YYYY-MM-DD]  
**Framework**: CRISP-DM + Lean  
**Tools**: Python, Pandas, NumPy, Matplotlib, Seaborn  
**Status**: 🟡 In Progress | 🟢 Complete | 🔴 On Hold

---

## Executive Summary

[2-3 paragraphs answering:]
- What business problem does this project address?
- What is the main insight or finding?
- What decision does it enable?

**Key Findings**:
1. [Finding 1 — with metric and business impact]
2. [Finding 2 — with metric and business impact]
3. [Finding 3 — with metric and business impact]

**Recommendation**: [One clear, actionable recommendation for stakeholders]

---

## Business Context

| Attribute | Description |
|-----------|-------------|
| **Industry** | [e.g., Retail, Mining, Technology, Labor Market] |
| **Stakeholders** | [Who uses this analysis?] |
| **Business Problem** | [Detailed description of the problem] |
| **Expected Value** | [What decision improves? How much saves? What optimizes?] |
| **Success Criteria** | [How do we know this analysis is useful?] |

---

## Methodology: CRISP-DM + Lean

This project follows the **CRISP-DM** framework enhanced with **Lean** principles.  
See [METHODOLOGY.md](./docs/METHODOLOGY.md) for detailed documentation.

### CRISP-DM Phases Applied

| Phase | Notebook | Lean Filter | Status |
|-------|----------|-------------|--------|
| 1. Business Understanding | `01_business_understanding.ipynb` | Define value for stakeholder | ⬜ |
| 2. Data Understanding | `02_data_understanding.ipynb` | Only explore what informs decisions | ⬜ |
| 3. Data Preparation | `03_data_preparation.ipynb` | Minimum viable transformations | ⬜ |
| 4. Modeling | `04_modeling.ipynb` | Simplest model that answers the question | ⬜ |
| 5. Evaluation | `05_evaluation.ipynb` | Does it solve the business problem? | ⬜ |
| 6. Deployment | `06_deployment.ipynb` | Actionable deliverable for stakeholder | ⬜ |

---

## Project Structure

```
project-name/
├── README.md                     # This file
├── requirements.txt              # Python dependencies
├── .gitignore                    # Git exclusions
│
├── data/
│   ├── raw/                      # Original data (never modify)
│   ├── processed/                # Intermediate clean data
│   └── final/                    # Analysis-ready datasets
│
├── notebooks/
│   ├── 01_business_understanding.ipynb
│   ├── 02_data_understanding.ipynb
│   ├── 03_data_preparation.ipynb
│   ├── 04_modeling.ipynb
│   ├── 05_evaluation.ipynb
│   └── 06_deployment.ipynb
│
├── src/
│   ├── data_processing.py        # ETL functions
│   ├── analysis.py               # Statistical analysis
│   └── visualization.py          # Chart functions
│
├── reports/
│   ├── technical/                # For data scientists
│   ├── executive/                # For business stakeholders
│   └── figures/                  # Exported charts
│
├── docs/
│   ├── METHODOLOGY.md            # CRISP-DM + Lean framework
│   ├── data_dictionary.md        # Variable descriptions
│   ├── decisions_log.md          # Key decisions record
│   └── lean_retrospective.md    # Lessons learned
│
├── config/
│   └── config.py                 # Paths and parameters
│
└── tests/                        # Unit tests
```

---

## How to Reproduce

```bash
# 1. Clone the repository
git clone https://github.com/[username]/[project-name].git
cd [project-name]

# 2. Create and activate virtual environment
python -m venv venv
source venv/bin/activate        # Linux/Mac
# venv\Scripts\activate         # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run notebooks in order (01 → 06)
jupyter notebook
```

---

## Deliverables

| Deliverable | Audience | Format | Location |
|-------------|----------|--------|----------|
| Technical Report | Data Scientists | Markdown / Notebook | `reports/technical/` |
| Executive Summary | Business Stakeholders | PDF / PPTX | `reports/executive/` |
| Clean Dataset | Analysts | CSV | `data/final/` |
| Visualizations | All | PNG | `reports/figures/` |

---

## Lean Metrics

| Metric | Target | Actual |
|--------|--------|--------|
| Time to first insight | [X days] | [X days] |
| Analyses discarded (waste eliminated) | — | [count] |
| Business questions answered | [X] | [X] |
| Stakeholder feedback incorporated | — | [count] |

---

## Resumen Ejecutivo (Español)

[Misma información del Executive Summary, en español, para stakeholders hispanohablantes]

---

## License

[Choose: MIT / Apache 2.0 / CC BY 4.0 / Private]

---

*Built with CRISP-DM + Lean framework | Project-Based Learning methodology*
