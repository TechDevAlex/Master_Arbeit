#tests/tests_gui/test_main_window.py

import unittest
from PyQt6.QtWidgets import QApplication
from src.gui.main_window import MainWindow

class TestMainWindow(unittest.TestCase):
    def setUp(self):
        self.app = QApplication([])
        self.main_window = MainWindow()

    def test_connect_button_text(self):
        connect_button = self.main_window.findChild(QPushButton, "Connect")
        self.assertIsNotNone(connect_button)
        self.assertEqual(connect_button.text(), "Connect")

    def test_search_button_text(self):
        search_button = self.main_window.findChild(QPushButton, "Search")
        self.assertIsNotNone(search_button)
        self.assertEqual(search_button.text(), "Search")

if __name__ == '__main__':
    unittest.main()
