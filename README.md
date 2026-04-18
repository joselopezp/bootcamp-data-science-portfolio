# Data Science Bootcamp Portfolio

> **Jose Lopez Pino** | Industrial Engineer → Data Scientist | Business Focus
> SENCE / Alkemy Data Science Bootcamp · 2025–2026

![Python](https://img.shields.io/badge/Python-3.12.10-3776AB?logo=python&logoColor=white)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-F7931E?logo=scikitlearn&logoColor=white)
![Big Data](https://img.shields.io/badge/Big%20Data-PySpark%20%7C%20AWS%20EMR-E25A1C?logo=apachespark&logoColor=white)
![Business Analytics](https://img.shields.io/badge/Focus-Business%20Analytics-4CAF50)
![Framework](https://img.shields.io/badge/Framework-CRISP--DM%20%2B%20LEAN-2E86AB)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

[🇪🇸 Versión en Español](#portafolio-del-bootcamp-de-ciencia-de-datos)

---

## Table of Contents

- [About This Portfolio](#about-this-portfolio)
- [Learning Approach: PBL + CBL](#learning-approach-pbl--cbl)
- [Projects (PBL)](#projects-pbl)
- [Case Studies (CBL)](#case-studies-cbl)
- [Methodology: CRISP-DM + Lean](#methodology-crisp-dm--lean)
- [Skills](#skills)
- [Author](#author)
- [License](#license)

---

## About This Portfolio

My Industrial Engineering background shaped a principle I've applied ever since —
in engineering, in business, and now in Data Science:

**Start with the problem. Not the data.**

---

Industrial Civil Engineering in Chile is a 5.5-year professional degree combining
business disciplines — strategy, finance, marketing, economics, operations, and
technology management — with rigorous quantitative training in statistics,
probability, optimization, linear algebra, and operations research.

That foundation developed one thing above all: a structured analytical mindset
focused on real decisions, not academic exercises.

My thesis put that to the test early. I built a **GJR-GARCH model to forecast
volatility of IPSA stock returns** (Bolsa de Santiago) — applying statistical
rigor to live financial markets before Data Science was part of my vocabulary.

---

The **Data Science Fundamentals Bootcamp** (SENCE / Alkemy, 2025–2026) modernized
and deepened that analytical base. Its value wasn't just theory — it was execution:
building real projects in Python and applying modern tools across the full analytics
stack.

Every project here follows the same chain of reasoning:

```
Business Problem → Decision to Support → Data → Model → Actionable Insight
```

Projects that start at "Model" look junior.  
Projects that start at "Business Problem" look senior.

> 📂 Post-bootcamp applied projects: [applied-data-science-portfolio](https://github.com/joselopezp/applied-data-science-portfolio)

---

## Learning Approach: PBL + CBL

This bootcamp integrated two complementary learning modalities:

**Project-Based Learning (PBL)** — End-to-end data products built across the full CRISP-DM lifecycle, from business understanding to deployment-ready artifacts. Each project inherits validated outputs from the previous one (no-rework principle).

**Case-Based Learning (CBL)** — Consulting-style analytical cases focused on applying specific techniques to real business problems. Shorter in scope, deeper in technical focus. Cases are documented in the [`cases/`](cases/) folder.

---

## Projects (PBL)

| Module | Project | Key Technique | Description | Status |
|:---|:---|:---|:---|:---:|
| 1 | *No project* | — | Orientation and Methodology | ✅ |
| 2 | [1. Contact Management System](projects/project-1-oop-contact-system) | OOP · CRUD | CRUD system with object-oriented design and encapsulation | ✅ |
| 3 | [2. Ecommerce PequeShop Analytics](projects/project-2-pequeshop-analytics) | ETL · KPIs | E-commerce ETL pipeline with business KPIs | ✅ |
| 4 | [3. Ecommerce PequeShop EDA](projects/project-3-eda-pequeshop) | EDA · OLS | Exploratory Data Analysis + OLS Regression | ✅ |
| 5 | [4. Student Health Analytics](projects/project-4-student-health-analytics) | Hypothesis Testing | Statistical inference over student habits data | ✅ |
|   | ⭐ **Bonus:** [PequeShop Statistical Inference](projects/project-4b-pequeshop-statistical-inference) | Inference · Effect Size | Statistical inference over customer data with effect sizes and CIs | ✅ |
| 6 | [5. Ecommerce PequeShop Spend Prediction](projects/project-5-ecommerce-spend-prediction) | Supervised ML · XGBoost | ML model to predict customer avg_ticket and drive marketing decisions | ✅ |
| 7 | [6. Ecommerce PequeShop Customer Segmentation](projects/project-6-unsupervised-ml) | KMeans · RFM | Unsupervised ML: RFM + KMeans customer segmentation | ✅ |
| 8 | [7. Deep Learning Fundamentals](projects/project-7-deep-learning) | CNN · TensorFlow | Neural Networks and CNNs for business classification | ✅ |
| 9 | [8. RetailMax — Retail Analytics Pipeline](projects/project-8-big-data-retailmax) | PySpark · AWS EMR | Big Data pipeline with PySpark, Spark SQL, MLlib + AWS EMR Serverless | ✅ |
| 10 & 11 | 9. Job Search Project | — | Portfolio curation, GitHub optimization, LinkedIn positioning | ✅ |

> **Note:** In addition to synchronous classes, personal study and project development were required outside scheduled sessions.

> ⭐ **Bonus** projects are self-initiated extensions developed beyond bootcamp requirements to deepen business understanding.

---

## Case Studies (CBL)

Consulting-style analytical cases applying specific techniques to focused business problems. Each case includes an executive summary and follows CRISP-DM + Lean principles.

| # | Case | Key Technique | Business Result | Status |
|:---:|:---|:---|:---|:---:|
| 1 | [ETL Quality — FinTech](https://github.com/joselopezp/bootcamp-data-science-portfolio/tree/main/cases/case-1-etl-quality-fintech) | Data Wrangling · ETL | Systemic ETL failure diagnosed — 87.96% record removal rate flagged | ✅ |
| 2 | [Mining Stock Returns](https://github.com/joselopezp/bootcamp-data-science-portfolio/tree/main/cases/case-2-mining-stock-returns) | NumPy · Vectorized Computing | BHP, FCX, RIO, VALE, SCCO returns — 426x speedup over pure Python | ✅ |
| 3 | [Mining Ops Data Consolidation](https://github.com/joselopezp/bootcamp-data-science-portfolio/tree/main/cases/case-3-mining-ops-data-consolidation) | Pandas · Multi-format Ingestion | Mining operations unified from CSV, Excel, and HTML sources | ✅ |
| 4 | [Used Car Price Prediction](https://github.com/joselopezp/bootcamp-data-science-portfolio/tree/main/cases/case-4-used-car-price-prediction) | Regression · Scikit-learn | Dealership pricing model — R²=0.9541, MAPE=6.74% | ✅ |
| 5 | [Retail Customer Preprocessing](https://github.com/joselopezp/bootcamp-data-science-portfolio/tree/main/cases/case-5-retail-customer-preprocessing) | Preprocessing Pipeline | Full imputation, encoding, and scaling pipeline for customer classifier | ✅ |
| 6 | [Clinical Dimensionality Reduction](https://github.com/joselopezp/bootcamp-data-science-portfolio/tree/main/cases/case-6-clinical-dimensionality-reduction) | PCA · t-SNE | PCA vs t-SNE for early-diagnosis pipeline — 95% variance in 10 components | ✅ |
| 7 | [Marketing Customer Segmentation](https://github.com/joselopezp/bootcamp-data-science-portfolio/tree/main/cases/case-7-marketing-customer-segmentation) | PCA · KMeans | Segment discovery for marketing — 2,240 customers, KL divergence=0.8887 | ✅ |
| 8 | [Workforce Income Segmentation](https://github.com/joselopezp/bootcamp-data-science-portfolio/tree/main/cases/case-8-workforce-income-segmentation) | PySpark · MLlib | Socioeconomic segmentation on UCI 1994 Census — AUC=0.9028, 4 segments | ✅ |
| 9 | [Spark SQL Retail Analytics](https://github.com/joselopezp/bootcamp-data-science-portfolio/tree/main/cases/case-9-spark-sql-retail-analytics) | Spark SQL · Catalyst | 1M RetailMax transactions queried in seconds — ~USD 500M revenue dataset | ✅ |

> Cases follow naming convention `case-N-business-context` and live in the `cases/` folder.
> Each case includes: `notebooks/`, `src/`, `data/`, `reports/`, and an executive summary in `reports/executive/`.

---

## Methodology: CRISP-DM + Lean

This portfolio adopts **CRISP-DM** as the primary framework due to its clarity, traceability, and strong alignment with business decision-making. CRISP-DM structures projects consistently from problem understanding to data preparation and actionable insights.

Complementarily, the approach incorporates **Lean principles**, prioritizing:

- Short, progressive iterations
- Early value delivery for business stakeholders
- Scope adjustment as data understanding improves
- No-rework: later projects inherit validated outputs from prior ones

This hybrid approach reflects how data projects develop in real contexts, where requirements evolve and decisions must balance analytical rigor with speed and pragmatism.

### Limitations and Flexibility

CRISP-DM is not applied rigidly. Depending on the context, industry, or type of problem, projects may:

- Stop at early phases (e.g., descriptive analysis or data preparation)
- Focus more deeply on specific stages such as modeling, evaluation, or deployment
- Adapt the methodology to other analytical approaches when required by the problem

The goal is to demonstrate **structured thinking, analytical judgment, and adaptability** when addressing data problems across different business contexts and industries.

---

## Skills

**ML & Modeling**
Supervised Learning (Regression, Classification) · Unsupervised Learning (Clustering, Dimensionality Reduction) · XGBoost · Boosting · Cross Validation · Model Evaluation · Feature Scaling · Scikit-learn

**Statistical Methods**
Statistical Inference · Hypothesis Testing · OLS Regression · Effect Sizes · Confidence Intervals · GARCH Volatility Modeling

**Data Engineering & Big Data**
ETL Pipelines · Data Wrangling · PySpark · Spark SQL · RDDs · Parquet · MLlib · AWS EMR Serverless · Scalable ML

**Deep Learning**
Neural Networks · Convolutional Neural Networks (CNN) · TensorFlow · SciKeras

**Data Analysis & Visualization**
Pandas · NumPy · Matplotlib · Seaborn · Exploratory Data Analysis

**Programming & Tools**
Python · SQL · Git · GitHub · Jupyter Notebook · VS Code · Google Colab · Python Virtual Environments

**Frameworks & Methodologies**
CRISP-DM · Lean Thinking · DMAIC · Business Analytics · Customer Analytics · PBL · CBL

---

## Author

**Jose Lopez Pino**
Industrial Engineer → Data Scientist | Business-First Approach

I combine engineering problem-solving discipline, business understanding,
quantitative reasoning, and modern Data Science tools to turn data into
decisions with measurable impact.

*Thesis: Volatility Forecasting of IPSA Stock Returns (Bolsa de Santiago) using a GJR-GARCH model.*

[![GitHub](https://img.shields.io/badge/GitHub-joselopezp-181717?style=flat&logo=github)](https://github.com/joselopezp)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-jose--lopez--pino-0077B5?style=flat&logo=linkedin)](https://www.linkedin.com/in/jose-lopez-pino/)
[![Portfolio](https://img.shields.io/badge/Portfolio-applied--ds--portfolio-4CAF50?style=flat&logo=github)](https://github.com/joselopezp/applied-data-science-portfolio)

📧 jose.lopezpino@gmail.com

---

## License

This portfolio is licensed under the [MIT License](LICENSE).

© 2026 Jose Lopez Pino

---
---

# Portafolio del Bootcamp de Ciencia de Datos

> **Jose Lopez Pino** | Ingeniero Civil Industrial → Científico de Datos | Enfoque en Negocios
> Bootcamp SENCE / Alkemy · 2025–2026

## Tabla de Contenidos

- [Acerca de este Portafolio](#acerca-de-este-portafolio)
- [Enfoque de Aprendizaje: PBL + CBL](#enfoque-de-aprendizaje-pbl--cbl)
- [Proyectos (PBL)](#proyectos-pbl)
- [Casos de Estudio (CBL)](#casos-de-estudio-cbl)
- [Metodología: CRISP-DM + Lean](#metodología-crisp-dm--lean)
- [Habilidades](#habilidades)
- [Autor](#autor)
- [Licencia](#licencia)

---

## Acerca de este Portafolio

Mi formación en Ingeniería Civil Industrial me enseñó un principio que aplico
desde entonces — en ingeniería, en negocios, y ahora en Ciencia de Datos:

**Empieza por el problema. No por los datos.**

---

La Ingeniería Civil Industrial en Chile es una carrera profesional de 5,5 años
que combina disciplinas de negocio — estrategia, finanzas, marketing, economía,
operaciones y gestión tecnológica — con una rigurosa formación cuantitativa en
estadística, probabilidad, optimización, álgebra lineal e investigación de
operaciones.

Esa base desarrolló principalmente una cosa: un pensamiento analítico estructurado,
enfocado en decisiones reales, no en ejercicios académicos.

Mi Memoria de Título lo puso a prueba temprano. Construí un **modelo GJR-GARCH
para pronosticar la volatilidad de acciones del IPSA** (Bolsa de Santiago) —
aplicando rigor estadístico a mercados financieros reales antes de que Ciencia
de Datos fuera parte de mi vocabulario.

---

El **Bootcamp de Fundamentos de Ciencia de Datos** (SENCE / Alkemy, 2025–2026)
modernizó y profundizó esa base analítica. Su valor no fue solo teoría — fue
ejecución: construir proyectos reales en Python y aplicar herramientas modernas
a lo largo del stack completo de analytics.

Cada proyecto aquí sigue la misma cadena de razonamiento:

```
Problema de Negocio → Decisión a Apoyar → Datos → Modelo → Insight Accionable
```

Los proyectos que empiezan en "Modelo" se ven junior.  
Los que empiezan en "Problema de Negocio" se ven senior.

> 📂 Proyectos aplicados post-bootcamp: [applied-data-science-portfolio](https://github.com/joselopezp/applied-data-science-portfolio)

---

## Enfoque de Aprendizaje: PBL + CBL

Este bootcamp integró dos modalidades de aprendizaje complementarias:

**Aprendizaje Basado en Proyectos (PBL)** — Productos de datos end-to-end construidos a lo largo del ciclo completo CRISP-DM, desde la comprensión del negocio hasta artefactos listos para despliegue. Cada proyecto hereda los outputs validados del anterior (principio de no retrabajo).

**Aprendizaje Basado en Casos (CBL)** — Casos analíticos de estilo consulting enfocados en aplicar técnicas específicas a problemas de negocio concretos. Más acotados en alcance, más profundos en enfoque técnico. Los casos están documentados en la carpeta [`cases/`](cases/).

---

## Proyectos (PBL)

| Módulo | Proyecto | Técnica Clave | Descripción | Estado |
|:---|:---|:---|:---|:---:|
| 1 | *Sin proyecto* | — | Orientación y metodología | ✅ |
| 2 | [1. Contact Management System](projects/project-1-oop-contact-system) | POO · CRUD | Sistema CRUD con diseño orientado a objetos y encapsulación | ✅ |
| 3 | [2. Ecommerce PequeShop Analytics](projects/project-2-pequeshop-analytics) | ETL · KPIs | Pipeline ETL de e-commerce con KPIs de negocio | ✅ |
| 4 | [3. Ecommerce PequeShop EDA](projects/project-3-eda-pequeshop) | EDA · OLS | Análisis Exploratorio de Datos + Regresión OLS | ✅ |
| 5 | [4. Student Health Analytics](projects/project-4-student-health-analytics) | Pruebas de Hipótesis | Inferencia estadística sobre hábitos de estudiantes | ✅ |
|   | ⭐ **Bonus:** [PequeShop Statistical Inference](projects/project-4b-pequeshop-statistical-inference) | Inferencia · Tamaño de Efecto | Inferencia estadística sobre clientes con tamaños de efecto e IC | ✅ |
| 6 | [5. Ecommerce PequeShop Spend Prediction](projects/project-5-ecommerce-spend-prediction) | ML Supervisado · XGBoost | Modelo ML para predecir avg_ticket y optimizar decisiones de marketing | ✅ |
| 7 | [6. Ecommerce PequeShop Customer Segmentation](projects/project-6-unsupervised-ml) | KMeans · RFM | ML No Supervisado: segmentación RFM + KMeans | ✅ |
| 8 | [7. Deep Learning Fundamentals](projects/project-7-deep-learning) | CNN · TensorFlow | Redes Neuronales y CNNs para clasificación aplicada a negocios | ✅ |
| 9 | [8. RetailMax — Retail Analytics Pipeline](projects/project-8-big-data-retailmax) | PySpark · AWS EMR | Pipeline Big Data con PySpark, Spark SQL, MLlib + AWS EMR Serverless | ✅ |
| 10 & 11 | 9. Proyecto Búsqueda Laboral | — | Curación de portafolio, optimización GitHub, posicionamiento LinkedIn | ✅ |

> **Nota:** Además de las clases sincrónicas, fue necesario estudio personal y desarrollo de proyectos fuera de las sesiones programadas.

> ⭐ Los proyectos **Bonus** son extensiones de iniciativa propia desarrolladas más allá de los requisitos del bootcamp para profundizar el entendimiento del negocio.

---

## Casos de Estudio (CBL)

Casos analíticos de estilo consulting que aplican técnicas específicas a problemas de negocio focalizados. Cada caso incluye un resumen ejecutivo y sigue los principios CRISP-DM + Lean.

| # | Caso | Técnica Clave | Resultado de Negocio | Estado |
|:---:|:---|:---|:---|:---:|
| 1 | [Calidad ETL — FinTech](https://github.com/joselopezp/bootcamp-data-science-portfolio/tree/main/cases/case-1-etl-quality-fintech) | Data Wrangling · ETL | Falla sistémica diagnosticada — tasa de eliminación 87,96% | ✅ |
| 2 | [Retornos Acciones Mineras](https://github.com/joselopezp/bootcamp-data-science-portfolio/tree/main/cases/case-2-mining-stock-returns) | NumPy · Cómputo Vectorizado | BHP, FCX, RIO, VALE, SCCO — aceleración 426x vs Python puro | ✅ |
| 3 | [Consolidación Datos Mineros](https://github.com/joselopezp/bootcamp-data-science-portfolio/tree/main/cases/case-3-mining-ops-data-consolidation) | Pandas · Ingesta Multi-formato | Datos operacionales unificados desde CSV, Excel y HTML | ✅ |
| 4 | [Predicción Precio Vehículos Usados](https://github.com/joselopezp/bootcamp-data-science-portfolio/tree/main/cases/case-4-used-car-price-prediction) | Regresión · Scikit-learn | Modelo de precios para concesionaria — R²=0,9541, MAPE=6,74% | ✅ |
| 5 | [Preprocesamiento Clientes Retail](https://github.com/joselopezp/bootcamp-data-science-portfolio/tree/main/cases/case-5-retail-customer-preprocessing) | Pipeline Preprocesamiento | Imputación, encoding y escalado completo para clasificador de clientes | ✅ |
| 6 | [Reducción Dimensionalidad Clínica](https://github.com/joselopezp/bootcamp-data-science-portfolio/tree/main/cases/case-6-clinical-dimensionality-reduction) | PCA · t-SNE | PCA vs t-SNE para diagnóstico temprano — 95% varianza en 10 componentes | ✅ |
| 7 | [Segmentación Clientes Marketing](https://github.com/joselopezp/bootcamp-data-science-portfolio/tree/main/cases/case-7-marketing-customer-segmentation) | PCA · KMeans | Descubrimiento de segmentos — 2.240 clientes, KL divergence=0,8887 | ✅ |
| 8 | [Segmentación Socioeconómica Laboral](https://github.com/joselopezp/bootcamp-data-science-portfolio/tree/main/cases/case-8-workforce-income-segmentation) | PySpark · MLlib | Segmentación censo UCI 1994 — AUC=0,9028, 4 segmentos | ✅ |
| 9 | [Spark SQL Analytics Retail](https://github.com/joselopezp/bootcamp-data-science-portfolio/tree/main/cases/case-9-spark-sql-retail-analytics) | Spark SQL · Catalyst | 1M transacciones en segundos — ~USD 500M en ventas RetailMax | ✅ |

> Los casos siguen la convención `case-N-contexto-negocio` y están en la carpeta `cases/`.
> Cada caso incluye: `notebooks/`, `src/`, `data/`, `reports/` y resumen ejecutivo en `reports/executive/`.

---

## Metodología: CRISP-DM + Lean

Este portafolio adopta **CRISP-DM** como marco principal de trabajo debido a su claridad, trazabilidad y fuerte alineación con la toma de decisiones de negocio. CRISP-DM permite estructurar los proyectos de forma consistente desde la comprensión del problema hasta la generación de insights accionables.

De manera complementaria, el enfoque incorpora **principios Lean**, priorizando:

- Iteraciones cortas y progresivas
- Entregables con valor temprano para el negocio
- Ajuste del alcance a medida que crece el entendimiento de los datos
- No retrabajo: los proyectos posteriores heredan los outputs validados de los anteriores

Este enfoque híbrido refleja cómo se desarrollan los proyectos de datos en contextos reales, donde los requerimientos evolucionan y las decisiones deben balancear rigor analítico con velocidad y pragmatismo.

### Limitaciones y Flexibilidad

CRISP-DM no se aplica de forma rígida. Dependiendo del contexto, industria o tipo de problema, los proyectos pueden:

- Detenerse en fases tempranas (análisis descriptivo o preparación de datos)
- Profundizar en etapas específicas como modelado, evaluación o despliegue
- Adaptar la metodología a otros enfoques analíticos cuando el problema lo requiera

El objetivo es demostrar **pensamiento estructurado, criterio analítico y capacidad de adaptación** al abordar problemas de datos en distintos contextos empresariales e industrias.

---

## Habilidades

**ML y Modelado**
Aprendizaje Supervisado (Regresión, Clasificación) · Aprendizaje No Supervisado (Clustering, Reducción de Dimensionalidad) · XGBoost · Boosting · Validación Cruzada · Evaluación de Modelos · Escalado de Variables · Scikit-learn

**Métodos Estadísticos**
Inferencia Estadística · Pruebas de Hipótesis · Regresión OLS · Tamaños de Efecto · Intervalos de Confianza · Modelos GARCH de Volatilidad

**Ingeniería de Datos y Big Data**
Pipelines ETL · Data Wrangling · PySpark · Spark SQL · RDDs · Parquet · MLlib · AWS EMR Serverless · ML Escalable

**Deep Learning**
Redes Neuronales · Redes Neuronales Convolucionales (CNN) · TensorFlow · SciKeras

**Análisis y Visualización de Datos**
Pandas · NumPy · Matplotlib · Seaborn · Análisis Exploratorio de Datos

**Programación y Herramientas**
Python · SQL · Git · GitHub · Jupyter Notebook · VS Code · Google Colab · Entornos Virtuales Python

**Frameworks y Metodologías**
CRISP-DM · Lean Thinking · DMAIC · Business Analytics · Customer Analytics · PBL · CBL

---

## Autor

**Jose Lopez Pino**
Ingeniero Civil Industrial → Científico de Datos | Enfoque Business-First

Combino disciplina de ingeniería, comprensión de negocios, razonamiento
cuantitativo y herramientas modernas de Ciencia de Datos para convertir
datos en decisiones con impacto medible.

*Memoria de Título: Pronóstico de Volatilidad de acciones del IPSA (Bolsa de Santiago) usando un modelo GJR-GARCH.*

[![GitHub](https://img.shields.io/badge/GitHub-joselopezp-181717?style=flat&logo=github)](https://github.com/joselopezp)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-jose--lopez--pino-0077B5?style=flat&logo=linkedin)](https://www.linkedin.com/in/jose-lopez-pino/)
[![Portafolio](https://img.shields.io/badge/Portafolio-applied--ds--portfolio-4CAF50?style=flat&logo=github)](https://github.com/joselopezp/applied-data-science-portfolio)

📧 jose.lopezpino@gmail.com

---

## Licencia

Este portafolio está licenciado bajo la [Licencia MIT](LICENSE).

© 2026 Jose Lopez Pino
