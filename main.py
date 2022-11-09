from jetblue import fetch_flight_status
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    number = 1974
    date = "2022-11-08"
    resp = fetch_flight_status(date, number)
    return resp
