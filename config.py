from os import environ, path


DB_ROOT = path.join(path.dirname(path.realpath('database')), 'database')

class BaseConfig():
    '''Base Flask config variables.'''

    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TWILIO_ACCOUNT_SID = environ.get('TWILIO_ACCOUNT_SID', 'ACc944af0b96c32d22c4a83230a024ba16')
    TWILIO_AUTH_TOKEN = environ.get('TWILIO_AUTH_TOKEN', '5514e655c604e0f4d00ac99423a53a21')
    TWILIO_FROM = '+15005550006'


class Test(BaseConfig):

    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_DATABASE_URI = f'sqlite:////{DB_ROOT}/test.db'
    TESTING = True


class Development(BaseConfig):

    SQLALCHEMY_DATABASE_URI = f'sqlite:////{DB_ROOT}/dev.db'


class Production(BaseConfig):

    DEBUG = False
    SQLALCHEMY_DATABASE_URI = f'sqlite:////{DB_ROOT}/prod.db'
    TWILIO_FROM = '+19842052360'
