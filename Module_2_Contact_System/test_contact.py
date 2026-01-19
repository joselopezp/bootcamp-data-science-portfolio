"""Unit tests for Contact and ContactManager classes."""
import unittest

from contact import Contact, ContactManager


class TestContact(unittest.TestCase):
    """Tests for Contact class."""
    
    def test_create_valid_contact(self):
        """Test creating a contact with valid data."""
        contact = Contact("Juan Pérez", "12345678", "juan@gmail.com", "Av. Principal 123")
        
        self.assertEqual(contact.name, "Juan Pérez")
        self.assertEqual(contact.phone, "+569 1234 5678")
        self.assertEqual(contact.email, "juan@gmail.com")
        self.assertEqual(contact.address, "Av. Principal 123")
    
    def test_name_formatting(self):
        """Test that name is formatted with title case."""
        contact = Contact("JUAN PÉREZ", "12345678", "juan@gmail.com", "Dir")
        
        self.assertEqual(contact.name, "Juan Pérez")
    
    def test_invalid_name_empty(self):
        """Test that empty name raises ValueError."""
        with self.assertRaises(ValueError):
            Contact("", "12345678", "juan@gmail.com", "Dir")
    
    def test_invalid_phone_short(self):
        """Test that short phone raises ValueError."""
        with self.assertRaises(ValueError):
            Contact("Juan", "1234", "juan@gmail.com", "Dir")
    
    def test_invalid_email_no_at(self):
        """Test that email without @ raises ValueError."""
        with self.assertRaises(ValueError):
            Contact("Juan", "12345678", "juangmail.com", "Dir")
    
    def test_invalid_email_extension(self):
        """Test that invalid email extension raises ValueError."""
        with self.assertRaises(ValueError):
            Contact("Juan", "12345678", "juan@gmail.xyz", "Dir")


class TestContactManager(unittest.TestCase):
    """Tests for ContactManager class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.manager = ContactManager()
        self.contact1 = Contact("Juan Pérez", "12345678", "juan@gmail.com", "Dir 1")
        self.contact2 = Contact("María López", "87654321", "maria@gmail.com", "Dir 2")
    
    def test_add_contact(self):
        """Test adding a contact."""
        result = self.manager.add(self.contact1)
        
        self.assertTrue(result)
        self.assertEqual(len(self.manager.get_all()), 1)
    
    def test_add_duplicate_contact(self):
        """Test that duplicate contact returns False."""
        self.manager.add(self.contact1)
        duplicate = Contact("Juan Pérez", "11112222", "otro@gmail.com", "Otra dir")
        
        result = self.manager.add(duplicate)
        
        self.assertFalse(result)
    
    def test_search_by_name(self):
        """Test searching contacts by name."""
        self.manager.add(self.contact1)
        self.manager.add(self.contact2)
        
        results = self.manager.search_by_name("Juan")
        
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].name, "Juan Pérez")
    
    def test_search_by_phone(self):
        """Test searching contacts by phone."""
        self.manager.add(self.contact1)
        
        results = self.manager.search_by_phone("1234")
        
        self.assertEqual(len(results), 1)
    
    def test_delete_by_name(self):
        """Test deleting contact by name."""
        self.manager.add(self.contact1)
        self.manager.add(self.contact2)
        
        deleted = self.manager.delete_by_name("Juan")
        
        self.assertEqual(deleted, 1)
        self.assertEqual(len(self.manager.get_all()), 1)
    
    def test_edit_contact(self):
        """Test editing a contact."""
        self.manager.add(self.contact1)
        
        result = self.manager.edit("Juan", phone="99998888")
        
        self.assertTrue(result)
        self.assertEqual(self.manager.search_by_name("Juan")[0].phone, "+569 9999 8888")


if __name__ == "__main__":
    unittest.main()