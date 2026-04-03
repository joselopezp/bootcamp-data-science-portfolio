# Case Study — Data Preprocessing & Feature Scaling
### RetailData Analytics | Recurring Customer Prediction Pipeline

![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![Framework](https://img.shields.io/badge/Framework-CRISP--DM%20%2B%20LEAN-2E86AB)
![Type](https://img.shields.io/badge/Type-CBL%20Case-orange)
![Module](https://img.shields.io/badge/Module-M5%20ML%20Fundamentals-blueviolet)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

> **Executive Summary:**
> RetailData Analytics received a 4-column customer demographics dataset with 1 missing value (25% of `Income`), unencoded city categories, and a 1,000x numeric scale mismatch between `Age` (25–45) and `Income` (30k–50k). Applying CRISP-DM + LEAN, this case delivers a complete preprocessing pipeline — mean imputation, Label Encoding, One-Hot Encoding, Dummy variables, Min-Max normalization, and Z-Score standardization — producing a 12-column model-ready feature matrix and a documented decision rationale for each transformation.

---

## Table of Contents

1. [Business Objective](#business-objective)
2. [Problem Statement Canvas](#problem-statement-canvas)
3. [Solution Overview](#solution-overview)
4. [Repository Structure](#repository-structure)
5. [CRISP-DM Phases](#crisp-dm-phases)
6. [Key Insights](#key-insights)
7. [Business Recommendations](#business-recommendations)
8. [Limitations](#limitations)
9. [Next Steps](#next-steps)
10. [How to Run](#how-to-run)
11. [Footer](#footer)

---

## Business Objective <a id='business-objective'></a>

**Problem:** A supermarket chain wants to identify customers most likely to make recurring purchases. The raw dataset is not model-ready — it contains missing values, unencoded categorical variables, and inconsistent numeric scales that would bias any ML model trained on it.

**Why it matters:** Distance-based models (KNN, SVM, KMeans) assign weight proportional to numeric magnitude. With unscaled data, `Income` (range: 20,000) dominates `Age` (range: 20) by a factor of 1,000 — effectively rendering age irrelevant in any distance calculation, distorting customer segmentation.

**Decision to support:** Which preprocessing strategy produces the cleanest, most model-compatible feature matrix for a recurring purchase classifier?

**Expected impact:** A correctly preprocessed dataset enables the downstream model to learn true customer behavior patterns rather than scale artifacts — directly improving prediction accuracy and marketing ROI.

---

## Problem Statement Canvas <a id='problem-statement-canvas'></a>

| Element | Description |
|---|---|
| **Business Problem** | Raw customer dataset is unfit for ML modeling: 1 missing income value, 1 unencoded categorical column, 1,000x scale mismatch between numeric features |
| **Business Impact** | Unprocessed data produces biased models → poor customer segmentation → ineffective loyalty campaigns → lost repeat purchase revenue |
| **Decision to Support** | Which customers should receive targeted promotions to maximize recurring purchase rate? |
| **Analytical Question** | Can we transform the raw 4-column dataset into a clean, encoded, and scaled 12-column feature matrix suitable for supervised classification? |
| **Success Metrics** | Zero missing values · All categoricals numerically encoded · Numeric features in [0,1] (Min-Max) and standardized (Z-Score, mean=0) |
| **Proposed Approach** | Mean imputation → Label Encoding → One-Hot Encoding → Dummy variables → Min-Max normalization → Z-Score standardization using scikit-learn and pandas |

---

## Solution Overview <a id='solution-overview'></a>

| Attribute | Detail |
|---|---|
| **Case type** | Case-Based Learning (CBL) — consulting-style analysis |
| **Dataset** | RetailData Analytics customer fragment — 4 rows × 4 columns (synthetic) |
| **Input features** | `ID`, `Age`, `City`, `Income` |
| **Output features** | 12 columns: original + Label Encoded + OHE + Min-Max + Z-Score |
| **Missing values** | 1 (25% of `Income`) → resolved via mean imputation ($40,000) |
| **Key libraries** | pandas 3.0, scikit-learn 1.8, matplotlib 3.10, seaborn 0.13 |
| **Output file** | `data/processed/retaildata_preprocessed.csv` |

---

## Repository Structure <a id='repository-structure'></a>

```
case-preprocessing-scaling-retaildata/
├── notebooks/
│   └── case_preprocessing_scaling_retaildata_EN.ipynb
├── data/
│   ├── raw/                    # Original 4-row fragment — never modified
│   └── processed/
│       └── retaildata_preprocessed.csv
├── reports/
│   └── scaling_comparison.png  # Raw vs Min-Max vs Z-Score bar chart
├── src/
│   └── __init__.py
├── requirements.txt
└── README.md
```

---

## CRISP-DM Phases <a id='crisp-dm-phases'></a>

| Phase | Notebook Section | Key Output |
|---|---|---|
| 1 — Business Understanding | Problem Statement Canvas | Defined preprocessing goal and success metrics |
| 2 — Data Understanding | Data Quality Audit | 1 missing value identified · 1,000x scale mismatch quantified |
| 3 — Data Preparation | Steps 1–6 | 12-column model-ready feature matrix |
| 4 — Modeling | *(not in scope — next case)* | — |
| 5 — Evaluation | Reflection Q&A + Summary Table | Documented rationale for each transformation |
| 6 — Deployment | CSV export | `retaildata_preprocessed.csv` ready for classifier input |

---

## Key Insights <a id='key-insights'></a>

**Insight 1 — Scale mismatch is a silent model killer**

Context: The raw dataset has `Age` ranging 25–45 and `Income` ranging 30,000–50,000 — a 1,000x difference in magnitude. Analysis: After Min-Max normalization, both features map to [0,1]: Age(25)→0.00, Age(45)→1.00, Income(30k)→0.00, Income(50k)→1.00. After Z-Score, Age std=1.1547, Income std=1.1547 — perfectly equalized. Insight: Without scaling, any distance-based model would treat a $1 income difference as equivalent to 1,000 years of age — a mathematically nonsensical comparison. Possible decision: Always apply Z-Score as the default scaler for production models where new out-of-range data is expected.

**Insight 2 — Encoding choice determines model compatibility**

Context: `City` has 3 nominal categories (Barcelona, Madrid, Sevilla) with no natural order. Analysis: Label Encoding assigns Barcelona=0, Madrid=1, Sevilla=2 — implying Sevilla is "twice" Madrid, which is false. One-Hot Encoding creates 3 binary columns with no ordinal assumption. Dummy encoding (drop_first=True) reduces to 2 columns, eliminating the multicollinearity risk in regression models. Insight: The encoding choice is not stylistic — it determines whether the model learns true relationships or mathematical artifacts. Possible decision: Use OHE for linear/distance models; Label Encoding only for tree-based models (Decision Tree, XGBoost).

**Insight 3 — Mean imputation is context-dependent**

Context: Row 3 (ID=3, Madrid) has missing `Income`. Known values: $30,000, $50,000, $40,000. Analysis: Mean = $40,000 — which happens to equal the known value for Row 4 (Barcelona). The imputed value falls exactly at the median of the known distribution. Insight: Mean imputation is conservative and appropriate for small, symmetric datasets without outliers. In production with thousands of customers, geographic median imputation (by city) would be more accurate — Madrid customers may have systematically different income than Barcelona customers. Possible decision: For the full dataset, apply `GroupBy('City')['Income'].transform('median')` as the imputation strategy.

---

## Business Recommendations <a id='business-recommendations'></a>

| Priority | Recommendation | Rationale |
|---|---|---|
| 🔴 High | Use Z-Score as the default scaler for the production classifier | Handles out-of-range new customer data gracefully; Min-Max produces values >1 for customers outside training range |
| 🔴 High | Apply One-Hot Encoding (not Label Encoding) for `City` in the final model | Label Encoding introduces false ordinal relationships that bias linear and distance-based models |
| 🟡 Medium | Replace mean imputation with city-level median imputation on the full dataset | Income distribution likely differs by city — group-level imputation reduces bias |
| 🟢 Low | Wrap this pipeline in a scikit-learn `Pipeline` + `ColumnTransformer` | Prevents data leakage by fitting scalers only on training data, not the full dataset |

---

## Limitations <a id='limitations'></a>

**Data:** Fragment of 4 rows is insufficient for statistical conclusions — used exclusively as a preprocessing demonstration. Real customer dataset required for model training.

**Imputation:** Mean imputation computed on n=3 known values. With only 3 data points, the mean is highly sensitive to any single value — not robust for production.

**Scaling:** Both scalers fitted on the full 4-row dataset. In a real ML pipeline, scalers must be fitted on training data only and applied (transform only) to validation and test sets to prevent data leakage.

---

## Next Steps <a id='next-steps'></a>

| Horizon | Action | Module |
|---|---|---|
| Immediate | Apply this pipeline to the full RetailData customer dataset using `Pipeline` + `ColumnTransformer` | M5 |
| Short-term | Train Logistic Regression classifier on the preprocessed features — predict recurring purchase probability | M5–M6 |
| Long-term | Refactor into `src/preprocessing.py` reusable module following the `wrangling.py` pattern from the fintech case | Portfolio |

---

## How to Run <a id='how-to-run'></a>

```powershell
# From portfolio root
cd "C:\Users\Carolina Miranda\Documents\Jose\bootcamp-data-science-portfolio"
.venv\Scripts\Activate.ps1

# Navigate to case
cd cases\case-preprocessing-scaling-retaildata

# Launch notebook
jupyter lab notebooks\case_preprocessing_scaling_retaildata_EN.ipynb
```

Run all cells in order: **Kernel → Restart & Run All**

Output CSV: `data/processed/retaildata_preprocessed.csv`
Output figure: `reports/scaling_comparison.png`

---

*Framework: CRISP-DM + LEAN | Methodology: Case-Based Learning (CBL)*

**Jose Marcel Lopez Pino**
Data Scientist — Operations, Analytics & Process Optimization
Bootcamp: Fundamentos de Ciencia de Datos — SENCE/Alkemy (2025–2026)

*From a personal perspective, data preprocessing maps directly to incoming quality control in manufacturing operations: raw inputs must pass inspection and transformation before entering the production line. Skipping this step is the data equivalent of feeding defective materials into a CNC machine — the output will be unreliable regardless of the algorithm's sophistication.*

[![GitHub](https://img.shields.io/badge/GitHub-joselopezp-181717?style=flat&logo=github)](https://github.com/joselopezp)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-jose--lopez--pino-0077B5?style=flat&logo=linkedin)](https://www.linkedin.com/in/jose-lopez-pino/)
