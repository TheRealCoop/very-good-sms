from app.models import Contact


def test_create_contact(client):
    new_contact = Contact.create(first_name='Ronald',
                                 last_name='Redacted',
                                 number='9195555555')

    assert new_contact.first_name == 'Ronald'
    assert new_contact.last_name == 'Redacted'
    assert new_contact.number == 9195555555


def test_serialize_contact(client, contact):
    assert contact.serialize() == {
        'id': contact.id,
        'first_name': contact.first_name,
        'last_name': contact.last_name,
        'number': '919-555-5555'
    }


def test_delete_contact(client, contact):
    assert Contact.query.count() == 1
    contact.delete()
    assert Contact.query.count() == 0


def assert_clean_number(client):
    examples = ['919-555-5555', '919 555 5555', 9195555555, '9195 55  55 55']
    for phone in examples:
        contact = Contact.create(first_name='a', last_name='b', number=phone)
        assert contact.number == 9195555555
