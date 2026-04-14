# 1 Millón de Transacciones Consultadas en Segundos: Spark SQL para Decisiones Retail
### Analytics de Ventas Distribuido — RetailMax · ~USD 500M en Ventas | CRISP-DM + LEAN

**Autor:** Jose Marcel Lopez Pino
**Rol:** Data Scientist — Operaciones, Analytics & Optimización de Procesos
**Framework:** CRISP-DM + LEAN | Aprendizaje Basado en Casos (CBL)
**Módulo:** M9 — Fundamentos de Big Data (Bootcamp Alkemy)
**Fecha:** Abril 2026
**Estado:** ✅ Completo

---

## Conclusión Ejecutiva

Tres consultas Spark SQL sobre 1 millón de transacciones RetailMax revelan que **Tecnología concentra el 40% de los ingresos totales** (CLP 190.436M) — pero el hallazgo más accionable es que el ticket promedio es prácticamente idéntico entre las 4 categorías (dispersión de solo 0,3%). El revenue no lo determina el precio: lo determina el volumen de transacciones. Esto reencuadra la estrategia de marketing desde subir precios en Tecnología hacia aumentar tráfico en Accesorios y Útiles. El mismo código SQL escala de local a AWS EMR Serverless sin modificaciones — de miles a miles de millones de registros.

---

## 1. Contexto de Negocio

| | |
|---|---|
| **Industria** | Retail |
| **Unidad de Negocio** | Analítica de Ventas y Operaciones |
| **Stakeholder** | Director Comercial / Gerente de Operaciones |
| **Decisión a Apoyar** | ¿Dónde asignar inventario y presupuesto de marketing entre categorías de producto y sucursales? |

> **Situación:** RetailMax opera una red multisucursal con más de 1 millón de transacciones de venta en el período actual. Sin capacidad de consulta distribuida, las preguntas analíticas sobre mix de categorías, rendimiento por sucursal y transacciones de alto valor requieren muestreo manual o agregación offline — limitando la velocidad y precisión de las decisiones.

---

## 2. Problema

> ¿Cómo puede RetailMax responder preguntas operativas sobre su historial transaccional completo (millones de registros) en segundos, usando una interfaz de consulta que escale a datos en la nube sin necesidad de reescribir código?

**Impacto si no se resuelve:**
- Las decisiones de inventario y marketing se toman con muestras parciales o agregados desactualizados
- ~1M de transacciones por período exceden el límite práctico del análisis con pandas en una sola máquina
- La incapacidad de profundizar en patrones de transacciones de alto valor retrasa las decisiones de reposición

---

## 3. Enfoque Analítico

| Aspecto | Detalle |
|---|---|
| **Datos** | 1.000.000 de transacciones de venta RetailMax · 4 categorías · 2025 |
| **Método** | Tres consultas Spark SQL — filtro, agregación, top-N — sobre una vista temporal registrada |
| **Herramienta** | Python · PySpark 4.1.1 · Spark SQL · Optimizador Catalyst |
| **Validación** | Inspección del plan de ejecución de Catalyst (`explain(True)`) para confirmar predicate pushdown y projection pruning |

---

## 4. Hallazgos Principales

### Hallazgo 1 — Tecnología domina el mix de ingresos (40%)

- **Contexto:** Cuatro categorías de producto operan en la red de sucursales; el mix no está cuantificado a nivel ejecutivo.
- **Análisis:** `Tecnologia` genera **CLP 190.436M** (40% del total), seguida por `Oficina` (CLP 142.972M / 30%), `Utiles` (CLP 94.521M / 20%) y `Accesorios` (CLP 47.749M / 10%) — una distribución Pareto textbook.
- **Insight:** La concentración de ingresos en Tecnología es estructural, no una anomalía. La distribución 40-30-20-10 es consistente y puede anclar la planificación presupuestaria.
- **Decisión posible:** Asignar presupuesto de marketing e inventario proporcionalmente a la contribución de ingresos como línea base, luego probar inversiones de crecimiento en las categorías de menor participación.

### Hallazgo 2 — El volumen impulsa los ingresos, no el precio

- **Contexto:** La práctica convencional del retail asume que las categorías de alto ingreso tienen precios premium.
- **Análisis:** El ticket promedio entre las cuatro categorías es casi idéntico: Tecnologia CLP 475.452 · Oficina CLP 476.326 · Utiles CLP 475.090 · Accesorios CLP 475.825 — una dispersión de solo **0,3%**.
- **Insight:** El mix de ingresos de RetailMax es puramente una función de **cantidad de transacciones**, no de pricing. La ventaja de Tecnología viene de vender 4 veces más transacciones que Accesorios con esencialmente el mismo ticket promedio.
- **Decisión posible:** Reformular la pregunta de marketing desde *"¿podemos subir precios en Tec?"* hacia *"¿podemos aumentar el volumen de transacciones en Accesorios y Útiles?"*. Priorizar campañas generadoras de tráfico por sobre iniciativas de pricing premium.

### Hallazgo 3 — El segmento Tecnología de alto valor es suficientemente grande para gestionarlo como línea propia

- **Contexto:** Las transacciones con precios premium (>CLP 300K) suelen ser una minoría que merece atención especial de reposición.
- **Análisis:** **274.143 transacciones de Tecnología** superan los CLP 300K — aproximadamente **27% de todas las ventas de Tecnología** y **27%** del total de transacciones del dataset.
- **Insight:** No es un segmento de nicho. Las ventas de Tec de alto valor son suficientemente grandes para justificar tracking de inventario dedicado, cadencia de reposición separada y condiciones específicas con proveedores.
- **Decisión posible:** Establecer un dashboard a nivel SKU dedicado para transacciones Tec >CLP 300K con revisión semanal de reposición, distinto de las operaciones generales de inventario.

---

## 5. Recomendaciones (Priorizadas)

| Prioridad | Recomendación | Impacto Esperado | Esfuerzo |
|---|---|---|---|
| 🔴 Alto | Establecer proceso de reposición dedicado para transacciones Tec >CLP 300K (~274K transacciones) | Menos quiebres de stock en el segmento de mayor margen | Medio |
| 🟡 Medio | Reasignar inversión de marketing hacia campañas generadoras de volumen en Útiles y Accesorios | Cierra brecha de 20–30 pp en participación de ingresos vs Tec | Medio |
| 🟢 Bajo | Convertir datos de ventas a formato Parquet para acelerar 10x las consultas analíticas recurrentes | Ciclos de decisión más rápidos; menor costo de cómputo | Bajo |

---

## 6. Limitaciones

- **Datos:** Dataset sintético de un único período — sin comparación año contra año ni análisis de estacionalidad
- **Alcance:** Tres patrones de consulta (filtro, agregación, top-N) demuestran la capacidad central pero no incluyen funciones de ventana, agregaciones temporales ni joins
- **Contexto de sucursales:** Los IDs de sucursal están anonimizados — el enriquecimiento geográfico o demográfico fortalecería el hallazgo del top 5

---

## 7. Próximos Pasos

| Horizonte | Acción |
|---|---|
| **Inmediato** | Convertir `ventas.csv` a Parquet; aceleración ~10x esperada para consultas analíticas repetidas |
| **Corto plazo** | Agregar funciones de ventana y consultas temporales (`MONTH(fecha)`, `YEAR(fecha)`) para análisis de estacionalidad y ranking por sucursal |
| **Largo plazo** | Migrar a AWS EMR Serverless + S3 — mismo código SQL, ejecución distribuida a escala productiva |

---

## 8. Entregables del Caso

| Archivo | Propósito |
|---|---|
| `notebooks/01_spark_sql_retail_analytics.ipynb` | Tres consultas Spark SQL ejecutadas y validadas con Catalyst |
| `data/raw/ventas.csv` | Dataset de 1M transacciones RetailMax (excluido de Git) |
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

**Fuente de datos:** Transacciones sintéticas RetailMax — 1.000.000 registros · 4 categorías · 2025
**Fecha de ejecución:** Abril 2026
**Estado:** ✅ Análisis completo | Catalyst validado | 3 queries ejecutadas sobre 1M registros
