# src/data_conversion.py
import pandas as pd

def convert_to_dataframe(data, columns=None):
    # If columns are not provided, infer them from the data
    if columns is None:
        df = pd.DataFrame(data)
    else:
        df = pd.DataFrame(data, columns=columns)
    return df
