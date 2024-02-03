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
        # Simulate a button click in the ConnectionDialog without opening it by immediately calling the thus called function
        # The dialog is modular, which prevents further action until the window is closed or there is a user interaction, stopping the automated tests here if just a click is simulated
        self.window.connection_controller.toggle_connection()

        # Assert that the status label in the main window is set to "Status: Connected"
        self.assertEqual(self.window.status_label.text(), "Status: Connected")
if __name__ == '__main__':
    unittest.main()