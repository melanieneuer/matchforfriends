from flask import Flask
from flask import Blueprint, flash, redirect, render_template, redirect, url_for, flash
from app import db, bcrypt
from app.forms import RegistrationForm, LoginForm, MatchForm
from flask_login import login_user, logout_user, current_user
from app.models import User, Match_Data
import sqlite3

loggedInUser = None

auth = Blueprint('auth', __name__)

connection = sqlite3.connect("site.db", check_same_thread=False)
cursor = connection.cursor()

@auth.route("/home", methods=["POST", "GET"])
def home():
    return render_template("home.html")

@auth.route('/login', methods=["POST", "GET"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('auth.match'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('auth.match'))
        else:
            flash("Login Unsuccessful. Please check email and password", "danger")
        return redirect(url_for('auth.login'))
    return render_template('login.html', title="Login", form=form)

@auth.route("/logout")
def logout():
    logout_user()
    return redirect (url_for('auth.home'))

@auth.route('/signup', methods=["POST", "GET"])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('auth.match'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created. You are now able to log in.', 'success')
        return redirect(url_for('auth.login'))
    return render_template('signup.html', title='Signup', form=form)

@auth.route('/about')
def about():
    return render_template('about.html')

@auth.route('/match', methods=["POST", "GET"])
def match():
    form = MatchForm()
    if form.validate_on_submit():
        match_data = Match_Data(fav_food=form.fav_food.data, fav_movie=form.fav_movie.data, fav_holiday=form.fav_holiday.data, coffee_routine=form.coffee_routine.data)
        db.session.add(match_data)
        db.session.commit()
        flash(f'Thank you for your answers! We will now find you some friends.', 'success')
        return redirect(url_for('auth.matches'))
    return render_template('match.html', title='Match Your Friends', form=form)

@auth.route('/matches')
def matches():
    #sql = "SELECT * FROM 'match__data' " \
    #    "WHERE fav_food = 'pizza'"
    #cursor.execute(sql)
    #for dsatz in cursor:
    #    print (dsatz[2], dsatz[3])
    #print()
    #connection.close()
    return render_template('matches.html', title='Your Matches')

@auth.route('/profile')
def profile():
    image_file = url_for("static", filename="profile_pics/" + current_user.image_file)
    return render_template('profile.html', title="Profile", image_file=image_file )

