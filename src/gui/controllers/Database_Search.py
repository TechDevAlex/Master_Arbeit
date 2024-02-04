#requirements pip install pandas

import pandas as pd

class DataBase:
    def __init__(self, file_path):
        self.file_path = file_path
        #attributes TODO: (property, property_class)
        #polymers

    def read_excel(self, sheet_name=None):
        """
        Read Excel file and return a dataframe.

        Parameters:
        - sheet_name (str or None): Name of the sheet to read. If None, reads the first sheet.

        Returns:
        - pd.DataFrame: A pandas dataframe containing the data from the Excel file.
        """
        try:
            if sheet_name:
                df = pd.read_excel(self.file_path, sheet_name)
            else:
                df = pd.read_excel(self.file_path)
            return df
        except Exception as e:
            print(f"Error reading Excel file: {e}")
            return None

# Example usage:
excel_handler = ExcelHandler("your_excel_file.xlsx")
dataframe = excel_handler.read_excel("Sheet1")  # Specify sheet name if needed

if dataframe is not None:
    print(dataframe.head())