from os import environ

from pytest import fixture

from app import DB, create_app
from app.models import Contact


@fixture()
def app():
    environ['FLASK_ENV'] = 'test'
    _app = create_app()
    with _app.app_context():
        DB.create_all()
        yield _app
        DB.session.remove()
        DB.drop_all()
    return _app


@fixture()
def contact():
    return Contact.create(first_name='Ronald',
                          last_name='Redacted',
                          number='919-555-5555')
