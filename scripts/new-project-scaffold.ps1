# ============================================================================
# new-project-scaffold.ps1 — PBL (Project-Based Learning) CRISP-DM + LEAN
# Version: 1.1 | 2026-04-06
# ============================================================================
param(
    [string]$ProjectName
)

# Si no se pasa ProjectName, pedirlo al usuario
if (-not $ProjectName) {
    $ProjectName = Read-Host "Ingresa el nombre del proyecto (ej. project-8-retailmax-big-data)"
}

# Resolve portfolio root as the parent of the scripts\ folder
$PortfolioRoot = Split-Path -Parent $PSScriptRoot
$ProjectsPath  = Join-Path $PortfolioRoot "projects"
$ProjectPath   = Join-Path $ProjectsPath $ProjectName

# Validar nombre estilo kebab-case
if ($ProjectName -notmatch '^project-\d+-[a-z0-9]+(-[a-z0-9]+)*$') {
    Write-Host "WARNING: Name '$ProjectName' may not follow convention: project-N-descriptive-name" -ForegroundColor Yellow
    Write-Host "Example: project-8-retailmax-big-data" -ForegroundColor Yellow
}

# Abort if project already exists
if (Test-Path $ProjectPath) {
    Write-Host "ERROR: Project already exists at $ProjectPath" -ForegroundColor Red
    exit 1
}

Write-Host "Creating new PBL project: $ProjectName in $ProjectPath" -ForegroundColor Green

# ==========================================================================
# 1. Crear estructura de directorios
# ==========================================================================
$Dirs = @(
    "data\raw",
    "data\processed",
    "data\final",
    "notebooks",
    "src",
    "docs"
)

foreach ($Dir in $Dirs) {
    New-Item -ItemType Directory -Path (Join-Path $ProjectPath $Dir) -Force | Out-Null
}

Set-Location $ProjectPath

# ==========================================================================
# 2. project.yaml — metadata
# ==========================================================================
@"
name: $ProjectName
type: PBL
framework: CRISP-DM + LEAN
author: Jose Marcel Lopez Pino
created: $(Get-Date -Format 'yyyy-MM-dd')
status: In Progress
module: "M9 - Fundamentos de Big Data"
python: "3.12"
"@ | Out-File project.yaml -Encoding UTF8

# ==========================================================================
# 3. .gitignore — project-level
# ==========================================================================
@"
# Data files (raw data excluded from Git)
data/raw/*
data/processed/*
data/final/*
!data/raw/README.md
!data/processed/README.md
!data/final/README.md

# Parquet and large files
*.parquet
*.snappy

# Spark
spark-warehouse/
metastore_db/
derby.log

# Models
models/*.pkl
models/*.joblib

# OS
.DS_Store
Thumbs.db
"@ | Out-File .gitignore -Encoding UTF8

# ==========================================================================
# 4. README.md — placeholder
# ==========================================================================
@"
# $ProjectName

> **CRISP-DM + LEAN — PBL Project** | Module 9: Fundamentos de Big Data

![Status](https://img.shields.io/badge/Status-In%20Progress-orange)
![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![Framework](https://img.shields.io/badge/Framework-CRISP--DM%20%2B%20LEAN-2E86AB)
![Type](https://img.shields.io/badge/Type-Big%20Data%20%2B%20ML-blueviolet)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

> README will be completed after all 6 CRISP-DM notebooks are finished.
> See ``notebooks/`` for current progress.
"@ | Out-File README.md -Encoding UTF8

# ==========================================================================
# 5. src/__init__.py
# ==========================================================================
@"
# $ProjectName — source modules
"@ | Out-File src\__init__.py -Encoding UTF8

Write-Host "Project scaffold created successfully!" -ForegroundColor Cyan