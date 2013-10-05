import uuid

from flask import jsonify


def create_uuid():
    "Creates a uuid4 and returns a string."
    return str(uuid.uuid4())


def jsonify_with_status(status, *args, **kwargs):
    """
    Takes a status code and an object to be jsonified and returns a response
    object that can be returned from an API endpoint.
    """
    response = jsonify(*args, **kwargs)
    response.status_code = status
    return response
