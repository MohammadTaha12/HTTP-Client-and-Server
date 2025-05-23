from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager() # Initialize LoginManager

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app) # Configure LoginManager
    login_manager.login_view = 'auth.login' # Set the login view
    login_manager.login_message = 'يرجى تسجيل الدخول للوصول إلى هذه الصفحة.' # Translated message
    login_manager.login_message_category = 'info'

    # Configure UPLOAD_FOLDER
    import os # Make sure os is imported
    app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'static/product_images')
    # Ensure the directory exists (optional here, can be in the route)
    # if not os.path.exists(app.config['UPLOAD_FOLDER']):
    #     os.makedirs(app.config['UPLOAD_FOLDER'])

    from app.models import User # Import User model

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Import blueprints
    from app.auth_bp import auth_bp
    from app.admin_bp import admin_bp
    from app.routes import main_bp # Import the new main_bp

    # Register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(main_bp) # Register main_bp
    from .cart_bp import cart_bp # Import cart_bp
    app.register_blueprint(cart_bp) # Register cart_bp

    # Context Processor for cart
    from flask import session # Ensure session is imported
    @app.context_processor
    def utility_processor():
        cart = session.get('cart', {})
        cart_item_count = len(cart)
        cart_total_value = sum(item['price'] * item['quantity'] for item in cart.values())
        return dict(cart_item_count=cart_item_count, session_cart_items=cart, session_cart_total=cart_total_value)

    # Models are typically imported at the top or within the files that need them (like views/routes)
    # The import of 'models' here might still be okay, but 'routes' is now handled by blueprints.
    from app import models # Ensure models is imported if still needed globally

    # Register CLI commands
    from app import cli
    cli.register_commands(app)

    return app

# This instance is created for convenience for flask shell or other scripts.
# For running the app, `run.py` should use `create_app`.
# It's generally better not to create an instance here if 'run.py' is the sole entry point for app creation.
# However, if other scripts or flask shell rely on it, it can stay.
# For 'flask db' commands, FLASK_APP=run.py should correctly use create_app from run.py.
# app_instance = create_app() # Renamed to avoid confusion with 'app' from Flask itself.

# Removing the global app_instance as it can cause issues with application context,
# especially with blueprints and CLI commands. `run.py` should be the entry point.
# The `from app import app` in the old routes.py was problematic due to this.
