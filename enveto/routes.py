from flask import render_template, url_for, flash, redirect
from enveto.models import User, Post
from enveto.forms import RegisterForm, LoginForm
from enveto import app, db, bcrypt
from flask_login import login_user, logout_user, current_user

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("aboutpage.html")


@app.route("/create")
def create():
    return render_template("create.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    reg_form = RegisterForm()
    if reg_form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(reg_form.password.data).decode('utf-8') # hashing the password
        user = User(first_name=reg_form.first_name.data, last_name=reg_form.last_name.data, email=reg_form.email.data, password=hashed_password) # creating user
        db.session.add(user) # adding user to the database
        db.session.commit() # commit changes to database

        print("Account registered!") # change to flash
        return redirect(url_for('login'))

    return render_template("register.html", form=reg_form)


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email=login_form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, login_form.password.data):
            login_user(user, remember=login_form.remember.data)
            return redirect(url_for('home'))
        else:
            print('Login Failed. Please check email and password.')

    return render_template("login.html", form=login_form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

