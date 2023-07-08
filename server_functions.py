import sqlite3
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
    cursor.execute('INSERT INTO time_table (datetime, user) VALUES (?, ?)',
                   data)
    connection.commit()


def print_db(db_name):
    connection, cursor = get_db(db_name)
    result = cursor.execute("SELECT * FROM time_table")
    print(result.fetchall())
