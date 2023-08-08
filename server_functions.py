import os
import sqlite3
import Adafruit_DHT
from datetime import datetime
import time
import requests
import config_db


def db_exits(db_name):
    dir_path = os.path.dirname(os.path.abspath(__file__))
    filepath = dir_path + os.sep + db_name + ".db"
    if os.path.exists(filepath):
        return True
    else:
        return False


def make_db(db_name, columns):
    print(f"File not on disk. Creating {db_name + '.db'}")
    connection, cursor = get_db(db_name)  # Creates db file
    columns_formatted = ", ".join(columns)  # Formatting for table
    cursor.execute(f"CREATE TABLE {db_name}_table ({columns_formatted})")


def get_db(db_name):
    connection = sqlite3.connect(f"{db_name}.db")
    cursor = connection.cursor()
    return connection, cursor


def get_date_time():
    return str(datetime.now())


def get_weather(city):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    api_key = config_db.userdata["openweather_apikey"]
    url = base_url + "appid=" + api_key + "&q=" + city
    response = requests.get(url).json()
    temprature = round(kelvin_to_celsius(response["main"]["temp"]), 2)
    humidity = response["main"]["humidity"]
    weather_main = response["weather"][0]["main"]
    return temprature, humidity, weather_main


def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius


def write_time_data(db_name, user):
    connection, cursor = get_db(db_name)
    data = (get_date_time(), user)
    cursor.execute(f"INSERT INTO {db_name}_table "
                   f"(datetime, user) VALUES (?, ?)", data)
    connection.commit()


def write_humidtemp_data(db_name, columns, room):

    if not db_exits(db_name):
        make_db(db_name, columns)

    connection, cursor = get_db(db_name)
    sensor = Adafruit_DHT.DHT11
    pin = 17

    countdown_duration = 120  # Dont put lower than 30 seconds

    while True:
        end_time = time.time() + countdown_duration
        last_temperature, last_humidity = 0.0, 0.0
        while time.time() < end_time:
            humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
            if humidity is not None and temperature is not None:
                last_temperature, last_humidity = temperature, humidity
        ext_temperature, ext_humidity, ext_weather = get_weather(
                                                    config_db.userdata["city"])
        data = (get_date_time(), room, last_temperature, last_humidity,
                ext_temperature, ext_humidity, ext_weather)
        cursor.execute(
            f"INSERT INTO {db_name}_table "
            f"(datetime, room, temperature, humidity, "
            f"ext_temperature, ext_humidity, ext_weather) VALUES (?, ?, ?, ?, "
            f"?, ?, ?)",
            data,
        )
        print(f"Storing: {data} ,into {db_name}")
        connection.commit()


def print_db(db_name):
    connection, cursor = get_db(db_name)
    result = cursor.execute(f"SELECT * FROM {db_name}_table")
    print(result.fetchall())
