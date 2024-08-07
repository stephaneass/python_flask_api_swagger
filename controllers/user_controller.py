from app import app
from models.userModel import Users


@app.route('/users/register')
def register():
    user = Users()
    return user.getName()