import sqlite3


class Database:
    def __init__(self, db_name: str, columns: list):
        self.name = db_name
        self.columns = columns
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def create_db(self):



time_db = Database("time_db", ["datetime", "room"])
