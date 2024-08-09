from marshmallow import Schema, fields, validate

# Marshmallow Schemas

class UserSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    email = fields.Email()
    phone = fields.String()
    created_at = fields.DateTime()

class Register(Schema):
    name = fields.String(required=True, validate=validate.Length(min=3))
    phone = fields.String(required=True, validate=validate.Length(min=8))
    email = fields.Email(required=True)
    password = fields.String(required=True, validate=validate.Length(min=4))
    
class RegisterResponse(Schema):
    message = fields.String()
    access_token = fields.String()
    data = fields.Nested(UserSchema)