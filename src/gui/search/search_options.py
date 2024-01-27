import os
import pandas as pd


class Dataframe:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_excel_to_dataframe(self):
        """
        Load an Excel file into a DataFrame.

        Returns:
        - df: DataFrame containing the data from the Excel file
        """
        try:
            df = pd.read_excel(self.file_path)
            return df
        except Exception as e:
            print("Error loading Excel file:", e)
            return None


# Example usage:
file_path = os.path.join(os.environ.get('HOME'),'Desktop')
print(file_path)

# Create an instance of ExcelLoader with the file path
df = Dataframe(file_path + "/AM_filaments_FFF_small.xlsx")

# Load the Excel file into a DataFrame
df = df.load_excel_to_dataframe()

# Display the DataFrame
if df is not None:
    print(df.head())




