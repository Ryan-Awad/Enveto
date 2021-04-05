from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config["SECRET_KEY"] = "SECRET_KEY_HERE"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///databases/enveto.db"
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from enveto import routes
