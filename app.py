import json
from pathlib import Path
from flask import Flask, jsonify
import Adafruit_DHT


SENSOR_TYPES = {
    "DHT11": Adafruit_DHT.DHT11,
    "DHT12": Adafruit_DHT.DHT22,
    "AM2302": Adafruit_DHT.AM2302
}


class Configuration():
    def __init__(self, config_path):
        self.config = self.get_config_file(config_path)

    def get_config_file(self, config_path):
        path = Path(config_path)
        if not path.exists():
            raise FileNotFoundError(f"Cannot find config file: {config_path}")
        try: 
            with open(config_path) as config_file:
                config = json.load(config_file)
                return config
        except json.JSONDecodeError as error:
            raise ValueError(f"Cannot decode JSON in config file: {error}")

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


class Sensor():
    def __init__(self, sensor_type, sensor_pin):
        self.sensor_type = sensor_type
        self.sensor_pin = sensor_pin

    def read_data(self):
        if self.sensor_type in SENSOR_TYPES:
            read_retries = 999
            humidity, temperature = Adafruit_DHT.read_retry(SENSOR_TYPES
                                                            [self.sensor_type],
                                                            self.sensor_pin, retries=read_retries)
            if humidity is None and temperature is None:
                raise ValueError(f"Could not get humidity and temprature after 
                                 {read_retries} retries")
            return humidity, temperature
        else:
            raise ValueError(f"Unsupported sensor type: {self.sensor_type}")


class Server:
    def __init__(self) -> None:
        self.config = Configuration("config.json")

    def get_data(self):
        sensor = Sensor(self.config.get_sensor_type(),
                        self.config.get_sensor_pin())
        humidity, temperature = sensor.read_data()
        room = self.config.get_room()
        data = {
            "room": room,
            "temperature": temperature,
            "humidity": humidity,
        }
        return jsonify(data)


app = Flask(__name__)


@app.route("/data")
def data_rute():
    server = Server()
    return server.get_data()


def main():
    app.run(host="0.0.0.0", port=5000)


if __name__ == "__main__":
    main()
