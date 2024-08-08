from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_seeder import FlaskSeeder
from config.config import dbconfig

app = Flask(__name__)

app.config['SECRET_KEY'] = "My Super Secret Key"
#Config database for Mysql
## Échappez le caractère @ dans le mot de passe
password = 'stephaneP%40ssw0rd'
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+mysqlconnector://{dbconfig['user']}:{dbconfig['password']}@{dbconfig['hostname']}/{dbconfig['database']}"

#init database
db = SQLAlchemy(app)

seeder = FlaskSeeder(app, db)

from controllers import *
@app.route("/")
def index():
    return "You're on the index page"

if __name__ == '__main__':
    app.run(debug=True)