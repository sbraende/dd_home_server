import server_functions as sf
import config_db


def get_room_id():
    return open("room_id.txt", "r").read()


if __name__ == "__main__":
    sf.write_humidtemp_data(config_db.humidtemp_db.name,
                            config_db.humidtemp_db.columns,
                            get_room_id()
                            )
