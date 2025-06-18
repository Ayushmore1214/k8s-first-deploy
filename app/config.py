import os

class Config:
    SECRET_KEY = os.environ.get("FLASK_SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    GITHUB_CLIENT_ID = os.environ.get("GH_CLIENT_ID")
    GITHUB_CLIENT_SECRET = os.environ.get("GH_CLIENT_SECRET")
    GCS_BUCKET_NAME = os.environ.get("GCS_BUCKET_NAME")
