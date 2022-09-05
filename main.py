import requests
from flask import Flask, render_template,url_for
from requests import request
import json


app = Flask(__name__)


@app.route('/')
def mars_rover_photo():
    req = requests.get('https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/latest_photos?api_key=DEMO_KEY')
    # преобразует строку json в объект.py
    json_data = json.loads(req.text)
    # извлекаем список последних фоток
    photos = json_data['latest_photos']
    return render_template('index.html', photos=photos)


app.run(debug=True)