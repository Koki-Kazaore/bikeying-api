from fastapi import FastAPI

# Create a FastAPI instance.
# This object represents the FastAPI application.
app = FastAPI(debug=True)

# Import api module.
# It can register view functions when imported.
from bikes.api import api