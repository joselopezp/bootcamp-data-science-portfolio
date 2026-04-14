# De 6 Horas Semanales de Limpieza Manual a 5 Minutos de Pipeline Automatizado
### Consolidación de Datos Operacionales Mineros — Fuentes CSV, Excel y HTML | CRISP-DM + LEAN

**Autor:** Jose Marcel Lopez Pino
**Rol:** Data Scientist — Operaciones, Analytics & Optimización de Procesos
**Framework:** CRISP-DM + LEAN | Aprendizaje Basado en Casos (CBL)
**Módulo:** M3 — Adquisición y Preparación de Datos (Bootcamp Alkemy)
**Fecha:** Abril 2026
**Estado:** ✅ Completo

---

## Conclusión Ejecutiva

Un pipeline de ingesta automatizado con Pandas consolida datos operacionales de tres sistemas no integrados de una minera de cobre — CMMS (CSV), ERP (Excel) y tabla HTML de benchmarks de industria — reduciendo la preparación manual de **4–6 horas semanales a menos de 5 minutos por ejecución** (~50x de mejora). El análisis revela que la inconsistencia estructural en las exportaciones de los sistemas de origen es el problema dominante, no los valores faltantes — y que corregir las plantillas de exportación en el CMMS y el ERP eliminaría la mayor parte del trabajo de limpieza downstream.

---

## 1. Contexto de Negocio

| | |
|---|---|
| **Industria** | Minería — Operaciones de Cobre |
| **Unidad de Negocio** | Operaciones & Mantenimiento |
| **Stakeholder** | Director de Operaciones / Jefe de Mantenimiento |
| **Decisión a Apoyar** | ¿Puede automatizarse el reporte diario de KPIs (disponibilidad, producción, costo de mantenimiento) sin preparación manual de datos? |

> **Situación:** Una minera de cobre de tamaño mediano consolida datos operacionales desde tres sistemas no integrados: un CMMS que exporta registros de mantenimiento en CSV, un ERP que exporta reportes de producción en Excel, y tablas web públicas con benchmarks de la industria. Cada fuente llega semanalmente con problemas de calidad que requieren 4–6 horas de limpieza manual antes de poder generar cualquier reporte — bloqueando las decisiones operacionales hasta en un día hábil.

---

## 2. Problema

> ¿Puede un pipeline Pandas cargar, limpiar y estandarizar automáticamente datos desde tres fuentes heterogéneas para habilitar reportería operacional diaria sin intervención humana?

**Impacto si no se resuelve:**
- 4–6 horas/semana de trabajo analítico en preparación manual (~$10–15k USD/año en costo laboral)
- Dashboards de KPIs retrasados hasta 1 día hábil — decisiones de mantenimiento tomadas sobre datos desactualizados
- Registros de producción duplicados inflan el tonelaje reportado, distorsionando métricas de desempeño
- Sin reproducibilidad — los pasos manuales no están documentados y dependen del operador

---

## 3. Enfoque Analítico

| Aspecto | Detalle |
|---|---|
| **Datos** | Tres fuentes simuladas que replican arquitectura real de faena: 120 registros de mantenimiento (CSV), 90 registros diarios de producción (Excel), tabla de referencia de 8 minas (HTML) |
| **Método** | Pipeline CRISP-DM Fase 3: carga → auditoría → limpieza → transformación → exportación |
| **Herramienta** | Python · pandas 3.0.0 · openpyxl · lxml |
| **Validación** | Assertions validan completitud, duplicados y tipos de dato en cada paso antes de continuar |

---

## 4. Hallazgos Principales

### Hallazgo 1 — La inconsistencia estructural es el problema dominante, no los valores nulos

- **Contexto:** Las tres fuentes fueron cargadas y auditadas antes de aplicar cualquier limpieza.
- **Análisis:** Los errores de tipo y las inconsistencias de nomenclatura (nombres de columnas con caracteres especiales, columnas de tipo mixto, casing inconsistente) superaron en número a los valores nulos. La fuente Excel tenía 7 filas duplicadas (~8%) y 3 columnas con nombres que contenían espacios y paréntesis — incompatibles con joins automatizados.
- **Insight:** La causa raíz está upstream — configuraciones de exportación inconsistentes en el CMMS y el ERP, no errores de ingreso de datos. Corregir las plantillas de exportación eliminaría la mayor parte del trabajo de limpieza downstream.
- **Decisión posible:** TI de Operaciones debe estandarizar las plantillas de exportación del CMMS y el ERP para forzar nomenclatura consistente y eliminar el comportamiento de exportación duplicada en origen.

### Hallazgo 2 — Imputación por mediana preserva el 15% de registros de mantenimiento con costo aceptable

- **Contexto:** La columna `maintenance_cost` tenía ~15% de valores nulos — una tasa demasiado alta para eliminar filas sin perder confiabilidad estadística.
- **Análisis:** La distribución de costos presentaba sesgo positivo (rango: $500–$15.000 USD). Se eligió imputación por mediana ($4.823 USD) sobre la media para evitar inflar la tendencia central por eventos de alto costo atípico.
- **Insight:** Los registros imputados quedan marcados implícitamente por el pipeline — cualquier análisis downstream debe tratar los valores de costo imputados como estimaciones, no como valores reales. Los intervalos de confianza en KPIs de costo deben reflejar esta incertidumbre.
- **Decisión posible:** El equipo de mantenimiento debe establecer el ingreso de costo como campo obligatorio en el cierre de órdenes de trabajo en el CMMS para eliminar nulos en origen en un plazo de 60 días.

### Hallazgo 3 — El pipeline reduce la preparación de datos de horas a minutos

- **Contexto:** La limpieza manual actual toma 4–6 horas semanales para las tres fuentes.
- **Análisis:** El pipeline completo — carga, auditoría, limpieza, transformación, exportación — ejecuta en menos de 5 minutos en un laptop estándar, con validación por assertions en cada paso.
- **Insight:** El pipeline es reproducible e independiente del operador. El mismo input siempre produce el mismo output, eliminando los pasos manuales no documentados que actualmente generan problemas de control de versiones y auditoría.
- **Decisión posible:** Programar el pipeline para ejecución diaria automatizada (cron/Airflow) para entregar datasets listos para análisis a la capa de BI cada mañana antes de la revisión del turno de operaciones.

---

## 5. Recomendaciones (Priorizadas)

| Prioridad | Recomendación | Impacto Esperado | Esfuerzo |
|---|---|---|---|
| 🔴 Alto | Programar pipeline para ejecución diaria automatizada | Elimina 4–6 h/semana de preparación manual; habilita reportería KPI el mismo día | Bajo |
| 🔴 Alto | Forzar ingreso obligatorio de `maintenance_cost` en cierre de OT en el CMMS | Elimina ~15% de tasa de nulos; mejora confiabilidad del KPI de costos | Bajo |
| 🟡 Medio | Estandarizar plantillas de exportación del ERP y CMMS (nombres de columnas, sin duplicados) | Elimina inconsistencia estructural en origen; reduce complejidad del pipeline | Medio |
| 🟢 Bajo | Extender pipeline con paso `merge` uniendo mantenimiento y producción por `faena` | Habilita análisis integrado de disponibilidad + costo en un solo dataset | Bajo |

---

## 6. Limitaciones

- **Datos:** Datasets simulados — los volúmenes de producción y costos reales diferirán; la lógica del pipeline está validada pero las métricas de negocio requieren datos reales antes de su uso en decisiones
- **Método:** Ingesta y preparación únicamente — sin análisis predictivo ni diagnóstico en esta versión
- **Alcance:** Nulos de `maintenance_cost` imputados con mediana — los valores imputados deben tratarse como estimaciones en cálculos de KPI de costos, no como valores reales

---

## 7. Próximos Pasos

| Horizonte | Acción |
|---|---|
| **Inmediato** | Usar `equipment_maintenance_clean.csv` como input para caso EDA M3 (frecuencia por tipo de falla, costo por tipo de equipo) |
| **Corto plazo** | Agregar paso de merge uniendo producción y mantenimiento por `faena` para dashboard integrado de disponibilidad + costo |
| **Largo plazo** | Programar pipeline para ejecución diaria automatizada vía cron o Apache Airflow en entorno de producción |

---

## 8. Entregables del Caso

| Archivo | Propósito |
|---|---|
| `notebooks/01_mining_ops_data_consolidation.ipynb` | Análisis CRISP-DM + LEAN completo; pipeline de ingesta multi-fuente ejecutado y validado |
| `data/raw/` | Datos simulados de las tres fuentes (CSV, Excel, HTML) |
| `data/processed/` | Datasets limpios listos para análisis |
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

**Fuente de datos:** Datos simulados — arquitectura equivalente a sistemas reales de faena minera
**Fecha de ejecución:** Abril 2026
**Estado:** ✅ Análisis completo | Pipeline validado con assertions | Listo para producción
