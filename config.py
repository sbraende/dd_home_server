class Database:
    def __init__(self, name: str, columns: list):
        self.name = name
        self.columns = columns


time_db = Database("time_db", ["datetime", "room"])