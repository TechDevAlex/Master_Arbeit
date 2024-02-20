# src/gui/screens/main_window.py

import sys, os
from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QApplication,  QLabel
from gui.controllers.main_window_controller import DBController
from gui.controllers.load_media_controller import MediaController
from gui.screens.personal_workspace_window import personal_workspace_window
from gui.widgets.main_widgets import label, small_button
from gui.screens.search_window import SearchWindow
from gui.screens.data_entry_window import data_entry_window
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
        layout.addWidget(self.connect_button)

        # Add a Load_data button
        self.load_data_button = small_button("Load Data")
        self.load_data_button.setEnabled(False)  # Initially disabled
        self.load_data_button.setObjectName("Load_Data_Button")
        layout.addWidget(self.load_data_button)
        
        # Add a "Search" button
        self.search_button = small_button("Search")
        self.search_button.setObjectName("Search_Button")
        layout.addWidget(self.search_button)

        # Set the central widget for the main window
        self.setCentralWidget(central_widget)

        # Add a personal workspace button
        self.personal_workspace_button = small_button("Personal Workspace")
        self.personal_workspace_button.setObjectName("Personal_Workspace_Button")
        layout.addWidget(self.personal_workspace_button)

        
        # Add a data entry button
        self.data_entry_button = small_button("Data Entry")
        self.data_entry_button.setObjectName("Data_Entry_Button")
        layout.addWidget(self.data_entry_button)

        # Create the controller and pass the widgets to it
        self.main_window_controller = DBController(
            app=self.app,
            status_label=self.status_label,
            database_name_label=database_name_label,
            connect_button=self.connect_button,
            load_data_button=self.load_data_button,
        )

    
        # Connect the buttons to the controller methods
        self.connect_button.clicked.connect(self.main_window_controller.show_connection_dialog)
        self.personal_workspace_button.clicked.connect(self.main_window_controller.open_personal_workspace_window)
        self.data_entry_button.clicked.connect(self.main_window_controller.open_data_entry_window)
        self.search_button.clicked.connect(self.main_window_controller.open_search_window)


        # Show the Main Window
        self.adjustSize()
        self.show()

if __name__ == "__main__":
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    window = MainWindow(app)
    app.exec()