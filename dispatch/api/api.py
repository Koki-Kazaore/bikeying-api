import uuid
from datetime import datetime

from flask.views import MethodView
from flask_smorest import Blueprint

# Import marshmallow models
from api.schemas import (
  DispatchRequestSchema,
  DispatchBikeSchema,
  DispatchedBikeSchema,
  GetDispatchedBikeSchema
)

# Create an instance of the Blueprint class
blueprint = Blueprint('dispatch', __name__, description='Dispatch API')

# Declare a list of hard-coded assignments results
results = [
  {
    "bike_id": str(uuid.uuid4()),
    "user_queue_index": str(uuid.uuid4())
  },
  {
    "bike_id": str(uuid.uuid4()),
    "user_queue_index": str(uuid.uuid4())
  },
]

# Using Blueprint's response() decorator,
# Register a marshmallow model for the response pyaload
@blueprint.response(status_code=200, schema=GetDispatchedBikeSchema)
# Implement an URL path as function-based view
@blueprint.route('/bikes/dispatch', methods=['POST'])
@blueprint.arguments(DispatchBikeSchema)
def dispatch_bike(dispath_request):
    """
    Dispatch a bike to a user
    """
    return results