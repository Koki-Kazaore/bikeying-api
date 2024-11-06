from marshmallow import Schema, fields, validate, EXCLUDE

class LocationSchema(Schema):
  # Prohibit unknown properties using EXCLUDE
  class Meta:
    unknown = EXCLUDE

  latitude = fields.Float(
    required=True,
    validate=validate.Range(min=-90, max=90),
    description="latitude"
  )
  longitude = fields.Float(
    required=True,
    validate=validate.Range(min=-180, max=180),
    description="longitude"
  )

class DispatchRequestSchema(Schema):
  class Meta:
    unknown = EXCLUDE

  tpep_pickup_datetime = fields.DateTime(
    required=True,
    description="リクエストの受付日時"
  )
  tpep_dropoff_datetime = fields.DateTime(
    required=True,
    description="リクエストの返却日時"
  )
  PULocation = fields.Nested(LocationSchema, required=True)
  DOLocation = fields.Nested(LocationSchema, required=True)

class DispatchBikeSchema(Schema):
  df_requests = fields.List(fields.Nested(DispatchRequestSchema), required=True)

class DispatchedBikeSchema(Schema):
  class Meta:
    unknown = EXCLUDE

  bike_id = fields.Str(
    required=True,
    description="Assigned bike ID"
  )
  user_queue_index = fields.Str(
    required=True,
    description="リクエストID"
  )

class GetDispatchedBikeSchema(Schema):
  class Meta:
    unknown = EXCLUDE

  results = fields.List(fields.Nested(DispatchedBikeSchema), required=True)