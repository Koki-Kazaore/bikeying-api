from pathlib import Path
import yaml
from apispec import APISpec

from flask import Flask
from flask_smorest import Api

# Import the BaseConfig class
from config import BaseConfig
# Import the blueprint
from api.api import blueprint

# Create an instance of the Flask application object
app = Flask(__name__)

# Load the configuration from the BaseConfig class
app.config.from_object(BaseConfig)

# Create an instance of the API object
dispatch_api = Api(app)

# Register the blueprint with the Dispatch API object
dispatch_api.register_blueprint(blueprint)

api_spec = yaml.safe_load((Path(__file__).parent / "oas.yaml").read_text())
spec = APISpec(
    title=api_spec["info"]["title"],
    version=api_spec["info"]["version"],
    openapi_version=api_spec["openapi"],
)
spec.to_dict = lambda: api_spec
dispatch_api.spec = spec