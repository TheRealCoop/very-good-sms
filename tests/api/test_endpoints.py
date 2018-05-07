from app.models import Contact
from tests.helpers import delete, get, post

def test_get_all_contacts(client, contact):
    response = get(client, 'api.contacts')
    assert response.status_code == 200
    assert response.json['contacts'] == [contact.serialize()]


def test_create_contact(client):
    payload = {'first_name': 'Ronald',
               'last_name': 'Redacted',
               'number': '9195555555'}
    response = post(client, payload, 'api.contacts')
    created = Contact.query.first()
    assert response.status_code == 200
    assert response.json['contact'] == created.serialize()


def test_delete_contact(client, contact):
    response = delete(client, 'api.delete_contact', contact_id=contact.id)
    assert response.status_code == 200
    assert response.json['success'] == True
