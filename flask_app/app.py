import dotenv
from flask import Flask
from flask_login import LoginManager
from .routes import main_blueprint, auth_blueprint
from .models import User, db

def create_app():
    # create Flask object
    app = Flask(__name__)
    
    # set app config
    app.config['SECRET_KEY'] = b'\xcfm\xd4\x98\x04$\x11,\x98j\x81\xa1z{k\x93\xb2`\x02\xb6\x99\x9e\xdf\x9e\xe9\x0fQ\x13I{\x97\xaf'
    app.config['SQLALCHEMY_DATABASE_URI'] = dotenv.get_key('.env', "DATABASE_URL")

    # register app blueprints
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint)

    # initialize the SQLAlchemy db object with the flask app
    db.init_app(app)

    # create the tables
    with app.app_context():
        db.create_all()

    # initalize login manager
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    # login manager user loader callback function
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app