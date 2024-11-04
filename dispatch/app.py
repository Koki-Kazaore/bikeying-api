from flask import Flask
from flask_smorest import Api

# Import the BaseConfig class
from config import BaseConfig

# Create an instance of the Flask application object
app = Flask(__name__)

# Load the configuration from the BaseConfig class
app.config.from_object(BaseConfig)

# Create an instance of the API object
dispatch_api = Api(app)