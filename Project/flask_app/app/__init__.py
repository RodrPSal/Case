from flask import Flask

from config import Config
from app.extensions import db

from app.blueprints.main import bp as mainBp
from app.blueprints.user import bp as userBp

def create_app(configClass=Config):
    app = Flask(__name__)
    app.config.from_object(configClass)

    # Initialize extensions
    db.init_app(app)

    # Blueprints
    app.register_blueprint(mainBp)
    app.register_blueprint(userBp, url_prefix = "/user")

    with app.app_context():
        db.create_all()

    return app