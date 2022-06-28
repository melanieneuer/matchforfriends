from flask_sqlalchemy import SQLAlchemy

from app import db, login_manager

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default="profile_pic.jpeg")
    password = db.Column(db.String(60), nullable=False)
    #posts = db.relationship('Post', backref='author', lazy=True) example
    match_data = db.relationship('Match_Data', backref='User', lazy=True) 

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

# example
"""""
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
"""""

class Match_Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fav_food = db.Column(db.String(100), nullable=False)
    fav_movie = db.Column(db.String(100), nullable=False)
    fav_holiday = db.Column(db.String(100), nullable=False)
    coffee_routine = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

def __repr__(self):
        return f"User('{self.title}', '{self.date_posted}')"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
