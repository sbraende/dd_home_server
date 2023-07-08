import os
import sqlite3


class Database:
    def __init__(self, db_name: str, columns: list):
        self.name = db_name
        self.columns = columns
        self.filename = self.name + ".db"


# Config time_db:
time_db = Database("time", ["datetime", "user"])