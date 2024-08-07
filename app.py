from flask import Flask

app = Flask(__name__)

from controllers import *
@app.route("/")
def index():
    return "You're on the index page"
