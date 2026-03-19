# Configuración del Entorno de Desarrollo - Bootcamp Data Science

## Información General

| Campo | Valor |
|-------|-------|
| **Fecha de configuración** | Enero 2025 |
| **Última actualización** | Febrero 2026 |
| **Python** | 3.12.10 |
| **Tipo de entorno** | Virtual environment (.venv) |
| **IDE principal** | VS Code |
| **Notebooks** | Jupyter (integrado en VS Code) |

---

## Estructura del Proyecto

```
Bootcamp_Data_Science_Portfolio/
├── .venv/                          # Entorno virtual (no subir a Git)
├── Learning/                       # Ejercicios de práctica (no subir a Git)
├── Projects/                       # Proyectos de portafolio
│   ├── Module_2_Contact_System/    # Proyecto Módulo 2: OOP
│   └── Module_3_Data_Preparation/  # Proyecto Módulo 3: ETL Pipeline
│       ├── data/
│       │   ├── raw/                # Datos originales
│       │   └── processed/          # Datos limpios
│       ├── notebooks/
│       ├── docs/
│       └── README.md
├── .gitignore
├── entorno_desarrollo_bootcamp.md  # Este archivo
├── README.md
└── requirements.txt                # Dependencias del proyecto
```

---

## Paquetes Instalados

### Esenciales para Data Science
| Paquete | Propósito |
|---------|-----------|
| **numpy** | Operaciones numéricas y arrays |
| **pandas** | Manipulación y análisis de datos |
| **scipy** | Métodos estadísticos (Z-score, regresiones) |
| **matplotlib** | Visualización básica |
| **seaborn** | Visualización estadística |

### Notebooks
| Paquete | Propósito |
|---------|-----------|
| **jupyter** | Notebooks interactivos |
| **ipykernel** | Kernel de Python para Jupyter |

### Utilitarios
| Paquete | Propósito |
|---------|-----------|
| **openpyxl** | Lectura/escritura de archivos Excel (.xlsx) |
| **lxml** | Parsing de HTML para web scraping |

---

## Comandos Útiles

### Gestión del Entorno Virtual

```bash
# Activar el entorno virtual (Windows)
.venv\Scripts\activate

# Activar el entorno virtual (Mac/Linux)
source .venv/bin/activate

# Desactivar el entorno
deactivate
```

### Gestión de Paquetes

```bash
# Ver paquetes instalados
pip list

# Buscar un paquete específico
pip list | findstr nombre_paquete      # Windows
pip list | grep nombre_paquete         # Mac/Linux

# Instalar un paquete nuevo
pip install nombre_paquete

# Actualizar requirements.txt después de instalar
pip freeze > requirements.txt

# Instalar desde requirements.txt
pip install -r requirements.txt
```

### Jupyter Notebook

```bash
# Abrir Jupyter Notebook (navegador)
jupyter notebook

# Abrir notebook específico
jupyter notebook notebooks/data_preparation.ipynb
```

---

## Configuración de VS Code

### Extensiones Instaladas
| Extensión | Propósito |
|-----------|-----------|
| Python (Microsoft) | Soporte de Python |
| Pylint | Linting y análisis de código |
| Better Comments | Comentarios con colores |
| Jupyter | Soporte de notebooks en VS Code |

### Seleccionar Intérprete Python
1. `Ctrl+Shift+P`
2. Escribir "Python: Select Interpreter"
3. Seleccionar `.venv` (Python 3.12.10)

### Ejecutar Notebooks en VS Code
1. Abrir archivo `.ipynb`
2. Seleccionar kernel `.venv` (esquina superior derecha)
3. Ejecutar celdas con `Shift+Enter`

---

## Configuración de Jupyter

### Kernel Registrado
| Campo | Valor |
|-------|-------|
| **Nombre** | bootcamp-ds |
| **Display** | Bootcamp DS (3.12) |
| **Ubicación** | `C:\Users\carol\AppData\Roaming\jupyter\kernels\bootcamp-ds` |

### Registrar/Actualizar Kernel
```bash
python -m ipykernel install --user --name=bootcamp-ds --display-name="Bootcamp DS (3.12)"
```

---

## Recrear el Entorno desde Cero

Si necesitas reinstalar todo (nuevo computador, Mac, formateo, etc.):

### Windows
```bash
# 1. Crear entorno virtual
python -m venv .venv

# 2. Activar
.venv\Scripts\activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Registrar kernel de Jupyter
python -m ipykernel install --user --name=bootcamp-ds --display-name="Bootcamp DS (3.12)"
```

### Mac/Linux
```bash
# 1. Crear entorno virtual
python3 -m venv .venv

# 2. Activar
source .venv/bin/activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Registrar kernel de Jupyter
python -m ipykernel install --user --name=bootcamp-ds --display-name="Bootcamp DS (3.12)"
```

---

## Solución de Problemas Comunes

### "El paquete no se encuentra"
- Verificar que el entorno está activado (debe aparecer `(.venv)` en el terminal)
- Ejecutar `pip install nombre_paquete`

### "ModuleNotFoundError" en el notebook
- Verificar que el kernel correcto está seleccionado en VS Code
- Reinstalar el paquete: `pip install nombre_paquete`

### Jupyter no reconoce el kernel
```bash
python -m ipykernel install --user --name=bootcamp-ds --display-name="Bootcamp DS (3.12)"
```

### VS Code usa otro Python
- `Ctrl+Shift+P` → "Python: Select Interpreter" → Seleccionar `.venv`

### Conflicto entre Windows y Mac
- El `.venv` es específico del sistema operativo
- Usar `requirements.txt` para recrear el entorno en otra máquina

---

## Archivos Excluidos de Git (.gitignore)

```
.venv/
Learning/
.ipynb_checkpoints/
spyder_config.ini
*.pyc
__pycache__/
.DS_Store
Thumbs.db
```

---

## Notas Adicionales

- El entorno `.venv` NO se sube a GitHub (está en `.gitignore`)
- Siempre actualizar `requirements.txt` después de instalar nuevos paquetes
- Los notebooks se pueden ejecutar tanto en Jupyter (navegador) como en VS Code
- Para proyectos complejos usar VS Code; para práctica rápida Jupyter está bien
