#tests/test_db_config.py

import unittest
from database.db_config import get_db_credentials

class TestDBConfig(unittest.TestCase):
    def test_get_db_credentials(self):
        # Call the function
        dbname, user, password, host, port = get_db_credentials()

        # Check that the function returns the correct number of values
        self.assertEqual(len(get_db_credentials()), 5)

        # Check that the returned values are strings
        self.assertIsInstance(dbname, str)
        self.assertIsInstance(user, str)
        self.assertIsInstance(password, str)
        self.assertIsInstance(host, str)
        self.assertIsInstance(port, str)

if __name__ == '__main__':
    unittest.main()