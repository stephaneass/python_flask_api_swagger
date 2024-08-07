from app import app
from flask import request, jsonify
from json import dumps, loads
from models.userModel import Users
from marshmallow import Schema, fields, validate, ValidationError

class Register(Schema):
    name = fields.String(required=True, validate=validate.Length(min=3))
    phone = fields.String(required=True, validate=validate.Length(min=8))
    email = fields.Email(required=True)
    password = fields.String(required=True, validate=validate.Length(min=4))

@app.route('/users/register', methods=['POST'])
def register():
    data = request.json
    schema = Register()
    try: 
        result = schema.load(data)
    except ValidationError as err:
        # Return a nice message if validation fails
        return jsonify(err.messages), 400

    #user = Users.getByEmail(request.form['email'])
    return result['name']