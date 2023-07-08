import server_functions as sf
import config_db
import time

sf.create_db(config_db.time_db.name, config_db.time_db.columns)

while True:
    sf.write_time_data(config_db.time_db.name, "Sebby")
    sf.print_db(config_db.time_db.name)
    time.sleep(1)
