from flask import Flask
from src.routes.user_routes import user_bp
from src.config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Register Blueprints
    app.register_blueprint(user_bp, url_prefix='/api')

    return app
