from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = "My Super Secret Key"
#Config database for Mysql
## Échappez le caractère @ dans le mot de passe
password = 'stephaneP%40ssw0rd'
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://stephane:{password}@localhost/flask_api"

#init database
db = SQLAlchemy(app)

from controllers import *
@app.route("/")
def index():
    return "You're on the index page"
