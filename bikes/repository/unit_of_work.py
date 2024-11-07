from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class UnitOfWork:

  def __init__(self):
    # Get session factory object
    self.session_maker = sessionmaker(
      bind=create_engine('sqlite:///bikes.db')
    )

  def __enter__(self):
    # Open a new database session
    self.session = self.session_maker()
    # Return instance of UnitOfWork object
    return self

  # Access to exceptions raised during the execution of an existing context
  def __exit__(self, exc_type, exc_val, traceback):
    # Check whether an exception has been raised
    if exc_type is not None:
      # Rollback the transaction if an exception has been raised
      self.rollback()
      # Close the database session
      self.session.close()
    self.session.close()

  def commit(self):
    # Wrapper for SQLAlchemy commit method
    self.session.commit()

  def rollback(self):
    # Wrapper for SQLAlchemy rollback method
    self.session.rollback()