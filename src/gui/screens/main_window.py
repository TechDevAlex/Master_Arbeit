# src/gui/screens/main_window.py

import sys, os
from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QApplication,  QLabel
from gui.controllers.db_connection_controller import DBController
from gui.controllers.load_media_controller import MediaController
from gui.widgets.widgets import label, small_button, data_button
from gui.screens.search_window import SearchWindow
from gui.dialogues.connection_dialog import ConnectionDialog
from PyQt6 import QtGui


class MainWindow(QMainWindow):
    def __init__(self, app=None):
        super().__init__()
        self.app = app if app is not None else QApplication(sys.argv)
        self.initializeMainWindow()
        

    def initializeMainWindow(self):

        #Taskbar
        self.setWindowTitle('Sustainable Material Database BIOMEC')
        self.icon = "resources/pictures/logo.png" #TODO: Check from which path we are coming evtl. implement a solid path strategy so its traceable
        self.setWindowIcon(QtGui.QIcon(self.icon))

        # Create the central widget
        central_widget = QWidget()

        # Set up the layout for the central widget
        layout = QVBoxLayout(central_widget)

        # Create and add widgets from widgets.py
        self.status_label = label("Status: ")
        layout.addWidget(self.status_label)

        database_name_label = label("Database: Not Connected")
        layout.addWidget(database_name_label)

        #Main picture
        #TODO: insert main Database pictures from pictures folder
        main_picture_label = QLabel(self)
        main_picture_controller = MediaController()
        # construct the path to the main picture
        base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
        image_path_main_picture = os.path.join(base_dir, "src", "gui", "resources", "pictures", "pic_front_page.png")
        # call the media controller to insert the image into the label
        main_picture_controller.insert_image(main_picture_label, image_path_main_picture)
        # add the label to the layout
        layout.addWidget(main_picture_label)

        # Connect button
        self.connect_button = small_button("Establish Connection")
        self.connect_button.setObjectName("Establish_Connection_Button")
        self.connect_button.clicked.connect(self.show_connection_dialog)  # When the 'Connect' button is clicked, the 'show_connection_dialog' method is triggered.
        layout.addWidget(self.connect_button)

        # Add an "Initiate Data" button
        self.data_load_button = data_button("Load Data")
        self.data_load_button.setEnabled(False)  # Initially disabled
        layout.addWidget(self.data_load_button)
        
        # Add a "Search" button
        search_button = small_button("Search")
        search_button.setObjectName("Search_Button")
        search_button.clicked.connect(self.open_search_window)  # Connect the button click event to a function that opens the search window
        layout.addWidget(search_button)

        # Set the central widget for the main window
        self.setCentralWidget(central_widget)

        # Create the controller and pass the widgets to it
        self.connection_controller = DBController(
            status_label=self.status_label,
            database_name_label=database_name_label,
            connect_button=self.connect_button,
            data_button=self.data_load_button,
        )

        self.setGeometry(100,100,800,600)
        self.show()

    def open_search_window(self):
        # Create an instance of the search window
        self.search_window = SearchWindow()

        # Show the search window
        self.search_window.show()

    def show_connection_dialog(self):        
        self.connection_dialog = ConnectionDialog()
        if self.connection_dialog.exec():
            username = self.connection_dialog.username_input.text()
            password = self.connection_dialog.password_input.text()
            license_code = self.connection_dialog.license_input.text()
            self.connection_controller.toggle_connection(username, password, license_code)
    

if __name__ == "__main__":
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    window = MainWindow(app)
    app.exec()