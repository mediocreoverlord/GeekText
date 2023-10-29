import mysql.connector
import os, json


# DO NOT TOUCH THIS CLASS, if needed talk to Nageline
class DataAccess:
    def connect(self, config):
        try:
            self.connection = mysql.connector.connect(**config)
            if self.connection.is_connected():
                print("Successfully connected to MySQL!")
        except Exception as e:
            print(f"Error in making connection: {e}")

    def execute_query(self, query, params=None):
        try:
            cursor = self.connection.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            return result
        except mysql.connector.Error as e:
            raise Exception(f"Error executing query: {e}")

    def close(self):
        if self.connection.is_connected():
            self.connection.clsoe()
            print("Database connection is closed")


config_file = 'resources/db_config.json'
# Create MySQLConnection instance with the loaded config_data
# Connect to the MySQL database
if os.path.exists(config_file):
    with open(config_file, "r") as json_file:
        config_data = json.load(json_file)
        db_connection = DataAccess()
        db_connection.connect(config_data)
else:
    print(f"Configuration file '{config_file}' not found. \n Please create"
          f"a new db_config.json file and fill it out with the correct"
          f" db connection info.")
    exit(1)  # Exit the application if config file is not found
