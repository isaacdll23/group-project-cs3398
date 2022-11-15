from flask import Blueprint, render_template

# create blueprint for the main route of the site
main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/')
def index():
    render_template()