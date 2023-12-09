# src/data_retrieval.py
from sqlalchemy import text
from src.database.db_connection import create_connection
from src.database.create_session import create_session

def retrieve_data_from_database(table_name):
    # Create a session
    session = create_session()

    # Execute the query from selected table
    result = session.execute(text(f"SELECT * FROM {table_name}")) 

    # Fetch all the data
    data = result.fetchall()

    # Close the session
    session.close()

    return data

def retrieve_table_names_from_database():
    # Create a session
    session = create_session()

    # Query to retrieve all table names
    query = text("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public' AND table_type = 'BASE TABLE'")
    result = session.execute(query)

    # Fetch all table names and ensure correct case
    tables = [row[0] for row in result.fetchall()]
    
    tables = ['"{}"'.format(table) for table in tables]  

    # Close the session
    session.close()

    return tables