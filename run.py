import server_functions as sf
import config_db
import time

# sf.create_db(config_db.time_db.name, config_db.time_db.columns)
# sf.create_db(config_db.humidtemp_db.name, config_db.humidtemp_db.columns) 

sf.write_humidtemp_data(config_db.humidtemp_db.name, "bedroom")

# while True:
#    sf.write_ht_data(config_db.ht_db.name, "bedroom")
#    sf.print_db(config_db.ht_db.name)
#    time.sleep(10)

# while True:
#    sf.write_time_data(config_db.time_db.name, "Sebby")
#    sf.print_db(config_db.time_db.name)
#    time.sleep(1)
