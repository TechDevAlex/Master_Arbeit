# src/data_insertion.py
import pandas as pd
from src.database.data_conversion import convert_csv_to_dataframe
from src.database.db_connection import create_connection

def create_table_from_csv(csv_file_path, table_name):
    # Create a connection to the database
    engine = create_connection()

    # Read the CSV file into a pandas DataFrame
    df = convert_csv_to_dataframe(csv_file_path)

    # Write the data from the DataFrame to the table
    df.to_sql(table_name, engine, if_exists='replace', index=False)
