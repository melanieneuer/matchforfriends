from flask import Blueprint
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

forms = Blueprint('forms', __name__)

@forms.route("/forms",  methods=["POST", "GET"])

class RegistrationForm(FlaskForm):
    username = StringField("Username", validators = [DataRequired(), Length(min=2, max=20)])
    email = StringField("Email", validators = [DataRequired(), Email()])
    password = PasswordField("Password", validators = [DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Sign Up")

class LoginForm(FlaskForm):
    email = StringField("Email", validators = [DataRequired(), Email()])
    password = PasswordField("Password", validators = [DataRequired()])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Log in")

class MatchForm(FlaskForm):
    fav_food = StringField("What is your favorite food?", validators = [DataRequired()])
    fav_movie = StringField("What is your favorite movie?", validators = [DataRequired()])
    fav_holiday = StringField("What is your favorite holiday destination?", validators = [DataRequired()])
    coffee_routine = StringField("How do you drink your coffee?", validators = [DataRequired()])
    submit = SubmitField("Submit your answers.")