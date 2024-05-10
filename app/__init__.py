from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from dotenv import load_dotenv 
import os

# Load environment variables
load_dotenv()

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    env = os.environ.get('FLASK_ENV', 'development')  # Get the environment or default to development

    # Environment specific configuration
    if env == 'production':
        from config import ProductionConfig
        app.config.from_object(ProductionConfig)
    elif env == 'testing':
        from config import TestingConfig
        app.config.from_object(TestingConfig)
    else:
        from config import DevelopmentConfig
        app.config.from_object(DevelopmentConfig)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    # User loader
    @login_manager.user_loader
    def load_user(user_id):
        from .models import User
        return User.query.get(int(user_id))
    
    @app.context_processor
    def inject_user():
        return dict(user=current_user) # inject user to all templates

    # Import and register blueprints
    from .auth import auth as auth_blueprint
    from .routes import main as main_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/')
    app.register_blueprint(main_blueprint, url_prefix='/')

    return app

def create_database(app):
    with app.app_context():
        db.create_all()
