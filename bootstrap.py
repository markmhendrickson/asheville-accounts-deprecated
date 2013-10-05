from shared.app import app
from shared.db import db
from shared.models import User


if app.config["ENVIRONMENT"] == "production":
    raise Exception("Cannot run bootstrap in production!")

print "Dropping and creating the database.."
db.drop_all()
db.create_all()
