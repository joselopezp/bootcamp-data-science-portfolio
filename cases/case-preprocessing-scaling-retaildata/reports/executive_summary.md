# Executive Summary — Data Preprocessing & Feature Scaling

**Author:** Jose Marcel Lopez Pino
**Role:** Data Scientist — Operations, Analytics & Process Optimization
**Framework:** CRISP-DM + LEAN | Case-Based Learning (CBL)
**Date:** April 2026
**Status:** ![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

---

## 1. Business Context

| | |
|---|---|
| **Industry** | Retail — Supermarket Chain |
| **Business Unit** | Customer Analytics / Marketing |
| **Stakeholder** | Data Science Team — RetailData Analytics |
| **Decision to Support** | Which preprocessing strategy produces the cleanest, most model-compatible feature matrix for a recurring customer purchase classifier? |

> **Situation:** RetailData Analytics was contracted by a supermarket chain to build a predictive model identifying customers most likely to make recurring purchases. During the initial data intake phase, the team discovered that the raw dataset — containing customer demographics and behavioral data — was unfit for modeling: it contained missing income values, unencoded city categories, and a 1,000x numeric scale mismatch between age and income. Before any model can be trained, a complete preprocessing pipeline must be designed, applied, and documented.

---

## 2. Problem Statement

> How can the raw 4-column customer dataset be transformed into a clean, encoded, and properly scaled feature matrix that eliminates modeling biases caused by missing values, nominal categories, and inconsistent numeric scales?

**Business Impact if Unresolved:**
- Distance-based models (KNN, SVM, KMeans) would assign 99.9% of their weight to `Income` and effectively ignore `Age` — distorting customer segmentation and producing unreliable recurring purchase predictions.
- A model trained on unimputed data would either crash or silently impute zeros, introducing systematic bias toward the minimum income bracket.
- Unencoded city categories would prevent model fitting entirely — scikit-learn does not accept string inputs.

---

## 3. Analytical Approach

> Non-technical summary — what was done, not how.

| Step | Description |
|---|---|
| **Data** | RetailData Analytics customer fragment — 4 rows × 4 columns (ID, Age, City, Income). Synthetic dataset provided as part of M5 L3 case. |
| **Method** | Sequential preprocessing pipeline: missing value imputation → categorical encoding (3 methods) → numeric feature scaling (2 methods) |
| **Tool** | Python · pandas 3.0 · scikit-learn 1.8 · matplotlib 3.10 |
| **Validation** | Post-imputation: 0 missing values confirmed. Post-scaling: mean=0.0000 and std=1.1547 verified for both Z-Score features. Output CSV shape (4, 12) confirmed. |

---

## 4. Key Findings

### Finding 1 — Scale mismatch silently distorts model learning
- **Context:** Raw dataset has `Age` ranging 25–45 and `Income` ranging 30,000–50,000 — a 1,000x difference in magnitude. Both features are equally relevant for predicting customer behavior.
- **Analysis:** After Min-Max normalization, both features map to [0.0000, 1.0000]. After Z-Score standardization, both features achieve mean=0.0000 and std=1.1547. Before scaling, a $1 income difference was mathematically equivalent to 1,000 years of age in any distance calculation.
- **Insight:** Unscaled features do not cause visible errors — the model trains and predicts without warnings. The bias is silent, embedded in the learned weights, and only detectable through careful feature importance analysis. This makes scale mismatch one of the most dangerous preprocessing omissions in production ML pipelines.
- **Possible Decision:** Establish Z-Score standardization as the default scaler for all customer models — it handles out-of-range new customer data gracefully, unlike Min-Max which produces values outside [0,1] for customers with income beyond the training range.

### Finding 2 — Encoding choice determines model compatibility, not just performance
- **Context:** `City` has 3 nominal categories (Barcelona, Madrid, Sevilla) with no natural order. Three encoding strategies were applied and compared.
- **Analysis:** Label Encoding assigns Barcelona=0, Madrid=1, Sevilla=2 — implying Sevilla is mathematically "twice" Madrid, which is semantically false. One-Hot Encoding creates 3 binary columns with no ordinal assumption. Dummy encoding (drop_first=True) reduces to 2 columns (Madrid, Sevilla), with Barcelona as the implicit reference category — eliminating multicollinearity in regression models.
- **Insight:** Encoding is not a formatting step — it is a modeling decision. A linear regression trained on Label-Encoded cities would learn a false linear relationship between city codes and purchase frequency. The choice between OHE and Dummy depends entirely on the downstream model architecture, not on personal preference.
- **Possible Decision:** Use One-Hot Encoding for linear and distance-based models (Logistic Regression, SVM, KNN); use Label Encoding only for tree-based models (Decision Tree, Random Forest, XGBoost) where splits handle ordinal artifacts correctly.

### Finding 3 — Mean imputation is conservative but geographically naive
- **Context:** Row 3 (ID=3, City=Madrid) had missing `Income`. Three known values were available: $30,000 (Madrid), $50,000 (Sevilla), $40,000 (Barcelona).
- **Analysis:** Global mean = (30,000 + 50,000 + 40,000) / 3 = **$40,000** — the imputed value. This equals the known Barcelona income, and coincidentally matches the overall median. Post-imputation: 0 missing values, dataset complete.
- **Insight:** Mean imputation ignores geographic income variation. Madrid customers may have systematically different income profiles than Sevilla or Barcelona customers. With only 4 rows this difference is undetectable, but in the full production dataset a city-level median imputation (`GroupBy('City')['Income'].transform('median')`) would produce more accurate fills and reduce segmentation bias.
- **Possible Decision:** For the full RetailData customer dataset, replace global mean imputation with city-level median imputation — a one-line change with meaningful accuracy improvement for geographic customer segmentation.

---

## 5. Business Recommendations

| Priority | Recommendation | Expected Impact | Effort |
|---|---|---|---|
| 🔴 High | Adopt Z-Score as the default scaler for all production customer models | Eliminates scale-induced model bias; handles new out-of-range customer data without breaking the pipeline | Low |
| 🔴 High | Use One-Hot Encoding for `City` in linear and distance-based models; Label Encoding only for tree-based models | Prevents false ordinal relationships from distorting model coefficients | Low |
| 🟡 Medium | Replace global mean imputation with city-level median imputation on the full dataset | Reduces geographic income bias in customer segmentation — directly improves cluster quality | Low |
| 🟢 Low | Wrap the full pipeline in scikit-learn `Pipeline` + `ColumnTransformer` | Prevents data leakage by ensuring scalers are fitted on training data only — critical for model evaluation integrity | Medium |

---

## 6. Limitations

- **Data:** Fragment of 4 rows is a demonstration dataset — statistical conclusions require the full customer database. No generalization is possible from n=4.
- **Imputation:** Mean computed on n=3 known values. With only 3 data points, the mean is highly sensitive to any single extreme value — not robust for production use.
- **Scaling:** Both scalers fitted on the full 4-row dataset. In a real ML pipeline, scalers must be fitted on training data only and applied (transform only) to validation and test sets to prevent data leakage.
- **Scope:** Preprocessing only — no model was trained in this case. Business impact of encoding and scaling choices will only be quantifiable once a classifier is fitted on the processed data.

---

## 7. Next Steps

| Horizon | Action |
|---|---|
| **Immediate** | Apply this preprocessing pipeline to the full RetailData customer dataset using `Pipeline` + `ColumnTransformer` from scikit-learn |
| **Short-term** | Train a Logistic Regression classifier on the preprocessed features and evaluate recurring purchase prediction accuracy (AUC, precision, recall) |
| **Long-term** | Refactor into `src/preprocessing.py` reusable module — paralleling the `wrangling.py` approach from the M3 fintech wrangling case — for deployment as a production data preparation service |

---

*Framework: CRISP-DM + LEAN | Methodology: Case-Based Learning (CBL)*

**Jose Marcel Lopez Pino**
Data Scientist — Operations, Analytics & Process Optimization | Data Science & Business Analytics
Bootcamp: Fundamentos de Ciencia de Datos — SENCE/Alkemy (2025–2026)

[![GitHub](https://img.shields.io/badge/GitHub-joselopezp-181717?style=flat&logo=github)](https://github.com/joselopezp)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-jose--lopez--pino-0077B5?style=flat&logo=linkedin)](https://www.linkedin.com/in/jose-lopez-pino/)
