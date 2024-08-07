from app import app
from models.userModel import User


@app.route('/users/register')
def register():
    user = User()
    return user.getName()