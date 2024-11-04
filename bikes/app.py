from fastapi import FastAPI
from pathlib import Path
import yaml

# Create a FastAPI instance.
# This object represents the FastAPI application.
app = FastAPI(
  debug=True, openapi_url='/openapi/bikes.json', docs_url='/docs/bikes'
)

# Load API specification using PyYAML
oas_doc = yaml.safe_load(
  (Path(__file__).parent / './oas.yaml').read_text()
)

# Ovverride FASTAPI's OpenAPI property to return API sepcification
app.openapi = lambda: oas_doc

# Import api module.
# It can register view functions when imported.
from bikes.api import api