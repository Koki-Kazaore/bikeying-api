import uuid

from datetime import datetime
from typing import Optional
from uuid import UUID

from fastapi import HTTPException
from starlette.responses import Response
from starlette import status

from bikes.bikes_service.exceptions import BikeNotFoundError
from bikes.bikes_service.bikes_service import BikesService
from bikes.repository.bikes_repository import BikesRepository
from bikes.repository.unit_of_work import UnitOfWork
from app import app
# import pydantic model to be used for verification
from schemas import (
  GetBikeSchema,
  CreateBikeSchema,
  GetBikesSchema,
  BikeStatus
)

# /bikes endpoint
@app.get("/bikes", response_model=GetBikesSchema)
# Add URL query parameters to function signature
def get_bikes(status: Optional[BikeStatus] = None, limit: Optional[int] = None):
  # Start Unit of Work context
  with UnitOfWork() as unit_of_work:
    repo = BikesRepository(unit_of_work.session)
    bikes_service = BikesService(repo)
    results = bikes_service.list_bikes(
      status=status, limit=limit
    )
  return {'bikes': [result.to_dict() for result in results]}

# Specify that the response status code is 201(Created)
@app.post(
  "/bikes",
  status_code=status.HTTP_201_CREATED,
  response_model=GetBikeSchema
)
def create_bike(payload: CreateBikeSchema):
  with UnitOfWork() as unit_of_work:
    repo = BikesRepository(unit_of_work.session)
    bikes_service = BikesService(repo)
    bike = payload.model_dump()
    # Add a bike to the database
    bike = bikes_service.add_bike(bike)
    unit_of_work.commit()
    # Access bike dictionary expression before exiting the context
    # print(bike.model_dump())
    return_payload = bike.to_dict()
  return return_payload

# define URL parameters such as bike_id in curly brackets
@app.get("/bikes/{bike_id}", response_model=GetBikeSchema)
def get_bike(bike_id: UUID):
  # Capture Order Not Found Error exception using try-except block
  try:
    with UnitOfWork() as unit_of_work:
      repo = BikesRepository(unit_of_work.session)
      bikes_service = BikesService(repo)
      bike = bikes_service.get_bike(bike_id=bike_id)
    return bike.to_dict()
  except BikeNotFoundError:
    raise HTTPException(
      status_code=404, detail=f'Bike with ID {bike_id} not found'
    )

@app.put("/bikes/{bike_id}", response_model=GetBikeSchema)
def update_bike(bike_id: UUID, order_details: CreateBikeSchema):
  try:
    with UnitOfWork() as unit_of_work:
      repo = BikesRepository(unit_of_work.session)
      bikes_service = BikesService(repo)
      bike = order_details.model_dump()
      bike = bikes_service.update_bike(bike_id=bike_id, bike_info=bike)
      unit_of_work.commit()
    return bike.to_dict()
  except BikeNotFoundError:
    raise HTTPException(
      status_code=404, detail=f'Bike with ID {bike_id} not found'
    )

@app.delete("/bikes/{bike_id}",
            status_code=status.HTTP_204_NO_CONTENT,
            response_class=Response)
def delete_bike(bike_id: UUID):
  try:
    with UnitOfWork() as unit_of_work:
      repo = BikesRepository(unit_of_work.session)
      bikes_service = BikesService(repo)
      bikes_service.delete_bike(bike_id=bike_id)
      unit_of_work.commit()
  except BikeNotFoundError:
    raise HTTPException(
      status_code=404, detail=f'Bike with ID {bike_id} not found'
    )