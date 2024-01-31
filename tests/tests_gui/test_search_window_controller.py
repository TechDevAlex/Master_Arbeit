# tests\tests_gui\test_search_window_controller.py

import unittest
from PyQt6.QtWidgets import QApplication
from gui.screens.search_window import SearchWindow  # Assuming this is the module where SearchWindow is defined
from gui.controllers.search_window_controller import SearchWindowController

class TestSearchLogicController(unittest.TestCase):
    def setUp(self):
        # Create a QApplication instance
        self.app = QApplication([])

        # Create an instance of SearchWindow
        self.view = SearchWindow()

        # Create an instance of SearchLogicController
        self.controller = SearchWindowController(self.view)

    def test_perform_search(self):
        # Set the text of the QLineEdit to a valid table name
        self.view.table_input.setText('unittest_table')

        # Call the method
        self.controller.perform_search()

        # Assert that the results table is not empty
        self.assertNotEqual(self.view.results_table.rowCount(), 0)
        self.assertNotEqual(self.view.results_table.columnCount(), 0)

    def tearDown(self):
        # Clean up after each test
        # Not implemented yet, but will be necessary once we start connecting to the database
        pass

if __name__ == '__main__':
    unittest.main()