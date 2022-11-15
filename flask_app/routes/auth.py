from flask import Blueprint

# create blueprint for the authentication routes of the site
auth_blueprint = Blueprint('auth', __name__, url_prefix='/auth')
