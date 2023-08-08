userdata = {
    "city": "Fornebu",
    "room": "livingroom",
    "openweather_apikey": str(open("openweather_apikey.txt", "r").read())
}


class Database:
    def __init__(self, db_name: str, columns: list):
        self.name = db_name
        self.columns = columns
        self.filename = self.name + ".db"


# Config time datebase:
time_db = Database("time", ["datetime", "user"])

# Config humidtemp database:
humidtemp_db = Database("humidtemp",
                        ["datetime", "room", "temperature", "humidity",
                         "ext_temperature", "ext_humidity", "ext_weather"])
