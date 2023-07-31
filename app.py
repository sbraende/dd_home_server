import Adafruit_DHT
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hey, Seeb seb seb from Raspberry"

@app.route("/data")
def get_data():
    data = {
        "tempreature": 25.5,
        "humidity": 60.2,
        "status": "ok"
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


# def get_data():
#     sensor = Adafruit_DHT.DHT11
#     pin = 17
#     humidity, temperature = Adafruit_DHT.read(sensor, pin)
    
#     room = open("room_id.txt", "r").read()

#     data = {
#         "room": room,
#         "temprature": temperature,
#         "humidity": humidity,
#         "status": "ok", 
#     }
#     return jsonify(data)