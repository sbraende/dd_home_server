from flask import Flask, jsonify
import Adafruit_DHT
import config_db
import server_functions as sf

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hey from Raspberry"


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


@app.route("/database")
def get_database():
    connection, cursor = sf.get_db(config_db.humidtemp_db.name)
    cursor.execute(f"SELECT * FROM {config_db.humidtemp_db.name}_table")
    data = cursor.fetchall()
    columns_names = config_db.humidtemp_db.columns
    response_data = {
        "columns": columns_names,
        "data": data 
    }
    return jsonify(response_data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
