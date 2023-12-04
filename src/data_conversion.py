# src/data_conversion.py
import pandas as pd
from src.create_session import create_session
from sqlalchemy import text
from src.db_connection import create_connection

def convert_table_to_dataframe(table):
        
    df = pd.DataFrame(table)
    
    return df

def convert_csv_to_dataframe(csv_filepath):

    df = pd.read_csv(csv_filepath, delimiter=';')

    return df
