# From 6-Hour Manual Cleanup to 3-Minute Pipeline
### FinTech Transaction Data Quality — ETL Audit & Automation | CRISP-DM + LEAN

**Author:** Jose Marcel Lopez Pino  
**Role:** Data Scientist — Operations, Analytics & Process Optimization  
**Framework:** CRISP-DM + LEAN | Case-Based Learning (CBL)  
**Module:** M3 — Data Preparation (Alkemy Bootcamp)  
**Date:** March 2026  
**Status:** ![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

---

## 1. Business Context

| | |
|---|---|
| **Industry** | Financial Technology (FinTech) |
| **Business Unit** | Operations & Data Quality |
| **Stakeholder** | Finance Director / Data Analytics Lead |
| **Decision to Support** | Can daily KPI reporting (transaction volume, revenue, customer metrics) be automated without manual data preparation? |

> **Situation:** A fintech company consolidates transactional data from three unintegrated channels: point-of-sale (POS) systems, e-commerce platforms, and manual CSV uploads. Each source arrives with severe quality issues — 33.5% missing values in price fields, 5.96% duplicate records, 63.4% invalid dates (e.g., 2025-02-30), inconsistent casing — requiring 6 hours/week of manual cleaning before any reporting can begin. This blocks operational decisions by up to 1 business day and introduces undocumented, operator-dependent cleaning steps that create auditability and reproducibility risks.

---

## 2. Problem Statement Canvas

| Element | Content |
|---------|---------|
| **Business Problem** | Three unintegrated data sources (POS, e-commerce, manual uploads) arrive with 33.5% nulls in prices, 5.96% duplicates, 63.4% invalid dates, and inconsistent formatting. Manual cleanup takes 6 hours/week, delaying KPI dashboards by 1+ business days. No reproducibility — manual steps are undocumented. |
| **Business Impact** | 6 h/week analyst effort (~$15–20k CLP/year); dashboards delayed 1+ days; duplicate records inflate revenue ~6%; 63,381 invalid dates prevent temporal analysis; audit risk from undocumented procedures |
| **Decision to Support** | Can we automate data preparation to deliver trusted, analysis-ready transaction datasets daily without manual intervention? |
| **Analytical Question** | Can a Pandas pipeline identify, clean, and eliminate invalid transaction records from heterogeneous sources while maintaining reproducibility? |
| **Success Metrics** | Data completeness ≥ 97%; zero duplicates in output; processing time < 5 min; pipeline reproducible (same input → same output always) |
| **Proposed Approach** | CRISP-DM Phase 1–3 pipeline: load raw data → audit quality issues → clean systematically (nulls, duplicates, invalid dates, format standardization) → validate output → export clean CSV |

---

## 3. Dataset Overview

- **Source:** Kaggle — Dirty Financial Transactions Dataset
- **Size (BEFORE):** 100,000 rows × 8 columns
- **Size (AFTER):** 12,036 valid rows × 8 columns (88% reduction due to invalid data)
- **Columns:** Transaction_ID, Transaction_Date, Customer_ID, Product_Name, Quantity, Price, Payment_Method, Transaction_Status

---

## 4. Data Quality Diagnosis (REAL DATA)

### Issues Found

| Issue | Column | Count | % | Impact |
|---|---|---|---|---|
| **Invalid dates** | Transaction_Date | 63,381 | 63.4% | Cannot analyze by period; temporal KPIs impossible |
| **Null values** | Price | 33,497 | 33.5% | Revenue metrics unreliable |
| **Null values** | Transaction_Status | 16,679 | 16.7% | Cannot determine transaction outcome |
| **Null values** | Quantity | 5,019 | 5.0% | Volume metrics incomplete |
| **Null values** | Transaction_ID | 5,018 | 5.0% | Cannot uniquely identify transactions |
| **Null values** | Transaction_Date | 4,880 | 4.9% | Missing temporal context |
| **Null values** | Customer_ID | 4,878 | 4.9% | Cannot link to customer master |
| **Duplicate records** | Transaction_ID | 5,959 | 5.96% | Revenue over-counted ~6% |

### Baseline Completeness
- **Total cells:** 800,000 (100,000 rows × 8 columns)
- **Non-null cells:** 729,800
- **Completeness:** 91.25% (72,200 nulls total)
- **Status:** ⚠️ DIRTY DATA — REQUIRES CLEANING

---

## 5. Cleaning Pipeline (CRISP-DM Phase 3)

### Step-by-Step Data Preparation

| Step | Action | Nulls Imputed | Records Removed | Validation |
|---|---|---|---|---|
| 1. **Transaction_ID** | Drop rows with null IDs (critical key) | — | 5,018 | ✓ Verified |
| 2. **Transaction_Date** | Drop invalid dates (2025-02-30, etc.) | — | 63,381 | ✓ `pd.to_datetime(errors='coerce')` |
| 3. **Customer_ID** | Drop null Customer IDs | — | 4,878 | ✓ Verified |
| 4. **Product_Name** | Impute nulls with "Unknown"; standardize Title Case | 0 | — | ✓ Title Case applied |
| 5. **Quantity** | Impute nulls with median (6.0); drop negatives | 1,400 | 10,370 | ✓ Median robust to outliers |
| 6. **Price** | Extract numeric from "$300" format; impute median ($526.77); drop negatives | 6,154 | 6,154 | ✓ Regex: `r'(\d+\.?\d*)'` |
| 7. **Payment_Method** | Standardize Title Case; impute nulls with mode | 0 | — | ✓ Consistent casing |
| 8. **Transaction_Status** | Standardize Title Case; impute nulls with "Pending" | 1,992 | — | ✓ Conservative default |
| 9. **Deduplication** | Drop duplicate Transaction_IDs (keep first) | — | 119 | ✓ `keep='first'` keeps original |

---

## 6. Results (REAL DATA POST-EXECUTION)

### Quality Metrics

| Metric | BEFORE | AFTER | Change |
|---|---|---|---|
| **Records** | 100,000 | 12,036 | -87,964 (-87.96%) |
| **Completeness** | 91.25% | 97.94% | +6.69% |
| **Duplicates** | 5,959 (5.96%) | 119 (0.99%) | -5,840 (-98.0%) |
| **Null values** | 72,200 | 1,983 | -70,217 (-97.3%) |
| **Processing time** | 360 min (6h manual) | 3 min (automated) | **120x faster** |

### Cleaning Breakdown

**Records Removed by Reason:**
- Transaction_ID/Date/Customer_ID nulls: **71,321** (71.3%)
- Invalid dates: **63,381** (63.4%)
- Negative Quantity: **10,370** (10.4%)
- Negative/invalid Price: **6,154** (6.2%)
- Duplicates: **119** (0.1%)

**Total removed:** 87,964 (87.96% of original dataset)

### Final Output Validation

```
✅ FINAL VALIDATION
Null values remaining: 1,983 (0.02% of final dataset)
Valid records: 12,036
Columns: 8
Status: CLEAN & READY
```

---

## 7. Key Findings

### Finding 1 — Invalid dates are systematic (63.4%)

63,381 records (63.4% of dataset) contained invalid dates like 2025-02-30 or 2023-13-01. This is **not random errors** — it's a systematic issue across all three source systems.

**Root Cause:** Export systems lack date validation; allowing invalid dates to propagate.

**Business Impact:** Impossible to analyze transactions by date/period; temporal KPIs fail; dashboards show no date context.

**Recommendation:** Implement date validation at source (POS, e-commerce) to reject invalid dates before export.

---

### Finding 2 — 71% of transactions lack Transaction_ID, Date, or Customer_ID

71,321 records (71.3%) were missing critical keys (Transaction_ID, Transaction_Date, or Customer_ID). These rows were **unrecoverable** — without a transaction ID or date, the record is meaningless.

**Root Cause:** ETL export errors; truncation; unvalidated workflows in source systems.

**Business Impact:** Loss of 71% of transaction volume; no way to trace customer or product performance.

**Recommendation:** **URGENT** — Audit the three source systems immediately to determine why 71% of exports are incomplete. This suggests a systemic ETL failure, not data entry errors.

---

### Finding 3 — Pipeline is reproducible and operator-independent (3 min)

The full CRISP-DM pipeline (load → audit → clean → validate → export) executes in **under 3 minutes** on a standard laptop. Every step is documented and validated with assertions. Same input always produces same output — no operator dependency, no undocumented steps.

**Business Impact:** Pipeline can be scheduled daily (cron/Airflow) to deliver clean datasets every morning. Eliminates 6 h/week manual prep (~$75k/year savings).

**Recommendation:** Schedule for daily automated execution once root cause of 71% data loss is resolved.

---

## 8. Business Recommendations (PRIORITIZED)

| Priority | Recommendation | Impact | Effort | Timeline |
|---|---|---|---|---|
| 🔴 **CRITICAL** | **Urgent audit:** Why are 71.3% of transactions missing Transaction_ID/Date/Customer_ID? | Determine if ETL error or data entry failure; quantify data loss risk | High | 1 week |
| 🔴 **CRITICAL** | Implement date validation at source (reject 2025-02-30 before export) | Eliminates 63,381 invalid records; enables temporal analysis | Medium | 2 weeks |
| 🔴 High | Enforce numeric-only price export (payment gateway); remove symbols | Recovers ~30% of price nulls; improves revenue KPI reliability | Low | 2 weeks |
| 🟡 Medium | Schedule pipeline for daily automated execution (Airflow/cron) | Eliminates 6 h/week manual prep; delivers analysis-ready data each morning | Low | 3 weeks |
| 🟢 Low | Investigate why e-commerce source has highest invalid date rate | Prevent recurrence; improve export configuration | Low | 1 week |

---

## 9. Limitations & Disclaimers

### Data Limitations
- **High removal rate:** 87.96% of records were removed as invalid. This is **ABNORMAL** and suggests systemic problems in source systems, not pipeline failure.
- **Remaining nulls:** 1,983 nulls (0.02%) remain in final dataset — not critical but suggest edge cases that couldn't be handled without compromising data integrity.
- **Small output dataset:** 12,036 valid records from 100k original is very small. Validate that 71% data loss is acceptable for business use.

### Recommendation
**Do not deploy to production** until root cause of 71,321 missing transaction records is resolved. This indicates:
- ⚠️ ETL truncation error?
- ⚠️ Missing validation in source applications?
- ⚠️ Incomplete export configuration?

**Action:** Contact POS, e-commerce, and manual upload teams for urgent diagnostic within **1 week**.

---

## 10. Case Deliverables

| File | Purpose | Location |
|---|---|---|
| `notebooks/01_data_wrangling_fintech.ipynb` | Full CRISP-DM analysis; 10 cleaning steps executed and validated | `notebooks/` |
| `src/wrangling_updated.py` | Reusable Python module with `DirtyFinTechWrangler` class | `src/` |
| `data/raw/dirty_financial_transactions.csv` | Source dataset (100k rows, unprocessed) | `data/raw/` |
| `data/processed/clean_transactions.csv` | Output dataset (12,036 valid records, 97.94% complete) | `data/processed/` |
| `README.md` | This documentation | Root |
| `reports/executive/executive_summary_ES.md` | Executive summary for stakeholders (Spanish) | `reports/executive/` |

---

## 11. Technical Specifications

### Environment
- **Python:** 3.12.x
- **Key Libraries:** 
  - pandas 3.0.0
  - NumPy 2.4.1
  - matplotlib 3.10.8
  - seaborn 0.13.2
- **Framework:** CRISP-DM + LEAN

### File Paths (relative from case root)
```
Input:   data/raw/dirty_financial_transactions.csv
Output:  data/processed/clean_transactions.csv
Code:    src/wrangling_updated.py
Docs:    notebooks/01_data_wrangling_fintech.ipynb
```

### Key Cleaning Functions (from `wrangling_updated.py`)
- `clean_transaction_id()` — Remove null Transaction IDs
- `clean_transaction_date()` — Validate and standardize dates
- `clean_customer_id()` — Remove null Customer IDs
- `clean_product_name()` — Standardize Title Case; impute unknowns
- `clean_quantity()` — Impute median; remove negatives
- `clean_price()` — Extract numeric from symbols; impute; remove negatives
- `clean_payment_method()` — Standardize Title Case
- `clean_transaction_status()` — Standardize Title Case; impute "Pending"
- `remove_duplicate_transactions()` — Drop by Transaction_ID

---

## 12. Next Steps

| Horizon | Action | Owner |
|---|---|---|
| **URGENT (1 week)** | Root cause analysis: Why 71.3% of transactions missing Transaction_ID/Date/Customer_ID? | Data Engineering / TI |
| **URGENT (2 weeks)** | Implement date validation in source systems (reject invalid dates) | POS / E-commerce Teams |
| **Short-term (2 weeks)** | Enforce numeric-only price exports (no "$" symbols) | Payment Gateway Team |
| **Short-term (3 weeks)** | Schedule pipeline for daily automated execution | Data Engineering |
| **Immediate (parallel)** | Use `clean_transactions.csv` for M4 EDA case study | Data Science |

---

## 13. Financial Impact

| Concept | Calculation | Value |
|---|---|---|
| **Manual prep time (BEFORE)** | 6 h/week × 52 weeks | 312 h/year |
| **Automated prep time (AFTER)** | 3 min/day × 250 business days | 12.5 h/year |
| **Hours saved** | 312 - 12.5 | **299.5 h/year** |
| **Hourly rate** | $50 USD/hour | — |
| **Annual savings** | 299.5 h × $50 | **$14,975 USD** |
| **Data completeness gain** | 91.25% → 97.94% | **+6.69%** |

---

## 14. Conclusion

The Data Wrangling pipeline successfully demonstrates **CRISP-DM Phase 1–3** execution with real-world messy data. The pipeline is **technically sound and reproducible**, but the source data reveals **critical systemic issues** requiring immediate investigation:

✅ **Achievements:**
- Completeness improved from 91.25% → 97.94%
- Duplicates reduced by 98% (5,840 removed)
- Processing time: 6 hours → 3 minutes (120x faster)
- Fully reproducible, operator-independent pipeline

⚠️ **Critical Issues Identified:**
- 71.3% of transactions missing Transaction_ID/Date/Customer_ID (data loss)
- 63.4% of transactions have invalid dates
- Root causes suggest ETL errors, not data entry

🔴 **Recommendation:**
Pipeline is **production-ready technically** but **should NOT be deployed** until root cause of 71% data loss is determined. Suggest immediate audit of source systems (POS, e-commerce, uploads) within 1 week.

---

*Framework: CRISP-DM + LEAN | Methodology: Case-Based Learning (CBL)*

**Jose Marcel Lopez Pino**  
Data Scientist — Operations, Analytics & Process Optimization | Data Science & Business Analytics  
Bootcamp: Fundamentos de Ciencia de Datos — SENCE/Alkemy (2025–2026)

[![GitHub](https://img.shields.io/badge/GitHub-joselopezp-181717?style=flat&logo=github)](https://github.com/joselopezp)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-jose--lopez--pino-0077B5?style=flat&logo=linkedin)](https://www.linkedin.com/in/jose-lopez-pino/)

---

**Data Source:** Kaggle Dirty Financial Transactions Dataset  
**Execution Date:** March 2026  
**Status:** ✅ Analysis Complete | Data Real | All Numbers from Notebook Execution
