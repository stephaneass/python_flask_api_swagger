from app import app, db
from datetime import datetime
from werkzeug.security import check_password_hash, generate_password_hash
from flask_migrate import Migrate

migrate = Migrate(app, db)

class Roles(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    label = db.Column(db.String(20), nullable = False, unique = True)
    users = db.relationship('Users', backref='role')

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    phone = db.Column(db.String(40), nullable=False, unique=True)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

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
    
    def getByPhone(cls, phone):
        return Users.query.filter_by(phone = phone).first()
    
    def register(cls, data):
        user = Users(name = data['name'], email = data['email'], phone = data['phone'], 
                     password = data['password'], role = 'user')
        try :
            db.session.add(user)
            db.session.commit()
            return user
        except :
            return None
    
    getByEmail = classmethod(getByEmail)
    getByPhone = classmethod(getByPhone)
    register = classmethod(register)