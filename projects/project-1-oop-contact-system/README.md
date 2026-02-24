# Contact Management System

> **OOP + Encapsulation + Unit Testing** | Module 2: Programación Orientada a Objetos

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![Paradigm](https://img.shields.io/badge/Paradigm-OOP%20%2B%20Encapsulation-blueviolet)
![Testing](https://img.shields.io/badge/Testing-Unit%20Tests%20%2812%29-green)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Architecture](#architecture)
- [Installation](#installation)
- [Usage](#usage)
- [Validations](#validations)
- [Testing](#testing)
- [Tech Stack](#tech-stack)
- [Credits](#credits)
- [License](#license)

---

## Project Overview

A Python-based CRUD system for managing personal contacts, enabling efficient
storage, search, editing, and deletion of contact information.

This project applies **Object-Oriented Programming** with encapsulation
principles, PEP 8 style conventions, and unit testing with Python's
`unittest` framework.

**What I learned:** Designing class hierarchies with private attributes and
property-based validation, writing unit tests after implementation to verify
business rules (phone format, email format), and structuring a CLI application
with separation of concerns between data model, business logic, and interface.

---

## Features

- **Contact Registration**: Add new contacts with name, phone, email, and address
- **Flexible Search**: Search contacts by name or phone (partial matching)
- **Selective Editing**: Modify only desired fields without affecting others
- **Safe Deletion**: Confirmation required before deleting a contact
- **CSV Export**: Export all contacts to a CSV file
- **Data Validation**: Automatic verification of phone and email format

---

## Project Structure

```
project-1-oop-contact-system/
├── config.py           # Constants and configurations
├── contact.py          # Contact and ContactManager classes
├── main.py             # Interactive menu (user interface)
├── test_contact.py     # Unit tests (12 tests)
├── LICENSE
└── README.md           # Documentation
```

---

## Architecture

### Contact Class

Represents an individual contact with attribute encapsulation:

- Private attributes (`_name`, `_phone`, `_email`, `_address`)
- Properties with getters and setters for validation
- `to_dict()` method for dictionary conversion
- `__str__()` method for readable representation

### ContactManager Class

Manages the contact collection:

| Method | Description |
|--------|-------------|
| `add()` | Add a new contact |
| `search_by_name()` | Search by name (partial match) |
| `search_by_phone()` | Search by phone (partial match) |
| `edit()` | Edit specific fields |
| `delete_contact()` | Delete a contact |
| `get_all()` | Get all contacts |
| `export_to_csv()` | Export to CSV file |

---

## Installation

```bash
# 1. Clone the repository
git clone https://github.com/joselopezp/bootcamp-data-science-portfolio.git
cd projects/project-1-contact-management-system

# 2. Verify Python version (3.10+ required for match-case)
python --version

# 3. No external dependencies — standard library only
python main.py
```

---

## Usage

When running the program, an interactive menu is displayed:

```
========================================
   CONTACT MANAGEMENT SYSTEM
========================================
1. Add contact
2. Search by name
3. Search by phone
4. Edit contact
5. Delete contact by number
6. View all contacts
7. Export contacts to CSV
0. Exit
========================================
```

### Usage Examples

**Adding a contact:**
```
Name: Juan Pérez
Phone: 12345678
Email: juan@gmail.com
Address: 123 Main Ave, Concepción
✓ Contact added successfully
```

**Searching by name:**
```
Name to search: Juan
Found 1 contact(s):
   Name: Juan Pérez | Phone: +569 1234 5678 | Email: juan@gmail.com
```

---

## Validations

The system automatically validates:

| Field | Validation |
|-------|------------|
| Name | Cannot be empty |
| Phone | Must have 8 digits (Chilean format) |
| Email | Must contain @ and valid extension (.com, .cl, .ar, etc.) |
| Address | Cannot be empty |

---

## Testing

Run unit tests:

```bash
python test_contact.py
```

Expected output:
```
............
----------------------------------------------------------------------
Ran 12 tests in 0.012s

OK
```

Tests cover: contact creation, field validation (phone format, email format),
search by name and phone, edit and delete operations, and CSV export.

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.10+ | Core language (`match-case` syntax) |
| OOP + Encapsulation | Data model design pattern |
| `unittest` | Unit testing framework |
| `csv` | Data export module |
| PEP 8 | Code style guide |
| Google-style Docstrings | Documentation standard |

**Skills Demonstrated:**
`Python` · `OOP` · `Encapsulation` · `CRUD` · `Unit Testing` · `unittest` ·
`PEP 8` · `CLI Application` · `Data Validation` · `CSV Export` ·
`Separation of Concerns` · `Google-style Docstrings`

---

## Credits

**Project:** Developed as part of Module 2 of the Alkemy / SENCE Data Science
Bootcamp (2025–2026). Designed and implemented by Jose Marcel Lopez Pino.

**References:**
- Python OOP: [Python Docs — Classes](https://docs.python.org/3/tutorial/classes.html)
- Unit Testing: [Python Docs — unittest](https://docs.python.org/3/library/unittest.html)
- PEP 8: [Python Style Guide](https://peps.python.org/pep-0008/)
- Google Docstrings: [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)

---

## License

This project is licensed under the [MIT License](LICENSE).

© 2026 Jose Marcel Lopez Pino

---

*Paradigm: OOP + Encapsulation | Methodology: Project-Based Learning (PBL)*

**Jose Marcel Lopez Pino**
Industrial Engineer (Business + Operations) | Data Science & Business Analytics
Bootcamp: Fundamentos de Ciencia de Datos - SENCE/Alkemy (2025–2026)

*Industrial Engineering in Chile encompasses finance, marketing, economics,
and operations management — enabling a unique business + analytics perspective.*

[![GitHub](https://img.shields.io/badge/GitHub-joselopezp-181717?style=flat&logo=github)](https://github.com/joselopezp)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Jose%20Lopez%20Pino-0077B5?logo=linkedin&logoColor=white)](https://linkedin.com/in/jose-lopez-pino)
