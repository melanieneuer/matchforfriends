from flask import Flask, render_template, request, flash
from flask_login import login_user, login_required, logout_user
from flask_wtf import FlaskForm
from config import Config
from wtforms import StringField, PasswordField, SelectField
from wtforms.validators import InputRequired
import pandas as pd
import datetime
from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
# from app.models import User

from flask import Blueprint
from . import db

main = Blueprint('main', __name__)


@main.route("/",  methods=["POST", "GET"])
@main.route('/login')
def login():
    return render_template('login.html')

@main.route('/sign-up')
def signup():
    return render_template('signup.html')

@main.route("/home", methods=["POST", "GET"])
def home():
    return render_template("home.html")

#@main.route("/match", methods=["GET", "POST"])
#def wtf_quiz():
#    form = PopQuiz()
#    form.validate_on_submit()
 #   from app.quiz import points, questions, quiz_achieve
#    if points / questions >= quiz_achieve:
#        return render_template("passed.html", value=f"Youve gotten {(points / questions) * 100}% of the questions right")

 #   return render_template("quiz.html", form=form)


@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@main.route("/Profile",  methods=["POST", "GET"])
def Me():
    return render_template("profile.html")