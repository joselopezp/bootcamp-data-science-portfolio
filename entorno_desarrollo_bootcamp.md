# Configuración del Entorno de Desarrollo - Bootcamp Data Science

## Información General

| Campo | Valor |
|-------|-------|
| **Fecha de configuración** | Enero 2025 |
| **Python** | 3.12.10 |
| **Tipo de entorno** | Virtual environment (.venv) |
| **IDE principal** | VS Code |
| **Notebooks** | Jupyter |

---

## Estructura del Proyecto

```
Bootcamp_Data_Science_Portfolio/
├── .venv/                    # Entorno virtual (no subir a Git)
├── Module_2_Contact_System/  # Challenge 1
├── .gitignore
├── README.md
└── requirements.txt          # Dependencias del proyecto
```

---

## Paquetes Instalados

### Esenciales para Data Science
- **numpy** - Operaciones numéricas y arrays
- **pandas** - Manipulación de datos
- **matplotlib** - Visualización básica
- **seaborn** - Visualización estadística
- **jupyter** - Notebooks interactivos
- **ipykernel** - Kernel de Python para Jupyter

---

## Comandos Útiles

### Activar el entorno virtual
```bash
.venv\Scripts\activate
```

### Desactivar el entorno
```bash
deactivate
```

### Abrir Jupyter Notebook
```bash
jupyter notebook
```

### Instalar dependencias desde requirements.txt
```bash
pip install -r requirements.txt
```

### Actualizar requirements.txt después de instalar nuevos paquetes
```bash
pip freeze > requirements.txt
```

### Ver paquetes instalados
```bash
pip list
```

### Instalar un paquete nuevo
```bash
pip install nombre_paquete
```

---

## Configuración de VS Code

### Extensiones recomendadas
- Python (Microsoft)
- Pylint
- Better Comments
- Jupyter

### Seleccionar intérprete
1. `Ctrl+Shift+P`
2. "Python: Select Interpreter"
3. Seleccionar `.venv` (Python 3.12.10)

---

## Configuración de Jupyter

### Kernel registrado
- **Nombre**: bootcamp-ds
- **Display**: "Bootcamp DS (3.12)"
- **Ubicación**: `C:\Users\carol\AppData\Roaming\jupyter\kernels\bootcamp-ds`

### Crear nuevo notebook con el kernel correcto
1. `jupyter notebook`
2. Click en "New"
3. Seleccionar "Bootcamp DS (3.12)"

---

## Recrear el Entorno desde Cero

Si necesitas reinstalar todo (nuevo computador, formateo, etc.):

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

---

## Solución de Problemas Comunes

### "El paquete no se encuentra"
Verificar que el entorno está activado (debe aparecer `(.venv)` en el terminal).

### Jupyter no reconoce el kernel
```bash
python -m ipykernel install --user --name=bootcamp-ds --display-name="Bootcamp DS (3.12)"
```

### VS Code usa otro Python
`Ctrl+Shift+P` → "Python: Select Interpreter" → Seleccionar `.venv`

---

## Notas Adicionales

- El entorno `.venv` NO se sube a GitHub (está en `.gitignore`)
- Siempre actualizar `requirements.txt` después de instalar nuevos paquetes
- Spyder pospuesto - usando VS Code + Jupyter por ahora
