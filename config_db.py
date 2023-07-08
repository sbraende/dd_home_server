import os
import sqlite3


class Database:
    # def get_database_path(self):
    #     current_dir = os.path.dirname(os.path.abspath(__file__))
    #     database_path = os.path.join(current_dir, self.filename)
    #     return database_path
    #
    # def create_table(self):
    #     columns_formatted = ", ".join(self.columns)
    #     self.cursor.execute(f"CREATE TABLE {self.name}_table ({columns_formatted})")

    # def table_exits(self):
    #     table = self.cursor.execute(f"SELECT name FROM sqlite_master WHERE type=table AND name='{self.columns[0]}'")
    #     print(table)

    def __init__(self, db_name: str, columns: list):
        self.name = db_name
        self.columns = columns
        # self.filename = self.name + ".db"
        # self.connection = sqlite3.connect(self.filename)
        # self.cursor = self.connection.cursor()

        # # Check if table exits, if not create the table
        # if os.path.exists(self.get_database_path()):
        #     print("It's there")
        # else:
        #     print("No db, create it")


        # self.cursor = self.connection.cursor()

        # columns_formatted = ", ".join(self.columns)
        # self.cursor.execute(f"CREATE TABLE {self.name}_table ({columns_formatted})")

        # self.connection = create.create_db_file(self.name)
        # self.cursor = self.connection.cursor()

        #create.create_db_table(self.cursor, self.name, self.columns)

        # If table exits:
        # # Check for table in data base
        # self.create_table()


# Config time_db:
time_db = Database("time", ["datetime", "user"])