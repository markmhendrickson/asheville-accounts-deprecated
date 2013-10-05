from shared.red import red
from shared.db import db
from shared.bootstrap import app


class UnitTest(object):

    def setup_method(self, method):
        app.config['TESTING'] = True
        app.config['DEBUG'] = True
        # Before every test we want to create the schema
        db.create_all()

    def teardown_method(self, method):
        # After every test we want to drop all tables so we start
        # from scratch on each test.
        db.drop_all()


class IntegrationTest(object):

    def setup_method(self, method):
        app.config['TESTING'] = True
        app.config['DEBUG'] = True
        # Before every test we want to create the schema
        db.create_all()
        # Attach the client
        self.client = app.test_client()

    def teardown_method(self, method):
        # After every test we want to drop all tables so we start
        # from scratch on each test.
        db.drop_all()
