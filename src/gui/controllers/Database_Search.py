# src\gui\controllers\Database_Search.py
#requirements pip install pandas
# in my opinion the search functions and also import functions like the read_excel
# belongs in the src\serch folder, the controllers are only meant to handle which functions are called when buttons
# are clicked or smth like that, no actual functionality
# also, it might be beneficial to have testcode for executing functions in a main function, otherwise it gets "accidentally" run when the file is imported somewhere

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


# added main to stop this running when imported
# example usage:
if __name__ == "__main__":
    excel_handler = DataBase("your_excel_file.xlsx")
    dataframe = excel_handler.read_excel("Sheet1")  # Specify sheet name if needed

    if dataframe is not None:
        print(dataframe.head())