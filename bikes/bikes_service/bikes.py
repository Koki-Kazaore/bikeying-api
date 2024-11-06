import requests

from bikes.bikes_service.exceptions import (
  APIIntegrationError, InvalidActionError
)

# Bussiness object to represent location
class Location:
  # Declare initializer parameters for Location
  def __init__(self, latitude, longitude):
    self.latitude = latitude
    self.longitude = longitude

class Bike:
  def __init__(self, id, model, status, location,
               created_at, updated_at, bike_=None):
    # bike_ parameter represents an instance of the BikeModel object
    self._bike = bike_
    # IDs are resolved dynamically,
    # so the specified ID is stored as a private property
    self.id = id
    self.model = model
    self.status = status
    self.location = location
    self.created_at = created_at
    self.updated_at = updated_at

  # Resolve IDs dynamically using property() decorator
  @property
  def id(self):
    return self._id or self._bike.id

  @property
  def created_at(self):
    return self._created_at or self._bike.created_at

  @property
  def updated_at(self):
    return self._updated_at or self._bike.updated_at

  @property
  def status(self):
    return self._status or self._bike.status

  def dispatch(self):
    # Call Dispatch API to dispatch a bike
    df_requests = [
      {
        "tpep_pickup_datetime": "2024-11-06T04:41:22.761Z",
        "tpep_dropoff_datetime": "2024-11-06T04:41:22.761Z",
        "PULocation": {
          "latitude": self.location.latitude,
          "longitude": self.location.longitude
        },
        "DOLocation": {
          "latitude": self.location.latitude,
          "longitude": self.location.longitude
        }
      }
    ]
    response = requests.post(
      'http://localhost:3000/bike/dispatch',
      json={'df_requests': df_requests}
    )
    # Returns dispatched results
    # if received susccess response from Dispatch API
    if response.status_code == 201:
      return response.json()
    raise APIIntegrationError(
      f'Could not dispatch bike {self.id}'
    )