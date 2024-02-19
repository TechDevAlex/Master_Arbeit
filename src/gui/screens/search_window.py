#src\gui\screens\search_window.py
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QGridLayout, QWidget, QFileDialog, QTableWidget, QComboBox, QTableWidgetItem
from gui.controllers.search_window_controller import SearchWindowController

class SearchWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initializeSearchWindow()

    def initializeSearchWindow(self):
        self.setWindowTitle("Search Window")

        # Widgets
        self.table_table_label = QLabel("Names of uploaded tables:", self)
        self.table_table = QTableWidget(self) #DONE: should list the uploaded table names
        self.delete_instance = QPushButton("Delete Table", self) #TODO: Should delete instance (Delete from Dataframe?)
        self.clear_table = QPushButton("Clear Tables", self) #TODO: should clear table and delete list of tables

        table_label = QLabel("Insert table name", self)
        self.table_input = QLineEdit(self)
        # Set the name of the line edit
        self.table_input.setObjectName("table_input")

        self.search_button = QPushButton("Display Table", self)
        self.help_search = QPushButton("help", self) #DONE: (Search-)Help menu should pop up



        self.search_options_label = QLabel("Select search options", self)
        self.search_options_button = QComboBox(self) #TODO: Click on option should pop up another window for further search refinement
        self.search_options_button.addItems(['Simple Search', 'Parameter Search', 'Combined Search', 'Complete Search'])
        self.help_search_options = QPushButton("help", self) #TODO: Help menu should pop up

        self.results_table = QTableWidget(self) #TODO: Is it possible to click into the components of a table?

        self.export_button = QPushButton('Export', self) #TODO: Export menu should pop up
        self.clipboard_button = QPushButton('Clipboard',self) #TODO: Results should be stored at a clipboard

        # Create an instance of SearchLogicController
        self.controller = SearchWindowController(self)

        # Connect help button to function in controller to open help window
        self.help_search.clicked.connect(self.controller.open_help_search_window)


        # Get the list of uploaded table names
        table_names = self.controller.get_table_names()

        # Set the number of rows in the table to the number of table names
        self.table_table.setRowCount(len(table_names))

        # Set the number of columns in the table (needs to be configured for QTableWidget, data outside of configured columns will not be displayed)
        self.table_table.setColumnCount(1)

        # For each table name, create a new item in the table
        for i, table_name in enumerate(table_names):
            item = QTableWidgetItem(table_name)
            self.table_table.setItem(i, 0, item)

        self.table_table.viewport().update()

        # Create a combo box for the table names
        self.table_names_combo_box = QComboBox(self)

        # Set the name of the combo box
        self.table_names_combo_box.setObjectName("table_names_combo_box")

        # Add the table names to the combo box
        self.table_names_combo_box.addItems(table_names)

        # Connect combobox signal to controller to update table in search window upon selection in combobox
        self.table_names_combo_box.currentTextChanged.connect(self.controller.update_table_name)

        # Layout
        layout = QGridLayout()

        layout.addWidget(self.table_table_label, 1,0)
        layout.addWidget(self.table_table,2,0)
        layout.addWidget(self.delete_instance, 2,1)
        layout.addWidget(self.clear_table, 3,0)
        layout.addWidget(table_label,4,0)
        layout.addWidget(self.table_names_combo_box, 4,1) #TODO (added by ALEX): will only hold the most recently selected table names 
        layout.addWidget(self.table_input, 5,0)
        layout.addWidget(self.search_button, 6,0)
        layout.addWidget(self.help_search, 6,1)
        layout.addWidget(self.search_options_label, 7,0)
        layout.addWidget(self.search_options_button, 8,0)
        layout.addWidget(self.help_search_options, 8,1)
        layout.addWidget(self.results_table,9,0)
        layout.addWidget(self.export_button, 10,0)
        layout.addWidget(self.clipboard_button, 10,1)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Keep a reference to the QFileDialog to prevent it from being garbage-collected
        file_dialog = QFileDialog()
        self.file_dialog = file_dialog

        # Use adjust size to autmatically resize the window so all widgets are visible 
        self.adjustSize()

        # Show the window
        self.show()

if __name__ == "__main__":
    app = QApplication([])
    search_window = SearchWindow()
    app.exec()