# Descubriendo Segmentos Ocultos de Clientes: PCA vs t-SNE en 2.240 Clientes Reales
### Targeting de Campañas de Marketing — Analytics de Personalidad de Clientes | CRISP-DM + LEAN

**Autor:** Jose Marcel Lopez Pino
**Rol:** Data Scientist — Operaciones, Analytics & Optimización de Procesos
**Framework:** CRISP-DM + LEAN | Aprendizaje Basado en Casos (CBL)
**Módulo:** M7 — Machine Learning No Supervisado (Bootcamp Alkemy)
**Fecha:** Abril 2026
**Estado:** ✅ Completo

---

## Conclusión Ejecutiva

Dos técnicas de reducción de dimensionalidad — PCA y t-SNE — fueron aplicadas y comparadas sobre datos reales de 2.240 clientes (30 variables de demografía, gasto por categoría, comportamiento de canal y respuesta a campañas). **t-SNE revela segmentos de clientes compactos y bien separados** (KL divergence = 0,8887) que PCA no puede exponer en 2D — directamente accionables para el equipo de marketing sin necesidad de expertise estadístico. PCA, en cambio, es la herramienta correcta para preprocesamiento en pipelines ML (95% de varianza en 24 componentes). Recomendación: **dos pistas complementarias** — t-SNE para descubrimiento y presentación de segmentos; PCA para todo el preprocesamiento ML.

---

## 1. Contexto de Negocio

| | |
|---|---|
| **Industria** | Analytics de Clientes / Consultoría de Marketing |
| **Unidad de Negocio** | Analytics & Visualización |
| **Stakeholder** | Director de Marketing |
| **Decisión a Apoyar** | ¿Qué técnica de reducción de dimensionalidad debe usarse para revelar segmentos naturales de clientes para targeting de campañas? |

> **Situación:** Una consultora de analytics de clientes recibió un dataset de encuesta con más de 100 variables por cliente — demografía, hábitos de consumo y preferencias digitales. Los modelos ML actuales tienen bajo rendimiento por la alta dimensionalidad, y las visualizaciones ejecutivas no logran comunicar patrones claros de clientes al equipo de marketing.

---

## 2. Problema

> ¿Cómo comprimir un dataset de alta dimensionalidad a 2D preservando suficiente estructura para revelar segmentos naturales de clientes para campañas de marketing diferenciadas?

**Impacto si no se resuelve:**
- Todos los clientes son tratados de igual forma — sin targeting diferenciado de campañas
- Los tiempos de entrenamiento de modelos ML permanecen prohibitivos a dimensionalidad completa
- El equipo de marketing no puede actuar sobre visualizaciones de 100 variables ilegibles

---

## 3. Enfoque Analítico

| Aspecto | Detalle |
|---|---|
| **Datos** | Customer Personality Analysis (Kaggle) — 2.240 clientes × 29 variables. Ingeniería de variables a 30 features: edad, antigüedad, gasto por categoría, comportamiento de canal, respuesta a campañas, demografía codificada |
| **Método** | Dos técnicas de reducción de dimensionalidad aplicadas y comparadas: PCA (lineal, global) y t-SNE (no lineal, local). Pre-reducción PCA a 24 componentes (95% varianza) aplicada antes de t-SNE como buena práctica de la industria |
| **Herramienta** | Python · scikit-learn · matplotlib |
| **Validación** | PCA: curva de varianza explicada acumulada. t-SNE: minimización de KL divergence (final = 0,8887, bajo umbral de 1,0) |

---

## 4. Hallazgos Principales

### Hallazgo 1 — PCA retiene varianza limitada en 2D

- **Contexto:** Marketing necesita una visualización 2D para presentar segmentos de clientes en reuniones ejecutivas.
- **Análisis:** PCA comprimió 30 variables a 2 componentes reteniendo solo el **28,8%** de la varianza total (PC1 = 21,5%, PC2 = 7,3%). Alcanzar el 80% de varianza requiere 16 componentes; el 95% requiere 24.
- **Insight:** Una proyección PCA en 2D pierde más del 70% de la información — insuficiente para revelar clusters de clientes claramente en forma visual, aunque los ejes mantienen interpretabilidad (PC1 impulsado por variables de gasto).
- **Decisión posible:** Usar PCA con 24 componentes como paso de preprocesamiento antes de modelos ML — no como herramienta principal de visualización para presentaciones de marketing.

### Hallazgo 2 — t-SNE revela clusters de clientes compactos y bien separados

- **Contexto:** Los mismos 2.240 clientes proyectados en 2D con t-SNE (perplexity=40, 1.000 iteraciones).
- **Análisis:** t-SNE alcanzó una KL divergence de **0,8887** — bajo el umbral de calidad de 1,0 — con estructuras de clusters visualmente distintas no visibles en PCA.
- **Insight:** t-SNE revela exitosamente agrupaciones naturales de clientes que PCA no puede exponer en 2D, haciéndolo directamente accionable para el equipo de marketing.
- **Decisión posible:** Usar el output 2D de t-SNE como base para los mapas de segmentos de clientes en presentaciones de marketing. Combinar con etiquetas KMeans en el siguiente paso de análisis.

### Hallazgo 3 — Las dos técnicas son complementarias, no competidoras

- **Contexto:** El equipo de marketing necesita tanto visualizaciones ejecutivas (exploración) como un paso de preprocesamiento para modelos predictivos (pipeline).
- **Análisis:** t-SNE no tiene método `transform()` — no puede puntuar nuevos clientes ni integrarse en pipelines sklearn. PCA sí.
- **Insight:** Las dos técnicas resuelven problemas distintos. Una recomendación de herramienta única sería analíticamente limitante (solo PCA) u operacionalmente incompleta (solo t-SNE).
- **Decisión posible:** Adoptar un enfoque de dos pistas: t-SNE para descubrimiento de segmentos y presentación; PCA (24 componentes) para todo el preprocesamiento de pipelines ML.

---

## 5. Recomendaciones (Priorizadas)

| Prioridad | Recomendación | Impacto Esperado | Esfuerzo |
|---|---|---|---|
| 🔴 Alto | Desplegar visualización t-SNE para presentación de segmentos de marketing | Habilita targeting diferenciado de campañas por segmento identificado | Bajo |
| 🔴 Alto | Aplicar PCA (24 componentes, 95% varianza) como preprocesamiento para todos los modelos ML downstream | Reduce tiempo de entrenamiento; elimina ruido de 30 → 24 dimensiones | Bajo |
| 🟡 Medio | Combinar clusters t-SNE con etiquetas KMeans para perfiles de segmento accionables | Cuantifica tamaño y características del segmento para asignación de presupuesto | Medio |
| 🟢 Bajo | Evaluar UMAP como reemplazo de largo plazo para t-SNE | Más rápido a escala, soporta `transform()`, mejor preservación de estructura global | Medio |

---

## 6. Limitaciones

- **Datos:** Dataset cubre una sola fotografía temporal — sin comportamiento temporal. Los segmentos de clientes pueden cambiar estacionalmente
- **Modelo:** Los ejes de t-SNE no tienen significado — las distancias entre clusters no son confiables. Calidad de clusters no validada formalmente (silhouette score pendiente)
- **Estado civil:** Categoría `YOLO` presente en datos originales — mantenida tal cual; puede reflejar problemas de calidad en la encuesta original
- **Alcance:** Fase de despliegue fuera de alcance para este caso CBL — sin integración de pipeline de producción

---

## 7. Próximos Pasos

| Horizonte | Acción |
|---|---|
| **Inmediato** | Aplicar PCA (24 componentes) como paso de preprocesamiento antes de KMeans — validar calidad de clusters con silhouette score |
| **Corto plazo** | Superponer etiquetas KMeans sobre plot t-SNE — producir mapa de segmentos con código de colores para presentación de marketing |
| **Largo plazo** | Evaluar UMAP para escala de producción (>50k clientes) — soporta `transform()` para scoring de clientes en tiempo real |

---

## 8. Entregables del Caso

| Archivo | Propósito |
|---|---|
| `notebooks/01_marketing_customer_segmentation.ipynb` | Análisis CRISP-DM + LEAN completo; PCA y t-SNE aplicados y comparados |
| `data/raw/marketing_campaign.csv` | Dataset original Kaggle (2.240 clientes, 29 variables) |
| `data/processed/marketing_scaled.csv` | Output StandardScaler (30 variables) |
| `reports/figures/` | 5 visualizaciones: distribuciones de gasto, varianza PCA, proyección PCA 2D, proyección t-SNE 2D, comparación |
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

**Fuente de datos:** Customer Personality Analysis — Kaggle (imakash3011) — datos reales de campaña de marketing
**Fecha de ejecución:** Abril 2026
**Estado:** ✅ Análisis completo | 5 visualizaciones generadas | Recomendación de dos pistas documentada
