# tests/test_data_conversion.py
import unittest
from src.data_conversion import convert_to_dataframe

class TestDataConversion(unittest.TestCase):
    def test_convert_to_dataframe(self):
        data = [(1, 'A', 'X'), (2, 'B', 'Y'), (3, 'C', 'Z')]  # Update with actual test data
        df = convert_to_dataframe(data)
        self.assertIsNotNone(df)
        # more assertions

if __name__ == '__main__':
    unittest.main()