from flask import Flask, jsonify
import Adafruit_DHT
import config_db
import server_functions as sf

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hey, Seeb seb seb from Raspberry"


@app.route("/data")
def get_data():
    sensor = Adafruit_DHT.DHT11
    pin = 17
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    ext_temperature, ext_humidity, ext_weather = sf.get_weather(
                                                    config_db.userdata["city"])
    room = config_db.userdata["room"]

    data = {
        "time": sf.get_date_time(),
        "room": room,
        "temprature": temperature,
        "humidity": humidity,
        "ext_temperature": ext_temperature,
        "ext_humidity": ext_humidity,
        "ext_weather": ext_weather,
        "status": "ok",
    }
    return jsonify(data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
