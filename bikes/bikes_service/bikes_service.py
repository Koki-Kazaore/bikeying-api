from bikes.bikes_service.exceptions import BikeNotFoundError

class BikesService:
  # Instantiation of BikesService class reuires an instance of the Bike Repository
  def __init__(self, bikes_repository):
    self.bikes_repository = bikes_repository

  def add_bike(self, bike):
    # add a bike to create database record
    return self.bikes_repository.add(bike)

  def get_bike(self, bike_id):
    # Pass the requested ID to the bike repository to get bike details
    bike = self.bikes_repository.get(bike_id)
    # Generate BikeNotFoundError exception if the bike is not found
    if bike is not None:
      return bike
    raise BikeNotFoundError(f'Bike with id {bike_id} not found')

  def update_bike(self, bike_id, bike_info):
    bike = self.bikes_repository.get(bike_id)
    if bike is None:
      raise BikeNotFoundError(f'Bike with id {bike_id} not found')
    return self.bikes_repository.update(bike_id, bike_info)

  def list_bikes(self, **filters):
    # Capture dictonary as filters using keyword arguments
    status = filters.pop('status', None)
    limit = filters.pop('limit', None)
    return self.bikes_repository.list(limit, **filters)

  def delete_bike(self, bike_id):
    bike = self.bikes_repository.get(bike_id)
    if bike is None:
      raise BikeNotFoundError(f'Bike with id {bike_id} not found')
    return self.bikes_repository.delete(bike_id)