from datetime import datetime
from uuid import UUID

from starlette.responses import Response
from starlette import status

from bikes.app import app
# import pydantic model to be used for verification
from bikes.api.schemas import (
  GetBikeSchema,
  CreateBikeSchema,
  GetBikesSchema
)

# define a bike object to response
bikes = {
  "id": "601e69ec-4f29-490d-a14f-be0184742640",
  "status": "available",
  "location": {
    "latitude": 35.681236,
    "longitude": 139.767125
  }
}

# /bikes endpoint
# @app.get("/bikes", response_model=List[GetBikeSchema])
@app.get("/bikes", response_model=GetBikesSchema)
def get_bikes():
  return {'bikes': [bikes]}

# Specify that the response status code is 201(Created)
@app.post(
  "/bikes",
  status_code=status.HTTP_201_CREATED,
  response_model=GetBikeSchema
)
def create_bike(bike_details: CreateBikeSchema):
  return bikes

# define URL parameters such as bike_id in curly brackets
@app.get("/bikes/{bike_id}", response_model=GetBikeSchema)
def get_bike(bike_id: UUID):
  # get a URL parameter as an argument
  return bikes

@app.put("/bikes/{bike_id}", response_model=GetBikeSchema)
def update_bike(bike_id: UUID, order_details: CreateBikeSchema):
  return bikes

@app.delete("/bikes/{bike_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_bike(bike_id: UUID):
  # return Response(status_code=status.HTTP_204_NO_CONTENT)
  return bikes