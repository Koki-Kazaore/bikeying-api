# Exception notifying that the bike is not present
class BikeNotFoundError(Exception):
  pass

# Exception notifying that an API integration error has occurred
class APIIntegrationError(Exception):
  pass

# Exception notifying that action being performed is invalid
class InvalidActionError(Exception):
  pass