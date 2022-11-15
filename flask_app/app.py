from flask import Flask
from .routes import main_blueprint, auth_blueprint
import dotenv

def create_app():
    # create Flask object
    app = Flask(__name__)
    
    # set app config
    app.config['SECRET_KEY'] = b'\xcfm\xd4\x98\x04$\x11,\x98j\x81\xa1z{k\x93\xb2`\x02\xb6\x99\x9e\xdf\x9e\xe9\x0fQ\x13I{\x97\xaf'
    app.config['SQLALCHEMY_DATABASE_URI'] = dotenv.get_key('.env', "DATABASE_URL")

    # registe app blueprints
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint)

    return app