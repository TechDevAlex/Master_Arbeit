# src\create_session.py
from sqlalchemy.orm import sessionmaker
from src.database.db_connection import create_connection

def create_session():
    engine = create_connection()
    Session = sessionmaker(bind=engine)
    return Session()
