# tests/test_search_logic.py
import unittest
import pandas as pd
from search.search_logic import search

class TestSearchLogic(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Random DataFrame for testing
        data = {
            'Material': ['Steel', 'Aluminum', 'Wood', 'Glass'],
            'E_Modulus': [200e9, 70e9, 10e9, 70e9],  # E-moduli in Pascals
        }
        cls.materials_dataframe = pd.DataFrame(data)

    def test_search_keyword_in_dataframe(self):
        result = search(self.materials_dataframe, keyword='Aluminum')

        # Expected result without considering indices
        expected_result = pd.DataFrame({'Material': ['Aluminum'], 'E_Modulus': [70e9]})

        # Search changes the index from the results, leads to bug in comparison, resetting the index before the comparison
        result_reset = result.reset_index(drop=True)
        expected_result_reset = expected_result.reset_index(drop=True)

        # Comparison
        self.assertTrue(result_reset.equals(expected_result_reset))

if __name__ == '__main__':
    unittest.main()
