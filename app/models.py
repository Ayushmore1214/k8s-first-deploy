from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class BackupHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    repo_name = db.Column(db.String(120))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    gcs_path = db.Column(db.String(200))
