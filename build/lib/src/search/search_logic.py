#src/search/search_logic.py
import pandas as pd

class SearchLogic:
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def search(self, keyword=None):
        if keyword:
            keyword = keyword.lower()
            mask = self.dataframe.apply(
                lambda row: any(str(cell).lower().find(keyword) != -1 for cell in row),
                axis=1
            )
            return self.dataframe[mask]
        else:
            return self.dataframe
