import unittest
import psycopg2

# Replace these values with your database credentials
DB_NAME = "UserCredentials"
DB_USER = "testuser"
DB_PASSWORD = "12345"
DB_HOST = "localhost"  # When connecting from outside Docker, use localhost

class TestDatabaseConnection(unittest.TestCase):
    def test_database_connection(self):
        try:
            connection = psycopg2.connect(
                dbname=DB_NAME,
                user=DB_USER,
                password=DB_PASSWORD,
                host=DB_HOST
            )

            cursor = connection.cursor()

            # Execute a sample query
            cursor.execute("SELECT version();")
            db_version = cursor.fetchone()
            self.assertIsNotNone(db_version)  # Assert that a version is fetched

            # Close the cursor and connection
            cursor.close()
            connection.close()

        except psycopg2.Error as e:
            self.fail(f"Error connecting to the database: {e}")

if __name__ == '__main__':
    unittest.main()
