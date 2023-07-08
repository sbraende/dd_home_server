import main
import config_db
import time

main.create_db(config_db.time_db.name, config_db.time_db.columns)

while True:
    main.write_time_data(config_db.time_db.name, "Sebby")
    main.print_db(config_db.time_db.name)
    time.sleep(1)
