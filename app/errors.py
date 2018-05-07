from flask import jsonify


class FlaskError(Exception):
    def __init__(self, message=None, status_code=None):
        Exception.__init__(self)
        self.status_code = status_code
        self.payload = {'error': message}


    def to_dict(self):
        return self.payload


class UniqueConstraint(FlaskError):
    def __init__(self):
        super().__init__('Contact already exists with that information', 409)


class InternalError(FlaskError):
    def __init__(self):
        super().__init__('Oops, bad request!', 500)


def handle_flask_error(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response
