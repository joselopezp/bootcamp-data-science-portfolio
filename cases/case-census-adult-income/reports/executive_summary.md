# Executive Summary — Census Adult Income: Income Prediction & Workforce Segmentation

**Author:** Jose Marcel Lopez Pino
**Role:** Industrial Engineer (Operations, Analytics & Process Optimization)
**Framework:** CRISP-DM + LEAN | Case-Based Learning (CBL)
**Date:** March 2026
**Status:** ![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

---

## 1. Business Context

| | |
|---|---|
| **Industry** | Retail / E-commerce |
| **Business Unit** | Marketing & Customer Loyalty |
| **Stakeholder** | Marketing Director / CRM Manager |
| **Decision to Support** | Which customer profiles should receive premium loyalty campaign offers vs standard promotions? |

> **Situation:** RetailMax operates loyalty campaigns across a broad customer base but applies a uniform strategy regardless of purchasing power. Without a data-driven segmentation of income capacity, premium offers reach low-value segments — diluting ROI and inflating campaign costs.

---

## 2. Problem Statement

> Can we predict whether a worker earns above USD 50K/year and identify distinct socioeconomic profiles, to enable RetailMax to focus premium loyalty campaigns on high purchasing-power segments?

**Business Impact if Unresolved:**
- Premium campaign budget wasted on low-income segments — estimated misallocation affects ~75% of the audience (share of workers earning ≤50K)
- No segmentation baseline means all customers receive identical offers, reducing conversion rates for high-value tiers

---

## 3. Analytical Approach

> Non-technical summary — what was done, not how.

| Step | Description |
|---|---|
| **Data** | UCI Adult Census Income · 32,561 records · 15 variables (numeric + categorical) · UCI ML Repository |
| **Method** | Binary classification (Logistic Regression) to predict income >50K + unsupervised clustering (KMeans k=4) to segment workforce profiles |
| **Tool** | Python · PySpark 4.1.1 · MLlib Pipelines · Spark SQL |
| **Validation** | AUC-ROC on held-out test set (20%) · Silhouette score for cluster cohesion · Baseline comparison (majority classifier) |

---

## 4. Key Findings

### Finding 1 — Supervised model exceeds performance target
- **Context:** A majority classifier (always predicting ≤50K) achieves ~75% accuracy — the minimum baseline to beat.
- **Analysis:** Logistic Regression achieved AUC-ROC = 0.9005 and Accuracy = 0.85+ on the test set, well above the 0.85 AUC target.
- **Insight:** The model has strong discriminatory power — it correctly separates high-income workers from low-income workers 90% of the time.
- **Possible Decision:** Deploy model scoring to flag high-income probability customers for premium campaign targeting.

### Finding 2 — Four distinct workforce profiles identified
- **Context:** RetailMax needed audience segments beyond binary income prediction — actionable groups for differentiated campaign strategies.
- **Analysis:** KMeans k=4 produced 4 clusters differentiated by age, education level, hours worked per week, and capital gain.
- **Insight:** Clusters represent interpretable profiles (e.g. young high-education professionals vs mature blue-collar workers) that map directly to campaign tiers.
- **Possible Decision:** Assign each cluster a campaign tier (Premium / Standard / Reactivation / Exclusion) based on profile characteristics.

### Finding 3 — Education and occupation are the strongest income signals
- **Context:** The dataset contains 15 variables — not all contribute equally to income prediction.
- **Analysis:** Spark SQL JOIN analysis against an income benchmark table confirmed that Bachelors+ education levels correlate with benchmark incomes above USD 52K, concentrated in Management and Professional sectors.
- **Insight:** Education level and occupation sector are the two most actionable variables for campaign audience building — available in most CRM systems.
- **Possible Decision:** Use education + occupation filters as a lightweight proxy for income scoring when full model scoring is not available.

---

## 5. Business Recommendations

| Priority | Recommendation | Expected Impact | Effort |
|---|---|---|---|
| 🔴 High | Score existing customer base with Logistic Regression model (AUC = 0.9005) to identify high-income probability profiles | Reduce premium campaign misallocation from ~75% to <20% of audience | Medium |
| 🟡 Medium | Apply KMeans k=4 segmentation to assign customers to campaign tiers (Premium / Standard / Reactivation) | Increase campaign ROI through differentiated offer strategies per segment | Medium |
| 🟢 Low | Use education + occupation as lightweight income proxy filters in CRM for campaigns where full model scoring is unavailable | Quick win — no model deployment required, actionable with existing CRM data | Low |

---

## 6. Limitations

- **Data:** Census data from UCI repository — not RetailMax transactional data. Model must be retrained on company CRM data before production deployment.
- **Model:** Logistic Regression is the MVP model — non-linear relationships may be better captured by Random Forest or GradientBoosting (next iteration).
- **Scope:** Binary income threshold (>50K USD) is a proxy for purchasing power — does not capture wealth, savings, or discretionary spend directly.
- **Fairness:** Model includes `sex` as a feature — fairness audit required before deployment to ensure no discriminatory campaign targeting.

---

## 7. Next Steps

| Horizon | Action |
|---|---|
| **Immediate** | Interpret KMeans centroids to assign business names to each of the 4 clusters |
| **Short-term** | Optimize hyperparameters with CrossValidator (`regParam`, `elasticNetParam`) and evaluate Elbow Method for optimal k |
| **Long-term** | Retrain pipeline on RetailMax CRM data · Deploy via FastAPI scoring endpoint · Monitor data drift quarterly |

---

*Framework: CRISP-DM + LEAN | Methodology: Case-Based Learning (CBL)*

**Jose Marcel Lopez Pino**
Industrial Engineer (Operations, Analytics & Process Optimization) | Data Science & Business Analytics
Bootcamp: Fundamentos de Ciencia de Datos — SENCE/Alkemy (2025–2026)

[![GitHub](https://img.shields.io/badge/GitHub-joselopezp-181717?style=flat&logo=github)](https://github.com/joselopezp)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-jose--lopez--pino-0077B5?style=flat&logo=linkedin)](https://www.linkedin.com/in/jose-lopez-pino/)
