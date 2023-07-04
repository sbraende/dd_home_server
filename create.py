import sqlite3
import config

def create_db(name):
    con = sqlite3.connect(name)
    cur = con.cursor()
    cur.execute(f"CREATE TABLE {name}_table (datetime, user)")


