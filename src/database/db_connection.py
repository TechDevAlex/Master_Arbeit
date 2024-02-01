# src/db_connection.py
from sqlalchemy import create_engine
from database.db_config import get_db_credentials

def create_connection(username=None, password=None, license_code=None):
    # For now, license_code is not used

    dbname, default_user, default_password, host, port = get_db_credentials()

    # Use default values if username or password is None or an empty string
    # 'not username' evaluates to True if username is None or ''.
    user = username if username else default_user
    password = password if password else default_password
    
    try:
        # Create a SQLAlchemy engine
        engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{dbname}')
        
        # Try to establish a connection
        with engine.connect():
            pass
        return engine
    except Exception as e:
        print("Unable to connect to database.", str(e))
        print("Please check the credentials in 'db_credentials.txt' and try again.")
        return None
