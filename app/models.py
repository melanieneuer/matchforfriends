from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from flask_login import UserMixin

from app import db, login_manager

class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), ForeignKey('username'), unique=True, nullable=False,)
    email = db.Column(db.String(100), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default="profile_pic.jpeg")
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"
""
class Match_Data(db.Model):
    __tablename__ = "match_data"
    id = db.Column(db.Integer, primary_key=True)
    username = db.relationship('User', primaryjoin="and_(Match_Data.username==User.username)")
    fav_food = db.Column(db.String(100), nullable=False)
    fav_movie = db.Column(db.String(100), nullable=False)
    fav_holiday = db.Column(db.String(100), nullable=False)
    coffee_routine = db.Column(db.String(100), nullable=False)

    def __repr__(self):
            return f"Match_Data('{self.fav_food}', '{self.fav_movie}', '{self.fav_holiday}', '{self.coffee_routine})"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
