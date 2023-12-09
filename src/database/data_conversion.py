# src/data_conversion.py
import os
import pandas as pd
from src.database.data_retrieval import retrieve_table_names_from_database, retrieve_data_from_database

def convert_table_to_dataframe(table):
    df = pd.DataFrame(table)
    return df

def convert_csv_to_dataframe(csv_filepath):
    df = pd.read_csv(csv_filepath, delimiter = ',', header = None)
    return df

def convert_database_to_dataframe():
    # Get table names from the database
    table_names = retrieve_table_names_from_database()

    # Create an empty list to store DataFrames for each table
    all_dataframes = []

    for table_name in table_names:
        print(table_name)
        try:
            # Retrieve data from the database
            data = retrieve_data_from_database(table_name)
            


            # Convert data to DataFrame
            df = convert_table_to_dataframe(data)

            # Append the DataFrame to the list
            all_dataframes.append(df)
        except Exception as e:
            print(f"Error converting table {table_name} to DataFrame: {e}")

    # Concatenate all DataFrames into one
    combined_df = pd.concat(all_dataframes, ignore_index=True)

    # Save the combined DataFrame to a CSV file
    save_path = os.path.join("data", "combined_data.csv")
    combined_df.to_csv(save_path, index=False)

    return combined_df
