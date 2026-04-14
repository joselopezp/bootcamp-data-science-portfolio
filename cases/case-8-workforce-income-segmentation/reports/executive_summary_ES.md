# Identificando Perfiles de Alto Valor a Escala: Clasificación de Ingresos y Segmentación con PySpark MLlib
### Segmentación Socioeconómica de la Fuerza Laboral — Censo UCI 1994 · AUC = 0,9028 | CRISP-DM + LEAN

**Autor:** Jose Marcel Lopez Pino
**Rol:** Data Scientist — Operaciones, Analytics & Optimización de Procesos
**Framework:** CRISP-DM + LEAN | Aprendizaje Basado en Casos (CBL)
**Módulo:** M9 — Fundamentos de Big Data (Bootcamp Alkemy)
**Fecha:** Marzo 2026
**Estado:** ✅ Completo

---

## Conclusión Ejecutiva

Un pipeline MLlib end-to-end con PySpark 4.1.1 clasifica perfiles de alto valor (ingresos >50K USD) con **AUC = 0,9028** — 90% de poder discriminatorio sobre 30.162 registros del Censo de EEUU 1994. El modelo supera ampliamente el baseline del clasificador mayoritario (75% de accuracy). KMeans k=4 identifica 4 segmentos socioeconómicos diferenciados — directamente aplicables a estrategias de targeting en retail, banca, seguros, RRHH y políticas públicas. La educación y la ocupación son los dos predictores más accionables: trabajadores con educación universitaria completa en sectores profesionales concentran el 3,7x en ganancias de capital respecto al nivel promedio.

---

## 1. Contexto de Negocio

| | |
|---|---|
| **Industria** | Analytics de Clientes / Perfilamiento Socioeconómico |
| **Fuente de Datos** | UCI Adult Census Income — Censo de EEUU 1994 |
| **Caso de Uso Principal** | Modelado de valor de cliente y segmentación conductual (ingreso como proxy) |
| **Decisión a Apoyar** | ¿Podemos identificar perfiles de alto valor y segmentar la población para habilitar estrategias diferenciadas usando el ingreso como proxy? |

> **Situación:** Organizaciones de retail, banca y plataformas digitales necesitan identificar clientes de alto valor — pero frecuentemente dependen de análisis manuales en planillas de cálculo con escalabilidad limitada y bajo poder predictivo. Este caso demuestra un pipeline MLlib escalable que reemplaza el análisis estático con scoring y segmentación basados en datos, habilitando toma de decisiones dirigida en analytics de clientes.

---

## 2. Problema

> ¿Puede un pipeline de Machine Learning identificar perfiles de alto valor usando el ingreso como proxy y segmentar la población en grupos accionables para toma de decisiones diferenciada?

**Impacto si no se resuelve:**
- Sin clasificación de ingresos, las organizaciones aplican estrategias uniformes a poblaciones heterogéneas — asignación ineficiente de recursos y oportunidades de targeting desperdiciadas
- Sin segmentación, el ~25% de perfiles de alto valor permanece sin identificar dentro de la población general, reduciendo el ROI de cualquier estrategia diferenciada

---

## 3. Enfoque Analítico

| Aspecto | Detalle |
|---|---|
| **Datos** | UCI Adult Census Income · 32.561 registros · 15 variables (numéricas + categóricas) · UCI ML Repository |
| **Método** | Clasificación binaria (Regresión Logística) para predecir ingreso >50K USD + clustering no supervisado (KMeans k=4) para segmentar perfiles socioeconómicos |
| **Herramienta** | Python · PySpark 4.1.1 · MLlib Pipelines · Spark SQL |
| **Optimización** | CrossValidator 5-fold · 12 combinaciones de parámetros · Método del Codo k=2..8 |
| **Validación** | AUC-ROC en test set retenido (20%) · CrossValidator 5-fold · Silhouette score · Método del Codo · Comparación con baseline mayoritario |

---

## 4. Hallazgos Principales

### Hallazgo 1 — El modelo supervisado supera el objetivo de rendimiento tras optimización

- **Contexto:** Un clasificador mayoritario (siempre predice <=50K) alcanza ~75% de accuracy — el baseline mínimo a superar.
- **Análisis:** Regresión Logística alcanzó AUC-ROC = 0,9005 antes de optimización. CrossValidator (5-fold, 12 combinaciones) identificó los mejores parámetros: regParam=0,001, elasticNetParam=0,5 — mejorando AUC a 0,9028 (+0,0023). Nota LEAN: la mejora marginal confirma que el modelo MVP original ya estaba bien calibrado.
- **Insight:** El modelo tiene fuerte poder discriminatorio — separa perfiles de alto valor de bajo valor (usando ingreso como proxy) con 90% de AUC independientemente de la etapa de optimización.
- **Decisión posible:** Desplegar scoring del modelo para marcar perfiles de alto valor basados en probabilidad predicha para tratamiento diferenciado en cualquier aplicación downstream.

### Hallazgo 2 — Cuatro perfiles conductuales y socioeconómicos distintos identificados

- **Contexto:** La predicción binaria de ingreso sola es insuficiente — las organizaciones necesitan segmentos de audiencia accionables, no solo una bandera binaria.
- **Análisis:** KMeans k=4 produjo 4 clusters diferenciados por edad, nivel educacional, horas trabajadas por semana y ganancias de capital. El Método del Codo (k=2..8) no mostró inflexión geométrica dominante — k=4 validado como elección basada en interpretabilidad de negocio.
- **Insight:** Los 4 clusters representan arquetipos socioeconómicos interpretables (ej. profesionales de alta educación vs trabajadores manuales) aplicables al diseño de estrategias diferenciadas.
- **Decisión posible:** Mapear cada cluster a un nivel estratégico — Premium / Estándar / Desarrollo / Exclusión — basado en las características del perfil.

### Hallazgo 3 — Educación y ocupación son las señales de ingreso más fuertes

- **Contexto:** El dataset tiene 15 variables — no todas contribuyen igualmente a la predicción de ingreso.
- **Análisis:** El análisis JOIN con Spark SQL contra una tabla de benchmark de ingresos confirmó que educación universitaria completa o superior correlaciona con ingresos benchmark superiores a USD 52K, concentrados en sectores de Gestión y Profesionales. Trabajadores de Prof-school con ingresos >50K promedian USD 14.274 en ganancias de capital — 3,7x sobre el nivel universitario promedio.
- **Insight:** Nivel educacional y sector de ocupación son las dos variables más accionables y ampliamente disponibles para segmentación basada en ingresos.
- **Decisión posible:** Usar educación + ocupación como filtros proxy livianos cuando el scoring completo del modelo no esté disponible — accionable con la mayoría de sistemas CRM o RRHH.

---

## 5. Recomendaciones (Priorizadas)

| Prioridad | Recomendación | Impacto Esperado | Esfuerzo |
|---|---|---|---|
| 🔴 Alto | Aplicar pipeline de Regresión Logística (AUC = 0,9028) para puntuar la población objetivo y clasificar perfiles de alto valor | Reducir tasa de error de clasificación desde baseline del 25% (mayoritario) a <10% | Medio |
| 🟡 Medio | Usar clusters KMeans k=4 para diseñar estrategias diferenciadas por segmento socioeconómico | Habilitar enfoques dirigidos vs tratamiento uniforme — efectividad estimada +15% | Medio |
| 🟢 Bajo | Usar educación + ocupación como proxy liviano de ingreso en sistemas basados en reglas | Victoria rápida — sin despliegue de modelo requerido, accionable con infraestructura de datos existente | Bajo |

---

## 6. Limitaciones

- **Datos:** Censo de EEUU 1994 — no representativo del mercado laboral actual. Los umbrales de ingreso, estructura de ocupaciones y patrones educacionales han cambiado significativamente. Reentrenar con datos actuales antes del uso en producción
- **Modelo:** Regresión Logística es el modelo MVP — las relaciones no lineales pueden ser mejor capturadas por Random Forest o GradientBoosting en una próxima iteración
- **Alcance:** Umbral binario de ingreso (>50K USD, 1994) es un proxy histórico — no refleja poder adquisitivo actual ni diferencias de costo de vida entre regiones
- **Equidad:** El modelo incluye `sex` como variable — se requiere auditoría de equidad antes del despliegue para asegurar que no haya resultados de targeting discriminatorios
- **Clustering:** El Método del Codo no muestra inflexión geométrica dominante — k=4 es una elección de interpretabilidad de negocio, no un óptimo geométrico basado en datos

---

## 7. Próximos Pasos

| Horizonte | Acción |
|---|---|
| **Inmediato** | Interpretar centroides KMeans para asignar nombres descriptivos de negocio a cada uno de los 4 clusters |
| **Corto plazo** | Reentrenar pipeline con datos de censo o CRM actuales · Agregar Random Forest como modelo de comparación · Realizar auditoría de equidad sobre variable `sex` |
| **Largo plazo** | Desplegar vía endpoint de scoring FastAPI · Integrar MLflow para seguimiento de experimentos · Monitorear drift de distribución de ingresos trimestralmente |

---

## 8. Entregables del Caso

| Archivo | Propósito |
|---|---|
| `notebooks/01_workforce_income_segmentation.ipynb` | Pipeline MLlib end-to-end con optimización CrossValidator |
| `reports/figures/model_performance_summary.png` | Resumen visual de métricas del modelo |
| `reports/figures/roc_curve.png` | Curva ROC con anotación AUC |
| `reports/figures/elbow_method.png` | Método del Codo k=2..8 |
| `requirements.txt` | Dependencias pinned |
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

**Fuente de datos:** UCI Machine Learning Repository — Adult Census Income Dataset (Kohavi, 1996)
**Fecha de ejecución:** Marzo 2026
**Estado:** ✅ Análisis completo | AUC = 0,9028 | 4 segmentos identificados | Pipeline reproducible
