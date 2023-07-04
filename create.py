import sqlite3
import config


def create_db(name: str, columns: list):
    con = sqlite3.connect(name)
    cur = con.cursor()

    columns_formatted = ", ".join(columns)
    cur.execute(f"CREATE TABLE {name}_table ({columns_formatted})")


create_db(config.time_db.name, config.time_db.columns)