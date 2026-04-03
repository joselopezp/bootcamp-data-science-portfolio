param(
    [Parameter(Mandatory=$true)]
    [string]$CaseName
)

# Resolve portfolio root as the parent of the scripts\ folder
$PortfolioRoot = Split-Path -Parent $PSScriptRoot
$CasesPath     = Join-Path $PortfolioRoot "cases"
$CasePath      = Join-Path $CasesPath $CaseName

Write-Host "🚀 Creating new CBL case: $CaseName"

# Create base folder inside cases\
New-Item -ItemType Directory -Path $CasePath | Out-Null
Set-Location $CasePath

# Create standard CBL folder structure
New-Item -ItemType Directory notebooks | Out-Null
New-Item -ItemType Directory src       | Out-Null
New-Item -ItemType Directory data      | Out-Null
New-Item -ItemType Directory reports   | Out-Null

# README.md — primary CBL deliverable (populate before executive summary)
@"
# $CaseName

## Business Problem
Describe the business problem.

## Context
Case context (industry, data type, etc.)

## Objective
What you want to achieve.

## Methodology
- Ingestion
- Cleaning
- Transformation
- Modeling (if applicable)

## Results
Key findings.

## Business Impact
- Improved decision-making
- Risk reduction
- Process optimization

## Stack
- Python
- Pandas / PySpark
- Other
"@ | Out-File README.md

# Create CBL notebook skeleton — standard cell structure (SKILL_DATA_SCIENCE)
$NotebookName = $CaseName -replace '-', '_'
@"
{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Case Study — Module MN: [Module Name]\n",
    "## [Lesson Title]\n",
    "\n",
    "| | |\n",
    "|---|---|\n",
    "| **Author** | Jose Marcel Lopez Pino |\n",
    "| **Framework** | CRISP-DM + LEAN |\n",
    "| **Phases** | Phase N — [Phase Name] |\n",
    "| **Module** | MN — [Module Name] (Alkemy Bootcamp) |\n",
    "| **Dataset** | [Dataset name and source] |\n",
    "| **Case** | LN — [Case Title] |\n",
    "| **Date** | YYYY-MM |\n",
    "\n",
    "---\n",
    "\n",
    "> **Executive Summary:**\n",
    "> [2-3 sentences: what this case does, what decision it enables, what the key output is.]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Table of Contents\n",
    "\n",
    "1. [Phase 1 — Business Understanding](#phase-1)\n",
    "2. [Phase 2 — Data Understanding](#phase-2)\n",
    "3. [Phase 3 — Analysis / Modeling](#phase-3)\n",
    "4. [Phase 5 — Evaluation and Reflection](#phase-5)\n",
    "5. [LEAN Filter — Waste Elimination Review](#lean-filter)\n",
    "6. [Decisions Log](#decisions-log)\n",
    "7. [Next Steps](#next-steps)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "---\n",
    "\n",
    "## 1. Phase 1 — Business Understanding <a id='phase-1'></a>\n",
    "\n",
    "### Problem Statement Canvas\n",
    "\n",
    "| Element | Description |\n",
    "|---|---|\n",
    "| **Business Problem** | [What hurts? What is broken?] |\n",
    "| **Business Impact** | [What does it cost? (%, customers, CLP)] |\n",
    "| **Decision to Support** | [What decision do we want to improve?] |\n",
    "| **Analytical Question** | [What prediction/analysis answers the decision?] |\n",
    "| **Success Metrics** | [How do we measure success?] |\n",
    "| **Proposed Approach** | [What model/analysis will we use?] |\n",
    "\n",
    "### Personal Perspective — ICI Background\n",
    "\n",
    "[Connect the analytical problem to an operations/process engineering analogy.]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "---\n",
    "\n",
    "## 2. Phase 2 — Data Understanding <a id='phase-2'></a>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# =============================================================================\n",
    "# IMPORTS\n",
    "# Standard Library\n",
    "import warnings\n",
    "\n",
    "# Core Data Science\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "\n",
    "# ML\n",
    "# from sklearn... import ...\n",
    "\n",
    "# Visualization\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "\n",
    "# Configuration\n",
    "warnings.formatwarning = lambda msg, *args, **kwargs: f'Warning: {msg}\n",
    "'\n",
    "warnings.simplefilter('always')\n",
    "\n",
    "pd.set_option('display.float_format', '{:.4f}'.format)\n",
    "pd.set_option('display.max_columns', None)\n",
    "\n",
    "print('Environment ready.')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "---\n",
    "\n",
    "## 3. Phase 3 — Analysis / Modeling <a id='phase-3'></a>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "---\n",
    "\n",
    "## 4. Phase 5 — Evaluation and Reflection <a id='phase-5'></a>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "---\n",
    "\n",
    "## 5. LEAN Filter — Waste Elimination Review <a id='lean-filter'></a>\n",
    "\n",
    "| LEAN Waste Type | Identified? | Detail | Eliminated? |\n",
    "|---|---|---|---|\n",
    "| **Defects** | | | |\n",
    "| **Overprocessing** | | | |\n",
    "| **Waiting** | | | |\n",
    "| **Inventory (data)** | | | |\n",
    "| **Motion** | | | |\n",
    "| **Transport** | | | |"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "---\n",
    "\n",
    "## 6. Decisions Log <a id='decisions-log'></a>\n",
    "\n",
    "| # | Decision | Rationale | LEAN Value | Alternative Considered |\n",
    "|---|---|---|---|---|\n",
    "| D1 | | | | |\n",
    "| D2 | | | | |"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "---\n",
    "\n",
    "## 7. Next Steps <a id='next-steps'></a>\n",
    "\n",
    "| Priority | Next Step | Module |\n",
    "|---|---|---|\n",
    "| 🔴 Immediate | | |\n",
    "| 🟡 Short-term | | |\n",
    "| 🟢 Long-term | | |\n",
    "\n",
    "---\n",
    "\n",
    "*Framework: CRISP-DM + LEAN | Methodology: Case-Based Learning (CBL)*\n",
    "\n",
    "**Jose Marcel Lopez Pino**  \n",
    "Data Scientist — Operations, Analytics & Process Optimization  \n",
    "Bootcamp: Fundamentos de Ciencia de Datos — SENCE/Alkemy (2025–2026)\n",
    "\n",
    "[![GitHub](https://img.shields.io/badge/GitHub-joselopezp-181717?style=flat&logo=github)](https://github.com/joselopezp)\n",
    "[![LinkedIn](https://img.shields.io/badge/LinkedIn-jose--lopez--pino-0077B5?style=flat&logo=linkedin)](https://www.linkedin.com/in/jose-lopez-pino/)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": ".venv (3.12.10)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbformat": 4,
   "nbformat_minor": 5,
   "pygments_lexer": "ipython3",
   "version": "3.12.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
"@ | Out-File "notebooks\$NotebookName.ipynb" -Encoding UTF8

# reports/executive_summary.md — main deliverable for CBL cases
@"
# Executive Summary

## Context
Describe the business context.

## Solution
High-level description of what was done.

## Results
- Metric 1
- Metric 2

## Business Impact
- Benefit 1
- Benefit 2
"@ | Out-File reports/executive_summary.md

Write-Host "✅ CBL case scaffold created at: $CasePath"