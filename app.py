from flask import Flask, render_template, url_for, flash, redirect
from forms import RegisterForm
import json
import hashlib

app = Flask(__name__)
app.config["SECRET_KEY"] = "b691319c58ebad7d5668e50058b2cf9d"

def encrypt_md5(string):
    string = string.encode()
    md5_digest = hashlib.md5(string).digest()
    return md5_digest


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
    reg_form = RegisterForm()
    if reg_form.validate_on_submit():
        password = encrypt_md5(reg_form.password.data)
        account_data = {
            "first_name": reg_form.first_name.data,
            "last_name": reg_form.last_name.data,
            "email": reg_form.email.data,
            "password": password
        }

        with open('database/accounts.json', 'r') as db_read:
            with open('database/accounts.json', 'w') as db_write:
                db_read = json.load(db_read)
                db_read.append(account_data)
                json.dump(db_read, db_write, indent=4)
        
        return redirect(url_for('home'))
        
    return render_template("register.html", form=reg_form)

@app.route("/login")
def login():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)