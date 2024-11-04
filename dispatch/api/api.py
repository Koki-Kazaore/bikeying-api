import uuid
from datetime import datetime

from flask.views import MethodView
from flask_smorest import Blueprint

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

# Implement an URL path as function-based view
@blueprint.route('/bikes/dispatch', methods=['POST'])
def dispatch_bike(dispath_request):
    """
    Dispatch a bike to users
    """
    return results, 200