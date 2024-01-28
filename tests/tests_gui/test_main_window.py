#tests/tests_gui/test_main_window.py

import unittest
import sys, time
from PyQt6.QtWidgets import QApplication, QPushButton
from src.gui.screens.main_window import MainWindow

class TestMainWindow(unittest.TestCase):
    def setUp(self):
        self.app = QApplication.instance()
        if self.app is None:
           self.app = QApplication(sys.argv)
        self.main_window = MainWindow()
        time.sleep(1)

    def test_connect_button_text(self):
        connect_button = self.main_window.findChild(QPushButton, "Connect_Button")
        self.assertIsNotNone(connect_button)
        self.assertEqual(connect_button.text(), "Establish Connection")

    def test_search_button_text(self):
        search_button = self.main_window.findChild(QPushButton, "Search_Button")
        self.assertIsNotNone(search_button)
        self.assertEqual(search_button.text(), "Search")
    
    def tearDown(self):
        # Close the MainWindow
        self.main_window.close()
        # Quit the QApplication
        self.app.quit()
        # Delete the QApplication instance
        self.app = None


    
if __name__ == '__main__':
    unittest.main()