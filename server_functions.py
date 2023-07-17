import sqlite3
import Adafruit_DHT
from datetime import datetime
import time


def create_db(db_name, columns):
    connection, cursor = get_db(db_name)
    columns_formatted = ", ".join(columns)
    cursor.execute(f"CREATE TABLE {db_name}_table ({columns_formatted})")


def get_db(db_name):
    connection = sqlite3.connect(f"{db_name}.db")
    cursor = connection.cursor()
    return connection, cursor


def get_date_time():
    return str(datetime.now())


def write_time_data(db_name, user):
    connection, cursor = get_db(db_name)
    data = (get_date_time(), user)
    cursor.execute(f'INSERT INTO {db_name}_table (datetime, user) VALUES (?, ?)',
                   data)
    connection.commit()


def write_humidtemp_data(db_name, room):
    connection, cursor = get_db(db_name)
    sensor = Adafruit_DHT.DHT11
    pin = 17
    
    countdown_duration = 60 # Dont put lower than 30
    
    while True:
        end_time = time.time() + countdown_duration
        while time.time() < end_time:
            humidity, temperature = Adafruit_DHT.read(sensor, pin)
            time.sleep(2)
            if humidity is not None and temperature is not None:
                last_temperature, last_humidity = temperature, humidity
        data = (get_date_time(), room, last_temperature, last_humidity)
        cursor.execute(f'INSERT INTO {db_name}_table (datetime, room, temperature, humidity) VALUES (?, ?, ?, ?)', data)
        print(f"Storing: {data} ,into {db_name}")
        connection.commit() 


def print_db(db_name):
    connection, cursor = get_db(db_name)
    result = cursor.execute(f"SELECT * FROM {db_name}_table")
    print(result.fetchall())
