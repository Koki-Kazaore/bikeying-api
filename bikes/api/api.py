from datetime import datetime
from uuid import UUID

from starlette.responses import Response
from starlette import status

from bikes.app import app

# define a bike object to response
bikes = {
  "bikeId": "bike_123456",
  "status": "available",
  "location": [35.681236, 139.767125]
}

# /bikes endpoint
# @app.get("/bikes", response_model=List[GetBikeSchema])
@app.get("/bikes")
def get_bikes():
  return {'bikes': [bikes]}

# Specify that the response status code is 201(Created)
@app.post("/bikes", status_code=status.HTTP_201_CREATED)
def create_bike():
  return bikes

# define URL parameters such as bike_id in curly brackets
@app.get("/bikes/{bike_id}")
def get_bike(bike_id: UUID):
  # get a URL parameter as an argument
  return bikes

@app.put("/bikes/{bike_id}")
def update_bike(bike_id: UUID):
  return bikes

@app.delete("/bikes/{bike_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_bike(bike_id: UUID):
  # return Response(status_code=status.HTTP_204_NO_CONTENT)
  return bikes