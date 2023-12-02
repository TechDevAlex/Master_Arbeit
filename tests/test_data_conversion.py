# tests/test_data_conversion.py
import unittest
import tempfile
import os
from src.data_conversion import convert_to_dataframe

class TestDataConversion(unittest.TestCase):
    def test_convert_to_dataframe(self):
        data = [(1, 'A', 'X'), (2, 'B', 'Y'), (3, 'C', 'Z')]

        # Create a temporary CSV file
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv') as temp_file:
            temp_file.write('column1;column2;column3\n')
            for row in data:
                temp_file.write(';'.join(map(str, row)) + '\n')

            # Get the file path
            file_path = temp_file.name

        try:
            # Call the function with the file path
            df = convert_to_dataframe(file_path)

            # Assertions on the DataFrame
            self.assertIsNotNone(df)
            # Add more assertions on the DataFrame content if needed
        finally:
            # Remove the temporary file
            os.remove(file_path)

if __name__ == '__main__':
    unittest.main()
