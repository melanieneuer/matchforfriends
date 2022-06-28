from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, logout_user
from flask_wtf import FlaskForm
from config import Config
import pandas as pd
#from app.models import User

from flask import Blueprint
from app import db

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

@main.route('/match')
def match():
    return render_template('match.html')

@main.route('/profile')
def profile():
    return render_template('profile.html')
