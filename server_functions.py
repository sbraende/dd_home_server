import sqlite3
import Adafruit_DHT

from datetime import datetime


def create_db(db_name, columns):
    connection, cursor = get_db(db_name)
    # If
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


def write_ht_data(db_name, room):
    connection, cursor = get_db(db_name)
    sensor = Adafruit_DHT.DHT11
    pin = 17
    humidity, temperature = Adafruit_DHT.read(sensor, pin)
    data = (get_date_time(), room, temperature, humidity)
    cursor.execute(f'INSERT INTO {db_name}_table (datetime, room, temperature, humidity) VALUES (?, ?, ?, ?)',
                   data)
    connection.commit()
    

def print_db(db_name):
    connection, cursor = get_db(db_name)
    result = cursor.execute(f"SELECT * FROM {db_name}_table")
    print(result.fetchall())
