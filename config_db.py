import os
import sqlite3


class Database:
    def __init__(self, db_name: str, columns: list):
        self.name = db_name
        self.columns = columns
        self.filename = self.name + ".db"


# Config time datebase:
time_db = Database("time", ["datetime", "user"])

# Config humidtemp database:
humidtemp_db = Database("humidtemp", 
                ["datetime", "room", "temperature", "humidity"])
