from flask import Blueprint, render_template
from flask_login import login_required

# create blueprint for the main route of the site
main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/')
def index():
    return render_template('index.html')

@login_required
@main_blueprint.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')
