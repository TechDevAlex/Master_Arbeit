# \src\gui\tests\tests_gui\test_main_window.py

import unittest
from PyQt6.QtWidgets import QApplication
from PyQt6.QtTest import QTest
from PyQt6.QtCore import Qt
from gui.screens.main_window import MainWindow

app = QApplication([])

class MainWindowTest(unittest.TestCase):
    def setUp(self):
        self.window = MainWindow()
        self.window.show()
        QTest.qWaitForWindowExposed(self.window)

    def test_connect_button(self):
        # Simulate a button click on the main window
        QTest.mouseClick(self.window.connect_button, Qt.MouseButton.LeftButton)

        # Wait for the LoadDataWindow to open
        while not self.window.load_data_window.isVisible():
            QTest.qWait(1)

        # Simulate a button click on the LoadDataWindow
        QTest.mouseClick(self.window.load_data_window.load_data_button, Qt.MouseButton.LeftButton)

        # Assert that the database_name_label text is "Connected"
        self.assertEqual(self.window.database_name_label.text(), "Connected")

if __name__ == '__main__':
    unittest.main()