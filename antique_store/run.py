from app import create_app # Corrected import
from config import Config # Ensure Config is imported

# Create the Flask app instance using the factory function
app = create_app(Config)

if __name__ == '__main__':
    # The app.run() call should ideally use the 'app' instance created by create_app
    app.run(debug=True)
