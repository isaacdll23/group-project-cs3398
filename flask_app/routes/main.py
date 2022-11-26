import json
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from flask_app.models import db, DailyTask, User
import requests
import dotenv

# create blueprint for the main route of the site
main_blueprint = Blueprint('main', __name__)

WEATHER_API_KEY = dotenv.get_key('.env','WEATHER_API_KEY')

@main_blueprint.route('/')
def index():
    return render_template('index.html')

@login_required
@main_blueprint.route('/dashboard')
def dashboard():
    daily_tasks = DailyTask.query.filter_by(user_id=current_user.id)
        
    return render_template('dashboard.html', daily_tasks=daily_tasks)

@login_required
@main_blueprint.route('/weather')
def weather():
    zipcode = User.query.filter_by(id=current_user.id).value(current_user.zipcode)
    response = requests.get(
        "http://api.openweathermap.org/geo/1.0/zip",
        params={
            'zip' : 76065,
            'appid' : WEATHER_API_KEY
        }
    )
    zip_data = response.json()
    loc_lat = zip_data['lat']
    loc_long = zip_data['lon']
    response = requests.get(
        "http://api.openweathermap.org/data/2.5/weather",
        params={
            'lat' : loc_lat,
            'lon' : loc_long,
            'appid' : WEATHER_API_KEY,
            'units' : 'imperial'
        }
    )
    weather_data = response.json()
    weather_description = weather_data['weather'][0]['description']
    current_temp = weather_data['main']['temp']
    feels_like_temp = weather_data['main']['feels_like']
    weather_img_id = weather_data['weather'][0]['icon']
    image_url = f"http://openweathermap.org/img/wn/{weather_img_id}@2x.png"
    return render_template('weather.html', zipcode=zipcode, 
        description=weather_description, current=current_temp, 
        feels_like=feels_like_temp, img_src=image_url)

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
    data = request.data.decode('utf8').replace("'", '"')
    data = json.loads(data)

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


@login_required
@main_blueprint.route('/deleteDailyTask', methods=['POST'])
def deleteDailyTask():
    task = DailyTask.query.filter_by(id=request.form['task_id']).first()
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('main.dashboard'))
