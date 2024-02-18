# src\create_session.py
from sqlalchemy.orm import sessionmaker
from database.db_connection import create_connection

def create_session():
    """
    Create a new SQLAlchemy session.

    A session in SQLAlchemy is a workspace for all the objects loaded into the 
    database session memory. It provides the entry point to communicate with the 
    database.

    This function creates a new SQLAlchemy session using the engine from the
    create_connection function. The session is ready to use for database
    transactions.

    Returns:
        session: A new SQLAlchemy session.
    """
    engine = create_connection()
    Session = sessionmaker(bind=engine)
    return Session()
