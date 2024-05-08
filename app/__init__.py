from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///marketplace.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    Migrate(app, db)

    from . import models
    from .routes import main
    from .auth import auth
    
    app.register_blueprint(main, url_prefix='/') # registering blueprints from routes
    app.register_blueprint(auth, url_prefix='/') # registering blueprints from auth

    return app
