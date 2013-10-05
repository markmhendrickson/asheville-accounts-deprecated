from .app import app
from shared.auth import check_api_auth
from shared.helpers import jsonify_with_status
from api.users import users
from api.admin import admin

app.register_blueprint(users, url_prefix='/v1')
app.register_blueprint(admin, url_prefix='/v1')


# The entire app is protected and needs an `X-Asheville-Auth` HTTP HEADER
app.before_request(check_api_auth)


@app.errorhandler(404)
def page_not_found(error):
    return jsonify_with_status(404, {"error": "resource not found"})
