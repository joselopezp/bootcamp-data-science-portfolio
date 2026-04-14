# De 6 Horas de Limpieza Manual a 3 Minutos de Pipeline Automatizado
### Calidad de Datos en Transacciones FinTech — Auditoría ETL & Automatización | CRISP-DM + LEAN

**Autor:** Jose Marcel Lopez Pino
**Rol:** Data Scientist — Operaciones, Analytics & Optimización de Procesos
**Framework:** CRISP-DM + LEAN | Aprendizaje Basado en Casos (CBL)
**Módulo:** M3 — Preparación de Datos (Bootcamp Alkemy)
**Fecha:** Marzo 2026
**Estado:** ✅ Completo

---

## Conclusión Ejecutiva

Un pipeline ETL automatizado en Python/Pandas reemplaza 6 horas semanales de limpieza manual de datos transaccionales en una empresa fintech, reduciendo el tiempo de procesamiento en **120 veces** (de 360 minutos a 3 minutos) y generando un ahorro estimado de **$15.000 USD anuales**. El análisis reveló además una pérdida sistémica del 71,3% de los registros — señal de fallas críticas en los sistemas de origen que requieren auditoría urgente antes del despliegue a producción.

---

## 1. Contexto de Negocio

| | |
|---|---|
| **Industria** | Tecnología Financiera (FinTech) |
| **Unidad de Negocio** | Operaciones & Calidad de Datos |
| **Stakeholder** | Director de Finanzas / Líder de Data Analytics |
| **Decisión a Apoyar** | ¿Puede automatizarse el reporte diario de KPIs sin preparación manual de datos? |

> **Situación:** Una empresa fintech consolida datos transaccionales desde tres canales no integrados: sistemas punto de venta (POS), plataformas e-commerce y cargas manuales en CSV. Los datos llegan con problemas graves de calidad: 33,5% de valores nulos en precios, 5,96% de registros duplicados, 63,4% de fechas inválidas (ej. 2025-02-30) y formato inconsistente. La limpieza manual requiere 6 horas semanales, retrasa los dashboards de KPIs en 1 día hábil e introduce pasos no documentados que generan riesgo de auditoría.

---

## 2. Problema

> ¿Puede un pipeline de Data Wrangling con Pandas identificar, limpiar y eliminar automáticamente los registros inválidos desde tres fuentes heterogéneas, habilitando reportería diaria sin intervención humana?

**Impacto si no se resuelve:**
- 6 horas/semana de trabajo analítico en limpieza manual (~$15.000 USD/año en costo laboral)
- Dashboards retrasados 1 día hábil — decisiones operacionales sobre datos desactualizados
- Registros duplicados inflan el revenue reportado ~6%, distorsionando métricas de desempeño
- 63.381 fechas inválidas (63,4%) impiden cualquier análisis temporal o reporte por período
- Sin reproducibilidad — los pasos manuales no están documentados y dependen del operador

---

## 3. Enfoque Analítico

| Aspecto | Detalle |
|---|---|
| **Datos** | Dataset Kaggle — Dirty Financial Transactions: 100.000 registros reales con problemas auténticos de calidad |
| **Método** | Pipeline CRISP-DM Fases 1–3: Comprensión del negocio → Comprensión de datos → Preparación de datos |
| **Herramienta** | Python · pandas 3.0.0 · NumPy · regex |
| **Validación** | Assertions y trazabilidad en cada paso; métricas antes/después documentadas |

---

## 4. Hallazgos Principales

### Hallazgo 1 — Las fechas inválidas son un problema sistémico (63,4% del dataset)

63.381 registros contienen fechas inválidas como 2025-02-30 o 2023-13-01. No son errores aislados — es una **falla sistémica** en los tres sistemas de origen.

**Causa raíz:** Los sistemas POS y e-commerce no validan fechas antes de exportar, permitiendo que los errores se propaguen al pipeline de datos.

**Impacto de negocio:** Imposible agrupar transacciones por período; los KPIs temporales fallan; los reportes diarios, semanales y mensuales son poco confiables.

**Decisión recomendada:** Implementar validación de fechas en origen (rechazar fechas inválidas antes de exportar). Plazo: 2 semanas.

---

### Hallazgo 2 — El 71,3% de las transacciones no tiene identificadores críticos

71.321 registros (71,3%) carecen de al menos un campo clave: Transaction_ID, Transaction_Date o Customer_ID. Estas filas son **irrecuperables** — sin ID o fecha, el registro no tiene valor analítico.

**Causa raíz:** Esta tasa de pérdida del 71,3% indica **fallas sistémicas en el ETL**, no errores de ingreso de datos. Causas probables: truncamiento en la exportación, workflows sin validación, sincronización incompleta entre sistemas.

**Impacto de negocio:** Pérdida del 71% del volumen transaccional — imposible analizar comportamiento de clientes, desempeño de productos o atribución de ingresos.

**Decisión recomendada:** **Auditoría urgente** de los tres sistemas de origen (POS, e-commerce, cargas manuales). Plazo: **1 semana** (ruta crítica).

---

### Hallazgo 3 — El pipeline es reproducible y ejecuta en menos de 5 minutos

El pipeline completo (carga → auditoría → limpieza → validación → exportación) **ejecuta en menos de 3 minutos** en un laptop estándar. Cada transformación está documentada, validada con assertions y registrada.

**Reproducibilidad:** Mismo dataset de entrada → Mismo dataset de salida, siempre. Sin dependencia del operador, sin pasos manuales no documentados.

**Mejora de calidad:**
- Completitud: 91,25% → 97,94% (+6,69%)
- Duplicados eliminados: reducción del 98% (5.840 de 5.959)
- Valores nulos eliminados: reducción del 97,3% (70.217 de 72.200)

**Decisión recomendada:** Programar ejecución diaria automatizada (cron/Airflow) una vez resuelta la causa raíz de la pérdida del 71% de datos.

---

## 5. Métricas Reales (Post-Ejecución)

| Métrica | ANTES | DESPUÉS | Cambio |
|---|---|---|---|
| **Registros válidos** | 100.000 | 12.036 | -87.964 (-87,96%) |
| **Completitud** | 91,25% | 97,94% | +6,69% |
| **Registros duplicados** | 5.959 (5,96%) | 119 (0,99%) | -5.840 (-98,0%) |
| **Valores nulos totales** | 72.200 | 1.983 | -70.217 (-97,3%) |
| **Tiempo de procesamiento** | 360 min (6h) | 3 min | **120x más rápido** |

---

## 6. Recomendaciones (Priorizadas)

| Prioridad | Recomendación | Impacto Esperado | Esfuerzo | Plazo |
|---|---|---|---|---|
| 🔴 **CRÍTICO** | Auditoría urgente: ¿Por qué el 71,3% de las transacciones no tiene Transaction_ID/Date/Customer_ID? | Identificar causa raíz; cuantificar riesgo de pérdida de datos | Alto | 1 semana |
| 🔴 **CRÍTICO** | Implementar validación de fechas en origen (rechazar fechas inválidas en POS/e-commerce) | Elimina 63.381 registros inválidos; habilita análisis temporal | Medio | 2 semanas |
| 🔴 Alto | Forzar exportación de precios solo en formato numérico; eliminar símbolos "$" | Recupera ~30% de nulos en precios sin imputación | Bajo | 2 semanas |
| 🟡 Medio | Programar pipeline para ejecución diaria automatizada (Airflow/cron) | Elimina 6h/semana de trabajo manual; ahorro ~$15.000 USD/año | Bajo | 3 semanas |
| 🟢 Bajo | Investigar por qué la fuente e-commerce tiene la mayor tasa de fechas inválidas | Prevenir recurrencia; mejorar calidad de datos en origen | Bajo | 1 semana |

---

## 7. Impacto Financiero Estimado

| Concepto | Cálculo | Valor |
|---|---|---|
| **Tiempo manual (ANTES)** | 6 h/semana × 52 semanas | 312 h/año |
| **Tiempo automatizado (DESPUÉS)** | 3 min/día × 250 días hábiles | 12,5 h/año |
| **Horas ahorradas** | 312 - 12,5 | **299,5 h/año** |
| **Tarifa analista** | $50 USD/hora | — |
| **Ahorro anual estimado** | 299,5 h × $50 | **$14.975 USD** |
| **Mejora en completitud** | 91,25% → 97,94% | **+6,69%** |

---

## 8. Limitaciones

- **Alta tasa de eliminación (87,96%):** Eliminar 87.964 de 100.000 registros es **anormal** e indica problemas sistémicos en los sistemas de origen, no fallas del pipeline.
- **Causa raíz desconocida:** La pérdida del 71,3% de registros debe diagnosticarse antes del despliegue a producción.
- **Dataset de salida pequeño:** 12.036 registros válidos desde 100k originales. Validar si este volumen es suficiente para los KPIs de negocio.

### Recomendación de Despliegue
**No desplegar a producción** hasta resolver la causa raíz de los 71.321 registros faltantes. Acción requerida: contactar a los equipos de POS, e-commerce y carga manual para diagnóstico en **1 semana**.

---

## 9. Entregables del Caso

| Archivo | Propósito |
|---|---|
| `notebooks/01_etl_quality_fintech_transactions.ipynb` | Análisis CRISP-DM + LEAN completo; 10 pasos de limpieza ejecutados y validados |
| `src/wrangling_updated.py` | Módulo Python reutilizable con clase `DirtyFinTechWrangler` (listo para producción) |
| `data/raw/dirty_financial_transactions.csv` | Dataset de origen (100.000 filas, sin procesar) |
| `data/processed/clean_transactions.csv` | Dataset de salida (12.036 registros válidos, 97,94% de completitud) |
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

**Fuente de datos:** Kaggle — Dirty Financial Transactions Dataset
**Fecha de ejecución:** Marzo 2026
**Estado:** ✅ Análisis completo | Datos reales | Todos los números provienen de la ejecución del notebook
