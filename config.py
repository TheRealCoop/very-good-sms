class BaseConfig():
    '''Base Flask config variables.'''

    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Test(BaseConfig):

    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/very-good-sms-test.db'
    TESTING = True


class Development(BaseConfig):

    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/very-good-sms-dev.db'


class Production(BaseConfig):

    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:////very-good-sms-prod.db'
