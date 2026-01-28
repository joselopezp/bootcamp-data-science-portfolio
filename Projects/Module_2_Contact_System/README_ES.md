# Sistema de Gestión de Contactos

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/Licencia-Educacional-green.svg)](#licencia)

[🇺🇸 English Version](README.md)

Sistema desarrollado en Python para gestionar contactos personales, permitiendo almacenar, buscar, editar y eliminar información de manera eficiente.

## Descripción

Este proyecto fue desarrollado como parte del Módulo 2 del bootcamp "Fundamentos de Ciencia de Datos". Implementa un sistema CRUD (Create, Read, Update, Delete) completo utilizando Programación Orientada a Objetos (POO) con principios de encapsulación.

## Características

- **Registro de contactos**: Agregar nuevos contactos con nombre, teléfono, correo y dirección
- **Búsqueda flexible**: Buscar contactos por nombre o teléfono (coincidencia parcial)
- **Edición selectiva**: Modificar solo los campos deseados sin afectar los demás
- **Eliminación segura**: Confirmar antes de eliminar un contacto
- **Exportación CSV**: Exportar todos los contactos a un archivo CSV
- **Validación de datos**: Verificación automática de formato de teléfono y correo electrónico

## Estructura del Proyecto

```
sistema_contactos/
├── config.py           # Constantes y configuraciones
├── contact.py          # Clases Contact y ContactManager
├── main.py             # Menú interactivo (interfaz de usuario)
├── test_contact.py     # Pruebas unitarias
├── README.md           # Documentación (Inglés)
└── README_ES.md        # Documentación (Español)
```

## Requisitos

- Python 3.10 o superior (requerido para `match-case`)
- No requiere librerías externas

## Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/tu-usuario/sistema-contactos.git
cd sistema-contactos
```

2. Ejecutar el programa:
```bash
python main.py
```

## Uso

Al ejecutar el programa, se muestra un menú interactivo:

```
========================================
   SISTEMA DE GESTION DE CONTACTOS
========================================
1. Agregar contacto
2. Buscar por nombre
3. Buscar por teléfono
4. Editar contacto
5. Eliminar contacto por número
6. Ver todos los contactos
7. Exportar contactos a CSV
0. Salir
========================================
```

### Ejemplos de Uso

**Agregar un contacto:**
```
Nombre: Juan Pérez
Teléfono: 12345678
Correo electrónico: juan@gmail.com
Dirección: Av. Principal 123, Concepción
✓ Contacto agregado exitosamente
```

**Buscar por nombre:**
```
Nombre a buscar: Juan
Se encontraron 1 contacto(s):
   Nombre: Juan Pérez | Teléfono: +569 1234 5678 | Correo: juan@gmail.com
```

## Validaciones

El sistema valida automáticamente:

| Campo | Validación |
|-------|------------|
| Nombre | No puede estar vacío |
| Teléfono | Debe tener 8 dígitos (formato chileno) |
| Correo | Debe contener @ y extensión válida (.com, .cl, .ar, etc.) |
| Dirección | No puede estar vacía |

## Arquitectura

### Clase Contact

Representa un contacto individual con encapsulación de atributos:

- Atributos privados (`_name`, `_phone`, `_email`, `_address`)
- Properties con getters y setters para validación
- Método `to_dict()` para conversión a diccionario
- Método `__str__()` para representación legible

### Clase ContactManager

Gestiona la colección de contactos:

| Método | Descripción |
|--------|-------------|
| `add()` | Agregar un nuevo contacto |
| `search_by_name()` | Buscar por nombre (coincidencia parcial) |
| `search_by_phone()` | Buscar por teléfono (coincidencia parcial) |
| `edit()` | Editar campos específicos |
| `delete_contact()` | Eliminar un contacto |
| `get_all()` | Obtener todos los contactos |
| `export_to_csv()` | Exportar a archivo CSV |

## Pruebas

Ejecutar las pruebas unitarias:

```bash
python test_contact.py
```

Resultado esperado:
```
............
----------------------------------------------------------------------
Ran 12 tests in 0.012s

OK
```

## Tecnologías Utilizadas

- **Python 3.10+**: Lenguaje de programación
- **POO**: Programación Orientada a Objetos con encapsulación
- **unittest**: Framework de pruebas unitarias
- **csv**: Módulo para exportación de datos
- **PEP 8**: Guía de estilo de código

## Autor

**Jose Marcel Lopez Pino**

Estudiante de Ciencia de Datos - Bootcamp SENCE 2025-2026

- GitHub: [@tu-usuario](https://github.com/tu-usuario)
- LinkedIn: [Tu LinkedIn](https://linkedin.com/in/tu-perfil)

## Licencia

Este proyecto fue desarrollado con fines educativos como parte del bootcamp "Fundamentos de Ciencia de Datos".
