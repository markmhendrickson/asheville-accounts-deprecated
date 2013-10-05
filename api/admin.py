from flask import Blueprint

admin = Blueprint("admin", __name__)


@admin.route("/admin/stats", methods=["GET"])
def get_stats(id):
    """
    Path:       /admin/stats
    Method:     GET
    Returns:    Stats as JSON
    """
    pass
