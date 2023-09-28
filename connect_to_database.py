import psycopg2
import json

def load_db_config():
    try:
        with open("db_config.json", "r") as config_file:
            db_config = json.load(config_file)
        return db_config
    except (FileNotFoundError, json.JSONDecodeError):
        return None

def connect_to_database():
    db_config = load_db_config()
    if db_config:
        try:
            connection = psycopg2.connect(**db_config)
            print("Connected to PostgreSQL")
            return connection
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL:", error)
            return None
    else:
        print("Database configuration not found. Please run db_config_setup.py to set it up.")
        return None

# The rest of your database functions

if __name__ == "__main__":
    connection = connect_to_database()
    if connection:
        # Perform any database operations or testing here
        cursor = connection.cursor()
        cursor.execute("SELECT version();")
        record = cursor.fetchone()
        print("You are connected to -", record[0])

    if connection:
        connection.close()
        print("PostgreSQL connection is closed")
