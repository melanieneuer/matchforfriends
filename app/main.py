from flask import Flask, render_template, request, flash
from flask_login import login_user, login_required, logout_user
from flask_wtf import FlaskForm
from config import Config
from wtforms import StringField, PasswordField, SelectField
from wtforms.validators import InputRequired
import app.App as App
import pandas as pd
import datetime
from app.quiz import PopQuiz
from flask import Blueprint, render_template, redirect, url_for, request, flash
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
    App.create_history()
    return render_template('signup.html')