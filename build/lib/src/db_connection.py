# src/db_connection.py
import psycopg2
from src.db_config import get_db_credentials

def create_connection():
    dbname, user, password, host, port = get_db_credentials()
    try:
          return psycopg2.connect(
            user=user,
            password=password,
            host=host,
            port=port,
            database=dbname
        )
    except psycopg2.OperationalError as e:
         print("Unable to connect to database.", str(e))
         print ("Please check the credentials in 'db_credentials.txt' and try again.")
         return None