# src/data_insertion.py
import pandas as pd
from database.data_conversion import convert_csv_to_dataframe
from database.db_connection import create_connection
from database.create_session import create_session
from sqlalchemy import MetaData, Table, Table, Column, String, Integer, Float, Boolean, VARCHAR, TEXT, text, and_, select, update, insert
from sqlalchemy.orm import sessionmaker

def create_table_from_csv(csv_file_path, table_name):
    """
    Create a new table in the database from a CSV file.

    This function reads a CSV file into a pandas DataFrame, and then writes the data from the DataFrame to a new table in the database. If a table with the same name already exists in the database, it will be replaced.

    Parameters:
    csv_file_path (str): The path to the CSV file.
    table_name (str): The name of the table to be created in the database.

    Returns:
    None
    """

    # Create a connection to the database
    engine = create_connection()

    # Read the CSV file into a pandas DataFrame
    df = convert_csv_to_dataframe(csv_file_path)

    # Write the data from the DataFrame to the table
    df.to_sql(table_name, engine, if_exists='replace', index=False)


def type_mapping_StringtoSQL():
    """
    Map SQLAlchemy types to Python types.

    This function takes a SQLAlchemy type and returns the corresponding Python type.

    Parameters:
    datatype (SQLAlchemy type): The SQLAlchemy type.

    Returns:
    Python type: The corresponding Python type.
    """
    
    # Mapping from SQLAlchemy types to Python types
    type_mapping = {
        'String': String,
        'Integer': Integer,
        'Float': Float,
        'Boolean': Boolean,
        'VARCHAR': VARCHAR,
        'TEXT': TEXT
    }
    return type_mapping


def type_mapping_SQLtoPython(datatype=None):
    """
    Map SQLAlchemy types to Python types.

    This function takes a SQLAlchemy type and returns the corresponding Python type.

    Parameters:
    datatype (SQLAlchemy type): The SQLAlchemy type.

    Returns:
    Python type: The corresponding Python type.
    """
    
    # Mapping from SQLAlchemy types to Python types
    type_mapping = {
        String: str,
        Integer: int,
        Float: float,
        Boolean: bool,
        VARCHAR: str,
        TEXT: str
    }
    if datatype is not None:
        return type_mapping[datatype]
    return type_mapping

def add_single_entry_to_table(table_name, material_name, material_class, trade_name, material_property, datatype, value):
    # Create a connection to the database
    engine = create_connection()

    # Check if the data fits the specified format
    if not all(isinstance(arg, str) for arg in [material_name, material_class, trade_name, material_property]):
        raise ValueError("Material name, class, trade name, and property must be strings")

    # Check if the value is of the correct type
    SQL_datatype = type_mapping_StringtoSQL()[datatype]
    if not isinstance(type_mapping_SQLtoPython(SQL_datatype)(value), type_mapping_SQLtoPython(SQL_datatype)):
        raise ValueError(f"Value must be of type {datatype}")

    # Read the table into a DataFrame
    df = pd.read_sql_table(table_name, engine)
  
    # Check if the required columns exist, and create them if they don't
    required_columns = ['material_name', 'material_class', 'trade_name', material_property]
    for column in required_columns:
        if not hasattr(df, column):
            df[column] = pd.Series(dtype='str')

    # Check if a row with the same material_name, material_class, trade_name, and material_property with the given value exists
    matching_rows = df.loc[(df['material_name'] == material_name) & (df['material_class'] == material_class) & (df['trade_name'] == trade_name) & (df[material_property] == value)]

    if matching_rows.empty:
        # Add a new row to the DataFrame
        new_row_index = len(df)
        df.loc[new_row_index, 'material_name'] = material_name
        df.loc[new_row_index, 'material_class'] = material_class
        df.loc[new_row_index, 'trade_name'] = trade_name
        df.loc[new_row_index, material_property] = value

    df.to_sql(table_name, engine, if_exists='replace', index=False)
