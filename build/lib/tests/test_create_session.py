# src/tests/test_create_session.py
import unittest
from src.database.create_session import create_session

class TestCreateSession(unittest.TestCase):
    def test_create_session(self):
        # Test the create_session function

        # Call the function
        session = create_session()

        # Check if the returned session is not None
        self.assertIsNotNone(session)

if __name__ == '__main__':
    unittest.main()
