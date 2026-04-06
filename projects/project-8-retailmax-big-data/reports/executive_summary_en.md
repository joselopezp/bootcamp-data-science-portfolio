# Executive Summary — RetailMax: Retail Analytics Pipeline

**Author:** Jose Marcel Lopez Pino
**Role:** Data Scientist — Operations, Analytics & Process Optimization
**Framework:** CRISP-DM + LEAN | Project-Based Learning (PBL)
**Date:** April 2026
**Status:** ![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

---

## 1. Business Context

| | |
|---|---|
| **Industry** | E-Commerce / Retail |
| **Business Unit** | Analytics & Machine Learning Department |
| **Stakeholder** | Marketing Director, RetailMax |
| **Decision to Support** | Identify which customers should receive personalized retention offers vs. standard promotions, and which segments to prioritize for targeted marketing campaigns. |

> **Situation:** RetailMax processes millions of daily transactions on its e-commerce platform, but its analytics process is slow and fragmented — data stored across multiple systems and traditional ML tools unable to scale. Marketing decisions rely on sampled data, missing patterns in long-tail customer segments. A scalable Big Data pipeline is needed to unify data sources and generate actionable insights.

---

## 2. Problem Statement

> Build a scalable Big Data + Machine Learning pipeline that classifies customers by value and segments them for targeted marketing campaigns, processing over 2 million records from transactions, reviews, and browsing behavior.

**Business Impact if Unresolved:**
- 15–25% waste in retention budget due to untargeted campaigns
- 19% of high-ticket customers are dissatisfied (avg review 2.1/5) — churn risk of ~$5.2M
- 77% of customers purchase only once — untapped reactivation opportunity

---

## 3. Analytical Approach

> A complete Big Data pipeline was built using Apache Spark, from data ingestion through scalable ML model generation, following the 6 CRISP-DM phases.

| Step | Description |
|---|---|
| **Data** | Brazilian E-Commerce (Olist, Kaggle) — 9 tables, ~100K orders, 2016–2018. Supplemented with 500K synthetic browsing events generated via `spark.range()`. Total: 2,055,860 records. |
| **Method** | RDD transformations + Spark SQL for business metrics. Logistic Regression (High/Low Value classification) + K-Means (customer segmentation, K=4). |
| **Tool** | Python 3.12 · PySpark 4.1.1 · Spark MLlib · Java 17 Temurin · Parquet |
| **Validation** | AUC-ROC for classification, Silhouette Score + Elbow Method for clustering. Metrics validated against Problem Statement Canvas targets. |

---

## 4. Key Findings

> Three findings following: **Context → Analysis → Insight → Decision**

### Finding 1 — 77% of customers are satisfied one-time buyers
- **Context:** RetailMax has a predominantly single-purchase customer base.
- **Analysis:** Cluster 0 ("One-time Satisfied"): 72,013 customers, avg ticket $112, avg review 4.6/5.
- **Insight:** These customers had a positive experience but never returned — the issue is not dissatisfaction but lack of stimulus for repeat purchase.
- **Possible Decision:** Launch personalized reactivation campaign 30 days post-first purchase. A 5% conversion rate would yield ~3,600 repeat customers (~$400K additional revenue).

### Finding 2 — High-ticket customers are the most dissatisfied
- **Context:** 19% of customers spend significantly above average.
- **Analysis:** Cluster 3 ("High-ticket Critics"): 17,911 customers, avg ticket $290, avg review 2.1/5 — the lowest across all segments.
- **Insight:** The highest spenders report the worst experience. This likely reflects an expectation gap in premium product delivery.
- **Possible Decision:** Service recovery program — personalized follow-up within 48h for orders with review ≤ 2. ROI is high: these customers spend 2.6x the average.

### Finding 3 — Loyal customers are rare but highly valuable
- **Context:** Only 0.8% of customers make sustained repeat purchases.
- **Analysis:** Cluster 1 ("Loyal Repeaters"): 703 customers, 2.3 avg orders, 256-day lifespan, avg review 4.3/5.
- **Insight:** This micro-segment represents the ideal customer profile. Their behavior is replicable if loyalty drivers are understood.
- **Possible Decision:** Create VIP program (free shipping, early access, rewards). Study which categories and purchase timing characterize this group to replicate the pattern.

---

## 5. Business Recommendations

| Priority | Recommendation | Expected Impact | Effort |
|---|---|---|---|
| 🔴 High | Service recovery program for High-ticket Critics (19%) | Mitigate ~$5.2M churn risk; improve reviews from 2.1 to 3.5+ | Medium |
| 🔴 High | Reactivation campaign for One-time Satisfied (77%) | ~$400K additional revenue (5% conversion to repeat purchase) | Low |
| 🟡 Medium | Bundle offers and volume discounts for Multi-item Buyers (3%) | Increase basket from $370 to $450 (+22%) | Medium |
| 🟢 Low | VIP program for Loyal Repeaters (0.8%) | Retain 95%+ of highest-value segment; model for scaling loyalty | Low |

---

## 6. Limitations

- **Data:** Olist dataset spans 2016–2018 — customer behavior patterns may differ in 2026.
- **Model:** Logistic Regression assumes linear relationship between features and probability — GBT or XGBoost could improve AUC.
- **Scope:** Clickstream data is synthetic — real browsing data would improve feature quality. Pipeline validated on local mode only — cloud validation pending.
- **Target:** "High Value" defined as avg_ticket > median — business should validate this threshold against actual CLV data.

---

## 7. Next Steps

| Horizon | Action |
|---|---|
| **Immediate** | Deliver segment report to marketing team for Q2 2026 campaign design. |
| **Short-term** | Validate pipeline on cloud environment (Google Colab or Databricks Community) to demonstrate scalability. |
| **Long-term** | Integrate real clickstream data + implement BG/NBD model for customer lifetime value prediction. Connect with PequeShop prescriptive analytics arc. |

---

*Framework: CRISP-DM + LEAN | Methodology: Project-Based Learning (PBL)*

**Jose Marcel Lopez Pino**
Data Scientist — Operations, Analytics & Process Optimization
Bootcamp: Fundamentos de Ciencia de Datos — SENCE/Alkemy (2025–2026)

[![GitHub](https://img.shields.io/badge/GitHub-joselopezp-181717?style=flat&logo=github)](https://github.com/joselopezp)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-jose--lopez--pino-0077B5?style=flat&logo=linkedin)](https://www.linkedin.com/in/jose-lopez-pino/)
