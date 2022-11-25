import json
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from flask_app.models import db, DailyTask

# create blueprint for the main route of the site
main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/')
def index():
    return render_template('index.html')

@login_required
@main_blueprint.route('/dashboard')
def dashboard():
    daily_tasks = DailyTask.query.filter_by(user_id=current_user.id)
        
    return render_template('dashboard.html', daily_tasks=daily_tasks)

@login_required
@main_blueprint.route('/createDailyTask', methods=['POST'])
def createDailyTask():
    task = DailyTask(task=request.form['task'], user_id=current_user.id)
    db.session.add(task)
    db.session.commit()
    return redirect(url_for('main.dashboard'))

@login_required
@main_blueprint.route('/updateDailyTask', methods=['PATCH'])
def updateDailyTask():
    print('raw: ', request.data)
    data = request.data.decode('utf8').replace("'", '"')
    data = json.loads(data)

    print(data)

    task = DailyTask.query.filter_by(task=data['task'], user_id=current_user.id).first()
    if data['day'] == 'daily_monday':
        task.monday = 1 if task.monday == 0 else 0

    elif data['day'] == 'daily_tuesday':
        task.tuesday = 1 if task.tuesday == 0 else 0

    elif data['day'] == 'daily_wednesday':
        task.wednesday = 1 if task.wednesday == 0 else 0

    elif data['day'] == 'daily_thursday':
        task.thursday = 1 if task.thursday == 0 else 0

    elif data['day'] == 'daily_friday':
        task.friday = 1 if task.friday == 0 else 0

    elif data['day'] == 'daily_saturday':
        task.saturday = 1 if task.saturday == 0 else 0

    elif data['day'] == 'daily_sunday':
        task.sunday = 1 if task.sunday == 0 else 0

    db.session.commit()
    return {"result": "GOOD"}, 200
