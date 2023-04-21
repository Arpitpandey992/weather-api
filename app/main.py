from flask import Flask, request
from flask_cors import CORS
from dotenv import load_dotenv

from app.utils import get_temperature


def createApp(testing: bool = True):
    app = Flask(__name__)
    CORS(app)
    load_dotenv()
    DEFAULT_CITY = 'Roorkee'

    # Routes
    @app.route('/weather', methods=['GET'])
    def getWeatherAPI():
        city = request.args.get('city', DEFAULT_CITY)
        print(f"Get request, city = {city}")
        return {"city": city, "weather": get_temperature(city)}

    return app
