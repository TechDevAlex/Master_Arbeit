import unittest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

class TestDatabaseConnection(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://testuser:12345@postgres-db/UserCredentials'
        self.db = SQLAlchemy(self.app)

    def test_database_connection(self):
        with self.app.app_context():
            try:
                with self.db.engine.connect() as connection:
                    connection.execute('SELECT 1')
                connection_status = True
            except Exception as e:
                connection_status = False

            self.assertTrue(connection_status, "Database connection failed")

if __name__ == '__main__':
    unittest.main()
