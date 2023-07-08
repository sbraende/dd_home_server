import sqlite3
import os
import config_db
from datetime import datetime


def get_date_time():
    return str(datetime.now())


def create_db(db_name, columns):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    columns_formatted = ", ".join(columns)
    cursor.execute(f"CREATE TABLE {db_name}_table ({columns_formatted})")
    return cursor


def write_time_data(db_name, datetime):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    data = (datetime, get_date_time())
    cursor.execute("INSERT INTO time_table (datetime, user) VALUES (?, ?)", data)
    connection.commit()


def print_db(db_name):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    result = cursor.execute("SELECT * FROM time_table")
    print(result.fetchall())


def get_date_time():
    return str(datetime.now())


# create_db(config_db.time_db.name, config_db.time_db.columns)
#write_time_data(config_db.time_db.name, "Sebby")
#print_db(config_db.time_db.name)


# def remove_db(db_name):
#     file_path = os.path.join(os.sep, "Users", "sbraende", "Documents",
#                  "Projects", "dd_home_server", db_name)
#     os.remove(file_path)
