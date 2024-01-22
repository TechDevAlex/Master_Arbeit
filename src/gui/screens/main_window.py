# src/gui/main_window.py
from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QApplication, QLabel

from gui.controllers.db_connection_controller import DBController
from gui.widgets.widgets import label, small_button, data_button
from gui.screens.search_window import SearchWindow
from gui.dialogues.connection_dialog import ConnectionDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initializeMainWindow()

    def initializeMainWindow(self):
        self.setWindowTitle('Main Window')

        # Create the central widget
        central_widget = QWidget()

        # Set up the layout for the central widget
        layout = QVBoxLayout(central_widget)

        # Create and add widgets from widgets.py
        status_label = label("Status: ")
        layout.addWidget(status_label)

        database_name_label = label("Database: Not Connected")
        layout.addWidget(database_name_label)

        # Connect button
        connect_button = small_button("Establish Connection")
        connect_button.clicked.connect(self.show_connection_dialog)  # When the 'Connect' button is clicked, the 'show_connection_dialog' method is triggered.
        layout.addWidget(connect_button)

        # Add an "Initiate Data" button
        self.data_load_button = data_button("Load Data")
        self.data_load_button.setEnabled(False)  # Initially disabled
        layout.addWidget(self.data_load_button)

        # Add an "Initiate Default Data" button
        self.data_default_button = data_button("Go on with Default Databases")
        self.data_default_button.setEnabled(False)  # Initially disabled
        self.data_default_button.clicked.connect(self.load_default_datasets)       
        layout.addWidget(self.data_default_button)  # DONE: Would be nice to have default datasets loaded when clicking that button
        
        # Add a "Search" button
        search_button = small_button("Search")
        search_button.clicked.connect(self.open_search_window)  # Connect the button click event to a function that opens the search window
        layout.addWidget(search_button)

        # Set the central widget for the main window
        self.setCentralWidget(central_widget)

        # Create the controller and pass the widgets to it
        self.connection_controller = DBController(
            status_label=status_label,
            database_name_label=database_name_label,
            connect_button=connect_button,
            data_button=self.data_load_button,
            data_default_button=self.data_default_button
        )

        self.setGeometry(100,100,250,150)
        self.show()

    def open_search_window(self):
        # Create an instance of the search window
        self.search_window = SearchWindow()

        # Show the search window
        self.search_window.show()

    def show_connection_dialog(self):
        dialog = ConnectionDialog()
        if dialog.exec():
            username = dialog.username_input.text()
            password = dialog.password_input.text()
            license_code = dialog.license_input.text()
            self.connection_controller.toggle_connection(username, password, license_code)
    
    def load_default_datasets(self):
        self.connection_controller.default_data_retrieval()

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    app.exec()