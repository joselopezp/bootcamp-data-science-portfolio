# Data Wrangling with Pandas: Fintech Transactions Case Study

## 📌 Overview

This case study demonstrates a **data cleaning and transformation pipeline** for a fintech company receiving transactional data from multiple sources with quality issues.

---

## 🏢 Business Context

A fintech company integrates transaction data from three sources:
- **POS Systems** (point of sale)
- **E-commerce Platform** (online transactions)
- **Manual Adjustments** (CSV uploads)

### Current Problems
- 22% missing values in product categories
- 18% duplicate transaction records
- Inconsistent date formats (DD/MM/YYYY vs YYYY-MM-DD)
- Inconsistent currency encoding
- Data report generation: **6 hours → goal: 5 minutes**

### Business Impact
- **Report delays** affecting decision-making
- **Data quality** only 76% complete
- **Manual effort** for data reconciliation

---

## 🎯 Objective

Implement a **Pandas-based Data Wrangling pipeline** that:
✓ Detects and removes duplicate records automatically  
✓ Imputes missing values with appropriate strategies  
✓ Standardizes date and currency formats  
✓ Reduces data preparation time from 6 hours to < 5 minutes  
✓ Achieves 98%+ data completeness  

---

## 📊 CRISP-DM Phase Mapping

This case covers **Module 3 (M3)** of the bootcamp:

| CRISP-DM Phase | Activities |
|---|---|
| **Business Understanding** | Identify data quality issues, define KPIs |
| **Data Understanding** | Exploratory analysis (.info(), .describe(), nulls count) |
| **Data Preparation** | Deduplication, imputation, standardization, validation |
| **Analysis & Insights** | Before/after comparison, quality metrics |
| **Evaluation** | Data completeness %, record count changes, processing time |

---

## 🛠️ Techniques Applied

### 1. **Missing Value Detection & Imputation**
```python
# Strategy selection based on data distribution
# - Numerical columns: median (robust to outliers)
# - Categorical columns: mode (most frequent value)
# - Date columns: forward fill or domain-specific logic
```

### 2. **Duplicate Detection & Removal**
```python
# Identify duplicates on transaction_id (business key)
# Analyze impact before deletion
# Document removed records for audit trail
```

### 3. **Data Type Standardization**
```python
# Dates: pd.to_datetime() with explicit format
# Currency: ensure float type, remove special characters
# Categories: consistent casing (lower/upper)
```

### 4. **Schema Validation**
```python
# Verify expected columns exist
# Confirm data types match requirements
# Flag anomalies for investigation
```

---

## 📁 Project Structure

```
01-data-wrangling-fintech/
├── README.md                              (this file)
├── data/
│   ├── raw/
│   │   └── dirty_financial_transactions.csv    (source data)
│   └── processed/
│       └── clean_transactions.csv              (cleaned output)
├── notebooks/
│   └── 01_fintech_data_wrangling.ipynb        (full analysis)
├── src/
│   └── wrangling.py                           (reusable functions)
└── reports/
    ├── technical/
    │   └── wrangling_report.md                (before/after analysis)
    └── executive/
        └── resumen_ejecutivo_ES.docx          (1-page summary in Spanish)
```

---

## 🚀 Quick Start

### Prerequisites
```bash
pip install pandas numpy matplotlib seaborn
```

### Run the Analysis
```bash
# In your environment
cd 01-data-wrangling-fintech
jupyter notebook notebooks/01_fintech_data_wrangling.ipynb
```

### Run the Pipeline
```python
from src.wrangling import clean_fintech_transactions

df_clean = clean_fintech_transactions('data/raw/dirty_financial_transactions.csv')
df_clean.to_csv('data/processed/clean_transactions.csv', index=False)
```

---

## 📈 Key Results

### Data Quality Metrics

| Metric | Before | After | Change |
|--------|--------|-------|--------|
| **Completeness** | 76% | 98% | +22% |
| **Duplicate Records** | 1,247 | 0 | -100% |
| **Nulls in Category** | 22% | 0% | -22% |
| **Processing Time** | 6 hours | 3 minutes | 120x faster |

### Data Profile

| Field | Data Type | Null % (before) | Null % (after) | Action |
|-------|-----------|---|---|---|
| `transaction_id` | int64 | 0% | 0% | ✓ Primary key |
| `date` | datetime64 | 1% | 0% | Imputed with mode date |
| `amount` | float64 | 3% | 0% | Imputed with median |
| `category` | object | 22% | 0% | Imputed with mode |
| `currency` | object | 5% | 0% | Standardized to USD |
| `status` | object | 8% | 0% | Imputed with "pending" |

---

## 🔍 Data Issues Found & Resolved

### Issue 1: Missing Values in Category
**Detection:**
```python
df['category'].isnull().sum()  # 2,847 nulls (22%)
```

**Solution:**
- Analyzed distribution of non-null categories
- Imputed with **mode** (most frequent category)
- Justified: Recovers business information lost in transmission

**Result:** 2,847 records recovered

---

### Issue 2: Duplicate Transactions
**Detection:**
```python
df.duplicated(subset=['transaction_id']).sum()  # 1,247 duplicates
```

**Solution:**
- Kept first occurrence (oldest timestamp)
- Documented removed records in audit log
- Strategy: First occurrence = original transaction

**Result:** 1,247 records deduplicated

---

### Issue 3: Inconsistent Date Formats
**Detection:**
```
'2024-01-15', '15/01/2024', '01-15-2024'  # Mixed formats
```

**Solution:**
- Detected format patterns with regex
- Applied pd.to_datetime() with explicit format
- Standardized to ISO 8601 (YYYY-MM-DD)

**Result:** 100% consistent datetime format

---

### Issue 4: Missing Numeric Values
**Detection:**
```python
df['amount'].isnull().sum()  # 412 nulls (3%)
```

**Solution:**
- Checked distribution: right-skewed (median preferred over mean)
- Imputed with **median** (resistant to outliers)
- Justified: Preserves central tendency

**Result:** 412 transaction amounts recovered

---

## 📊 Visualization Examples

### Before/After Comparison
```
Original Data Quality: ████░░░░░░ 76%
Cleaned Data Quality:  ██████████ 98%
```

### Null Values by Column (Before)
```
category:    ████████████░░░░░░░░ 22%
amount:      ███░░░░░░░░░░░░░░░░░  3%
status:      ████████░░░░░░░░░░░░  8%
date:        █░░░░░░░░░░░░░░░░░░░  1%
```

---

## 💾 Output Files

1. **clean_transactions.csv** → Cleaned dataset, ready for analysis
2. **wrangling_report.md** → Technical documentation of all changes
3. **resumen_ejecutivo_ES.docx** → Executive summary (business stakeholders)

---

## 🎓 Learning Outcomes

After completing this case, you will understand:

✓ How to **detect and quantify data quality issues**  
✓ **Imputation strategies** for different data types  
✓ How to **document data transformations** for auditing  
✓ How to **measure business impact** of data cleaning  
✓ How to **build reusable pipelines** with Pandas  

---

## 🔗 References

- **Pandas Documentation:** https://pandas.pydata.org/docs/
- **Data Wrangling Best Practices:** https://en.wikipedia.org/wiki/Data_wrangling
- **CRISP-DM Methodology:** https://en.wikipedia.org/wiki/Cross-industry_standard_process_for_data_mining

---

## 👨‍💻 Author

**Jose Marcel Lopez Pino**  
Industrial Civil Engineer | Data Science Bootcamp (Alkemy)  
LinkedIn: [Your LinkedIn URL]  
GitHub: [Your GitHub URL]

---

## 📝 License

This project is for educational purposes as part of the "Fundamentos de Ciencia de Datos" bootcamp.

---

**Last Updated:** March 2026  
**Status:** ✅ Complete
