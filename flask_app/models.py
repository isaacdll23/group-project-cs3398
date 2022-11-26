from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

# create db SQLAclchemy object
db = SQLAlchemy()

# create User class for users table and flask-login
class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    zipcode = db.Column(db.Integer, nullable=False)
    
    # to easily initialize a user object and hash the password
    def __init__(self, username, email, zipcode, password):
        self.username = username
        self.email = email
        self.zipcode = zipcode
        self.password = generate_password_hash(password)

    def verify_password(self, password):
        """
        Checks if the password matches the users stored hashed password.
        The password passed as an argument must be in plaintext. 
        """
        return check_password_hash(self.password, password)
    

class DailyTask(db.Model):
    __tablename__ = 'daily_tasks'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    task = db.Column(db.String(50), nullable=False)
    monday = db.Column(db.Integer, default=0)
    tuesday = db.Column(db.Integer, default=0)
    wednesday = db.Column(db.Integer, default=0)
    thursday = db.Column(db.Integer, default=0)
    friday = db.Column(db.Integer, default=0)
    saturday = db.Column(db.Integer, default=0)
    sunday = db.Column(db.Integer, default=0)
