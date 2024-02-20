# src\gui\screens\data_entry_window.py


"""
This windows handles manual data insertion.
An example entry is:
"""


from PyQt6.QtWidgets import QApplication, QLineEdit, QVBoxLayout, QWidget
import sys

class data_entry_window(QWidget):
    def __init__(self):
        super().__init__()

        # Create a QVBoxLayout to lay out the widgets
        layout = QVBoxLayout()

        # Create a QLineEdit widget
        self.input_field = QLineEdit()

        # Add the QLineEdit to the layout
        layout.addWidget(self.input_field)

        # Set the window's layout
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = data_entry_window()
    window.show()

    sys.exit(app.exec())