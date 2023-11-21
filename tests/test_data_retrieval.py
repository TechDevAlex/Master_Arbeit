# tests/test_data_retrieval.py
import unittest
from src.data_retrieval import retrieve_data_from_database
from src.db_connection import create_connection

class TestDataRetrieval(unittest.TestCase):
    def setUp(self):
        # Set up a database connection for testing
        self.connection = create_connection("users")  #will break if changed database name

    def tearDown(self):
        # Close the database connection after the test
        self.connection.close()

    def test_retrieve_data(self):
        data = retrieve_data_from_database(self.connection)
        self.assertIsNotNone(data)
        # Add more assertions as needed
