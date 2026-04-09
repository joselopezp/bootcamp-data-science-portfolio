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
| **Business Unit** | Departamento de Analítica y Machine Learning |
| **Stakeholder** | Marketing Director, RetailMax |
| **Decision to Support** | Identificar qué clientes deben recibir ofertas de retención personalizadas vs. promociones estándar, y qué segmentos priorizar para campañas de marketing. |

> **Situation:** RetailMax procesa millones de transacciones diarias en su plataforma e-commerce, pero su proceso analítico es lento y fragmentado — datos almacenados en múltiples sistemas y modelos de ML tradicionales que no escalan. Las decisiones de marketing se basan en datos muestreados, perdiendo patrones en segmentos de clientes de cola larga. Se requiere un pipeline de Big Data escalable que unifique las fuentes de datos y genere insights accionables.

---

## 2. Problem Statement

> Construir un pipeline escalable de Big Data + Machine Learning que clasifique clientes por valor y los segmente para campañas de marketing dirigidas, procesando más de 2 millones de registros de transacciones, reseñas y comportamiento de navegación.

**Business Impact if Unresolved:**
- 15–25% de desperdicio en presupuesto de retención por campañas no segmentadas
- El 19% de los clientes de alto ticket están insatisfechos (review promedio 2.1/5) — riesgo de churn de ~$5.2M
- El 77% de los clientes compran una sola vez — oportunidad de reactivación no aprovechada

---

## 3. Analytical Approach

> Se construyó un pipeline completo de Big Data utilizando Apache Spark, desde la ingesta de datos hasta la generación de modelos de ML escalables, siguiendo las 6 fases de CRISP-DM.

| Step | Description |
|---|---|
| **Data** | Brazilian E-Commerce (Olist, Kaggle) — 9 tablas, ~100K órdenes, 2016–2018. Complementado con 500K eventos de navegación sintéticos generados con `spark.range()`. Total: 2,055,860 registros. |
| **Method** | RDD transformations + Spark SQL para métricas de negocio. Logistic Regression (clasificación High/Low Value) + K-Means (segmentación de clientes, K=4). |
| **Tool** | Python 3.12 · PySpark 4.1.1 · Spark MLlib · Java 17 Temurin · Parquet |
| **Validation** | AUC-ROC para clasificación, Silhouette Score + Elbow Method para clustering. Métricas contrastadas contra targets del Problem Statement Canvas. |

---

## 4. Key Findings

> Tres hallazgos principales siguiendo: **Contexto → Análisis → Insight → Decisión**

### Finding 1 — El 77% de los clientes son compradores únicos satisfechos
- **Context:** RetailMax tiene una base de clientes predominantemente de una sola compra.
- **Analysis:** Cluster 0 ("One-time Satisfied"): 72,013 clientes, ticket promedio $112, review promedio 4.6/5.
- **Insight:** Estos clientes tuvieron una buena experiencia pero no volvieron — no es un problema de satisfacción, sino de falta de estímulo para la recompra.
- **Possible Decision:** Lanzar campaña de reactivación personalizada 30 días post-primera compra. Una conversión del 5% generaría ~3,600 clientes recurrentes (~$400K adicionales).

### Finding 2 — Los clientes de alto ticket son los más insatisfechos
- **Context:** El 19% de los clientes gasta significativamente más que el promedio.
- **Analysis:** Cluster 3 ("High-ticket Critics"): 17,911 clientes, ticket promedio $290, review promedio 2.1/5 — el más bajo de todos los segmentos.
- **Insight:** Los clientes que más gastan son los que peor experiencia reportan. Probablemente hay un problema de expectativa vs. entrega en productos premium.
- **Possible Decision:** Programa de recuperación de servicio — follow-up personalizado dentro de 48h para órdenes con review ≤ 2. El ROI es alto: estos clientes gastan 2.6x el promedio.

### Finding 3 — Los clientes leales son escasos pero valiosos
- **Context:** Solo el 0.8% de los clientes hace compras repetidas sostenidas.
- **Analysis:** Cluster 1 ("Loyal Repeaters"): 703 clientes, 2.3 órdenes promedio, lifespan de 256 días, review 4.3/5.
- **Insight:** Este micro-segmento representa el perfil ideal de cliente. Su comportamiento es replicable si se entienden los drivers de lealtad.
- **Possible Decision:** Crear programa VIP (envío gratis, acceso anticipado, rewards). Estudiar qué categorías y tiempos de compra caracterizan a este grupo para replicar el patrón.

---

## 5. Business Recommendations

| Priority | Recommendation | Expected Impact | Effort |
|---|---|---|---|
| 🔴 High | Programa de recuperación de servicio para High-ticket Critics (19%) | Mitigar ~$5.2M en riesgo de churn; mejorar review de 2.1 a 3.5+ | Medium |
| 🔴 High | Campaña de reactivación para One-time Satisfied (77%) | ~$400K en revenue adicional (5% de conversión a recompra) | Low |
| 🟡 Medium | Bundles y descuentos por volumen para Multi-item Buyers (3%) | Incrementar basket de $370 a $450 (+22%) | Medium |
| 🟢 Low | Programa VIP para Loyal Repeaters (0.8%) | Retener 95%+ del segmento más valioso; modelo para escalar lealtad | Low |

---

## 6. Limitations

- **Data:** Dataset Olist es de 2016–2018 — patrones de comportamiento pueden diferir en 2026.
- **Model:** Logistic Regression asume relación lineal entre features y probabilidad — modelos como GBT podrían mejorar AUC.
- **Scope:** Clickstream es sintético — datos reales de navegación mejorarían la calidad de features. Pipeline validado solo en modo local — validación en cloud pendiente.
- **Target:** "High Value" definido como avg_ticket > mediana — el negocio debe validar este umbral.

---

## 7. Next Steps

| Horizon | Action |
|---|---|
| **Immediate** | Entregar reporte de segmentos al equipo de marketing para diseño de campañas Q2 2026. |
| **Short-term** | Validar pipeline en Google Colab (entorno cloud) antes del 10 de abril de 2026. |
| **Post-certification** | Validación en AWS EMR Serverless + dashboard interactivo en Power BI para el equipo de marketing. |
| **Long-term** | Integrar datos reales de clickstream + modelo BG/NBD de lifetime value. Conectar con el arco prescriptivo de PequeShop. |

---

*Framework: CRISP-DM + LEAN | Methodology: Project-Based Learning (PBL)*

**Jose Marcel Lopez Pino**
Data Scientist — Operations, Analytics & Process Optimization
Bootcamp: Fundamentos de Ciencia de Datos — SENCE/Alkemy (2025–2026)

[![GitHub](https://img.shields.io/badge/GitHub-joselopezp-181717?style=flat&logo=github)](https://github.com/joselopezp)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-jose--lopez--pino-0077B5?style=flat&logo=linkedin)](https://www.linkedin.com/in/jose-lopez-pino/)
