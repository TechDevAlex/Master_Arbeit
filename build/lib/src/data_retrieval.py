# src/data_retrieval.py
from src.db_connection import create_connection

def retrieve_data_from_database(connection):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM users")  # Replace with your actual table name
        data = cursor.fetchall()

    return data

