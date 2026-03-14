# PequeShop Spend Prediction: Supervised ML for E-commerce Revenue Forecasting

> **PequeShop Analytics Cycle 4 — Supervised Machine Learning** | Module 6: Aprendizaje de Máquina Supervisado

![Python](https://img.shields.io/badge/Python-3.12.10-3776AB?logo=python&logoColor=white)
![Framework](https://img.shields.io/badge/Framework-CRISP--DM%20%2B%20LEAN-2E86AB)
![Type](https://img.shields.io/badge/Type-Supervised%20Regression-blueviolet)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## Table of Contents

- [Project Overview](#project-overview)
- [Business Context — Problem Statement Canvas](#business-context--problem-statement-canvas)
- [Key Results](#key-results)
- [Model Card](#model-card)
- [Model Performance](#model-performance)
- [Strategic Recommendations](#strategic-recommendations)
- [Business Impact Estimation](#business-impact-estimation)
- [Project Structure](#project-structure)
- [Tech Stack](#tech-stack)
- [How to Run](#how-to-run)
- [Deliverables](#deliverables)
- [MLOps Checklist](#mlops-checklist)
- [CRISP-DM Roadmap](#crisp-dm-roadmap)
- [Data Source](#data-source)
- [Credits](#credits)
- [License](#license)

---

## Project Overview

This project builds a supervised regression model to predict `avg_ticket`
(average purchase amount per customer, in CLP) for PequeShop — a Chilean
children's e-commerce business selling across MercadoLibre and Shopify.

The analysis moves beyond statistical inference (project-4b) to predictive
modeling: given a customer's platform, segment, and behavioral data, how much
will they spend? The model output enables personalized marketing offers,
optimized retargeting budget allocation, and differentiated channel strategies.

> **Lean principle — no re-work:** Data preparation was completed in
> `project-2-pequeshop-analytics`. EDA was completed in `project-3-eda-pequeshop`.
> Feature selection was statistically validated in `project-4b-pequeshop-statistical-inference`
> (H1–H4, α=0.05). This project builds directly on those outputs.

**What I learned:** Supervised regression pipeline end-to-end — train/test split,
K-Folds cross-validation, OneHotEncoder, StandardScaler, Linear Regression,
Polynomial Regression, KNN Regressor, Ridge, Lasso, GradientBoostingRegressor,
GridSearchCV, MAE/MSE/RMSE/R²/MAPE, MLOps artifact management, and translating
model output into evidence-based business decisions.

> **Dataset note:** The M6 consigna requests features such as age and site
> behavior. PequeShop does not have these — equivalent behavioral proxies are used:
> `total_transactions` and `total_revenue` (behavior), `retargeting_segment` and
> `primary_platform` (demographic/behavioral). Target variable `avg_ticket`
> correctly maps to "monto promedio de compra". See Decisions Log #7 in notebook 01.

---

## Business Context — Problem Statement Canvas

| Element | Content |
|---------|---------|
| **Business Problem** | PequeShop cannot personalize marketing offers — all customers receive the same promotions despite significantly different spending behavior across platforms and segments |
| **Business Impact** | avg_ticket deviates significantly from $25,000 CLP benchmark (H1: t=7.80, p<0.001) · Churn exceeds 30% threshold (H3: z=5.18, p<0.001) · ML and Shopify tickets differ (H2: t=2.27, p=0.024) · ~45 customers lost per cycle without targeted retention |
| **Decision to Support** | (1) Which customers receive high-value retention offers vs standard promotions? (2) How to concentrate retargeting/ads budget on customers with high predicted avg_ticket — improving promotion ROI |
| **Analytical Question** | Can we predict avg_ticket per customer from platform, behavioral, and segment data with sufficient accuracy to justify personalized marketing investment? |
| **Success Metrics** | R² > 0.70 · MAPE < 20% · RMSE < 20% of mean avg_ticket · MAE improvement > 20% over mean-predictor baseline |
| **Proposed Approach** | Supervised regression: Linear → Ridge/Lasso → GradientBoosting. Features pre-selected using project-4b statistical evidence |

---

## Key Results

| Metric | Baseline (mean predictor) | Best Model (GradientBoosting) | Improvement |
|--------|--------------------------|-------------------------------|-------------|
| R² test | 0.00 | **0.977** | +0.977 |
| MAE test (CLP) | ~8,000 | **1,185** | −85% |
| RMSE test (CLP) | ~8,500 | **1,668** | −80% |
| MAPE test (%) | — | **3.7%** | Model predicts within ~4% ✅ |

> Results obtained by executing notebooks 01–06 in order.
> GradientBoosting significantly outperformed all linear models — R²=0.977 vs R²≈0.53 for Linear/Ridge/Lasso.

**Customer Segmentation from Model Output:**

| Segment | Criterion | Customers (test set) | Action |
|---------|-----------|---------------------|--------|
| High Value | Predicted avg_ticket ≥ mean + 0.5σ | 29% (n=23) | Premium offers + priority ads |
| Medium Value | mean − 0.5σ ≤ predicted < mean + 0.5σ | 40% (n=31) | Standard promotions |
| Low Value | Predicted avg_ticket < mean − 0.5σ | 31% (n=24) | Re-engagement campaigns |

---

## Model Card

| Field | Details |
|-------|---------|
| **Model type** | GradientBoostingRegressor (ensemble of decision trees) |
| **Task** | Supervised Regression |
| **Training data** | PequeShop synthetic dataset — 392 customers, 1,192 transactions (March 2026) |
| **Features used** | 4 features: `primary_platform` (encoded), `retargeting_segment` (encoded), `total_transactions` (scaled), `total_revenue` (scaled) |
| **Target variable** | `avg_ticket` — average purchase amount per customer (CLP) |
| **Excluded feature** | `nps_category` — H4 not rejected (F=0.25, p=0.780); no predictive value confirmed |
| **Framework** | scikit-learn 1.3+ |
| **Training date** | March 2026 |
| **Artifact** | `models/model_final_v1.pkl` |

---

## Model Performance

| Metric | Description | Value |
|--------|-------------|-------|
| MAE (CLP) | Mean Absolute Error | **1,185** |
| MSE (CLP²) | Mean Squared Error | **2,782,253** |
| RMSE (CLP) | Root Mean Squared Error | **1,668** |
| R² | Variance explained | **0.977** |
| MAPE (%) | Mean Absolute % Error ➕ | **3.7%** |

> **Baseline:** Mean predictor (R² = 0.00) — all models must beat this.
> **MAPE note:** Added as extra metric beyond consigna requirements.
> Expresses error as percentage of actual value — more intuitive for business communication.

### Model Comparison (all models evaluated)

| Model | R² test | Overfit gap | Notes |
|-------|---------|-------------|-------|
| Baseline (mean) | 0.00 | — | Floor benchmark |
| Linear Regression | 0.527 | 0.152 | Interpretable baseline |
| Lasso (optimized) | 0.528 | 0.150 | L1 + feature selection |
| Ridge (optimized) | 0.537 | 0.141 | L2 regularization |
| KNN (optimized) | 0.721 | 0.167 | Distance-based contrast (L5) |
| Polynomial (degree=2) | 0.836 | 0.064 | Non-linear extension |
| **GradientBoosting** | **0.977** | **0.020** | **Final model ✅** |

> Execute notebook 05 for complete comparison table with GridSearchCV results.

---

## Strategic Recommendations

| Priority | Finding | Recommended Action | Evidence |
|----------|---------|-------------------|---------|
| **HIGH** | Churn exceeds 30% benchmark | Launch retention campaign targeting Dormant segment — concentrate budget on High Value customers | H3: z=5.18, p<0.001 + model segmentation |
| **HIGH** | avg_ticket differs significantly from $25k benchmark | Review pricing strategy vs Chilean e-commerce market | H1: t=7.80, p<0.001 |
| **MEDIUM** | MercadoLibre and Shopify tickets differ significantly | Develop differentiated pricing and promotion strategy per channel | H2: t=2.27, p=0.024 + feature importance |
| **LOW/HOLD** | NPS does not predict avg_ticket | Do not invest in NPS-based pricing segmentation — no statistical or ML evidence | H4: F=0.25, p=0.780 + Lasso coefficient = 0 |

> **Lean rule:** Only statistically and model-confirmed signals justify business investment.

> **Future enhancement:** Price analytics and price elasticity of demand (∂Q/∂P)
> would quantify: *"If we reduce price by 10%, does avg_ticket increase enough
> to justify the margin loss?"* Connecting directly to retargeting ROI decisions.

---

## Business Impact Estimation

| Scenario | Current State | Target | Estimated Impact |
|----------|--------------|--------|-----------------|
| Churn reduction | ~41% churn (Dormant segment) | Reduce to 30% benchmark | ~45 customers retained per cycle |
| Retargeting ROI | Uniform ad spend across all customers | Concentrate on High Value segment (~32%) | Reduce wasted ad spend on low-predicted-value customers |
| Channel optimization | Undifferentiated pricing ML vs Shopify | Platform-specific promotions | Potential avg_ticket uplift on lower-performing channel |

> **Methodology:** Estimates based on n=392 synthetic customers and project-4b hypothesis test results.
> **Assumptions:** Linear retention response; no cross-channel cannibalization.
> **Limitation:** Dataset is synthetic — effects may differ with real Tuttycosas Kids data.

---

## Project Structure

```
project-5-ecommerce-spend-prediction/
├── data/
│   ├── raw/                       # Original data (never modify)
│   ├── processed/                 # customers_final.csv, transactions_final.csv
│   └── final/                     # features_final.csv (encoded + scaled)
├── models/
│   ├── preprocessor_v1.pkl        # ColumnTransformer (OneHotEncoder + StandardScaler)
│   ├── model_lr_v1.pkl            # Linear Regression
│   ├── model_poly_v1.pkl          # Polynomial Regression (degree=2)
│   ├── model_knn_v1.pkl           # KNN Regressor (k=5)
│   ├── model_knn_optimized_v1.pkl # KNN optimized via GridSearchCV
│   ├── model_ridge_v1.pkl         # Ridge optimized via GridSearchCV
│   ├── model_lasso_v1.pkl         # Lasso optimized via GridSearchCV
│   ├── model_gb_v1.pkl            # GradientBoosting optimized
│   ├── model_final_v1.pkl         # Final selected model
│   └── model_card.md              # Model metadata
├── notebooks/
│   ├── 01_business_understanding.ipynb  # L1 — Problem Canvas, Classification vs Regression
│   ├── 02_data_understanding.ipynb      # L2 — Train/test split, K-Folds CV
│   ├── 03_data_preparation.ipynb        # L3 — Encoding, scaling, feature matrix
│   ├── 04_modeling.ipynb                # L4+L5 — Linear, Polynomial, KNN
│   ├── 05_evaluation.ipynb              # L6+L7 — Metrics, GridSearchCV, Ridge, Lasso
│   └── 06_deployment.ipynb              # L8 — GradientBoosting, forecast, segmentation
├── reports/
│   ├── figures/                   # All generated visualizations
│                
├── docs/
│   ├── METHODOLOGY.md
│   ├── data_dictionary.md
│   ├── decisions_log.md
│   └── lean_retrospective.md
├── src/
├── requirements.txt
├── .gitignore
└── README.md
```

### CRISP-DM Phase Mapping

| Notebook | CRISP-DM Phase | Lessons | Scope |
|----------|---------------|---------|-------|
| 01 | Business Understanding | L1 | Problem Statement Canvas · Classification vs Regression · ML Pipeline · No re-work principle |
| 02 | Data Understanding | L2 | Train/test split 80/20 · K-Folds k=5 · Overfitting/underfitting diagnosis |
| 03 | Data Preparation | L3 | OneHotEncoder · StandardScaler · Feature matrix assembly · Preprocessor saved as .pkl |
| 04 | Modeling | L4 + L5 | Linear · Polynomial (deg=2) · KNN Regressor · Baseline · Coefficient interpretation |
| 05 | Evaluation | L6 + L7 | MAE · MSE · RMSE · R² · MAPE · GridSearchCV · Ridge · Lasso · Model comparison |
| 06 | Deployment | L8 | GradientBoosting · Final model · avg_ticket forecast · 3-tier segmentation · Business recommendations |

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.12 | Core language |
| Pandas | Data manipulation and feature engineering |
| NumPy | Numerical operations, bootstrap simulation |
| scikit-learn | ML pipeline — preprocessing, models, GridSearchCV, metrics |
| SciPy | Statistical tests (inherited from project-4b) |
| Matplotlib | Custom visualizations |
| Seaborn | Distribution and comparison plots |
| joblib | Model artifact serialization (.pkl) |

**Skills Demonstrated:**
`Python` · `Supervised ML` · `Regression` · `Feature Engineering` · `Cross-Validation` · `GridSearchCV` · `Ridge` · `Lasso` · `GradientBoosting` · `scikit-learn` · `MLOps` · `CRISP-DM` · `Lean Thinking` · `Business Analytics` · `Decision Science`

---

## How to Run

```bash
git clone https://github.com/joselopezp/bootcamp-data-science-portfolio.git
cd projects/project-5-ecommerce-spend-prediction
python -m venv .venv
.venv\Scripts\activate          # Windows
pip install -r requirements.txt
jupyter notebook notebooks/01_business_understanding.ipynb
```

> ⚠️ Dataset is synthetic — `customers_final.csv` and `transactions_final.csv`
> are included in `data/processed/`. No external download required.
> Run notebooks in order: 01 → 02 → 03 → 04 → 05 → 06.
> Notebook 03 must be executed before 04-06 to generate `preprocessor_v1.pkl`.

---

## Deliverables

- [x] 6 notebooks following CRISP-DM + Lean structure (01–06)
- [x] Problem Statement Canvas (notebook 01)
- [x] Train/test split + K-Folds cross-validation (notebook 02)
- [x] Encoded and scaled feature matrix (notebook 03)
- [x] 4 regression models trained and compared (notebook 04)
- [x] Full metrics table — MAE, MSE, RMSE, R², MAPE (notebook 05)
- [x] GridSearchCV optimization — KNN, Ridge, Lasso (notebook 05)
- [x] GradientBoosting — final model (notebook 06)
- [x] avg_ticket forecast per customer — real vs predicted (notebook 06)
- [x] 3-tier customer segmentation with histogram (notebook 06)
- [x] Business recommendations in Lean priority order (notebook 06)
- [x] All model artifacts saved to `models/` folder
- [x] Visualizations in `reports/figures/`
- [x] PowerPoint presentation (technical audience, 6 slides, Spanish)
- [ ] Reporte técnico en PDF (pendiente)

---

## MLOps Checklist

### Reproducibility
- [x] Random seed fixed (`random_state=42`)
- [x] Requirements pinned (`requirements.txt`)
- [x] Preprocessor saved (`models/preprocessor_v1.pkl`)
- [x] Final model saved (`models/model_final_v1.pkl`)

### Model Versioning
- [x] All model artifacts saved to `models/` folder
- [x] Model filenames include version: `model_final_v1.pkl`
- [x] Training parameters logged in `docs/decisions_log.md`
- [x] Model card documented in `models/model_card.md`

### Monitoring (awareness level)
- [ ] Data drift: synthetic dataset — real-world Tuttycosas Kids data will differ
- [ ] Model limitations: n=392 synthetic customers; performance may degrade on real data
- [ ] Retraining trigger: when real transaction data from MercadoLibre is available

---

## CRISP-DM Roadmap

| Level | Question | Project | Module | Status |
|-------|----------|---------|--------|--------|
| Descriptive | What happened? | `project-2-pequeshop-analytics` | M3 — ETL | ✅ Complete |
| Diagnostic | Why did it happen? | `project-3-eda-pequeshop` | M4 — EDA | ✅ Complete |
| Inferential | Are the patterns statistically real? | `project-4b-pequeshop-statistical-inference` | M5 — Statistical Inference | ✅ Complete |
| Predictive | What will happen? | **`project-5-ecommerce-spend-prediction`** (this project) | M6 — Supervised ML | ✅ Complete |
| Prescriptive | Who are our customers? | `project-6-pequeshop-customer-segmentation` | M7 — Unsupervised ML | 🔲 Pending |

---

## Data Source

| Field | Details |
|-------|---------|
| **Dataset** | PequeShop synthetic e-commerce dataset |
| **Origin** | Generated in `project-2-pequeshop-analytics` (CRISP-DM Cycle 1) |
| **Records** | 392 customers · 1,192 transactions |
| **Columns** | customers: 15 · transactions: 19 |
| **Accessed** | March 2026 |

### How to Reproduce

> ⚠️ Data is synthetic — generated in project-2 and copied to `data/processed/`.
> No external source required. Full generation methodology documented in
> `project-2-pequeshop-analytics/`.

---

## Credits

**Data:** Synthetic dataset designed and generated by Jose Marcel Lopez Pino
as part of the PequeShop Analytics continuous case study, modeled after
real e-commerce behavior in the Chilean children's products market.

**Methodology References:**
- CRISP-DM: Chapman et al. (2000). *CRISP-DM 1.0: Step-by-step data mining guide*. SPSS Inc.
- Provost, F. & Fawcett, T. (2013). *Data Science for Business* (1st ed.). O'Reilly Media.
- Lean Thinking: Womack, J. & Jones, D. (1996). *Lean Thinking*. Simon & Schuster.
- Hastie, T., Tibshirani, R. & Friedman, J. (2009). *The Elements of Statistical Learning* (2nd ed.). Springer.
- scikit-learn: Pedregosa et al. (2011). *scikit-learn: Machine Learning in Python*. JMLR 12.

**Tools & Libraries:** See [Tech Stack](#tech-stack) section.

---

## License

MIT License — see [LICENSE](../../LICENSE) for details.

---

*Framework: CRISP-DM + Lean + DMAIC | Module 6 — Supervised Machine Learning*
*Jose Marcel Lopez Pino — Bootcamp Fundamentos de Ciencia de Datos, SENCE/Alkemy 2025-2026*
