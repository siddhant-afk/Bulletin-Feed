from flask import Flask,render_template, redirect,url_for,flash,get_flashed_messages
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SECRET_KEY'] = 'a049b89bf64d21fbd8e22a44'
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"
db = SQLAlchemy(app)
