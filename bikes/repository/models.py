import uuid
from datetime import datetime

from sqlalchemy import Column, Integer, DateTime, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# Create declarative_base model
Base = declarative_base()

# Custom function to generate UUID
def generate_uuid():
  return str(uuid.uuid4())

# All models have to inherit from Base
class BikeModel(Base):
  # Define the table name
  __tablename__ = 'bikes'

  # Each class property is mapped to a database column using the Column class
  id = Column(String, primary_key=True, default=generate_uuid)
  model = Column(String)
  status = Column(String, nullable=False, default='maintenance')
  # Define a relationship with the Location model
  location = relationship('LocationModel', backref='bikes', uselist=False)
  created_at = Column(DateTime, default=datetime.now)
  updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

  # Custom method to render the object as Python dictionary
  def dict(self):
    return {
      'id': self.id,
      'model': self.model,
      'status': self.status,
      'location': self.location.dict(),
      'created_at': self.created_at,
      'updated_at': self.updated_at
    }

class LocationModel(Base):
  __tablename__ = 'locations'

  id = Column(Integer, primary_key=True)
  latitude = Column(Integer)
  longitude = Column(Integer)
  bike_id = Column(String, ForeignKey('bikes.id'))

  def dict(self):
    return {
      'latitude': self.latitude,
      'longitude': self.longitude
    }