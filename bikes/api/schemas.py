from datetime import datetime
from enum import Enum
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel, field_validator

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

  @field_validator('status')
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