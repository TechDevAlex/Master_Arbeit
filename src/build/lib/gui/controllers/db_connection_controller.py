# src/gui/controllers/db_connection_controller.py
from PyQt6.QtWidgets import QMessageBox
from database.db_connection import create_connection
from database.db_config import get_db_credentials
from gui.screens.load_data_window import LoadDataWindow  # Import the LoadDataWindow

class DBController:
    def __init__(self, status_label, database_name_label, connect_button, data_button):
        self.status_label = status_label
        self.database_name_label = database_name_label
        self.connect_button = connect_button
        self.data_button = data_button
        self.is_connected = False
        self.load_data_window = None  # Store the reference to LoadDataWindow

        # Connect buttons to functions
        self.connect_button.clicked.connect(self.toggle_connection)
        self.data_button.clicked.connect(self.initiate_data)

    def toggle_connection(self):
        # Attempt to create a connection
        engine = create_connection()

        if engine is not None:
            # Successfully connected
            self.is_connected = True
            self.status_label.setText("Status: Connected")
            # Use get_db_credentials to obtain the database name
            dbname, _, _, _, _ = get_db_credentials()
            self.database_name_label.setText(f"Database: {dbname}")

            # Enable the "Initiate Data" button
            self.data_button.setEnabled(True)
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

