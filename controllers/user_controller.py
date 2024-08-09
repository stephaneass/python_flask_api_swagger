from app import app
from flask import jsonify, make_response
from models.userModel import Users
from marshmallow import ValidationError
from flask_apispec import FlaskApiSpec, doc, use_kwargs
from flask_jwt_extended import JWTManager, create_access_token
from apispec.ext.marshmallow import MarshmallowPlugin
from datetime import timedelta
from swagger.schemas import Register
from apispec import APISpec

# Configuration de JWT
app.config["JWT_SECRET_KEY"] = 'a Long TexTe Here caN yOu SeE IT?!=@'
app.config['JWT_TOKEN_LOCATION'] = ['headers']
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=10)  # Durée de vie du token d'accès
app.config['JWT_REFRESH_TOKEN_EXPIRES'] = timedelta(days=1)

# Configuration de l'application
app.config.update({
    'APISPEC_SPEC': APISpec(
        title='Flask API with Swagger',
        version='v1',
        openapi_version='3.0.2',
        plugins=[MarshmallowPlugin()],
    ),
    'APISPEC_SWAGGER_URL': '/swagger/',
    'APISPEC_SWAGGER_UI_URL': '/swagger-ui/',  # Le chemin pour Swagger UI statique
})

# Initialisation de JWT
jwt = JWTManager(app)

docs = FlaskApiSpec(app)

@app.route('/users/register', methods=['POST'])
@doc(description='Enregistrer un nouvel utilisateur.')
@use_kwargs(Register, location='json')
def register(name, phone, email, password):
    schema = Register()
    try:
        result = schema.load({'name': name, 'phone': phone, 'email': email, 'password': password})
    except ValidationError as err:
        print(f"ValidationError: {err.messages}")
        response = make_response(jsonify({
            "message": "Erreur de validation",
            "errors": err.messages
        }), 400)
        return response

    # Vérification de l'existence de l'email
    if Users.getByEmail(result['email']):
        response = make_response(jsonify({"message": "Email déjà utilisé"}), 400)
        return response
    
    # Vérification de l'existence du téléphone
    if Users.getByPhone(result['phone']):
        response = make_response(jsonify({"message": "Téléphone déjà utilisé"}), 400)
        return response
    
    # Enregistrement de l'utilisateur
    user = Users.register(result)

    if user:
        token = create_access_token(identity=user.id)
        response = make_response(jsonify({
            "message": "Enregistrement réussi",
            'access_token': token,
            "user": {
                "name": user.name,
                "email": user.email,
                "phone": user.phone,
                "role": user.role.label
            }
        }), 201)
        return response
    
    response = make_response(jsonify({"message": "Une erreur est survenue"}), 500)
    return response

# Initialisation de Flask-APISpec pour la documentation Swagger

docs.register(register)
