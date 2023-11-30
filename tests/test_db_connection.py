# tests/test_db_connection.py
import unittest
from sqlalchemy import create_engine, exc
from src.db_connection import create_connection

class TestDBConnection(unittest.TestCase):
    def test_create_connection_success(self):
        # Test that the function does not raise an exception when the connection is successful
        try:
            engine = create_connection()
            self.assertIsNotNone(engine)
            # Dispose the engine after the test
            engine.dispose()
        except Exception as e:
            self.fail(f"create_connection() raised {type(e).__name__} unexpectedly!")

    def test_create_connection_failure(self):
        # Modify the credentials to something incorrect
        incorrect_dbname = "wrong_dbname"
        incorrect_user = "wrong_user"
        incorrect_password = "wrong_password"
        incorrect_host = "wrong_host"
        incorrect_port = "-99"

        # Test that the function raises an exception when the connection fails
        with self.assertRaises(exc.OperationalError):
            engine = create_engine(f'postgresql://{incorrect_user}:{incorrect_password}@{incorrect_host}:{incorrect_port}/{incorrect_dbname}')
            conn = engine.connect()

if __name__ == '__main__':
    unittest.main()
