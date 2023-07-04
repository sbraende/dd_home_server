import sqlite3
import config


def connect_db(db_name):
    con = sqlite3.connect(db_name)
    cur = con.cursor()
    return con, cur

def print_db_data(connection, cursor):



print(connect_db(config.time_db.name))