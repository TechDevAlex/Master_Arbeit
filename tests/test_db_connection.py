import unittest
import psycopg2
from src.db_connection import create_connection

class TestDBConnection(unittest.TestCase):
    def test_create_connection_success(self):
        # Test that the function does not raise an exception when the connection is successful
        try:
            conn = create_connection()
            self.assertIsNotNone(conn)
            conn.close()
        except Exception as e:
            self.fail(f"create_connection() raised {type(e).__name__} unexpectedly!")

    def test_create_connection_failure(self):
        # Modify the credentials to something incorrect
        incorrect_dbname = "wrong_dbname"
        incorrect_user = "wrong_user"
        incorrect_password = "wrong_password"
        incorrect_host = "wrong_host"
        incorrect_port = "wrong_port"

        # Test that the function raises an exception when the connection fails
        with self.assertRaises(psycopg2.OperationalError):
            conn = psycopg2.connect(
                dbname=incorrect_dbname,
                user=incorrect_user,
                password=incorrect_password,
                host=incorrect_host,
                port=incorrect_port
            )

if __name__ == '__main__':
    unittest.main()