# Proyecto: Proyecto Sistema de Gestión de Contactos

"""Contact and ContactManager classes."""
import csv
import unicodedata

from config import VALID_EMAIL_EXTENSIONS, PHONE_LENGTH, PHONE_PREFIX

def normalize(text):
    """Remueve tildes de un texto."""
    return unicodedata.normalize('NFKD', text).encode('ASCII', 'ignore').decode('ASCII').lower()

class Contact:
    """Represents an individual contact with personal data."""    
    
    def __init__(self, name, phone, email, address):
        
        """ Initialize a new contact. 
        
        Args:
            name: Contact's full name
            phone: Phone number
            email: Email address
            address: Physical address
        """
    
        # Private attributes: encapsulation
        self._name = None
        self._phone = None
        self._email = None
        self._address = None
        
        # Assign using setters (which will validate data)
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
    
    
    @property
    def name(self):
        """Getter: returns the contact's name."""
        return self._name
    
    @name.setter
    def name(self, value):
        """Setter: validates and assigns the name."""
        if not value or not isinstance(value, str):
            raise ValueError("Name must be a non-empty text")
        if not value.strip():
            raise ValueError("Name cannot contain only spaces")
        self._name = value.strip().title()
        
    @property        
    def phone(self):
        """Getter: returns formatted phone for display."""
        if self._phone:
            return f"+569 {self._phone[:4]} {self._phone[4:]}"
        return None
    
    @phone.setter
    def phone(self, value):
        """Setter: validates and stores 8 digits for phone."""
        clean = str(value).replace(" ", "").replace("-", "")
        
        if clean.startswith("+569"):
            clean = clean[4:]
        elif clean.startswith("569"):
            clean = clean[3:]
        elif clean.startswith("9") and len(clean) == 9:
            clean = clean[1:]
           
        if not clean.isdigit():
            raise ValueError("El teléfono debe contener solo números")
        if len(clean) != PHONE_LENGTH:
            raise ValueError(f"El teléfono debe tener {PHONE_LENGTH} dígitos (excluyendo {PHONE_PREFIX})")
        
        self._phone = clean
    
    @property
    def email(self):
        """Getter: returns the email address."""
        return self._email
    
    @email.setter
    def email(self, value):
        """Setter: validates basic email format."""
        if not value or not isinstance(value, str):
            raise ValueError("El correo no puede estar vacio")
            
        value = value.strip().lower()
    
        # Validate that it contains exactly one @
        if value.count("@") != 1:
            raise ValueError("El correo debe contener sólo un @")
            
        # We separate user and domain ------------------------------------------
        user, domain = value.split("@")
        
        if not user:
            raise ValueError("El correo debe tener un nombre de usuario antes de @.")
            
        
        domain_name = domain.split(".")[0]
        if not domain_name:
            raise ValueError("El correo electrónico debe tener un nombre de dominio antes del punto.")
        
        if "." not in domain:
            raise ValueError("El correo electrónico debe tener un punto después del nombre de dominio.")
        
        has_valid_extension = any(domain.endswith(ext) for ext in VALID_EMAIL_EXTENSIONS)
        
        if not has_valid_extension:
            raise ValueError(f"La extensión del correo electrónico debe ser una de las siguientes: {VALID_EMAIL_EXTENSIONS}")
        
        self._email = value
        
    @property
    def address(self):
        """Getter: returns the contact's address."""
        return self._address
    
    @address.setter
    def address(self, value):
        """Setter: validates and assigns the address."""
        if not value or not isinstance(value, str):
            raise ValueError("La dirección no puede estar vacía")
        if not value.strip():
            raise ValueError("La dirección no puede contener solo espacios")
        self._address = value.strip()
    
    def to_dict(self):
        """Converts the contact to a dictionary."""
        return {
            "name": self._name,
            "phone": self._phone,
            "email": self._email,
            "address": self._address
        }
    
    def __str__(self):
        """Returns a readable representation of the contact."""
        return (
            f"Nombre: {self._name} | "
            f"Teléfono: {self.phone} | "
            f"Correo: {self._email}\n"
            f"Dirección: {self._address}"
        )


    
    
class ContactManager:
    """Manages a collection of contacts."""
    
    def __init__(self):
        """Initializes the manager with an empty contact list."""
        self._contacts = []
    
    def add(self, new_contact):
        """
        Adds a new contact to the list.
        
        Args:
            new_contact: Contact object
        
        Returns:
            bool: True if added, False if already exists
        """
        for contact in self._contacts:
            if contact.name.lower() == new_contact.name.lower():
                return False
        
        self._contacts.append(new_contact)
        return True
    
    def delete(self, name):
        """
        Deletes a contact by name.
    
        Args:
            name (str): Name of the contact to delete.
    
        Returns:
            bool: True if the contact was deleted, False if not found.
        """
        for contact in self._contacts:
            if contact.name.lower() == name.lower():
                self._contacts.remove(contact)
                return True
    
        return False
    
    def delete_contact(self, contact):
        """
        Deletes a contact by object reference.
    
        Args:
            contact (Contact): Contact to delete.
    
        Returns:
            bool: True if deleted, False otherwise.
        """
        if contact in self._contacts:
            self._contacts.remove(contact)
            return True
        return False
    
    def export_to_csv(self, file_path):
        """
        Exports all contacts to a CSV file.
    
        Args:
            file_path (str): Destination CSV file path.
        """
        with open(file_path, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
    
            # Write header
            writer.writerow(["Nombre", "Teléfono", "Correo", "Dirección"])
    
            # Write contact rows
            for contact in self._contacts:
                writer.writerow([
                    contact.name,
                    contact.phone,
                    contact.email,
                    contact.address
                ])

   
    def search_by_name(self, name):
        """
        Searches contacts containing the searched name.
        
        Args:
            name: Text to search in names
        
        Returns:
            list: List of matching contacts
        """
        name = normalize(name)
        results = []
        
        for contact in self._contacts:
            if name in normalize(contact.name):
                results.append(contact)
        
        return results
    
    def search_by_phone(self, phone):
        """
        Searches contacts containing the searched number.
        
        Args:
            phone: Digits to search in phones
        
        Returns:
            list: List of matching contacts
        """
        phone = str(phone).replace(" ", "").replace("-", "")
        
        if phone.startswith("+569"):
            phone = phone[4:]
        elif phone.startswith("569"):
            phone = phone[3:]
        
        
        results = []
        
        for contact in self._contacts:
            if phone in contact._phone:
                results.append(contact)
               
        return results
    
    def get_all(self):
        """
        Returns all contacts in the list.
        
        Returns:
            list: List of all Contact objects
        """
        return self._contacts
    
    def delete_by_name(self, name):
        """
        Deletes contacts matching the name.
        
        Args:
            name: Text to match in contact names
        
        Returns:
            int: Number of contacts deleted
        """
        name = name.lower().strip()
        deleted = 0
        
        # New list without the contacts that match
        new_list = []
        for contact in self._contacts:
            if name in contact.name.lower():
                deleted += 1
            else:
                new_list.append(contact)
                
        self._contacts = new_list
        return deleted
    
    def delete_by_phone(self, phone):
        """
        Deletes contacts matching the phone number.
        
        Args:
            phone: Digits to match in contact phones
        
        Returns:
            int: Number of contacts deleted
        """
        phone = str(phone).replace(" ", "").replace("-", "")
        
        if phone.startswith("+569"):
            phone = phone[4:]
        elif phone.startswith("569"):
            phone = phone[3:]
               
        deleted = 0
        
        new_list = []
        for contact in self._contacts:
            if phone in contact._phone:
                deleted += 1
            else:
                new_list.append(contact)
                
        self._contacts = new_list
        return deleted
    
    
    def edit(self, name, **new_data):
        """
        Edits a contact found by name.
        
        Args:
            name: Name to search for
            **new_data: Fields to update (name, phone, email, address)
        
        Returns:
            bool: True if edited, False if not found
        """
        name = name.lower().strip()
        
        for contact in self._contacts:
            if name in contact.name.lower():
                # Actualizar solo los campos que vienen en new_data
                if "name" in new_data:
                    contact.name = new_data["name"]
                if "phone" in new_data:
                    contact.phone = new_data["phone"]
                if "email" in new_data:
                    contact.email = new_data["email"]
                if "address" in new_data:
                    contact.address = new_data["address"]
                return True
        
        return False
    