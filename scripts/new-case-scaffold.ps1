param(
    [Parameter(Mandatory=$true)]
    [string]$CaseName
)

Write-Host "🚀 Creating new case: $CaseName"

# Crear carpeta base
New-Item -ItemType Directory -Path $CaseName | Out-Null
Set-Location $CaseName

# Estructura
New-Item -ItemType Directory notebooks | Out-Null
New-Item -ItemType Directory src | Out-Null
New-Item -ItemType Directory data | Out-Null
New-Item -ItemType Directory reports | Out-Null

# README.md
@"
# $CaseName

## Problema
Describe el problema de negocio.

## Contexto
Contexto del caso (industria, tipo de datos, etc.)

## Objetivo
Qué quieres lograr.

## Metodología
- Ingesta
- Limpieza
- Transformación
- Modelado (si aplica)

## Resultados
Principales hallazgos.

## Impacto
- Mejora en decisiones
- Reducción de riesgo
- Optimización de procesos

## Stack
- Python
- Pandas / PySpark
- Otros

"@ | Out-File README.md

# Executive Summary
@"
# Executive Summary

## Contexto
Describe el contexto del problema.

## Solución
Qué hiciste a alto nivel.

## Resultados
- Métrica 1
- Métrica 2

## Impacto
- Beneficio 1
- Beneficio 2

"@ | Out-File reports/executive_summary.md

# requirements.txt
New-Item requirements.txt | Out-Null

# .gitignore
@"
.venv/
__pycache__/
*.pyc
data/*
"@ | Out-File .gitignore

Write-Host "✅ Case scaffold creado correctamente"