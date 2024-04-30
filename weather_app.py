from flask import Flask, render_template, request
import requests
import json


with open('data/cities.json', 'r') as f:
    cities = json.load(f)
app = Flask(__name__)


def weather(city):
    res = cities['city'][0]
    for city_data in cities['city']:
        if city_data['name'] == city:
            res = city_data
            break
    return res


@app.route('/')
def index():
    url = 'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}'
    city = request.args.get('city') or 'London'
    response = requests.get(url.format(city=city, API_key='ffc6baf1e14ba9cccc804b569abeaed0'))
    weather_data = response.json()
    weather_data = weather("Москва")
    return render_template('index.html', weather_data=weather_data)


if __name__ == '__main__':
    app.run(debug=True)
