# Eliminando el Sesgo Silencioso: Pipeline de Preprocesamiento para Clasificación de Clientes
### Analytics de Clientes Retail — Imputación, Encoding & Escalado de Variables | CRISP-DM + LEAN

**Autor:** Jose Marcel Lopez Pino
**Rol:** Data Scientist — Operaciones, Analytics & Optimización de Procesos
**Framework:** CRISP-DM + LEAN | Aprendizaje Basado en Casos (CBL)
**Módulo:** M5 — Fundamentos de Machine Learning (Bootcamp Alkemy)
**Fecha:** Abril 2026
**Estado:** ✅ Completo

---

## Conclusión Ejecutiva

Un pipeline de preprocesamiento completo transforma un dataset de clientes con valores faltantes, categorías sin codificar y una diferencia de escala de **1.000 veces** entre variables numéricas en una matriz de 12 columnas lista para modelado — sin sesgo, sin fugas de datos, sin errores silenciosos. El hallazgo crítico: los modelos entrenados sobre datos sin escalar asignan el 99,9% de su peso al ingreso e ignoran efectivamente la edad — produciendo segmentaciones de clientes distorsionadas sin emitir ninguna advertencia. El preprocesamiento correcto no es un paso técnico opcional: es la diferencia entre un modelo que aprende comportamiento real del cliente y uno que aprende artefactos matemáticos.

---

## 1. Contexto de Negocio

| | |
|---|---|
| **Industria** | Retail — Cadena de Supermercados |
| **Unidad de Negocio** | Customer Analytics / Marketing |
| **Stakeholder** | Equipo de Data Science — RetailData Analytics |
| **Decisión a Apoyar** | ¿Qué estrategia de preprocesamiento produce la matriz de variables más limpia y compatible con el modelo para un clasificador de compras recurrentes? |

> **Situación:** RetailData Analytics fue contratada por una cadena de supermercados para construir un modelo predictivo que identifique los clientes con mayor probabilidad de realizar compras recurrentes. Durante la fase de ingesta inicial, el equipo descubrió que el dataset crudo era inapropiado para modelado: contenía valores de ingreso faltantes, categorías de ciudad sin codificar y una diferencia de escala de 1.000 veces entre edad e ingreso. Antes de entrenar cualquier modelo, es necesario diseñar, aplicar y documentar un pipeline completo de preprocesamiento.

---

## 2. Problema

> ¿Cómo transformar el dataset crudo de 4 columnas en una matriz de variables limpia, codificada y correctamente escalada que elimine los sesgos de modelado causados por valores faltantes, categorías nominales y escalas numéricas inconsistentes?

**Impacto si no se resuelve:**
- Los modelos basados en distancia (KNN, SVM, KMeans) asignarían el 99,9% de su peso al `Ingreso` e ignorarían efectivamente la `Edad` — distorsionando la segmentación de clientes y produciendo predicciones de compra recurrente poco confiables
- Un modelo entrenado sobre datos sin imputar colapsaría o imputaría ceros silenciosamente, introduciendo sesgo sistemático hacia el tramo de ingreso mínimo
- Las categorías de ciudad sin codificar impedirían el ajuste del modelo — scikit-learn no acepta inputs de tipo texto

---

## 3. Enfoque Analítico

| Aspecto | Detalle |
|---|---|
| **Datos** | Dataset fragmento de RetailData Analytics — 4 filas × 4 columnas (ID, Edad, Ciudad, Ingreso). Dataset sintético provisto como parte del caso M5 L3 |
| **Método** | Pipeline secuencial de preprocesamiento: imputación de valores faltantes → encoding categórico (3 métodos) → escalado numérico (2 métodos) |
| **Herramienta** | Python · pandas 3.0 · scikit-learn 1.8 · matplotlib 3.10 |
| **Validación** | Post-imputación: 0 valores faltantes confirmados. Post-escalado: media=0,0000 y std=1,1547 verificados para ambas variables Z-Score. Shape de salida CSV (4, 12) confirmado |

---

## 4. Hallazgos Principales

### Hallazgo 1 — La diferencia de escala distorsiona silenciosamente el aprendizaje del modelo

- **Contexto:** El dataset crudo tiene `Edad` en rango 25–45 e `Ingreso` en rango 30.000–50.000 — una diferencia de 1.000 veces en magnitud. Ambas variables son igualmente relevantes para predecir el comportamiento del cliente.
- **Análisis:** Tras normalización Min-Max, ambas variables se mapean a [0,0000; 1,0000]. Tras estandarización Z-Score, ambas alcanzan media=0,0000 y std=1,1547. Sin escalado, una diferencia de $1 en ingreso era matemáticamente equivalente a 1.000 años de edad en cualquier cálculo de distancia.
- **Insight:** Las variables sin escalar no generan errores visibles — el modelo entrena y predice sin advertencias. El sesgo es silencioso, está embebido en los pesos aprendidos y solo es detectable mediante análisis cuidadoso de importancia de variables. Esto convierte la omisión del escalado en uno de los errores de preprocesamiento más peligrosos en pipelines ML de producción.
- **Decisión posible:** Establecer Z-Score como escalador por defecto para todos los modelos de clientes en producción — maneja datos nuevos fuera de rango con gracia, a diferencia de Min-Max que produce valores fuera de [0,1] para clientes con ingreso superior al rango de entrenamiento.

### Hallazgo 2 — La elección del encoding determina la compatibilidad del modelo, no solo el rendimiento

- **Contexto:** `Ciudad` tiene 3 categorías nominales (Barcelona, Madrid, Sevilla) sin orden natural. Se aplicaron y compararon tres estrategias de encoding.
- **Análisis:** Label Encoding asigna Barcelona=0, Madrid=1, Sevilla=2 — implicando que Sevilla vale matemáticamente "el doble" que Madrid, lo cual es semánticamente falso. One-Hot Encoding crea 3 columnas binarias sin supuesto ordinal. Dummy encoding (drop_first=True) reduce a 2 columnas (Madrid, Sevilla), con Barcelona como categoría de referencia implícita — eliminando multicolinealidad en modelos de regresión.
- **Insight:** El encoding no es un paso de formato — es una decisión de modelado. Una regresión logística entrenada con ciudades Label Encoded aprendería una relación lineal falsa entre códigos de ciudad y frecuencia de compra. La elección entre OHE y Dummy depende enteramente de la arquitectura del modelo downstream, no de preferencia personal.
- **Decisión posible:** Usar One-Hot Encoding para modelos lineales y basados en distancia (Regresión Logística, SVM, KNN); usar Label Encoding solo para modelos basados en árboles (Decision Tree, Random Forest, XGBoost) donde los splits manejan correctamente los artefactos ordinales.

### Hallazgo 3 — La imputación por media es conservadora pero geográficamente ingenua

- **Contexto:** Fila 3 (ID=3, Ciudad=Madrid) tenía `Ingreso` faltante. Tres valores conocidos disponibles: $30.000 (Madrid), $50.000 (Sevilla), $40.000 (Barcelona).
- **Análisis:** Media global = (30.000 + 50.000 + 40.000) / 3 = **$40.000** — el valor imputado. Esto coincide con el ingreso conocido de Barcelona y casualmente iguala la mediana global. Post-imputación: 0 valores faltantes, dataset completo.
- **Insight:** La imputación por media ignora la variación de ingresos por zona geográfica. Los clientes de Madrid pueden tener perfiles de ingreso sistemáticamente diferentes a los de Sevilla o Barcelona. Con solo 4 filas esta diferencia es indetectable, pero en el dataset completo de producción una imputación por mediana a nivel ciudad (`GroupBy('Ciudad')['Ingreso'].transform('median')`) produciría rellenos más precisos y reduciría el sesgo de segmentación.
- **Decisión posible:** Para el dataset completo de RetailData, reemplazar la imputación global por media con imputación por mediana a nivel ciudad — un cambio de una línea con mejora significativa en precisión para segmentación geográfica de clientes.

---

## 5. Recomendaciones (Priorizadas)

| Prioridad | Recomendación | Impacto Esperado | Esfuerzo |
|---|---|---|---|
| 🔴 Alto | Adoptar Z-Score como escalador por defecto para todos los modelos de clientes en producción | Elimina sesgo de escala en el modelo; maneja datos nuevos fuera de rango sin romper el pipeline | Bajo |
| 🔴 Alto | Usar One-Hot Encoding para `Ciudad` en modelos lineales y basados en distancia; Label Encoding solo para modelos basados en árboles | Previene relaciones ordinales falsas que distorsionan los coeficientes del modelo | Bajo |
| 🟡 Medio | Reemplazar imputación global por media con imputación por mediana a nivel ciudad en el dataset completo | Reduce sesgo geográfico de ingreso en segmentación de clientes — mejora directamente la calidad del clustering | Bajo |
| 🟢 Bajo | Envolver el pipeline completo en scikit-learn `Pipeline` + `ColumnTransformer` | Previene fuga de datos asegurando que los escaladores se ajusten solo sobre datos de entrenamiento — crítico para integridad de evaluación del modelo | Medio |

---

## 6. Limitaciones

- **Datos:** Fragmento de 4 filas es un dataset de demostración — las conclusiones estadísticas requieren la base de clientes completa. No es posible generalizar desde n=4
- **Imputación:** Media calculada sobre n=3 valores conocidos. Con solo 3 datos, la media es muy sensible a cualquier valor extremo — no es robusta para producción
- **Escalado:** Ambos escaladores ajustados sobre el dataset completo de 4 filas. En un pipeline ML real, los escaladores deben ajustarse solo sobre datos de entrenamiento y aplicarse (solo transform) a validación y test para prevenir fuga de datos
- **Alcance:** Solo preprocesamiento — no se entrenó ningún modelo en este caso. El impacto de negocio de las decisiones de encoding y escalado solo será cuantificable una vez que se ajuste un clasificador sobre los datos procesados

---

## 7. Próximos Pasos

| Horizonte | Acción |
|---|---|
| **Inmediato** | Aplicar este pipeline al dataset completo de clientes RetailData usando `Pipeline` + `ColumnTransformer` de scikit-learn |
| **Corto plazo** | Entrenar clasificador de Regresión Logística sobre las variables preprocesadas y evaluar precisión de predicción de compra recurrente (AUC, precisión, recall) |
| **Largo plazo** | Refactorizar en módulo reutilizable `src/preprocessing.py` — siguiendo el patrón `wrangling.py` del caso fintech M3 — para despliegue como servicio de preparación de datos en producción |

---

## 8. Entregables del Caso

| Archivo | Propósito |
|---|---|
| `notebooks/01_retail_customer_preprocessing.ipynb` | Análisis CRISP-DM + LEAN completo; pipeline de preprocesamiento ejecutado y validado |
| `data/raw/` | Dataset fragmento original (4 filas, sin modificar) |
| `data/processed/retaildata_preprocessed.csv` | Matriz de 12 columnas lista para modelado |
| `reports/scaling_comparison.png` | Gráfico comparativo: crudo vs. Min-Max vs. Z-Score |
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

**Fuente de datos:** Dataset sintético RetailData Analytics — fragmento de demostración M5 L3
**Fecha de ejecución:** Abril 2026
**Estado:** ✅ Análisis completo | Pipeline validado | Matriz de 12 columnas exportada
