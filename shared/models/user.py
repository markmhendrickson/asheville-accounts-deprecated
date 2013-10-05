from flask import json
from shared.db import db
from shared.helpers import create_uuid


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.String(36), primary_key=True, default=create_uuid)

    def __init__(self):
        pass

    def __repr__(self):
        return '<User %s>' % (self.id)

    def serialize(self):
        obj = dict(self.__dict__)
        # Remove the sqlalchemy bit
        obj.pop("_sa_instance_state", None)
        return obj

    def serialize_json(self):
        return json.dumps(self.serialize())

    def update(self):
        pass

    def destroy(self):
        pass

    @staticmethod
    def new():
        pass
