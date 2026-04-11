# Executive Summary — Customer Value Modeling: Income Proxy & Behavioral Segmentation

**Author:** Jose Marcel Lopez Pino
**Role:** Industrial Engineer (Operations, Analytics & Process Optimization)
**Framework:** CRISP-DM + LEAN | Case-Based Learning (CBL)
**Date:** March 2026
**Status:** ![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

---

## 1. Business Context

| | |
|---|---|
| **Domain** | Customer Analytics / Socioeconomic Profiling (income as proxy)
| **Data Source** | UCI Adult Census Income — 1994 US Census |
| **Primary Use Case** | Customer value modeling and behavioral segmentation (income as proxy) |
| **Decision to Support** | Can we identify high-value customer profiles and segment the population to enable targeted strategies using income as a proxy? |

> **Situation:** Organizations across retail, banking, and digital platforms need to identify high-value customers — but often rely on manual, spreadsheet-based analysis with limited scalability and predictive power.  
> This case demonstrates a scalable MLlib pipeline that replaces static analysis with data-driven scoring and segmentation, enabling targeted decision-making in customer analytics.

---

## 2. Problem Statement

> Can a machine learning pipeline identify high-value customer profiles using income as a proxy and segment the population into actionable groups for targeted decision-making?

**Business Impact if Unresolved:**
- Without income classification, organizations apply uniform strategies to heterogeneous
  populations — inefficient resource allocation and missed targeting opportunities
- Without segmentation, the ~25% of high-value profiles remain unidentified 
within the broader population, reducing ROI of any differentiated strategy

---

## 3. Analytical Approach

> Non-technical summary — what was done, not how.

| Step | Description |
|---|---|
| **Data** | UCI Adult Census Income · 32,561 records · 15 variables (numeric + categorical) · UCI ML Repository |
| **Method** | Binary classification (Logistic Regression) to predict income >50K + unsupervised clustering (KMeans k=4) to segment socioeconomic profiles |
| **Tool** | Python · PySpark 4.1.1 · MLlib Pipelines · Spark SQL |
| **Optimization** | CrossValidator 5-fold · 12 parameter combinations · Elbow Method k=2..8 |
| **Validation** | AUC-ROC on held-out test set (20%) · CrossValidator 5-fold · Silhouette score · Elbow Method · Baseline comparison (majority classifier) |

---

## 4. Key Findings

### Finding 1 — Supervised model exceeds performance target after optimization
- **Context:** A majority classifier (always predicting <=50K) achieves ~75% accuracy — the minimum baseline to beat.
- **Analysis:** Logistic Regression achieved AUC-ROC = 0.9005 before optimization. CrossValidator (5-fold, 12 combinations) identified best params: regParam=0.001, elasticNetParam=0.5 — improving AUC to 0.9028 (+0.0023). Lean note: marginal improvement confirms the MVP model was already well-calibrated.
- **Insight:** The model has strong discriminatory power — separates high-value profiles from low-value profiles (using income as proxy) with 90% AUC regardless of optimization stage.
- **Possible Decision:** Deploy model scoring to flag high-value customer profiles based on predicted probability for differentiated treatment in any downstream application.

### Finding 2 — Four distinct behavioral and socioeconomic profiles identified
- **Context:** Binary income prediction alone is insufficient — organizations need actionable audience segments, not just a binary flag.
- **Analysis:** KMeans k=4 produced 4 clusters differentiated by age, education level, hours worked per week, and capital gain. Elbow Method (k=2..8) showed no dominant geometric inflection — k=4 validated as a business-interpretability-driven choice.
- **Insight:** The 4 clusters represent interpretable socioeconomic archetypes (e.g. high-education professionals vs blue-collar workers) applicable to differentiated strategy design.
- **Possible Decision:** Map each cluster to a strategic tier — Premium / Standard / Development / Exclusion — based on profile characteristics.

### Finding 3 — Education and occupation are the strongest income signals
- **Context:** The dataset has 15 variables — not all contribute equally to income prediction.
- **Analysis:** Spark SQL JOIN analysis against an income benchmark table confirmed that Bachelors+ education correlates with benchmark incomes above USD 52K, concentrated in Management and Professional sectors. Prof-school workers earning >50K average 14,274 USD in capital gains — 3.7x above Bachelors level.
- **Insight:** Education level and occupation sector are the two most actionable and widely available variables for income-based segmentation.
- **Possible Decision:** Use education + occupation as lightweight proxy filters when full model scoring is not available — actionable with most CRM or HR systems.

---

## 5. Business Recommendations

| Priority | Recommendation | Expected Impact | Effort |
|---|---|---|---|
| 🔴 High | Apply Logistic Regression pipeline (AUC = 0.9028) to score target population and classify high-value customer profiles (income as proxy) | Reduce misclassification from 25% baseline (majority) to <10% using model | Medium |
| 🟡 Medium | Use KMeans k=4 clusters to design differentiated strategies per socioeconomic segment | Enable targeted approaches vs uniform treatment — estimated +15% effectiveness | Medium |
| 🟢 Low | Use education + occupation as lightweight income proxy in rule-based systems | Quick win — no model deployment required, actionable with existing data infrastructure | Low |

---

## 6. Limitations

- **Data:** 1994 US Census — not representative of current labor market. Income thresholds, occupation structure, and education patterns have changed significantly. Retrain on current data before production use.
- **Model:** Logistic Regression is the MVP model — non-linear relationships may be better captured by Random Forest or GradientBoosting in a next iteration.
- **Scope:** Binary income threshold (>50K USD, 1994) is a historical proxy — does not reflect current purchasing power or cost-of-living differences across regions.
- **Fairness:** Model includes `sex` as a feature — fairness audit required before deployment to ensure no discriminatory targeting outcomes.
- **Clustering:** Elbow Method shows no dominant geometric inflection point — k=4 is a business-interpretability choice, not a data-driven geometric optimum.

---

## 7. Next Steps

| Horizon | Action |
|---|---|
| **Immediate** | Interpret KMeans centroids to assign descriptive business names to each of the 4 clusters |
| **Short-term** | Retrain pipeline on current census or CRM data · Add Random Forest as comparison model · Conduct fairness audit on `sex` feature |
| **Long-term** | Deploy via FastAPI scoring endpoint · Integrate MLflow for experiment tracking · Monitor income distribution drift quarterly |

---

*Framework: CRISP-DM + LEAN | Methodology: Case-Based Learning (CBL)*

**Jose Marcel Lopez Pino**
Industrial Engineer (Operations, Analytics & Process Optimization) | Data Science & Business Analytics
Bootcamp: Fundamentos de Ciencia de Datos — SENCE/Alkemy (2025–2026)

[![GitHub](https://img.shields.io/badge/GitHub-joselopezp-181717?style=flat&logo=github)](https://github.com/joselopezp)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-jose--lopez--pino-0077B5?style=flat&logo=linkedin)](https://www.linkedin.com/in/jose-lopez-pino/)
