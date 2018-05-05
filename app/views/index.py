from flask import Blueprint, send_from_directory


INDEX = Blueprint('index', __name__)


@INDEX.route('/', defaults={'this_path': ''})
@INDEX.route('/<path:this_path>')
def render_clientside(this_path):
    return send_from_directory('../client/', 'index.html')
