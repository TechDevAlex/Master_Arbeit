# src/data_conversion.py
import pandas as pd

def convert_to_dataframe(data):
    # Assuming data is a list of tuples
    columns = ["column1", "column2", "column3"]  # Replace with your actual column names
    df = pd.DataFrame(data, columns=columns)
    return df
