import Adafruit_DHT
import server_functions as sf
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hey, Seeb seb seb from Raspberry"


@app.route("/data")
def get_data():
    sensor = Adafruit_DHT.DHT11
    pin = 17
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
   
    room = open("room_id.txt", "r").read()

    data = {
        "time": sf.get_date_time(),
        "room": room,
        "temprature": temperature,
        "humidity": humidity,
        "status": "ok",
    }
    return jsonify(data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
