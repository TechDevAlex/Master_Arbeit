# src/tests/test_data_insertion.py
import unittest
import os
import pandas as pd
from sqlalchemy import text
from database.data_manipulation import *
from database.db_connection import create_connection


class Test_01_CreateTableFromCSV(unittest.TestCase):
    def setUp(self):
        # Create a temporary CSV file for testing
        self.csv_file_path = 'test_data.csv'
        self.test_data = {
            'material_name': ['test_material'],
            'material_class': ['test_class'],
            'trade_name': ['test_tradename'],
            'test_property': ['3']
        }
        pd.DataFrame(self.test_data).to_csv(self.csv_file_path, index=False)

    def test_create_table_from_csv(self):
        # Test the create_table_from_csv function
        create_table_from_csv(self.csv_file_path, "test_table")
      

    def tearDown(self):
        # Remove the temporary CSV file after the test
        os.remove(self.csv_file_path)


class Test_02_AddAndDeleteSingleEntryToTable(unittest.TestCase):
    def setUp(self):
        # Create a connection to the PostgreSQL database
        self.engine = create_connection()

    def test_add_and_delete_single_entry_to_table(self):
        # Call the function with some test data
        add_single_entry_to_table("test_table", 'test_material', 'test_class', 'test_tradename', 'test_property', '3', 'Integer')

        # Call the function again with the same test data
        matching_rows, old_value, overwritten_tag = add_single_entry_to_table("test_table", 'test_material', 'test_class', 'test_tradename', 'test_property', '3', 'Integer')
         # Check if the old_value and overwritten_tag are correct
        self.assertEqual(old_value, '3')
        self.assertFalse(overwritten_tag)



   # Check if there is any row in the DataFrame that contains all the expected data
        self.assertTrue(any((matching_rows['material_name'] == 'test_material') & 
                            (matching_rows['material_class'] == 'test_class') & 
                            (matching_rows['trade_name'] == 'test_tradename') & 
                            (matching_rows['test_property'] == '3')))


        # Delete the entry from the table
        delete_single_entry_from_table("test_table", 'test_material', 'test_class', 'test_tradename', 'test_property', '3')

        # Check if the entry was deleted
       # Read the table into a DataFrame
        df = pd.read_sql_table("test_table", self.engine)

        # Check if there is any row in the DataFrame that contains all the expected data
        self.assertFalse(any((df['material_name'] == 'test_material') & 
                        (df['material_class'] == 'test_class') & 
                        (df['trade_name'] == 'test_tradename') & 
                        (df['test_property'] == '3')))


class Test_03_DeleteRowsFromTable(unittest.TestCase):
    def setUp(self):
        # Create a connection to the PostgreSQL database
        self.engine = create_connection()

    def test_delete_rows_from_table(self):
        # Call the function with some test data
        add_single_entry_to_table("test_table", 'test_material', 'test_class', 'test_tradename', 'test_property', '3', 'Integer')

        # Delete the entry from the table
        delete_rows_from_table("test_table", 'test_material', 'test_class', 'test_tradename')

        # Check if the entry was deleted
        # Read the table into a DataFrame
        df = pd.read_sql_table("test_table", self.engine)

        # Check if there is any row in the DataFrame that contains all the expected data
        self.assertFalse(any((df['material_name'] == 'test_material') & 
                             (df['material_class'] == 'test_class') & 
                             (df['trade_name'] == 'test_tradename') & 
                             (df['test_property'] == '3')))




class TestDeleteTable(unittest.TestCase):
    def setUp(self):
        # Create a connection to the PostgreSQL database
        self.engine = create_connection()

        # Create a test table
        self.table_name = "test_deletion_table"
        df = pd.DataFrame({
            'material_name': ['test_material'],
            'material_class': ['test_class'],
            'trade_name': ['test_tradename'],
            'test_property': ['3']
        })
        df.to_sql(self.table_name, self.engine, if_exists='replace', index=False)

    def test_delete_table(self):
        # Call the function and get the returned DataFrame
        returned_df = delete_table(self.table_name)

        # Check if the returned DataFrame is correct
        self.assertTrue((returned_df['material_name'] == 'test_material').all())
        self.assertTrue((returned_df['material_class'] == 'test_class').all())
        self.assertTrue((returned_df['trade_name'] == 'test_tradename').all())
        self.assertTrue((returned_df['test_property'] == '3').all())

        # Check if the table was deleted
        with self.engine.connect() as connection:
            result = connection.execute(text(f"SELECT to_regclass('{self.table_name}')"))
            self.assertIsNone(result.scalar())



if __name__ == '__main__':
    unittest.main()





