# init/init_database.py
from src.db_connection import create_connection
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import os

def execute_sql_file(cursor, filename):
    with open(filename, 'r') as file:
        cursor.execute(file.read())

def create_database(db_name):
    # Connect to default database (postgres) for creating a new database
    connection = create_connection("postgres")
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    
    with connection.cursor() as cursor:
        # Create a new database
        cursor.execute(f"CREATE DATABASE {db_name}")

    # Connect to the newly created database
    connection.close()
    connection = create_connection(db_name)
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    with connection.cursor() as cursor:
        # Execute SQL commands from sample_data.sql
        sql_file_path = os.path.join(os.path.dirname(__file__), 'sample_data.sql')
        execute_sql_file(cursor, sql_file_path)

if __name__ == "__main__":
    # Change 'your_database_name' to the desired database name
    create_database("users")
