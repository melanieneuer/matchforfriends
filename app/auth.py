from flask import Flask
from flask import Blueprint, flash, redirect, render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

from app import db
from app.models import User
from app.forms import RegistrationForm
from app.forms import LoginForm

loggedInUser = None

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    form = LoginForm()
    if form.email.data == "admin@blog.com" and form.password.data == "password":
        flash("You have been logged in!", "success")
        return redirect(url_for('auth.home'))
    else:
        flash("Login Unsuccessful. Please check unsername and password", "danger")
    return render_template('login.html', title="Login", form=form)
    #return redirect(url_for('auth.login'))

@auth.route('/signup', methods=["POST", "GET"])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('auth.home'))
    return render_template('signup.html', title='Signup', form=form)

"""""
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
"""""

@auth.route("/home", methods=["POST", "GET"])
def home():
    return render_template("home.html")
    #return redirect(url_for('auth.home'))

"""""
@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()
    if user:
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))

    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('auth.login'))


@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))
    login_user(user, remember=remember)
    global loggedInUser
    loggedInUser = user
    return redirect(url_for('auth.home'))
"""""

@auth.route('/about')
def about():
    return render_template('about.html')
    #return redirect(url_for('auth.login'))

@auth.route('/match')
def match():
    return render_template('match.html')
    #return redirect(url_for('auth.login'))

@auth.route('/profile')
def profile():
    return render_template('profile.html')
    #return redirect(url_for('auth.login'))

