from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
import os

# Instantiate the extensions
db = SQLAlchemy()
migrate = Migrate()

# Login view of the app
login_manager = LoginManager()
login_manager.login_view = 'auth.login' 

def create_app():
    app = Flask(__name__)
    login_manager.init_app(app)
    
    from .models import User
    # User loader setup
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    # Configuration
    app.config['SECRET_KEY'] = 'your_secret_key_here'
    
    # Database configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///marketplace.db'  # Database file in the current directory
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Import blueprints
    from .auth import auth as auth_blueprint
    from .routes import main as main_blueprint
    
    # Register blueprints
    app.register_blueprint(auth_blueprint, url_prefix='/')
    app.register_blueprint(main_blueprint, url_prefix='/')
    
    return app

def create_database(app):
    with app.app_context():
        db.create_all()
