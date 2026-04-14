# 95.4% Accuracy Predicting Used Car Prices — Production-Ready in 3 Features
### Regression Model Evaluation — AutoPredict S.A. | CRISP-DM + LEAN

![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![Framework](https://img.shields.io/badge/Framework-CRISP--DM%20%2B%20LEAN-2E86AB)
![Type](https://img.shields.io/badge/Type-CBL%20Case-orange)
![Module](https://img.shields.io/badge/Module-M5%20Machine%20Learning%20Fundamentals-blueviolet)
![License](https://img.shields.io/badge/License-MIT-yellow)

## Executive Summary

AutoPredict S.A. required a documented evaluation procedure for its linear regression model predicting used vehicle sale prices. The original case dataset (n=4) was extended to n=35 records — 4 original + 31 synthetic generated under the same business rules — to enable statistically meaningful metric evaluation. Applying CRISP-DM + LEAN, a multiple linear regression model achieves **R²=0.9541** and **MAPE=6.74%** on the test set, well within the 15% deployment threshold for dealership pricing. Five performance metrics are computed, interpreted in business terms, and accompanied by a comparative visualization of actual vs. predicted prices and a prioritized improvement roadmap.

---

## Table of Contents

1. [Business Objective](#business-objective)
2. [Problem Statement Canvas](#problem-statement-canvas)
3. [Solution Overview](#solution-overview)
4. [Repository Structure](#repository-structure)
5. [Key Insights](#key-insights)
6. [Business Recommendations](#business-recommendations)
7. [Model Performance](#model-performance)
8. [Limitations](#limitations)
9. [Next Steps](#next-steps)
10. [How to Run](#how-to-run)

---

## Business Objective

**Problem:** AutoPredict S.A. has no documented procedure to evaluate whether its linear regression model for used vehicle pricing is fit for production deployment.

**Why it matters:** An unvalidated model exposes dealership clients to systematic pricing errors — overpricing reduces sales volume; underpricing erodes margin.

**Decision to support:** Should the current model be deployed to production, or does it require further refinement?

**Expected impact:** A validated, documented evaluation framework that can be reused across future model iterations.

---

## Problem Statement Canvas

| Element | Description |
|---|---|
| **Business Problem** | AutoPredict S.A. has no documented procedure to evaluate whether its linear regression model for used vehicle pricing is fit for production deployment. |
| **Business Impact** | Systematic pricing errors damage client trust and AutoPredict's commercial reputation — overpricing reduces sales volume; underpricing erodes margin. |
| **Decision to Support** | Should the current linear regression model be deployed to production, or does it require further refinement? |
| **Analytical Question** | What are the MAE, MSE, RMSE, R², and MAPE of the model on a representative dataset, and do these metrics meet the precision and reliability criteria required for deployment? |
| **Success Metrics** | R² > 0.80 on test set; MAPE < 15%; all five required metrics computed and interpreted in business terms. |
| **Proposed Approach** | Extend original n=4 dataset to n=35 (4 original + 31 synthetic under same business rules); train multiple linear regression (scikit-learn) on 80/20 split; compute all metrics; visualize actual vs. predicted prices; document improvement decisions. |

---

## Solution Overview

| Field | Detail |
|---|---|
| **Type** | Supervised ML — Regression (CBL Case) |
| **Model** | Multiple Linear Regression (`sklearn.linear_model.LinearRegression`) |
| **Features** | Age_years, Mileage_km, Doors |
| **Target** | Price_USD |
| **Dataset** | AutoPredict S.A. — n=35 (4 original + 31 synthetic), random_state=42 |
| **Split** | 80/20 (28 train / 7 test), random_state=42 |
| **Output** | Metrics table + actual vs. predicted bar chart |
| **Dependencies** | numpy, pandas, scikit-learn, matplotlib |

---

## Repository Structure

```
case-regression-metrics-autopredict/
├── README.md
├── notebooks/
│   └── case_regression_metrics_autopredict.ipynb
├── src/
├── data/
└── reports/
    ├── executive_summary.md
    └── actual_vs_predicted_prices.png
```

---

## Key Insights

**1. The model explains 95.4% of price variance (R²=0.9541) — strong fit for a 3-feature linear model**

Context: Used vehicle pricing is driven by multiple interacting factors. Age, mileage, and doors are the three features available in this dataset.
Analysis: R²=0.9541 on the test set indicates the model captures the dominant depreciation pattern — predominantly driven by age and mileage — with high accuracy.
Insight: For a first-version model, this is a strong baseline. The remaining 4.6% unexplained variance likely reflects factors not captured in the feature set (brand, condition, fuel type, transmission).
Possible Decision: Proceed to production pilot with dealership clients while collecting additional feature data for model v2.

**2. Vehicle age and mileage dominate pricing — doors has marginal but positive effect**

Context: Model coefficients — Age_years: −$326.99/year, Mileage_km: −$0.117/km, Doors: +$265.49/door, Intercept: $19,606.48.
Analysis: Every additional year reduces the estimated price by ~$327; every 10,000 km reduces it by ~$1,170. The Doors coefficient is positive (+$265) and directionally correct — 4-door vehicles typically command a small premium.
Insight: Age and mileage are highly correlated (r=0.996), which creates multicollinearity risk in OLS. Ridge regression would be more robust for production deployment.
Possible Decision: Evaluate Ridge regression as a drop-in replacement — same interpretability, reduced multicollinearity sensitivity.

**3. One outlier (Vehicle 27, error 21.99%) is a data artifact, not a model failure**

Context: Vehicle 27 (Age=10, Mileage=97,478 km) has an actual price of $7,000 — the floor value in the synthetic generation. The model predicts $5,461, below the floor.
Analysis: The model correctly identifies this vehicle as low-value; the error arises because the price floor truncates the natural depreciation curve at $7,000.
Insight: In a real dataset, very high-mileage vehicles would have more granular pricing below $7,000. The floor is a synthetic constraint, not a market reality.
Possible Decision: On real data, remove the price floor and allow the model to extrapolate naturally — or use a log-price transformation to handle the lower tail.

---

## Business Recommendations

| Priority | Recommendation | Impact |
|---|---|---|
| 🔴 Critical | Collect real transaction data (n ≥ 500) from client dealerships | Synthetic data captures depreciation logic but not market-specific dynamics |
| 🔴 Critical | Add features: brand, fuel type, transmission, vehicle condition | Age and mileage alone leave ~5% unexplained variance |
| 🟡 Important | Evaluate Ridge regression | Age_years and Mileage_km are highly correlated (r=0.996) — multicollinearity risk for OLS |
| 🟡 Important | Apply k-fold cross-validation (k=5) | More stable performance estimates than a single 80/20 split |
| 🟢 Enhancement | Test Gradient Boosting (XGBoost) | Captures non-linear mileage depreciation effects past 100k km |

---

## Model Performance

| Metric | Value | Unit | Interpretation |
|---|---|---|---|
| MAE | $671.96 | USD | Average absolute prediction error per vehicle |
| MSE | $625,445.37 | USD² | Penalizes large errors more heavily than MAE |
| RMSE | $790.85 | USD | Typical prediction error in the same unit as target |
| R² | 0.9541 | dimensionless | 95.4% of price variance explained by the model |
| MAPE | 6.74% | % | Model predicts within 6.74% of actual price on average |

**Model equation:**

`Price = 19,606.49 − 326.99 × Age_years − 0.117 × Mileage_km + 265.49 × Doors`

**Actual vs. Predicted — Test Set (n=7):**

| Vehicle | Actual (USD) | Predicted (USD) | Error (USD) | Error (%) |
|---|---|---|---|---|
| V27 | 7,000 | 5,460.58 | +1,539.42 | 21.99% ⚠️ |
| V14 | 13,162 | 13,580.33 | −418.33 | −3.18% |
| V25 | 13,187 | 12,477.57 | +709.43 | 5.38% |
| V22 | 8,494 | 8,334.99 | +159.01 | 1.87% |
| V16 | 8,876 | 8,386.76 | +489.24 | 5.51% |
| V30 | 18,549 | 19,017.66 | −468.66 | −2.53% |
| V20 | 13,691 | 12,771.36 | +919.64 | 6.72% |

> ⚠️ V27 outlier: artifact of $7,000 price floor in synthetic generation — documented in Decisions Log (D5).

---

## Limitations

**Data:** n=35 with 31 synthetic records — captures depreciation logic but not real market dynamics (brand premium, regional pricing, seasonal effects). Production validation requires real transaction data (n ≥ 500).

**Model:** OLS linear regression assumes linearity and no multicollinearity. Age_years and Mileage_km are highly correlated (r=0.996) — this inflates coefficient variance and reduces individual feature interpretability.

**Deployment:** The model was not tested on out-of-sample real data. The $7,000 price floor in synthetic generation creates a boundary artifact for high-mileage vehicles.

---

## Next Steps

| Priority | Next Step | Scope |
|---|---|---|
| 🔴 Immediate | Complete `reports/executive_summary.md` | CBL deliverable |
| 🟡 Short-term | Apply Ridge/Lasso on a real used vehicle dataset and compare against this baseline | M5–M6 |
| 🟢 Long-term | Integrate regression evaluation pipeline as reusable `src/evaluation.py` module | Portfolio |

---

## How to Run

```powershell
# From portfolio root — activate shared virtual environment
.venv\Scripts\Activate.ps1

# Navigate to case
cd cases\case-regression-metrics-autopredict

# Launch notebook
jupyter lab notebooks\case_regression_metrics_autopredict.ipynb
```

---

*Framework: CRISP-DM + LEAN | Methodology: Case-Based Learning (CBL)*

**Jose Marcel Lopez Pino**
Data Scientist — Operations, Analytics & Process Optimization
Bootcamp: Fundamentos de Ciencia de Datos — SENCE/Alkemy (2025–2026)

*Industrial Engineering in Chile (Academic degree: Bachelor of Science in Industrial Engineering — 5.5-year program, comparable to a U.S. M.S.) encompasses business strategy, finance, marketing, economics, operations management, and technology management — backed by a rigorous scientific foundation in calculus, linear algebra, probability and statistics, physics, and optimization — enabling a unique business + analytics perspective.*

[![GitHub](https://img.shields.io/badge/GitHub-joselopezp-181717?style=flat&logo=github)](https://github.com/joselopezp)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-jose--lopez--pino-0077B5?style=flat&logo=linkedin)](https://www.linkedin.com/in/jose-lopez-pino/)
