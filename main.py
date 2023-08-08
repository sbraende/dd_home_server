import server_functions as sf
import config_db


if __name__ == "__main__":
    sf.write_humidtemp_data(config_db.humidtemp_db.name,
                            config_db.humidtemp_db.columns,
                            config_db.userdata["room"]
                            )
