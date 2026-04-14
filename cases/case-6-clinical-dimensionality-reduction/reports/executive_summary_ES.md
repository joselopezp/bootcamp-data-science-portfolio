# 66% Menos Variables, Mismo Poder Diagnóstico: PCA vs t-SNE para Pipelines ML Clínicos
### Reducción de Dimensionalidad — DataMed Analytics, Diagnóstico Temprano Neurológico | CRISP-DM + LEAN

**Autor:** Jose Marcel Lopez Pino
**Rol:** Data Scientist — Operaciones, Analytics & Optimización de Procesos
**Framework:** CRISP-DM + LEAN | Aprendizaje Basado en Casos (CBL)
**Módulo:** M7 — Machine Learning No Supervisado (Bootcamp Alkemy)
**Fecha:** Abril 2026
**Estado:** ✅ Completo

---

## Conclusión Ejecutiva

PCA reduce 30 variables clínicas a 10 componentes reteniendo el **95% de la información** — una reducción del 66% en dimensionalidad que se traduce directamente en menor tiempo de entrenamiento, menor riesgo de sobreajuste y menor costo computacional. t-SNE produce separación visual superior entre casos malignos y benignos (KL divergence = 0,9658), pero es estructuralmente incompatible con pipelines de producción. Recomendación: **PCA para el pipeline predictivo, t-SNE para presentaciones al equipo clínico**. El análisis fue realizado sobre el dataset Wisconsin Breast Cancer (569 pacientes, 30 variables) como proxy clínico análogo al dataset neurológico real de DataMed Analytics.

---

## 1. Contexto de Negocio

| | |
|---|---|
| **Industria** | Salud / Analytics Clínico |
| **Unidad de Negocio** | Data Science — Estudios Neurológicos |
| **Stakeholder** | Líder de Data Science / Equipo de Visualización Clínica |
| **Decisión a Apoyar** | Seleccionar la técnica de reducción de dimensionalidad a integrar en el pipeline de clasificación para diagnóstico temprano |

> **Situación:** DataMed Analytics está desarrollando un modelo de clasificación para diagnóstico temprano de enfermedades neurodegenerativas usando un dataset clínico con más de 100 variables por paciente. El equipo de data science ha identificado tres problemas críticos: sobreajuste del modelo, tiempos de entrenamiento lentos y baja interpretabilidad. La reducción de dimensionalidad es requerida antes del plazo de entrega al centro clínico en dos semanas.

---

## 2. Problema

> ¿Qué técnica de reducción de dimensionalidad — PCA o t-SNE — responde mejor a los requerimientos del pipeline de DataMed Analytics: máxima retención de varianza, separabilidad de clases y compatibilidad con modelado predictivo downstream?

**Impacto si no se resuelve:**
- Los modelos de clasificación entrenados sobre 100+ variables correlacionadas sufrirán sobreajuste, produciendo diagnósticos tempranos poco confiables y aumentando el riesgo clínico
- Sin reducción de dimensionalidad, el tiempo de entrenamiento y los costos de memoria escalan cuadráticamente — bloqueando el compromiso de entrega en dos semanas

---

## 3. Enfoque Analítico

| Aspecto | Detalle |
|---|---|
| **Datos** | Dataset Wisconsin Breast Cancer (UCI / sklearn) — 569 pacientes, 30 variables numéricas, target binario clínico (Maligno / Benigno). Proxy análogo clínicamente al dataset neurológico real |
| **Método** | Normalización StandardScaler → PCA (análisis de varianza + proyección 2D + loadings de variables) → t-SNE (visualización de clusters) → análisis comparativo |
| **Herramienta** | Python · scikit-learn 1.8.0 · NumPy · pandas · Matplotlib · Seaborn |
| **Validación** | PCA: curva de varianza explicada acumulada. t-SNE: KL divergence (umbral < 1,0). Inspección visual de separación de clases en proyecciones 2D |

---

## 4. Hallazgos Principales

### Hallazgo 1 — PCA comprime 30 variables a 10 componentes reteniendo el 95% de la información

- **Contexto:** El dataset clínico tiene 30 variables numéricas correlacionadas derivadas de mediciones de núcleos celulares. Alta multicolinealidad es esperada en baterías de medición clínica.
- **Análisis:** PC1 solo explica el 44,3% de la varianza total; PC1+PC2 juntos explican el 63,2%. Exactamente 10 componentes son necesarios para retener el 95% de la varianza total — una reducción del 66% de 30 a 10 dimensiones.
- **Insight:** El dataset es altamente compresible. El codo pronunciado del scree plot después de PC3 confirma estructura latente fuerte — típico de datasets clínicos donde las correlaciones biológicas dominan las relaciones entre variables.
- **Decisión posible:** Establecer `PCA(n_components=10)` como primer paso obligatorio en el pipeline de clasificación, antes de cualquier entrenamiento de clasificador.

### Hallazgo 2 — Las variables de forma y tamaño celular son los principales impulsores de PC1

- **Contexto:** El equipo clínico necesita entender qué variables originales preserva mejor la transformación PCA, para validar la coherencia biológica de la reducción.
- **Análisis:** Los 5 principales contribuyentes a PC1 son: mean concave points (0,261), mean concavity (0,258), worst concave points (0,251), mean compactness (0,239) y worst perimeter (0,237). Todos relacionados con irregularidad de forma celular.
- **Insight:** PC1 captura la señal biológica más asociada con malignidad — formas celulares irregulares y cóncavas. La reducción PCA no es solo compresión matemática; preserva estructura clínicamente significativa.
- **Decisión posible:** Compartir el heatmap de loadings con el equipo clínico para validar que la representación reducida se alinea con los marcadores diagnósticos conocidos.

### Hallazgo 3 — t-SNE logra separación visual superior pero es incompatible con pipelines de producción

- **Contexto:** El equipo de visualización requería evidencia de separabilidad de clases antes de comprometerse con una estrategia de clasificación.
- **Análisis:** t-SNE produce clusters visualmente compactos y bien separados para casos Malignos y Benignos (KL divergence = 0,9658, bajo el umbral de calidad de 1,0). PCA muestra un límite lineal claro pero con más superposición en la proyección 2D.
- **Insight:** t-SNE es la mejor herramienta para comunicar separabilidad a stakeholders clínicos — pero su naturaleza estocástica y la ausencia de método `transform()` lo hacen estructuralmente incompatible con objetos sklearn Pipeline requeridos para despliegue en producción.
- **Decisión posible:** Usar t-SNE exclusivamente para análisis exploratorio y presentaciones a stakeholders; usar PCA para todos los pasos de pipeline y modelado.

---

## 5. Recomendaciones (Priorizadas)

| Prioridad | Recomendación | Impacto Esperado | Esfuerzo |
|---|---|---|---|
| 🔴 Alto | Integrar `PCA(n_components=10)` como primer paso en el pipeline de clasificación | Reducción del 66% en dimensionalidad → entrenamiento más rápido, menor sobreajuste, menor costo de memoria | Bajo |
| 🟡 Medio | Presentar visualizaciones t-SNE al equipo clínico para validar separabilidad de clases antes del despliegue del modelo | Genera confianza con los stakeholders médicos; valida el enfoque de clasificación en forma temprana | Bajo |
| 🟢 Bajo | Evaluar UMAP como reemplazo futuro de t-SNE a escala | Más rápido que t-SNE (O(n log n) vs O(n²)), soporta `transform()`, mejor preservación de estructura global | Medio |

---

## 6. Limitaciones

- **Datos:** Wisconsin Breast Cancer es un proxy clínicamente análogo — todos los resultados deben revalidarse sobre el dataset neurológico real de DataMed Analytics (100+ variables) antes del uso en producción
- **Modelo:** Este análisis cubre solo reducción de dimensionalidad. No se entrenó ni evaluó ningún clasificador downstream en este caso
- **Alcance:** t-SNE es estocástico; a pesar de `random_state=42`, los resultados pueden variar entre versiones de librerías o hardware. No apto para pipelines de producción reproducibles
- **Escala:** El costo computacional de t-SNE (O(n²)) se vuelve prohibitivo con miles de pacientes y 100+ variables — UMAP debe evaluarse a esa escala

---

## 7. Próximos Pasos

| Horizonte | Acción |
|---|---|
| **Inmediato** | Aplicar `PCA(n_components=10)` en un Pipeline sklearn completo con clasificador LogReg o SVM sobre este dataset; medir ganancia de rendimiento de clasificación vs. variables originales |
| **Corto plazo** | Benchmark UMAP vs t-SNE sobre el dataset Wisconsin — comparar calidad de clusters (equivalente KL divergence) y tiempo de ejecución |
| **Largo plazo** | Aplicar el pipeline PCA validado al dataset neurológico real de DataMed Analytics (100+ variables); validar coherencia de clusters contra etiquetas diagnósticas clínicas |

---

## 8. Entregables del Caso

| Archivo | Propósito |
|---|---|
| `notebooks/01_clinical_dimensionality_reduction.ipynb` | Análisis CRISP-DM + LEAN completo; PCA y t-SNE aplicados y comparados |
| `figures/fig1_pca_variance.png` | Curva de varianza explicada acumulada PCA |
| `figures/fig2_pca_2d.png` | Proyección 2D PCA con clases coloreadas |
| `figures/fig3_tsne_2d.png` | Proyección 2D t-SNE con separación de clusters |
| `figures/fig4_comparison.png` | Comparación lado a lado PCA vs t-SNE |
| `figures/fig5_pca_loadings.png` | Heatmap de loadings PCA — variables más influyentes |
| `reports/executive/executive_summary_ES.md` | Este documento |
| `reports/executive/executive_summary_EN.md` | Resumen ejecutivo en inglés |

---

*Framework: CRISP-DM + LEAN | Metodología: Aprendizaje Basado en Casos (CBL)*

**Jose Marcel Lopez Pino**
Data Scientist — Operaciones, Analytics & Optimización de Procesos | Data Science & Business Analytics
Bootcamp: Fundamentos de Ciencia de Datos — SENCE/Alkemy (2025–2026)

[![GitHub](https://img.shields.io/badge/GitHub-joselopezp-181717?style=flat&logo=github)](https://github.com/joselopezp)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-jose--lopez--pino-0077B5?style=flat&logo=linkedin)](https://www.linkedin.com/in/jose-lopez-pino/)

---

**Fuente de datos:** Wisconsin Breast Cancer Dataset — UCI / scikit-learn (proxy clínico análogo)
**Fecha de ejecución:** Abril 2026
**Estado:** ✅ Análisis completo | 5 visualizaciones generadas | Recomendación de técnica documentada
