from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config["SECRET_KEY"] = "b691319c58ebad7d5668e50058b2cf9d"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///databases/enveto.db"
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from enveto import routes