# \src\gui\tests\tests_gui\test_main_window.py

import unittest
from PyQt6.QtWidgets import QApplication
from PyQt6.QtTest import QTest
from PyQt6.QtCore import Qt
from gui.screens.main_window import MainWindow
from PyQt6.QtWidgets import QPushButton, QComboBox, QLineEdit

app = None  # Global QApplication instance

class MainWindowTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Initialize QApplication once for all tests."""
        global app
        app = QApplication.instance()
        if app is None:
            app = QApplication([])

    def setUp(self):
        """Set up method to prepare the test environment for each test."""
        # Pass the shared QApplication instance to MainWindow
        self.window = MainWindow(app)

    def tearDown(self):
        """Tear down method to clean up after each test."""
        self.window.close()

    def test_user_navigation(self):
        """
        Test the user navigation through the GUI.
        This test emulates a user clicking on the connect button, then the load data button, and so on.
        """

        # -------------------------
        # Testing Main Window
        # -------------------------

        # Emulate a user clicking on the connect button
        self.window.main_window_controller.toggle_connection()
        # Check if the status label is updated correctly
        self.assertEqual(self.window.status_label.text(), "Status: Connected")   

        # Check if the load data button is enabled
        self.assertTrue(self.window.load_data_button.isEnabled())
        # Emulate a user clicking on the load data button
        QTest.mouseClick(self.window.findChild(QPushButton, "Load_Data_Button"), Qt.MouseButton.LeftButton)
        # Check if the load data window is open
        self.assertTrue(self.window.main_window_controller.load_data_window.isVisible())
        # Emulate a user closing the load data window
        self.window.main_window_controller.load_data_window.close()
        # Check if the load data window is closed
        self.assertFalse(self.window.main_window_controller.load_data_window.isVisible())

        # Emulate a user clicking on the search button
        QTest.mouseClick(self.window.findChild(QPushButton, "Search_Button"), Qt.MouseButton.LeftButton)
        # Check if the search window is open
        self.assertTrue(self.window.search_window.isVisible())

        # -------------------------
        # Testing Search Window
        # -------------------------

        # Emulate a user selecting "test_data" in the combo box
        combo_box = self.window.search_window.findChild(QComboBox, "table_names_combo_box")


        # Check if the combo_box is not None
        if combo_box is not None:
            # Iterate over the items in the combo_box
            for i in range(combo_box.count()):
                # Check if the item text contains "test_data"
                if "test_data" in combo_box.itemText(i):
                    # Set the index to the current iteration value
                    index = i
                    break
            # Set the combo_box's current index to the found index
            combo_box.setCurrentIndex(index)
            # Assert that the input field text is "test_data", it should change automatically upon currentTextChanged calling update_table_name in the search controller
            self.assertEqual(self.window.search_window.findChild(QLineEdit, "table_input").text(), '"test_data"')
        else:
            # Fail the test if the combo_box is not found
            self.fail("Could not find combo box 'table_names_combo_box'")






        # Emulate a user closing the search window
        self.window.search_window.close()
        # Check if the search window is closed
        self.assertFalse(self.window.search_window.isVisible())




if __name__ == '__main__':
    unittest.main()