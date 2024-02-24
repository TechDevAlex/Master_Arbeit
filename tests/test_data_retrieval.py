# tests/test_data_retrieval.py
import unittest
from database.data_retrieval import retrieve_data_from_database, retrieve_table_names_from_database
from database.db_connection import create_connection

class TestDataRetrieval(unittest.TestCase):
    def setUp(self):
        # Set up a database connection for testing
        self.engine = create_connection()  #will connect according to db_config

    def tearDown(self):
        # Dispose the engine after the test
        self.engine.dispose()

    def test_retrieve_data(self):
        table_name = "testtable"
        data = retrieve_data_from_database(table_name)
        self.assertIsNotNone(data)

    def test_retrieve_data_from_unittesttable(self): #requires an existing table, therefore dependant on test_data_insertion.py
        table_name = "unittest_table"
        data = retrieve_data_from_database(table_name)
        self.assertIsNotNone(data)
        self.assertIsInstance(data, list)

    def test_retrieve_data_from_non_existent_table(self):
            table_name = "non_existent_table"
            with self.assertRaises(Exception):
                data = retrieve_data_from_database(table_name)
            
    def test_retrieve_table_names(self):
        table_names = retrieve_table_names_from_database()
        self.assertIsNotNone(table_names)
        self.assertIsInstance(table_names, list)


if __name__ == '__main__':
    unittest.main()