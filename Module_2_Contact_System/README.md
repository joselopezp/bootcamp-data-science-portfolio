# Contact Management System

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-Educational-green.svg)](#license)

[🇪🇸 Versión en Español](README_ES.md)

A Python-based system for managing personal contacts, enabling efficient storage, search, editing, and deletion of contact information.

## Description

This project was developed as part of Module 2 of the "Data Science Fundamentals" bootcamp. It implements a complete CRUD (Create, Read, Update, Delete) system using Object-Oriented Programming (OOP) with encapsulation principles.

## Features

- **Contact Registration**: Add new contacts with name, phone, email, and address
- **Flexible Search**: Search contacts by name or phone (partial matching)
- **Selective Editing**: Modify only desired fields without affecting others
- **Safe Deletion**: Confirmation required before deleting a contact
- **CSV Export**: Export all contacts to a CSV file
- **Data Validation**: Automatic verification of phone and email format

## Project Structure

```
contact_management_system/
├── config.py           # Constants and configurations
├── contact.py          # Contact and ContactManager classes
├── main.py             # Interactive menu (user interface)
├── test_contact.py     # Unit tests
├── README.md           # Documentation (English)
└── README_ES.md        # Documentation (Spanish)
```

## Requirements

- Python 3.10 or higher (required for `match-case`)
- No external libraries required

## Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/contact-management-system.git
cd contact-management-system
```

2. Run the program:
```bash
python main.py
```

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

## Validations

The system automatically validates:

| Field | Validation |
|-------|------------|
| Name | Cannot be empty |
| Phone | Must have 8 digits (Chilean format) |
| Email | Must contain @ and valid extension (.com, .cl, .ar, etc.) |
| Address | Cannot be empty |

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

## Technologies Used

- **Python 3.10+**: Programming language
- **OOP**: Object-Oriented Programming with encapsulation
- **unittest**: Unit testing framework
- **csv**: Data export module
- **PEP 8**: Code style guide

## Author

**Jose Marcel Lopez Pino**

Data Science Student - SENCE Bootcamp 2025-2026

- GitHub: [@your-username](https://github.com/your-username)
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/your-profile)

## License

This project was developed for educational purposes as part of the "Data Science Fundamentals" bootcamp.
