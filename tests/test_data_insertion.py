# src/tests/test_data_insertion.py
import unittest
import os
import pandas as pd
from sqlalchemy import text
from src.data_insertion import create_table_from_csv
from src.db_connection import create_connection

class TestCreateTableFromCSV(unittest.TestCase):
    def setUp(self):
        # Create a temporary CSV file for testing
        self.csv_file_path = 'test_data.csv'
        self.test_data = {
            'ID': [1, 2, 3],
            'Name': ['Alice', 'Bob', 'Charlie'],
            'Age': [25, 30, 35]
        }
        pd.DataFrame(self.test_data).to_csv(self.csv_file_path, index=False)

    def test_create_table_from_csv(self):
        # Test the create_table_from_csv function

        create_table_from_csv(self.csv_file_path, "unittest_table")

        engine = create_connection()
        with engine.connect() as connection:
            connection.execute(text("DROP TABLE IF EXISTS unittesttable"))
      
    def tearDown(self):
        # Remove the temporary CSV file after the test
        os.remove(self.csv_file_path)


if __name__ == '__main__':
    unittest.main()
