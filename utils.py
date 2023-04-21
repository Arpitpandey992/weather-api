import os
import requests

api_key_openweather = os.environ.get('API_KEY_OPENWEATHER')
api_key_pirate = os.environ.get('API_KEY_PIRATE')


def get_latiture_longitude(city):
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={api_key_openweather}"
    response = requests.get(url).json()
    return response[0]['lat'], response[0]['lon']


def get_temperature(city: str):
    lat, lon = get_latiture_longitude(city)
    url = f"https://api.pirateweather.net/forecast/{api_key_pirate}/{lat},{lon}?exclude=minutely,daily,currently,alerts&units=si"
    response = requests.get(url)
    response = response.json()
    return [resp for resp in response['hourly']['data'][:24]]
