# tests/test_data_retrieval.py
import unittest
from src.data_retrieval import retrieve_data_from_database
from src.db_connection import create_connection
from sqlalchemy.orm import sessionmaker

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

if __name__ == '__main__':
    unittest.main()