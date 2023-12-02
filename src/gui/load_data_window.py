# src/gui/load_data_window.py
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QFileDialog, QLabel, QLineEdit

from src.gui.widgets.widgets import load_data_window_widgets
from src.gui.controllers.load_data_controller import LoadDataController

class LoadDataWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Create widgets for the Load Data Window
        (
            self.label,
            self.load_sample_button,
            self.csv_filepath_label,
            self.csv_filepath_input,
            self.browse_button,
            self.load_data_button
        ) = load_data_window_widgets()

        # Create a new QLabel and QLineEdit for the table name
        self.table_name_label = QLabel("Table Name:", self)
        self.table_name_input = QLineEdit(self)

        # Set up layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.load_sample_button)
        layout.addWidget(self.csv_filepath_label)
        layout.addWidget(self.csv_filepath_input)
        layout.addWidget(self.browse_button)
        layout.addWidget(self.table_name_label)  # Add the table name label to the layout
        layout.addWidget(self.table_name_input)  # Add the table name input field to the layout
        layout.addWidget(self.load_data_button)

        # Keep a reference to the QFileDialog to prevent it from being garbage-collected
        file_dialog = QFileDialog()
        self.file_dialog = file_dialog

        # Create an instance of LoadDataController
        self.controller = LoadDataController(self, file_dialog)
