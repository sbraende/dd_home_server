import sqlite3
import os


# Add functionality to check if database exists...
def create_db_file(db_name):
    connect = sqlite3.connect(db_name)
    return connect


def create_db_table(cursor, db_name, columns):
    columns_formatted = ", ".join(columns)
    cursor.execute(f"CREATE TABLE {db_name}_table ({columns_formatted})")


def remove_db(db_name):
    file_path = os.path.join(os.sep, "Users", "sbraende", "Documents",
                 "Projects", "dd_home_server", db_name)
    os.remove(file_path)


# Create time_db
# create_db_table(config.time_db.cursor,
#           config.time_db.name,
#           config.time_db.columns
#           )

#remove_db(config.time_db.name)