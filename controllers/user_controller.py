from app import app
from flask import request, jsonify
from json import dumps, loads
from models.userModel import Users
from marshmallow import Schema, fields, validate, ValidationError
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt
from datetime import timedelta

app.config["JWT_SECRET_KEY"] = 'a Long TexTe Here caN yOu SeE IT?!=@'
app.config['JWT_TOKEN_LOCATION'] = ['headers']
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=10)  # Durée de vie du token d'accès
app.config['JWT_REFRESH_TOKEN_EXPIRES'] = timedelta(days=1)

# JWT Initialization
jwt = JWTManager(app)

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

    user = Users.getByEmail(result['email'])
    if user :
        return jsonify({
            "message":"Email already taken",
        }), 201
    
    user = Users.getByPhone(result['phone'])
    if user :
        return jsonify({
            "message":"Phone already taken",
        }), 201
    
    user = Users.register(result)

    if user :
        token = create_access_token(identity=user.id)
        return jsonify({
            "message":"Registration done successfully",
            'access_token': token,
            "user" : {
                "name": user.name,
                "email": user.email,
                "phone": user.phone,
                "role": user.role.label
            }
        }), 201
    
    return jsonify({
            "message":"An error occured",
        }), 500