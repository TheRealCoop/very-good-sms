import json
from flask import url_for


HEADERS = {'Content-Type': 'application/json'}


def get(client, endpoint, **kwargs):
    return client.get(url_for(endpoint, **kwargs))


def post(client, data, endpoint, **kwargs):
    return client.post(url_for(endpoint, **kwargs),
                       data=json.dumps(data),
                       headers=HEADERS)


def delete(client, endpoint, **kwargs):
    return client.delete(url_for(endpoint, **kwargs))
