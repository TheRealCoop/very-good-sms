from traceback import print_exc

from decorator import decorator
from flask import current_app as app
from sqlalchemy.exc import IntegrityError
from twilio.rest import Client

from app.errors import InternalError, UniqueConstraint, handle_flask_error
from app.models import Contact


@decorator
def handle_errors(func, *args, **kwargs):
    try:
        return func(*args, **kwargs)
    except Exception as error:
        if error.__class__ == IntegrityError:
            return handle_flask_error(UniqueConstraint)

        print_exc()
        return handle_flask_error(InternalError())


def get_contacts():
    return {'contacts': [x.serialize() for x in Contact.query.all()]}


def create_contact(request_json):
    return {'contact': Contact.create(**request_json).serialize()}


def send_sms(contact_id, request_json):
    to_number = Contact.query.filter_by(id=contact_id).first().number
    _make_twilio_request(request_json['message'], to_number)
    return {'success': True}


def _make_twilio_request(message, to_number):
    client = Client(app.config['TWILIO_ACCOUNT_SID'],
                    app.config['TWILIO_AUTH_TOKEN'])

    return client.messages.create(body=message,
                                  from_=app.config['TWILIO_FROM'],
                                  to='+1' + str(to_number))
