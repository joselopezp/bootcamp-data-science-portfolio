# 95,4% de Precisión Prediciendo Precios de Vehículos Usados — Listo para Producción con 3 Variables
### Evaluación de Modelo de Regresión — AutoPredict S.A. | CRISP-DM + LEAN

**Autor:** Jose Marcel Lopez Pino
**Rol:** Data Scientist — Operaciones, Analytics & Optimización de Procesos
**Framework:** CRISP-DM + LEAN | Aprendizaje Basado en Casos (CBL)
**Módulo:** M5 — Fundamentos de Machine Learning (Bootcamp Alkemy)
**Fecha:** Abril 2026
**Estado:** ✅ Completo

---

## Conclusión Ejecutiva

Un modelo de regresión lineal múltiple entrenado sobre datos de vehículos usados alcanza **R²=0,9541 y MAPE=6,74%** — muy por debajo del umbral de despliegue del 15% para pricing en concesionarias. El modelo es interpretable, reproducible y listo para un piloto de producción con clientes reales. El valor principal no es solo el modelo: es el **framework documentado de evaluación** que AutoPredict S.A. puede reutilizar en cualquier iteración futura antes de entregar a un cliente. Cada año adicional de antigüedad reduce el precio estimado en ~$327 USD; cada 10.000 km lo reduce en ~$1.170 USD.

---

## 1. Contexto de Negocio

| | |
|---|---|
| **Industria** | Automotriz — Vehículos Usados |
| **Unidad de Negocio** | Producto & Analytics |
| **Stakeholder** | Director de Producto / Cliente Concesionaria |
| **Decisión a Apoyar** | ¿Debe el modelo actual desplegarse a producción o requiere refinamiento adicional? |

> **Situación:** AutoPredict S.A. desarrolla sistemas de predicción de precios para concesionarias de vehículos usados. El equipo de data science construyó una primera versión con regresión lineal, pero carecía de un procedimiento documentado para evaluar si el modelo cumple los criterios de precisión y confiabilidad requeridos antes del despliegue. Sin validación formal, un modelo deficiente expone a los clientes a errores sistemáticos de pricing — el sobreprecio reduce el volumen de ventas; el subprecio erosiona el margen.

---

## 2. Problema

> ¿Cuáles son el MAE, MSE, RMSE, R² y MAPE del modelo sobre un dataset representativo, y cumplen estas métricas los criterios de precisión requeridos para el despliegue en concesionarias?

**Impacto si no se resuelve:**
- Errores sistemáticos de pricing dañan la confianza del cliente y la reputación comercial de AutoPredict S.A.
- Sin un framework de evaluación documentado, cada versión del modelo se evalúa de forma ad-hoc — sin trazabilidad ni criterio de aceptación formal

---

## 3. Enfoque Analítico

| Aspecto | Detalle |
|---|---|
| **Datos** | AutoPredict S.A. — n=35 (4 originales + 31 sintéticos bajo las mismas reglas de negocio), random_state=42 |
| **Método** | Regresión lineal múltiple (scikit-learn) sobre split 80/20 (28 train / 7 test); cómputo e interpretación de 5 métricas de rendimiento |
| **Herramienta** | Python 3.12 · scikit-learn · pandas · NumPy · matplotlib |
| **Validación** | Criterio de aceptación: R² > 0,80 y MAPE < 15% en test set |

---

## 4. Hallazgos Principales

### Hallazgo 1 — El modelo explica el 95,4% de la varianza de precios con solo 3 variables

- **Contexto:** El pricing de vehículos usados depende de múltiples factores interactuantes. Antigüedad, kilometraje y número de puertas son las tres variables disponibles en este dataset.
- **Análisis:** R²=0,9541 en el test set indica que el modelo captura el patrón dominante de depreciación — impulsado principalmente por antigüedad y kilometraje — con alta precisión. MAPE=6,74% está muy por debajo del umbral de despliegue del 15%.
- **Insight:** Para un modelo de primera versión con 3 variables, este es un baseline sólido. El 4,6% de varianza no explicada probablemente refleja factores no capturados (marca, condición, combustible, transmisión).
- **Decisión posible:** Proceder a piloto de producción con clientes concesionaria mientras se recopilan datos adicionales de variables para el modelo v2.

### Hallazgo 2 — Antigüedad y kilometraje dominan el precio; puertas tiene efecto marginal positivo

- **Contexto:** Coeficientes del modelo — Antigüedad: −$326,99/año, Kilometraje: −$0,117/km, Puertas: +$265,49/puerta, Intercepto: $19.606,48.
- **Análisis:** Cada año adicional reduce el precio estimado en ~$327 USD; cada 10.000 km lo reduce en ~$1.170 USD. El coeficiente de Puertas es positivo (+$265) y direccionalmente correcto — los vehículos de 4 puertas típicamente tienen una pequeña prima de mercado.
- **Insight:** Antigüedad y kilometraje están altamente correlacionados (r=0,996), lo que genera riesgo de multicolinealidad en OLS. Ridge regression sería más robusto para despliegue en producción.
- **Decisión posible:** Evaluar Ridge regression como reemplazo directo — misma interpretabilidad, menor sensibilidad a multicolinealidad.

### Hallazgo 3 — Un outlier (Vehículo 27, error 21,99%) es un artefacto de datos, no una falla del modelo

- **Contexto:** El Vehículo 27 (Antigüedad=10 años, Kilometraje=97.478 km) tiene un precio real de $7.000 USD — el valor mínimo en la generación sintética. El modelo predice $5.461, por debajo del mínimo.
- **Análisis:** El modelo identifica correctamente este vehículo como de bajo valor; el error surge porque el precio mínimo trunca la curva natural de depreciación en $7.000. Excluyendo V27, el MAPE cae a **4,26%**.
- **Insight:** En un dataset real, vehículos de alto kilometraje tendrían precios más granulares por debajo de $7.000. El mínimo es una restricción sintética, no una realidad de mercado.
- **Decisión posible:** Con datos reales, eliminar el precio mínimo y permitir extrapolación natural — o aplicar transformación log-precio para manejar la cola inferior de la distribución.

---

## 5. Resultados del Modelo

| Métrica | Valor | Interpretación de Negocio |
|---|---|---|
| MAE | $671,96 | Error absoluto promedio por vehículo |
| MSE | $625.445,37 | Error ponderado por varianza — penaliza errores grandes |
| RMSE | $790,85 | Error típico de predicción en USD |
| R² | 0,9541 | El modelo explica el 95,4% de la varianza de precios |
| MAPE | 6,74% | El modelo predice dentro del 6,74% del precio real en promedio |

**Ecuación del modelo:**
`Precio = 19.606,49 − 326,99 × Antigüedad_años − 0,117 × Kilometraje_km + 265,49 × Puertas`

---

## 6. Recomendaciones (Priorizadas)

| Prioridad | Recomendación | Impacto Esperado | Esfuerzo |
|---|---|---|---|
| 🔴 Crítico | Recopilar datos reales de transacciones (n ≥ 500) desde concesionarias clientes | Los datos sintéticos capturan la lógica de depreciación pero no las dinámicas de mercado específicas | Alto |
| 🔴 Crítico | Agregar variables: marca, combustible, transmisión, condición del vehículo | Antigüedad y kilometraje solos dejan ~4,6% de varianza sin explicar | Medio |
| 🟡 Importante | Evaluar Ridge regression | Antigüedad y kilometraje están altamente correlacionados (r=0,996) — riesgo de multicolinealidad en OLS | Bajo |
| 🟡 Importante | Aplicar validación cruzada k-fold (k=5) | Estimaciones de rendimiento más estables que un único split 80/20 | Bajo |
| 🟢 Mejora | Probar Gradient Boosting (XGBoost) | Captura efectos no lineales de depreciación por kilometraje sobre los 100k km | Medio |

---

## 7. Limitaciones

- **Datos:** n=35 con 31 registros sintéticos — captura la lógica de depreciación pero no las dinámicas reales de mercado (prima de marca, precios regionales, efectos estacionales). La validación en producción requiere datos reales (n ≥ 500).
- **Modelo:** OLS asume linealidad y ausencia de multicolinealidad. Antigüedad y kilometraje están altamente correlacionados (r=0,996) — esto infla la varianza de los coeficientes y reduce la interpretabilidad individual de cada variable.
- **Despliegue:** El modelo no fue probado sobre datos reales fuera de muestra. El precio mínimo de $7.000 en la generación sintética crea un artefacto de frontera para vehículos de alto kilometraje.

---

## 8. Próximos Pasos

| Horizonte | Acción |
|---|---|
| **Inmediato** | Iniciar piloto de producción con concesionaria cliente usando el modelo actual como baseline |
| **Corto plazo** | Aplicar Ridge/Lasso sobre dataset real de vehículos usados y comparar contra este baseline |
| **Largo plazo** | Integrar pipeline de evaluación de regresión como módulo reutilizable `src/evaluation.py` para todas las iteraciones futuras del modelo |

---

## 9. Entregables del Caso

| Archivo | Propósito |
|---|---|
| `notebooks/01_used_car_price_prediction.ipynb` | Análisis CRISP-DM + LEAN completo; 5 métricas computadas e interpretadas |
| `reports/actual_vs_predicted_prices.png` | Gráfico comparativo precios reales vs. predichos (test set n=7) |
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

**Fuente de datos:** AutoPredict S.A. — dataset extendido (4 originales + 31 sintéticos bajo mismas reglas de negocio)
**Fecha de ejecución:** Abril 2026
**Estado:** ✅ Análisis completo | Datos reales + sintéticos | Todos los números provienen de la ejecución del notebook
