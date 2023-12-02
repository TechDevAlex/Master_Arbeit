#src/search/search_logic.py
import pandas as pd

def search(dataframe, keyword=None):
    if keyword:
        keyword = keyword.lower()
        mask = dataframe.apply(
            lambda row: any(str(cell).lower().find(keyword) != -1 for cell in row),
            axis=1
        )
        return dataframe[mask]
    else:
        return dataframe
