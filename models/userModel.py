from app import db
from datetime import datetime
from werkzeug.security import check_password_hash, generate_password_hash

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    phone = db.Column(db.String(40), nullable=False, unique=True)
    role = db.Column(db.String(20), nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    @property
    def password(self):
        raise AttributeError("Password is not a readable attribute")
    
    @password.setter
    def password(self, pwd):
        self.password_hash = generate_password_hash(pwd)

    def verify_password(self, pwd):
        return check_password_hash(self.password_hash, pwd)
    
    # Create a String
    def __repr__(self):
        return '<Name %r>' % self.name
    
    def getByEmail(cls, email):
        return Users.query.filter_by(email = email).first()
    
    getByEmail = classmethod(getByEmail)