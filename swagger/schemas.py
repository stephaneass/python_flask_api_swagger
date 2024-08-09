from marshmallow import Schema, fields, validate

# Marshmallow Schemas

class Register(Schema):
    name = fields.String(required=True, validate=validate.Length(min=3))
    phone = fields.String(required=True, validate=validate.Length(min=8))
    email = fields.Email(required=True)
    password = fields.String(required=True, validate=validate.Length(min=4))