from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, current_user, logout_user
from flask_app.models import db, User

# create blueprint for the authentication routes of the site
auth_blueprint = Blueprint('auth', __name__, url_prefix='/auth')

@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        if current_user.is_authenticated:
            return redirect(url_for('main.dashboard'))
        return render_template('login.html')
    else:
        # POST method
        # credential syntax are validated on client side

        # find user by email address
        user = User.query.filter_by(email=request.form["email"]).first()

        if not user:
            flash('Invalid login credentials')
            return redirect(url_for('auth.login'))

        # check if passwords match
        if user.verify_password(request.form['password']):
            login_user(user)
            return redirect(url_for('main.dashboard'))
        else:
            flash('Invalid login credentials')
            return redirect(url_for('auth.login')) 


@auth_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        if current_user.is_authenticated:
            return redirect(url_for('main.dashboard'))
        return render_template('register.html')
    else:
        # POST method
        # credential syntax are validated on client side

        # check if user with that email already exists
        user = User.query.filter_by(email=request.form['email']).first()

        # if user already exists, flash message
        if user:
            flash('There already exists an account with the email address.')
            return redirect(url_for('auth.register'))

        # create user and redirect
        user = User(request.form['username'], request.form['email'], request.form['password'])
        try:
            db.session.add(user)
            db.session.commit()
        except Exception:
            flash('There was an error creating the account. Try again.')
            return redirect(url_for('auth.register'))

        flash('Successfully created account. Please Login.')

        return redirect(url_for('auth.login'))

@auth_blueprint.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
