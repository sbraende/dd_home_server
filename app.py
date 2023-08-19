import json
from flask import Flask, jsonify
import Adafruit_DHT

app = Flask(__name__)

SENSOR_TYPES = {
    "DHT11": Adafruit_DHT.DHT11,
    "DHT12": Adafruit_DHT.DHT22,
    "AM2302": Adafruit_DHT.AM2302
}


class Configuration():
    def __init__(self, config_path):
        with open(config_path) as config_file:
            self.config = json.load(config_file)

    def get_room(self):
        return self.config["room"]
    
    def get_host(self):
        return self.config["host"]
    
    def get_port(self):
        return self.config["port"]
    
    def get_sensor_type(self):
        return self.config["sensor_type"]
    
    def get_sensor_pin(self):
        return self.config["sensor_pin"]


config = Configuration("config.json")


class Sensor():
    def __init__(self, sensor_type, sensor_pin):
        self.sensor_type = sensor_type
        self.sensor_pin = sensor_pin
    
    def read_data(self):
        if self.sensor_type in SENSOR_TYPES:
            humidity, temperature = Adafruit_DHT.read_retry(SENSOR_TYPES[self.sensor_type], self.sensor_pin)
            return humidity, temperature
        else:
            raise ValueError(f"Unsupported sensor type: {self.sensor_type}")


my_sensor = Sensor(config.get_sensor_type(), config.get_sensor_pin())


@app.route("/data")
def get_data():
    sensor = 
    humidity, temperature = sensor.read_data()
    room = config.get_room
    data = {
        "room": room,
        "temprature": temperature,
        "humidity": humidity,
    }
    return jsonify(data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
