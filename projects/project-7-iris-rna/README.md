# PROJECT 7: NEURAL NETWORK FOR IRIS CLASSIFICATION

![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![Framework](https://img.shields.io/badge/Framework-TensorFlow%202.21-FF6F00?logo=tensorflow&logoColor=white)
![Type](https://img.shields.io/badge/Type-Deep%20Learning-blueviolet)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow)

**Module:** 8 - Deep Learning Fundamentals  
**Bootcamp:** Fundamentos de Ciencia de Datos - SENCE Talento Digital & Alkemy (2025-2026)  
**Date:** March 2026

---

## Table of Contents

1. [Overview](#overview)
2. [Project Scope](#project-scope)
3. [Results](#results)
4. [Architecture](#architecture)
5. [Tech Stack](#tech-stack)
6. [How to Run](#how-to-run)
7. [Project Structure](#project-structure)
8. [Key Findings](#key-findings)
9. [Next Steps](#next-steps)
10. [Author](#author)

---

## Overview

This project is an **educational exercise focused exclusively on Phase 4 (MODELING)** of the data science workflow. The goal is to understand how **Dense Neural Networks (DNN)** work mechanically through hands-on implementation on the Iris dataset.

**Key Learnings:**
- How layers, neurons, and activation functions transform data
- Backpropagation and gradient descent optimization
- Hyperparameter tuning with GridSearchCV and RandomizedSearchCV
- Model evaluation metrics: Accuracy, F1-Score, Confusion Matrix

---

## Project Scope

### ✅ What This Project Covers

- Building Dense Neural Networks (DNN) from scratch using TensorFlow/Keras
- Understanding layers, neurons, and activation functions (ReLU, Softmax)
- Training with backpropagation and gradient descent
- Hyperparameter optimization: GridSearchCV (exhaustive) + RandomizedSearchCV (random sampling)
- Evaluation metrics: Accuracy, F1-Score, Confusion Matrix, Classification Report
- Model convergence analysis and overfitting detection

### ❌ What This Project Does NOT Cover

- Full CRISP-DM cycle (Phases 1-3, 5-6 skipped) — **only Phase 4 implemented**
- Exploratory Data Analysis (EDA) — Iris dataset is clean and well-known
- Feature engineering — Iris has 4 direct, interpretable measurements
- Convolutional Neural Networks (CNN) for images
- Recurrent Neural Networks (RNN) for sequences
- Production deployment and model serving

### Dataset

| Aspect | Details |
|--------|---------|
| **Source** | UCI Machine Learning Repository / Kaggle |
| **Size** | 150 samples |
| **Features** | 4 (SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm) |
| **Classes** | 3 (Iris-setosa, Iris-versicolor, Iris-virginica) |
| **Purpose** | Educational prototype for understanding DNN mechanics |
| **Quality** | Clean (no missing values, balanced classes: 50-50-50) |

---

## Results

### Model Performance

| Metric | Value |
|--------|-------|
| **Final Accuracy** | 96.67% |
| **F1-Score (weighted)** | 0.9666 |
| **Precision (avg)** | 0.97 |
| **Recall (avg)** | 0.97 |
| **Validation Samples** | 30 |
| **Misclassified** | 1 out of 30 |

### Comparison: Baseline vs. Optimized

| Model | Accuracy | Epochs | Config |
|-------|----------|--------|--------|
| **Baseline** | 80.00% | 20 | 16 → 8 → 3 |
| **GridSearchCV (best)** | 96.67% | 80 | 16 → 4 → 3 |
| **RandomizedSearchCV (best)** | 95.83% | 120 | 30 → 14 → 3 |
| **Final Model** | **96.67%** | **80** | **16 → 4 → 3** |

**Improvement:** +16.67% over baseline

### Confusion Matrix

```
                Setosa  Versicolor  Virginica
Setosa            10        0           0      ✅ Perfect
Versicolor         0        9           1      ⚠️ 1 misclassified
Virginica          0        0          10      ✅ Perfect
```

**Interpretation:**
- Setosa: 100% correct classification
- Versicolor: 90% correct (1 sample confused with Virginica)
- Virginica: 100% correct classification
- **Total error rate: 3.33% (1 error in 30 samples)**

---

## Architecture

### Final Neural Network Structure

```
Input Layer (4 features)
    ↓
Dense Layer 1: 16 neurons + ReLU activation
    ↓
Dense Layer 2: 4 neurons + ReLU activation
    ↓
Output Layer: 3 neurons + Softmax activation
    ↓
Output: Class probabilities [Setosa, Versicolor, Virginica]
```

### Training Configuration (Best)

| Parameter | Value |
|-----------|-------|
| **Hidden Units 1** | 16 |
| **Hidden Units 2** | 4 |
| **Batch Size** | 8 |
| **Epochs** | 80 |
| **Optimizer** | Adam (lr=0.001) |
| **Loss Function** | Sparse Categorical Crossentropy |
| **Train/Val Split** | 80/20 (stratified) |

### Hyperparameter Optimization

**GridSearchCV (Exhaustive Search):**
- Tested 16 combinations × 3-fold CV = 48 total trainings
- Best configuration found with 96.67% accuracy
- Execution time: ~3 minutes

**RandomizedSearchCV (Random Sampling):**
- Tested 10 random combinations × 3-fold CV = 30 total trainings
- Best configuration: 95.83% accuracy
- Execution time: ~3-8 minutes

---

## Tech Stack

### Core Libraries

| Library | Version | Purpose |
|---------|---------|---------|
| **Python** | 3.12 | Programming language |
| **NumPy** | 2.4.1 | Linear algebra, arrays |
| **Pandas** | 3.0.0 | Data manipulation, CSV loading |
| **Matplotlib** | 3.10.8 | Visualization (loss/accuracy plots) |

### Machine Learning & Deep Learning

| Library | Version | Purpose |
|---------|---------|---------|
| **TensorFlow** | 2.21.0 | Deep Learning framework |
| **Keras** | Integrated in TF | Neural network API |
| **Scikit-learn** | 1.8.0 | Preprocessing, metrics, model selection |
| **SciKeras** | 0.13.0 | Keras wrapper for sklearn (GridSearchCV integration) |
| **SciPy** | 1.17.0 | Statistical distributions (RandomizedSearchCV) |

### Development

| Tool | Version | Purpose |
|------|---------|---------|
| **Jupyter Lab** | 4.5.2 | Interactive notebook environment |
| **IPython** | 9.9.0 | Enhanced Python kernel |

---

## How to Run

### Prerequisites

- Python 3.12+
- Virtual environment activated
- All dependencies installed

### Installation

```bash
# Navigate to project directory
cd projects/project-7-iris-rna

# Activate virtual environment
.venv\Scripts\Activate.ps1  # Windows PowerShell
# or
source .venv/bin/activate  # macOS/Linux

# Install dependencies
pip install -r requirements.txt
```

### Execute Notebook

```bash
# Start Jupyter Lab
jupyter lab

# Open: notebooks/04_modeling.ipynb
# Execute cells top-to-bottom (Shift + Enter)
```

**Execution time:** ~15-20 minutes (GridSearchCV + RandomizedSearchCV are computationally intensive)

### Quick Verification

```python
# Test imports
python -c "import tensorflow; import scikeras; print('✅ All libraries ready')"
```

---

## Project Structure

```
project-7-iris-rna/
├── README.md                                    # This file
├── requirements.txt                             # Python dependencies
├── .gitignore                                   # Git rules
│
├── data/
│   ├── raw/
│   │   └── Iris.csv                             # Original dataset (150 samples)
│   ├── processed/                               # (Reserved for future use)
│   └── final/                                   # (Reserved for future use)
│
├── notebooks/
│   └── 04_modeling.ipynb                        # Main notebook (Phase 4: MODELING)
│
├── src/
│   └── __init__.py                              # Module initialization
│
└── reports/
    ├── executive/                               # Executive summaries (empty)
    └── figures/                                 # Visualizations (empty)
```

**Note:** Only Phase 4 (MODELING) is implemented. Phases 1-3 (Business Understanding, Data Understanding, Data Preparation) and Phases 5-6 (Evaluation, Deployment) are skipped because the Iris dataset is educational and well-known.

---

## Key Findings

### 1. Architecture Matters

Progressive compression (16 → 4 → 3 neurons) outperformed deeper architectures:
- Simple architecture: 16 → 4 → 3 achieved 96.67% ✅
- Deeper architecture: 30 → 14 → 3 achieved 95.83%

**Insight:** For tabular data with few features (4), simpler architectures generalize better.

### 2. Batch Size Impact

Smaller batch size (8) converged faster and achieved higher accuracy than larger batches (16):
- Batch 8: 96.67% accuracy
- Batch 16: Lower accuracy (from GridSearchCV results)

**Insight:** Smaller batches = more frequent weight updates = better convergence for small datasets.

### 3. Training Duration

80 epochs was optimal; no benefit from 120 epochs:
- 80 epochs: 96.67% (best)
- 120 epochs: No improvement observed
- 40 epochs: Lower accuracy

**Insight:** Validation loss plateaued after ~40-50 epochs; early stopping could be beneficial.

### 4. Hyperparameter Optimization Value

GridSearchCV + RandomizedSearchCV improved accuracy significantly:
- Baseline (manual config): 80.00%
- GridSearchCV optimized: 96.67%
- **Improvement: +16.67 percentage points**

**Insight:** Systematic hyperparameter search is essential for optimal performance.

---

## Next Steps

### Immediate (Project 7B)

**Build Convolutional Neural Networks (CNN) for image classification:**
- Dataset: Fashion-MNIST (70k images, 10 clothing categories)
- Goal: Understand CNN architecture (Conv2D, MaxPooling, Dense)
- Apply Deep Learning fundamentals from Project 7 to image data
- Expected accuracy: >90% on Fashion-MNIST validation set

### Medium Term (Project 8)

**Big Data Processing with Apache Spark:**
- Retail Analytics Pipeline (RetailMax case study)
- Apache Spark fundamentals: RDDs, DataFrames, SQL
- Scalable ML with MLlib: LogisticRegression, KMeans
- Integration of Phase 4 models into production pipelines

### Long Term (Post-Bootcamp)

**Real-World Application:**
- Transfer Learning on PequeShop children's clothing dataset (5-10 years)
- Custom CNN trained on actual product images
- Production deployment for e-commerce platform
- MLOps integration: MLflow, DVC, Docker, FastAPI

---

## 👤 Author

**José Marcel López Pino**  
Industrial Engineer (Business + Operations) | Data Science & Business Analytics

**Bootcamp:** Fundamentos de Ciencia de Datos — SENCE Talento Digital / Alkemy (2025–2026)

Industrial Engineer with a strong foundation in business and operations, currently developing end-to-end data science projects focused on solving real-world business problems and enabling data-driven decision-making.

### Academic Background

**Bachelor of Science in Industrial Engineering** (~5.5-year program, comparable in rigor to a U.S. M.S.)
- Rigorous quantitative foundation: Calculus, Linear Algebra, Probability & Statistics, Physics, Optimization
- Business & Operations: Strategy, Finance, Marketing, Economics, Operations Management, Technology Management
- **Thesis:** Volatility Forecasting of IPSA Stock Returns (Chilean Stock Exchange) using GJR-GARCH modeling

### Professional Context

15+ years of experience across academic management, business operations, and technical roles, with a career spanning mining, forestry, and industrial sectors, including work with companies such as BHP, Collahuasi, Codelco, and Arauco.

**Target Roles:** Data Scientist | Business Analyst | Analytics Consultant  
**Location:** Chile | Open to remote roles (Chile & globally) and relocation to the U.S., Canada, the U.K., or the Netherlands

**Certification Exam:** Scheduled for May 6, 2026 (Modules 1–11, 3-hour assessment)

---

## Contact & Portfolio

- **GitHub:** [github.com/joselopezp/bootcamp-data-science-portfolio](https://github.com/joselopezp/bootcamp-data-science-portfolio)
- **LinkedIn:** [linkedin.com/in/jose-lopez-pino/](https://www.linkedin.com/in/jose-lopez-pino/)

---

## License

This project is licensed under the MIT License.

© 2026 Jose Marcel Lopez Pino

---

## Acknowledgments

- **Dataset:** UCI Machine Learning Repository / Kaggle (Iris dataset by Ronald A. Fisher)
- **Framework:** TensorFlow/Keras by Google Brain
- **Methodology:** CRISP-DM + LEAN principles for efficient project execution
- **Bootcamp:** Fundamentos de Ciencia de Datos - SENCE Talento Digital & Alkemy

---

**Last Updated:** March 26, 2026  
**Status:** Phase 4 (MODELING) Complete ✅  
**Next Phase:** Project 7B (CNN for Fashion-MNIST)