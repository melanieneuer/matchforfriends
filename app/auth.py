from flask import Flask
from flask import Blueprint, flash, redirect, render_template, redirect, url_for, flash
from app import app, db, bcrypt
from app.forms import RegistrationForm, LoginForm, MatchForm
from flask_login import login_user, logout_user, current_user
from app.models import User
loggedInUser = None

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=["POST", "GET"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data).first():
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            flash("Login Unsuccessful. Please check email and password", "danger")
        return redirect(url_for('auth.home'))
    return render_template('login.html', title="Login", form=form)

@auth.route("/logout")
def logout():
    logout_user()
    return redirect (url_for('home'))

@auth.route('/signup', methods=["POST", "GET"])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created. You are now able to log in.', 'success')
        return redirect(url_for('auth.login'))
    return render_template('signup.html', title='Signup', form=form)

@auth.route("/home", methods=["POST", "GET"])
def home():
    return render_template("home.html")

@auth.route('/about')
def about():
    return render_template('about.html')

@auth.route('/match', methods=["POST", "GET"])
def match():
    form = MatchForm()
    if form.validate_on_submit():
        flash(f'Thank you for your answers! We will now find you some friends.', 'success')
        return redirect(url_for('auth.match'))
    return render_template('match.html', title='Match Your Friends', form=form)

@auth.route('/profile')
def profile():
    return render_template('profile.html')

