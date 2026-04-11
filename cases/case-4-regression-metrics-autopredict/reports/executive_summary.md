# Executive Summary
## Case: Regression Algorithm Performance Metrics — AutoPredict S.A.
**Module M5 — Machine Learning Fundamentals | L6 | CBL Case | 2026-04**
**Framework: CRISP-DM + LEAN | Author: Jose Marcel Lopez Pino**

---

## Context

AutoPredict S.A. develops price prediction systems for car dealerships. A client requested a model to estimate used vehicle sale prices based on vehicle age, mileage, and number of doors. The data science team built a first version using linear regression but lacked a documented procedure to evaluate whether the model meets the precision and reliability criteria required before production deployment. The original case dataset (n=4) was extended to n=35 (4 original + 31 synthetic under the same business rules) to enable statistically meaningful evaluation.

---

## Solution

A multiple linear regression model was trained using scikit-learn on an 80/20 split (28 train / 7 test, random_state=42). Five performance metrics were computed — MAE, MSE, RMSE, R², and MAPE — and interpreted in business terms. A comparative bar chart of actual vs. predicted prices was generated and saved programmatically. Improvement decisions were prioritized using a 🔴🟡🟢 framework aligned with deployment readiness.

---

## Results

| Metric | Value | Business Interpretation |
|---|---|---|
| MAE | $671.96 | Average absolute prediction error per vehicle |
| MSE | $625,445.37 | Variance-weighted error — penalizes large misses |
| RMSE | $790.85 | Typical prediction error in USD |
| R² | 0.9541 | Model explains 95.4% of price variance |
| MAPE | 6.74% | Model predicts within 6.74% of actual price on average |

**Model equation:**

`Price = 19,606.49 − 326.99 × Age_years − 0.117 × Mileage_km + 265.49 × Doors`

**Test set predictions (n=7):**

| Vehicle | Actual (USD) | Predicted (USD) | Error (%) |
|---|---|---|---|
| V27 | 7,000 | 5,460.58 | 21.99% ⚠️ |
| V14 | 13,162 | 13,580.33 | −3.18% |
| V25 | 13,187 | 12,477.57 | 5.38% |
| V22 | 8,494 | 8,334.99 | 1.87% |
| V16 | 8,876 | 8,386.76 | 5.51% |
| V30 | 18,549 | 19,017.66 | −2.53% |
| V20 | 13,691 | 12,771.36 | 6.72% |

> ⚠️ V27 error (21.99%) is a boundary artifact of the $7,000 synthetic price floor — not a model failure. Excluding V27, MAPE drops to 4.26%.

---

## Business Impact

The model demonstrates strong predictive fit (R²=0.9541, MAPE=6.74%) — well within the 15% deployment threshold for dealership pricing. The primary business value is the **documented evaluation framework**: a reproducible procedure AutoPredict can apply to any future model version before client delivery. The model equation is interpretable: each additional year reduces the estimated price by ~$327; each 10,000 km reduces it by ~$1,170.

---

## Improvement Decisions

| Priority | Decision | Rationale |
|---|---|---|
| 🔴 Critical | Collect real transaction data (n ≥ 500) | Synthetic data captures depreciation logic but not market-specific dynamics |
| 🔴 Critical | Add features: brand, fuel type, transmission, condition | Age and mileage alone leave ~5% unexplained variance |
| 🟡 Important | Evaluate Ridge regression | Age_years and Mileage_km are highly correlated (r=0.996) — multicollinearity risk for OLS |
| 🟡 Important | Apply k-fold cross-validation (k=5) | More stable performance estimates than a single 80/20 split |
| 🟢 Enhancement | Test Gradient Boosting (XGBoost) | Captures non-linear depreciation effects past 100k km |

---

*Framework: CRISP-DM + LEAN | Methodology: Case-Based Learning (CBL)*
**Jose Marcel Lopez Pino** | Data Scientist — Operations, Analytics & Process Optimization
[![GitHub](https://img.shields.io/badge/GitHub-joselopezp-181717?style=flat&logo=github)](https://github.com/joselopezp)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-jose--lopez--pino-0077B5?style=flat&logo=linkedin)](https://www.linkedin.com/in/jose-lopez-pino/)
