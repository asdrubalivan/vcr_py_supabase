import unittest
import vcr
from main import create_contact, get_contacts, update_contact, delete_contact

# Configure VCR.py to store recordings in a 'cassettes' folder
my_vcr = vcr.VCR(
    cassette_library_dir='tests/cassettes',  # Store cassettes in the tests/cassettes directory
    record_mode='once',  # Record only once, reuse existing interactions
    match_on=['uri', 'method'],  # Match requests based on URI and method
    filter_headers=['Authorization', 'apikey']
)

class TestSupabaseAPI(unittest.TestCase):

    @my_vcr.use_cassette('create_contact.yaml')
    def test_create_contact(self):
        """Test inserting a new contact into Supabase"""
        response = create_contact('John Doe', 'john.doe@example.com')
        self.assertEqual(response.status_code, 201)

    @my_vcr.use_cassette('get_contacts.yaml')
    def test_get_contacts(self):
        """Test retrieving contacts from Supabase"""
        contacts = get_contacts()
        self.assertIsInstance(contacts, list)
        self.assertTrue(len(contacts) > 0)  # Ensure at least one contact exists

    @my_vcr.use_cassette('update_contact.yaml')
    def test_update_contact(self):
        """Test updating a contact's email in Supabase"""
        contacts = get_contacts()
        if not contacts:
            create_contact('Jane Doe', 'jane.doe@example.com')
            contacts = get_contacts()
        contact_id = contacts[0]['id']
        new_email = 'updated.email@example.com'
        response = update_contact(contact_id, new_email)
        self.assertEqual(response.status_code, 204)

    @my_vcr.use_cassette('delete_contact.yaml')
    def test_delete_contact(self):
        """Test deleting a contact from Supabase"""
        contacts = get_contacts()
        if not contacts:
            create_contact('Mark Smith', 'mark.smith@example.com')
            contacts = get_contacts()
        contact_id = contacts[0]['id']
        status_code = delete_contact(contact_id)
        self.assertEqual(status_code, 204)  # Ensure correct HTTP response for deletion