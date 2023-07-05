import create_db

class Database:
    def __init__(self, db_name: str, columns: list):
        self.name = db_name
        self.columns = columns

        self.connection = create.create_db_file(self.name)
        self.cursor = self.connection.cursor()

        create.create_db_table(self.cursor, self.name, self.columns)

# Create database command:
time_db = Database("time_db", ["datetime", "room"])

print(time_db.cursor)