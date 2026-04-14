# 426x Más Rápido: Métricas en Tiempo Real para Carteras Mineras con NumPy
### Analytics de Portafolio — BHP, FCX, RIO, VALE, SCCO | CRISP-DM + LEAN

**Autor:** Jose Marcel Lopez Pino
**Rol:** Data Scientist — Operaciones, Analytics & Optimización de Procesos
**Framework:** CRISP-DM + LEAN | Aprendizaje Basado en Casos (CBL)
**Módulo:** M3 — Adquisición y Preparación de Datos (Bootcamp Alkemy)
**Fecha:** Abril 2026
**Estado:** ✅ Completo

---

## Conclusión Ejecutiva

La migración de pipelines Python basados en loops a operaciones vectorizadas con NumPy entrega una aceleración de **426 veces** en el cómputo de métricas financieras para carteras mineras — sin cambios de infraestructura y con código más simple y legible. El análisis sobre precios reales de BHP, FCX, RIO, VALE y SCCO confirma que SCCO fue el activo de mayor retorno de la semana (+11,8% acumulado), con una recuperación sincronizada de todo el sector el día 3→4 que sugiere un catalizador macroeconómico común.

---

## 1. Contexto de Negocio

| | |
|---|---|
| **Industria** | Servicios Financieros — Renta Variable Minera |
| **Unidad de Negocio** | Gestión de Activos / Analytics de Portafolio |
| **Stakeholder** | Portfolio Manager |
| **Decisión a Apoyar** | ¿Debe el pipeline de analytics migrar de Python con loops a operaciones vectorizadas con NumPy? |

> **Situación:** Una firma de analytics financiero que monitorea carteras de renta variable minera opera con pipelines Python basados en loops anidados. A medida que crece el volumen de datos — más activos, ventanas de tiempo más largas — estos pipelines generan cuellos de botella que retrasan el cómputo de métricas en tiempo real, impactando directamente los tiempos de respuesta del portfolio manager en mercados volátiles.

---

## 2. Problema

> ¿Pueden las operaciones vectorizadas de NumPy reemplazar los loops Python para el cómputo de métricas financieras, reduciendo la complejidad del código y entregando ganancias de rendimiento medibles?

**Impacto si no se resuelve:**
- El retraso en métricas aumenta la latencia de decisión del portfolio manager — en mercados volátiles, los minutos importan
- Los pipelines con loops no escalan: agregar activos o extender ventanas de tiempo agrava el problema de rendimiento linealmente

---

## 3. Enfoque Analítico

| Aspecto | Detalle |
|---|---|
| **Datos** | Precios de cierre reales vía yfinance — BHP, FCX, RIO, VALE, SCCO — 5 días de trading (2026-03-26 → 2026-04-01) |
| **Método** | Estadísticas descriptivas, retornos diarios, retornos logarítmicos, normalización min-max, z-scores e índice de precio base 100 — todo vía broadcasting NumPy, sin loops explícitos |
| **Herramienta** | Python 3.12 · NumPy 2.4.1 · yfinance · matplotlib |
| **Validación** | Resultados NumPy verificados contra baseline Python con `np.allclose()` — resultados idénticos |

---

## 4. Hallazgos Principales

### Hallazgo 1 — SCCO fue el activo de mejor desempeño de la semana

- **Contexto:** Cinco acciones mineras vinculadas al cobre fueron monitoreadas durante 5 días de trading consecutivos.
- **Análisis:** SCCO entregó el mayor retorno diario (+8,024%, Día 3→4) y el mayor retorno acumulado a 5 días (+11,799%). FCX registró el peor retorno diario (-2,827%, Día 2→3).
- **Insight:** SCCO mostró tanto el mayor upside como la mayor volatilidad intradía — patrón consistente con su mayor beta respecto al precio del cobre.
- **Decisión posible:** El portfolio manager podría revisar el sizing de la posición en SCCO dado su comportamiento amplificado ante movimientos del commodity durante el período observado.

### Hallazgo 2 — Todos los activos se recuperaron fuertemente el Día 3→4

- **Contexto:** El Día 2→3 mostró retornos mixtos o negativos en la mayoría de los activos (FCX -2,827%, SCCO -1,721%, BHP -0,691%).
- **Análisis:** El Día 3→4 revirtió la tendencia con fuerza — los cinco activos registraron sus mayores ganancias diarias de la semana: SCCO +8,024%, FCX +7,557%, RIO +5,033%, BHP +5,390%, VALE +5,364%.
- **Insight:** La recuperación sincronizada de los cinco activos sugiere un catalizador sectorial (movimiento del precio del commodity o noticia macro) más que drivers específicos de cada empresa.
- **Decisión posible:** Monitorear catalizadores macro sectoriales como indicadores anticipados para decisiones de rebalanceo en posiciones mineras correlacionadas.

### Hallazgo 3 — NumPy entrega una aceleración de 426x sobre Python con loops

- **Contexto:** El pipeline actual usa loops Python anidados para el cómputo de métricas. A escala 5×5 la diferencia es invisible — pero el portafolio real opera con 500+ activos × 252 días de trading.
- **Análisis:** Benchmark a escala realista (500 activos × 252 días, 1.000 ejecuciones): Python con loops promedió 33,31 ms por llamada; NumPy promedió 0,08 ms — una aceleración de **426x**. El código se redujo de 6 líneas de loops anidados a 1 expresión NumPy legible.
- **Insight:** La brecha de rendimiento no es marginal — es estructural. El backend C vectorizado de NumPy elimina completamente el overhead del intérprete Python para operaciones sobre arrays.
- **Decisión posible:** Migrar el pipeline de analytics a NumPy de inmediato. Sin cambio de infraestructura — NumPy ya está disponible en todo entorno Python estándar de datos.

---

## 5. Recomendaciones (Priorizadas)

| Prioridad | Recomendación | Impacto Esperado | Esfuerzo |
|---|---|---|---|
| 🔴 Alto | Migrar el cómputo de métricas con loops a operaciones vectorizadas NumPy | 426x más rápido; métricas en tiempo real a escala completa del portafolio | Bajo — reemplazo directo, sin nueva infraestructura |
| 🟡 Medio | Extender la ventana de análisis a 30 días para habilitar volatilidad rolling y detección de tendencias | Señales más robustas para decisiones de rebalanceo | Medio — extensión del pipeline de datos |
| 🟢 Bajo | Modelar la volatilidad de activos vinculados al cobre (FCX, SCCO, VALE) usando GARCH — estándar de la industria para series financieras heterocedásticas | Estimaciones cuantificadas de volatilidad para gestión de riesgo | Alto — requiere expertise en modelado econométrico |

---

## 6. Limitaciones

- **Datos:** La ventana de 5 días es insuficiente para conclusiones de tendencia o volatilidad — extender a 30+ días mínimo para decisiones estratégicas
- **Modelo:** Análisis descriptivo únicamente — sin componente predictivo ni causal en esta versión
- **Alcance:** Solo precios de cierre ajustados — no considera volatilidad intradía, spreads bid-ask ni volumen de trading

---

## 7. Próximos Pasos

| Horizonte | Acción |
|---|---|
| **Inmediato** | Aplicar estos patrones NumPy como base para el módulo de pandas M3 |
| **Corto plazo** | Extender a ventana de 30 días para análisis de volatilidad rolling (`np.std` con ventana deslizante) |
| **Largo plazo** | Modelar volatilidad de activos vinculados al cobre (FCX, SCCO, VALE) usando GARCH — estándar de la industria para series financieras heterocedásticas. LSTM es una alternativa exploratoria válida con datos históricos suficientes (mínimo 12 meses), ya que puede capturar patrones temporales no lineales que GARCH no detecta — a costa de interpretabilidad y volumen de datos |

---

## 8. Entregables del Caso

| Archivo | Propósito |
|---|---|
| `notebooks/01_mining_stock_returns_numpy.ipynb` | Análisis CRISP-DM + LEAN completo; métricas vectorizadas y benchmark ejecutados |
| `data/raw/` | Precios de cierre descargados vía yfinance |
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

**Fuente de datos:** Yahoo Finance vía yfinance — precios reales de mercado
**Fecha de ejecución:** Abril 2026
**Estado:** ✅ Análisis completo | Datos reales | Todos los números provienen de la ejecución del notebook
