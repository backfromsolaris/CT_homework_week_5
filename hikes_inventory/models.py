from enum import unique
from flask_login.mixins import UserMixin
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
import uuid


# Adding Flask Security for Passwords
from werkzeug.security import generate_password_hash, check_password_hash

import secrets

# imports login manager from flask_login package
from flask_login import LoginManager, UserMixin

login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# acting as a DB class
db = SQLAlchemy()


class User(db.Model, UserMixin):
    id = db.Column(db.String, primary_key = True)
    email = db.Column(db.String(150), nullable = False, unique = True)
    password = db.Column(db.String, nullable = False)
    token = db.Column(db.String, unique = True)
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)

    def __init__(self, email, password, token = '', id = ''):
        self.id = self.set_id()
        self.email = email
        self.password = self.set_password(password)
        self.token = self.set_token(24)
    
    def set_id(self):
        return str(uuid.uuid4())
    
    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash

    def set_token(self, length):
        return secrets.token_hex(length)

class Hike(db.Model):
    id = db.Column(db.String, primary_key = True)
    hike_name = db.Column(db.String(150))
    country = db.Column(db.String(100))
    district = db.Column(db.String(100))
    city = db.Column(db.String(100))
    coordinates = db.Column(db.String(30), nullable = True)
    length = db.Column(db.Numeric(6.2))
    elevation_gain = db.Column(db.Numeric(5), nullable = True)
    hike_type = db.Column(db.String(50))
    difficulty = db.Column(db.String(30))
    parking = db.Column(db.Boolean, nullable = True)
    user_token = db.Column(db.String, db.ForeignKey('user.token', nullable = False))

