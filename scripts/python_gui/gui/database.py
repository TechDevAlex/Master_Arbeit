# gui/database.py
import psycopg2

def connect_to_database():
    # Replace these values with your database credentials
    DB_NAME = "UserCredentials"
    DB_USER = "testuser"
    DB_PASSWORD = "12345"
    DB_HOST = "localhost"  # When connecting from outside Docker, use localhost

    try:
        connection = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST
        )
        return connection  # Return the connection object

    except psycopg2.Error as e:
        print(f"Error connecting to the database: {e}")
        return None
