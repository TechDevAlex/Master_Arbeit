# src/tests/test_data_conversion.py
import unittest
import pandas as pd
import os
from src.database.data_conversion import convert_table_to_dataframe, convert_csv_to_dataframe

class TestDataConversion(unittest.TestCase):
    def test_convert_to_dataframe(self):
        # Test the convert_to_dataframe function

        # Mock data for testing
        mock_table = [(1, 'user1', 'password1'), (2, 'user2', 'password2'), (3, 'user3', 'password3')]
        columns = ['ID', 'Username', 'Password']

        # Call the function with the mock data
        result_df = convert_table_to_dataframe(mock_table)

        # Check if the DataFrame exists
        self.assertIsNotNone(result_df) 

    def test_convert_csv_to_dataframe(self):
        # Test the convert_csv_to_dataframe function

        # Create a temporary CSV file for testing
        csv_file_path = 'test_data.csv'
        test_data = {
            'ID': [1, 2, 3],
            'Username': ['user1', 'user2', 'user3'],
            'Password': ['password1', 'password2', 'password3']
        }
        pd.DataFrame(test_data).to_csv(csv_file_path, index=False)

        # Call the function with the mock data
        result_df = convert_csv_to_dataframe(csv_file_path)

        # Check if the DataFrame exists
        self.assertIsNotNone(result_df)

        # Remove the temporary CSV file
        os.remove(csv_file_path)


if __name__ == '__main__':
    unittest.main()
