from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

# create db SQLAclchemy object
db = SQLAlchemy()

# create User class for users table and flask-login
class User(UserMixin, db.Model):
    __tablename__ = 'users'
    raise NotImplementedError