from flask_seeder import Seeder
from models.userModel import Roles
from app import db

class RolesSeeder(Seeder):
    def run(self):
        role1 = Roles(label = 'admin')
        role2 = Roles(label = 'user')

        roles_list = [role1, role2]

        for role in roles_list :
            db.session.add(role)
            
        db.session.commit()