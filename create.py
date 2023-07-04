import config
import os

# Add fucntionality to check if database exists. If so,
# add warning. Also, watch out: db is actually created in config
# file!
def create_db_table(cursor, db_name: str, columns: list):
    columns_formatted = ", ".join(columns)
    cursor.execute(f"CREATE TABLE {db_name}_table ({columns_formatted})")


def remove_db(db_name):
    file_path = os.path.join(os.sep, "Users", "sbraende", "Documents",
                 "Projects", "dd_home_rdev", db_name)
    os.remove(file_path)


# Create time_db
create_db_table(config.time_db.cursor,
          config.time_db.name,
          config.time_db.columns
          )

remove_db(config.time_db.name)