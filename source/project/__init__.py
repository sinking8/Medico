from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app  =Flask(__name__)
app.config['SECRET_KEY']='d4552cab351cd4b708cbbd3d26ec2f04'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.init_app(app)

from project import routes