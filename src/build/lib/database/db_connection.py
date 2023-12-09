# src/db_connection.py
from sqlalchemy import create_engine
from src.database.db_config import get_db_credentials

def create_connection():
    dbname, user, password, host, port = get_db_credentials()
    try:
        # Create a SQLAlchemy engine
        engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{dbname}')
        
        # try to establish a connection
        with engine.connect():
            pass
        return engine
    except Exception as e:
        print("Unable to connect to database.", str(e))
        print ("Please check the credentials in 'db_credentials.txt' and try again.")
        return None