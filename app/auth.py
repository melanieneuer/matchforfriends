from flask import Flask
from flask import Blueprint, flash, redirect, render_template, redirect, url_for, flash

from app.models import User
from app.forms import RegistrationForm, LoginForm, MatchForm

loggedInUser = None

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=["POST", "GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash("You have been logged in!", "success")
        return redirect(url_for('auth.home'))
    else:
        flash("Login Unsuccessful. Please check unsername and password", "danger")
    return render_template('login.html', title="Login", form=form)

@auth.route('/signup', methods=["POST", "GET"])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('auth.home'))
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

