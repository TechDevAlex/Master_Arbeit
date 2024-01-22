# src/gui/controllers/db_connection_controller.py
from PyQt6.QtWidgets import QMessageBox
from database.db_connection import create_connection
from database.db_config import get_db_credentials
from database.data_retrieval import retrieve_data_from_database
from gui.controllers.load_data_controller import LoadDataController  
from gui.screens.load_data_window import LoadDataWindow  
import os

class DBController:
    def __init__(self, status_label, database_name_label, connect_button, data_button, data_default_button):
        self.status_label = status_label
        self.database_name_label = database_name_label
        self.connect_button = connect_button
        self.data_button = data_button
        self.data_default_button = data_default_button
        self.is_connected = False
        self.load_data_window = None 

        # Connect buttons to functions
        self.connect_button.clicked.connect(self.toggle_connection)
        self.data_button.clicked.connect(self.initiate_data)

    def toggle_connection(self, username=None, password=None, license_code=None):
        # Attempt to create a connection
        engine = create_connection(username=username, password=password, license_code=license_code)

        if engine is not None:
            # Successfully connected
            self.is_connected = True
            self.status_label.setText("Status: Connected")
            # Use get_db_credentials to obtain the database name
            dbname, _, _, _, _ = get_db_credentials()
            self.database_name_label.setText(f"Database: {dbname}")

            # Enable the "Initiate Data" button
            self.data_button.setEnabled(True)
            # Enable the "Initiate Default Data" button
            self.data_default_button.setEnabled(True)
        else:
            # Connection failed
            self.is_connected = False
            self.status_label.setText("Status: Not Connected")
            self.database_name_label.setText("Database: Not Connected")
            self.data_button.setEnabled(False)

            QMessageBox.critical(None, "Error", "Unable to connect to the database.")

    def initiate_data(self):
        # enable the Initiate Data button when the Database is connected
        self.load_data_window = LoadDataWindow()
        self.load_data_window.show()


    def default_data_retrieval(self, table_name='default_table'):

        print(f"Retrieving data from table: {table_name}")

        # Get the directory of the current file (db_connection_controller.py)
        current_dir = os.path.dirname(os.path.abspath(__file__))

        # Construct the path to the CSV file
        csv_filepath = os.path.join(current_dir, '..', '..', '..', 'data', 'Sample_Simple_1.csv')
        
        # Create a LoadDataWindow
        load_data_window = LoadDataWindow()

        # Initialize the LoadDataController with the LoadDataWindow and the CSV file path
        load_data_controller = LoadDataController(load_data_window, None, csv_filepath, table_name)

