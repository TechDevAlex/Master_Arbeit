#src/gui/load_data_window.py
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QFileDialog, QLabel, QLineEdit, QPushButton, QGridLayout, QTableWidget, QTableWidgetItem

from gui.widgets.main_widgets import load_data_window_widgets
from src.gui.controllers.load_data_controller import LoadDataController

class LoadDataWindow(QMainWindow):

    table_names = []

    def __init__(self):
        super().__init__()
        self.initializeLoadWindow()


    def initializeLoadWindow(self):

        self.setWindowTitle("Load Data Window")
        self.setGeometry(100, 100, 400, 200)


        # Create widgets for the Load Data Window
        (
            self.load_sample_button,
            self.csv_filepath_label,
            self.csv_filepath_input,
            self.browse_button,
            self.load_data_button
        ) = load_data_window_widgets()

        self.help_load_sample_data = QPushButton("help", self) # TODO: Help menu should pop up


        # Create a new QLabel and QLineEdit for the table name
        self.table_name_label = QLabel("Table Name:", self)
        self.table_name_input = QLineEdit(self)
        self.help_table_name = QPushButton("help", self)  # TODO: Help menu should pop up

        # Create a button for updating the DataFrame
        self.update_dataframe_button = QPushButton("Update DataFrame", self)
        self.update_dataframe_button.clicked.connect(self.update_dataframe)
        self.help_update_dataframe = QPushButton("help", self)  # TODO: Help menu should pop up



        self.table_names_table = QTableWidget(self)
        self.setCentralWidget(self.table_names_table)
        
        
        # Set up layout

        layout = QGridLayout()


        layout.addWidget(self.load_sample_button, 1,0)
        layout.addWidget(self.help_load_sample_data, 1,1)
        layout.addWidget(self.csv_filepath_label, 2,0)
        layout.addWidget(self.csv_filepath_input, 3,0)
        layout.addWidget(self.browse_button, 4,0)
        layout.addWidget(self.table_name_label, 5,0)
        layout.addWidget(self.help_table_name,4,1)
        layout.addWidget(self.table_name_input, 6,0)
        layout.addWidget(self.load_data_button, 7,0)
        layout.addWidget(self.update_dataframe_button, 8,0)  # Add the update button to the layout
        layout.addWidget(self.help_update_dataframe, 8,1)
        layout.addWidget(self.table_names_table, 9,0)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Keep a reference to the QFileDialog to prevent it from being garbage-collected
        file_dialog = QFileDialog()
        self.file_dialog = file_dialog

        # Create an instance of LoadDataController
        self.controller = LoadDataController(self, file_dialog)
        self.show()

    def update_dataframe(self):
        # Call a method in the controller to update the DataFrame
        self.controller.update_dataframe()


if __name__ == "__main__":
    app = QApplication([])
    search_window = LoadDataWindow()
    app.exec()
