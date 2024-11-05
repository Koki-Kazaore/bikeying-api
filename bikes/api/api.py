import uuid

from datetime import datetime
from typing import Optional
from uuid import UUID

from fastapi import HTTPException
from starlette.responses import Response
from starlette import status

from bikes.app import app
# import pydantic model to be used for verification
from bikes.api.schemas import (
  GetBikeSchema,
  CreateBikeSchema,
  GetBikesSchema,
  BikeStatus
)

# represent in-memory bike lists as Python lists
BIKES = []

# /bikes endpoint
# @app.get("/bikes", response_model=List[GetBikeSchema])
@app.get("/bikes", response_model=GetBikesSchema)
# Add URL query parameters to function signature
def get_bikes(status: Optional[BikeStatus] = None, limit: Optional[int] = None):
  # Returns control immiediately if no parameters are set
  if status is None and limit is None:
    return {'bikes': BIKES}

  # Narrow the list to query_set if either parameter is set
  query_set = BIKES

  # check if status is set
  if status is not None:
    query_set = [
      bike
      for bike in query_set
      if bike['status'] == status
    ]

  # If limit is set and its value is less than the size of the query_set,
  # returns a sbuset of query_set
  if limit is not None and len(query_set) > limit:
    return {'bikes': query_set[:limit]}

  return {'bikes': query_set}

# Specify that the response status code is 201(Created)
@app.post(
  "/bikes",
  status_code=status.HTTP_201_CREATED,
  response_model=GetBikeSchema
)
def create_bike(bike_details: CreateBikeSchema):
  # convert each bike to a dictionary
  bike = bike_details.model_dump()
  # extend order object with server-side attributes such as ID
  bike['id'] = uuid.uuid4()
  bike['created_at'] = datetime.now()
  # to create a bike add that bike to the BIKES list
  BIKES.append(bike)
  # return the created bike after adding it to the list
  return bike

# define URL parameters such as bike_id in curly brackets
@app.get("/bikes/{bike_id}", response_model=GetBikeSchema)
def get_bike(bike_id: UUID):
  # get a URL parameter as an argument
  # to search by bike_id, process the BIKES list in order and check ID
  for bike in BIKES:
    if bike['id'] == bike_id:
      return bike
  # if the bike is not found, raise an exception
  # generate HTTPException and return a 404 status code
  raise HTTPException(
    status_code=404, detail=f'Bike with ID {bike_id} not found'
  )

@app.put("/bikes/{bike_id}", response_model=GetBikeSchema)
def update_bike(bike_id: UUID, order_details: CreateBikeSchema):
  for bike in BIKES:
    if bike['id'] == bike_id:
      bike.update(order_details.model_dump())
      return bike
  raise HTTPException(
    status_code=404, detail=f'Bike with ID {bike_id} not found'
  )

@app.delete("/bikes/{bike_id}",
            status_code=status.HTTP_204_NO_CONTENT,
            response_class=Response)
def delete_bike(bike_id: UUID):
  # delete a bike from the BIKES list with list.pop() method
  for index, bike in enumerate(BIKES):
    if bike['id'] == bike_id:
      BIKES.pop(index)
      return Response(status_code=status.HTTP_204_NO_CONTENT)
  raise HTTPException(
    status_code=404, detail=f'Bike with ID {bike_id} not found'
  )