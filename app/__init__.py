from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import secrets
from flask_login import LoginManager

# Generate a random secret key
secret_key = secrets.token_hex(16)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SECRET_KEY'] = secret_key

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

from app import views