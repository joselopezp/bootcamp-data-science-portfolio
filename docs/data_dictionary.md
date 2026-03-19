# Data Dictionary — Customer Segmentation Dataset

**Source:** Kaggle — kaushiksuresh147/customer-segmentation  
**Acquisition Date:** TBD  
**File:** `data/raw/Train.csv` (and `Test.csv`)

---

| Variable | Type | Description | Values / Range | Missing % | Notes |
|----------|------|-------------|----------------|-----------|-------|
| ID | int | Unique customer identifier | — | 0% | Drop before modeling |
| Gender | categorical | Customer gender | Male / Female | TBD | Encode: 0/1 |
| Ever_Married | categorical | Marital status | Yes / No | TBD | Encode |
| Age | int | Customer age (years) | TBD | TBD | Check outliers |
| Graduated | categorical | Has university degree | Yes / No | TBD | Encode |
| Profession | categorical | Occupation | Multiple | TBD | One-hot encode |
| Work_Experience | int | Years of work experience | TBD | TBD | Check outliers |
| Spending_Score | categorical | Spending behavior | Low / Average / High | TBD | Ordinal encode |
| Family_Size | int | Number of family members | TBD | TBD | Check outliers |
| Var_1 | categorical | Anonymized behavioral variable | Cat_1…Cat_7 | TBD | One-hot encode |
| Segmentation | categorical | **Target label (held out)** | A / B / C / D | 0% | Use only for external validation |

---

## Encoding Strategy (Phase 3 decision)

- **Binary categoricals** (Gender, Ever_Married, Graduated): label encoding 0/1
- **Ordinal** (Spending_Score): Low=0, Average=1, High=2
- **Nominal with >2 categories** (Profession, Var_1): one-hot encoding
- **Numeric** (Age, Work_Experience, Family_Size): StandardScaler after outlier removal

---

> Note: `Segmentation` column is the original label. Do NOT use during unsupervised modeling. 
> It can be used post-hoc to evaluate cluster purity against ground truth.
