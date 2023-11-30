# src/data_retrieval.py
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
from src.db_connection import create_connection

def retrieve_data_from_database():
    # Create a session
    Session = sessionmaker(bind=create_connection())
    session = Session()

    # Execute the query
    result = session.execute(text("SELECT * FROM users")) 

    # Fetch all the data
    data = result.fetchall()

    # Close the session
    session.close()

    return data