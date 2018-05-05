from os import environ

from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from app.views import INDEX


DB = SQLAlchemy()
CONFIGS = {
    'development': 'config.Development',
    'production': 'config.Production',
    'test': 'config.Test'
}


def create_app():
    '''Create application.'''
    app = Flask(__name__,
                template_folder='../client',
                static_folder='../client')
    app.config.from_object(CONFIGS[environ['FLASK_ENV']])
    CORS(app)
    load_db(app)
    load_blueprints(app)
    return app


def load_blueprints(app):
    from app.api.endpoints import API

    app.register_blueprint(API)
    app.register_blueprint(INDEX)


def load_db(app):
    DB.app = app
    DB.init_app(app)

    Migrate(app, DB)
