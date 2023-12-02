# src/csv_to_postgres.py
import os
import pandas as pd
from src.data_insertion import create_table_from_csv
from src.db_connection import create_connection
from sqlalchemy import text

def test_csv_to_postgres(csv_filepath, table_name):
    #create the table
    create_table_from_csv(csv_filepath,table_name)
    #check if the table exists
    engine = create_connection()
    with engine.connect() as connection:
        #use sqlalchey text to insert text as direct sql statment
        result = connection.execute (text(f'SELECT table_name FROM information_schema.tables WHERE table_name = \'{table_name}\''))
        table_exists = result.fetchone() is not None
    if table_exists:
        print(f'Table {table_name} has been successfully created in the database.')


if __name__ == '__main__':
    #will be input fields in gui, hardcoded for testing
    #raw string to avoid python interpreting backlashes
    csv_filepath = r'C:\Users\alext\OneDrive\Desktop\Master_Arbeit\Github_Project\Master_Arbeit\init-scripts\sample_data_5_Add_Mat_Extrusion_FFF.csv'
    table_name = 'testtable'
    test_csv_to_postgres(csv_filepath,table_name)
