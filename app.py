from flask import Flask
from dotenv import load_dotenv

from utils import get_temperature
# Enter your OpenWeatherMap API key here

load_dotenv()


app = Flask(__name__)


@app.route('/weather', methods=['GET'])
def getWeatherAPI():
    return get_temperature('roorkee')


if __name__ == '__main__':
    app.run(debug=False)
