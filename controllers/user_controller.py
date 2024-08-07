from app import app

@app.route('/users/register')
def register():
    return "This is the registration form"