# src/db_connection.py
import psycopg2

def create_connection(database_name):
    return psycopg2.connect(
        user="postgres",
        password="12345",
        host="localhost",
        port="5432",
        database=database_name
    )
