from flask_seeder import Seeder
from models.userModel import Users
from app import db

class UserSeeder(Seeder):
    def run(self):
        
        user1 = Users(id=1, name="Dieu est grand", email='dieu@gmail.com', password="1111", phone="67710659", role='super_admin')
        user2 = Users(id=2, name="ASSOCLE Bright", email='bright@gmail.com', password="1111", phone="67710660", role='admin')
        user3 = Users(id=3, name="ASSOCLE Prisca", email='prisca@gmail.com', password="1111", phone="67710661", role='user')

        users_list = [ user1, user2, user3 ]

        for user in users_list:
            db.session.add(user)
            
        db.session.commit()