from flask import Blueprint, jsonify
from shared.models import User

users = Blueprint("users", __name__)


@users.route("/user/<id>", methods=["GET"])
def get_user(id):
    """
    Path:       /user/<id>
    Method:     GET
    Args:       ID: The id of the user to retrieve.
    Returns:    User object as JSON
    """
    return jsonify(User.query.get_or_404(id).serialize())


@users.route("/user", methods=["POST"])
def create_user():
    """
    Path:       /user
    Method:     POST
    Returns:    Created user object as JSON
    """
    pass


@users.route("/user/<id>", methods=["PATCH"])
def update_user(id):
    """
    Path:       /user/<id>
    Method:     PATCH
    Returns:    Modified user object as JSON.
    """
    pass


@users.route("/user/<id>", methods=["DELETE"])
def delete_user(id):
    """
    Path:       /user/<id>
    Method:     DELETE
    Returns:    Deleted user object as JSON
    """
    pass
