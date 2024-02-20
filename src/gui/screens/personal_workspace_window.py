# src\gui\screens\profile_window.py

"""
This module defines the window for interacting with the profile- dependent functionalities of the database.

- Viewing manually inserted data: Users can browse the data that they have manually added to the database.
- Loading past search results: Users can retrieve and view the results of their past searches.
- ...
"""

from PyQt6.QtWidgets import QApplication, QLineEdit, QVBoxLayout, QWidget
import sys
from src.gui.widgets.main_widgets import small_button

class personal_workspace_window(QWidget):
    def __init__(self):
        super().__init__()

        # Create a QVBoxLayout to lay out the widgets
        layout = QVBoxLayout()

        # Create a QLineEdit widget
        self.input_field = QLineEdit()

        # Add the QLineEdit to the layout
        layout.addWidget(self.input_field)


        # Add data entry button
        self.data_entry_button = small_button("Data Entry")
        self.data_entry_button.setObjectName("Data_Entry_Button")
        layout.addWidget(self.data_entry_button)


        # Set the window's layout
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = personal_workspace_window()
    window.show()

    sys.exit(app.exec())