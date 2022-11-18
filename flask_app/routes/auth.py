from flask import Blueprint, render_template, request

# create blueprint for the authentication routes of the site
auth_blueprint = Blueprint('auth', __name__, url_prefix='/auth')

@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        # POST method
        raise NotImplementedError


@auth_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        # POST method
        raise NotImplementedError
