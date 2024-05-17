from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, current_user
from dotenv import load_dotenv
from flask_admin import Admin
from flask_mail import Mail
import os

# Load environment variables
load_dotenv()

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
mail = Mail() # Initialize Flask-Mail


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
    mail.init_app(app)  # Initialize the Mail extension
    login_manager.login_view = 'auth.login'

    # User loader
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    @app.context_processor
    def inject_user():
        return dict(user=current_user)  # inject user to all templates

    # Import and register blueprints
    from .auth import auth as auth_blueprint
    from .routes import main as main_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/')
    app.register_blueprint(main_blueprint, url_prefix='/')

    # Import models here to avoid circular import issues
    from app.models import User, Vehicle

    # Initialize Flask-Admin
    from app.admin import MyAdminIndexView, MyModelView  # Import the custom admin views
    admin = Admin(app, name='EV Marketplace Admin', template_mode='bootstrap3', index_view=MyAdminIndexView())
    admin.add_view(MyModelView(User, db.session))
    admin.add_view(MyModelView(Vehicle, db.session))

    return app


def create_database(app):
    with app.app_context():
        db.create_all()
