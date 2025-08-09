from flask import Flask, render_template, request
import requests
from datetime import datetime

app = Flask(__name__)
WINDY_API_KEY = 'qBLO2tpiV0LYjGL7Kefenj4SBdQx8yR2'

def get_webcam(country_code):
    try:
        url = f"https://api.windy.com/api/webcams/v2/list/country={country_code}?show=webcams:player"
        headers = {"x-windy-key": WINDY_API_KEY}
        res = requests.get(url, headers=headers).json()
        webcams = res['result']['webcams']
        if webcams:
            return webcams[0]['player']['live']['embed']
        return None
    except:
        return None

def get_fun_fact(country_name):
    try:
        summary_url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{country_name}"
        res = requests.get(summary_url).json()
        return res.get('extract', 'No fun fact available.')
    except:
        return 'Fun fact unavailable.'


def get_weather_data(country_name):
    try:
        country_url = f"https://restcountries.com/v3.1/name/{country_name}"
        country_res = requests.get(country_url).json()[0]
        capital = country_res['capital'][0]
        lat = country_res['capitalInfo']['latlng'][0]
        lon = country_res['capitalInfo']['latlng'][1]
        country_code = country_res['cca2']

        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        weather_res = requests.get(weather_url).json()
        temperature = weather_res['current_weather']['temperature']

        now = datetime.utcnow()
        time_string = now.strftime('%Y-%m-%d %H:%M:%S')

        fun_fact = get_fun_fact(country_name)
        webcam = get_webcam(country_code)

        return {
            'country': country_name.title(),
            'capital': capital,
            'lat': lat,
            'lon': lon,
            'temperature': temperature,
            'description': 'N/A',
            'datetime': time_string,
            'fun_fact': fun_fact,
            'webcam': webcam
        }

    except Exception as e:
        print(f"Error: {e}")
        return None



@app.route('/', methods=['GET', 'POST'])
def index():
    data = None
    if request.method == 'POST':
        country = request.form.get('country')
        data = get_weather_data(country)
    return render_template('index.html', data=data)  # only index.html now

if __name__ == '__main__':
    app.run(debug=True)
