import requests
from keys import SUPABASE_URL, SUPABASE_KEY
# Replace with your Supabase project details

HEADERS = {
    'apikey': SUPABASE_KEY,
    'Authorization': f'Bearer {SUPABASE_KEY}',
    'Content-Type': 'application/json',
}

# Insert a new contact
def create_contact(name, email):
    url = f'{SUPABASE_URL}/rest/v1/contacts'
    data = {'name': name, 'email': email}
    response = requests.post(url, headers=HEADERS, json=data)
    return response

# Retrieve all contacts
def get_contacts():
    url = f'{SUPABASE_URL}/rest/v1/contacts'
    response = requests.get(url, headers=HEADERS)
    return response.json()

# Update a contact's email
def update_contact(contact_id, new_email):
    url = f'{SUPABASE_URL}/rest/v1/contacts?id=eq.{contact_id}'
    data = {'email': new_email}
    response = requests.patch(url, headers=HEADERS, json=data)
    return response

# Delete a contact
def delete_contact(contact_id):
    url = f'{SUPABASE_URL}/rest/v1/contacts?id=eq.{contact_id}'
    response = requests.delete(url, headers=HEADERS)
    return response.status_code

