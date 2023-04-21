from flask import Flask, request
from dotenv import load_dotenv

from utils import get_temperature


def create_app():
    app = Flask(__name__)
    load_dotenv()
    DEFAULT_CITY = 'Roorkee'

    # Routes
    @app.route('/weather', methods=['GET'])
    def getWeatherAPI():
        city = request.args.get('city', DEFAULT_CITY)
        return {"city": city, "weather": get_temperature(city)}

    return app
