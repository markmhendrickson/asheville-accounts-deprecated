"""
Contains a helper for checking incoming requests for proper
authorization headers.
"""
from shared.app import app
from shared.helpers import jsonify_with_status


def _authenticate():
    """
    Return true if the custom request header matches our API token,
    otherwise reutnr False to deny the request.
    """
    # TODO access the header
    token = "foobar"

    if token == app.config['API_TOKEN']:
        return True

    # Deny request
    return False


def check_api_auth():
    """
    Check the request for an API token. If it doesn't match the token
    from our configuration, deny the request with an error message.
    """
    if _authenticate():
        return None
    else:
        return jsonify_with_status(401, {"error": "authorization is required"})
