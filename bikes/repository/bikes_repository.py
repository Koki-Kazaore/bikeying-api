from bikes.bikes_service.bikes import Bike
from bikes.repository.models import BikeModel, LocationModel

class BikesRepository:
  # Repository initializer requests session object
  def __init__(self, session):
    self.session = session

  def add(self, bike):
    # Create a new BikeModel record
    record = BikeModel(
      model=bike['model'],
      status=bike['status'].value,
      location=LocationModel(
        latitude=bike['location']['latitude'],
        longitude=bike['location']['longitude']
      )
    )
    # Add the object to the session
    self.session.add(record)
    # Return instance of Bike class
    return Bike(**record.dict(), bike_=record)

  # Generic method to retrieve records by ID
  def _get(self, id_):
    # Get a record using first method of SQLAlchemy
    return (
      self.session.query(BikeModel)
      .filter(BikeModel.id == str(id_))
      .first()
    )

  def get(self, id_):
    # Get a record using _get()
    bike = self._get(id_)
    # Returns a Bike object if the bike exists
    if bike is not None:
      return Bike(**bike.dict())
    record = self._get(id_)

  # Returns limit parameters and other optional filters
  def list(self, limit=None, **filters):
    # Build a query dynamically
    query = self.session.query(BikeModel)
    # Using SQLAlchemy's filter method,
    # Filter by whether bike is available or not
    if 'status' in filters:
      status = filters.pop('status')
      query = query.filter(BikeModel.status == status.value)
    records = query.filter_by(**filters).limit(limit).all()
    # Return a list of Bike objects
    return [Bike(**record.dict()) for record in records]

  def update(self, id_, payload):
    record = self._get(id_)
    # To update an bike, after deleting an element associated with that bike,
    # Create a new elements based on the payload passed
    if record is not None:
      self.session.delete(record)
      record = BikeModel(
        id=str(id_),
        model=payload['model'],
        status=payload['status'].value,
        location=LocationModel(
          latitude=payload['location']['latitude'],
          longitude=payload['location']['longitude']
        )
      )
      self.session.add(record)
      return Bike(**record.dict())

  def delete(self, id_):
    # Call delte method of SQLAlchemy to delete a record
    self.session.delete(self._get(id_))