from datetime import datetime
from enum import Enum
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel, Extra, conint, conlist, validator

#　Declare an enumerated schema
class BikeStatus(Enum):
    available = "available"
    in_use = "in_use"
    maintenance = "maintenance"

# Each pydantic model inherits from pydantic's BaseModel
class LocationSchema(BaseModel):
  # specify the type of each field using the type hint
  latitude: float
  longitude: float

  # Use Config to prohibit properties not defined in the schema
  class Config:
    extra = 'forbid'

class CreateBikeSchema(BaseModel):
  # specify the default value
  status: Optional[BikeStatus] = BikeStatus.maintenance
  model: Optional[str] = None
  location: LocationSchema

  class Config:
    extra = 'forbid'

  @validator('status')
  def status_non_nullable(cls, value):
    assert value is not None, 'status may not be None'
    return value

class GetBikeSchema(BaseModel):
  id: UUID
  model: Optional[str] = None
  status: BikeStatus
  location: LocationSchema

class GetBikesSchema(BaseModel):
  bikes: List[GetBikeSchema]

class DispatchRequestSchema(BaseModel):
  tpep_pickup_datetime: datetime
  tpep_dropoff_datetime: datetime
  PULocation: LocationSchema
  DOLocation: LocationSchema

  class Config:
    extra = 'forbid'

class DispatchBikeSchema(BaseModel):
  df_requests: List[DispatchRequestSchema]

class DispatchedBikeSchema(BaseModel):
  bike_id: str
  user_queue_index: str

  class Config:
    extra = 'forbid'

class GetDispatchedBikeSchema(BaseModel):
  results: List[DispatchedBikeSchema]

  class Config:
    extra = 'forbid'