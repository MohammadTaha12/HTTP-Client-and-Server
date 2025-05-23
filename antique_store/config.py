import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # UPLOAD_FOLDER will be set in app/__init__.py for robustness,
    # using app.root_path to ensure correct path relative to the app instance.
    # Example: UPLOAD_FOLDER = os.path.join(basedir, 'app/static/product_images')
    # Add other configuration variables as needed
