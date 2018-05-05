from flask import Blueprint, jsonify, request

from app.api.helpers import (create_contact, get_contacts, handle_errors,
                             send_sms)
from app.models import Contact


API = Blueprint('api', __name__, url_prefix='/api')


@handle_errors
@API.route('/contacts', methods=['GET', 'POST'])
def contacts():
    if request.method == 'GET':
        return jsonify(get_contacts())
    else:
        return jsonify(create_contact(request.json))


@handle_errors
@API.route('/contacts/<int:contact_id>', methods=['DELETE'])
def delete_contact(contact_id):
    contact = Contact.query.filter_by(id=contact_id).first()
    if contact:
        return jsonify(contact.delete())
    return jsonify({'success': False})


@handle_errors
@API.route('/contacts/<int:contact_id>/sms', methods=['POST'])
def sms(contact_id):
    return jsonify(send_sms(contact_id, request.json))
