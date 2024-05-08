from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import DevelopmentConfig, TestingConfig, ProductionConfig
from dotenv import load_dotenv
import os

load_dotenv()
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    env = os.environ.get('FLASK_ENV', 'development')

    if env == 'production':
        app.config.from_object(ProductionConfig)
    elif env == 'testing':
        app.config.from_object(TestingConfig)
    else:
        app.config.from_object(DevelopmentConfig)

    db.init_app(app)
    Migrate(app, db)

    from .routes import main  # Assuming your routes are in this module
    app.register_blueprint(main)

    return app
