from flask import Flask
from .config import Config
from .auth import github_blueprint
from .routes import main as main_blueprint
from .models import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    app.register_blueprint(github_blueprint)
    app.register_blueprint(main_blueprint)

    return app
