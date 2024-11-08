import uuid

from datetime import datetime
from typing import Optional
from uuid import UUID

from fastapi import HTTPException
from starlette.responses import Response
from starlette import status

from app import app
# from flask.views import MethodView
# from flask_smorest import Blueprint

# Import marshmallow models
from schemas import (
  DispatchRequestSchema,
  DispatchBikeSchema,
  DispatchedBikeSchema,
  GetDispatchedBikeSchema
)

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

@app.post("/bikes/dispatch", response_model=GetDispatchedBikeSchema)
def dispatch_bike(dispath_request: DispatchBikeSchema):
    """
    Dispatch a bike to a user
    """
    return {"results": results}