from flask import Flask, render_template, url_for, flash, redirect
from forms import RegisterForm
import json
import hashlib

app = Flask(__name__)
app.config["SECRET_KEY"] = 'd18bc10be13889abf8b7e9c9a2ab8e8d'

def encrypt_md5(string): # MD5 encryption for passwords
    string = string.encode()
    hash_object = hashlib.md5(string)
    hash_digest = hash_object.hexdigest()
    return hash_digest


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/create")
def create():
    return render_template("create.html")

@app.route("/about")
def about():
    return render_template("aboutpage.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    reg_form = RegisterForm()
    if reg_form.validate_on_submit():
        # Encrypting the password
        password = encrypt_md5(reg_form.password.data)

        account_data = {
            "first_name": reg_form.first_name.data,
            "last_name": reg_form.last_name.data,
            "email": reg_form.email.data,
            "password": password,
        }

        db_read = json.load(open('database/accounts.json', 'r'))
        db_read.append(account_data)
        db = open('database/accounts.json', 'w')
        json.dump(db_read, db, indent=4)

        return redirect(url_for('home'))

    return render_template("register.html", form=reg_form)

@app.route("/login")
def login():
    return "<h1>Login Page</h1>"

if __name__ == "__main__":
    app.run(debug=True)