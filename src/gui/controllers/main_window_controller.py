# src/gui/controllers/main_window_controller.py
from PyQt6.QtWidgets import QMessageBox
from database.db_connection import create_connection
from database.db_config import get_db_credentials
from gui.screens.load_data_window import LoadDataWindow  
from gui.dialogues.connection_dialog import ConnectionDialog
from gui.screens.search_window import SearchWindow
from gui.screens.personal_workspace_window import personal_workspace_window
from gui.controllers.utils import open_data_entry_window

class DBController:
    def __init__(self, app, status_label, database_name_label, connect_button, load_data_button):
        self.app = app
        self.status_label = status_label
        self.database_name_label = database_name_label
        self.connect_button = connect_button
        self.data_button = load_data_button
        self.is_connected = False
        self.load_data_window = None 
        self.data_entry_window = None

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


    def show_connection_dialog(self):
        self.connection_dialog = ConnectionDialog()
        if self.connection_dialog.exec():
            username = self.connection_dialog.username_input.text()
            password = self.connection_dialog.password_input.text()
            license_code = self.connection_dialog.license_input.text()
            self.toggle_connection(username, password, license_code)

    def open_search_window(self):
        self.search_window = SearchWindow()
        self.search_window.show()

    def open_personal_workspace_window(self):
        self.personal_workspace_window = personal_workspace_window(self.app)
        self.personal_workspace_window.show()

    def open_data_entry_window(self):   
        self.data_entry_window = open_data_entry_window(self.app)
