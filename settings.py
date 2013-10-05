import os

DEBUG = "DEBUG" in os.environ

SECRET_KEY = os.environ.get("SECRET_KEY", "development")

# API Auth
API_TOKEN = os.environ.get("SECRET_KEY", "development")

ENVIRONMENT = os.environ.get("ENVIRONMENT", "development")

# DB
SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "sqlite:////tmp/test.db")

if ENVIRONMENT == "production":
    SQLALCHEMY_POOL_SIZE = os.environ.get("SQLALCHEMY_POOL_SIZE", 1)

# Test Settings
if ENVIRONMENT == 'test':
    CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/testing.db"
    DATABASE_URL = "sqlite:////tmp/testing.db"
    TESTING = True
