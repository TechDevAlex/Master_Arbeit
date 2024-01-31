from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout, QGridLayout, QWidget, QFileDialog, QTableWidget, QComboBox, QTableWidgetItem
from src.gui.controllers.search_window_controller import SearchWindowController

class SearchWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initializeSearchWindow()

    def initializeSearchWindow(self):
        self.setWindowTitle("Search Window")
        self.setGeometry(100, 100, 400, 200)

        # Widgets
        table_table_label = QLabel("Names of uploaded tables:", self)
        self.table_table = QTableWidget(self)

        table_label = QLabel("Insert table name", self)
        self.table_input = QLineEdit(self)

        self.search_button = QPushButton("Display Table", self)
        self.help_search = QPushButton("help", self)

        self.search_options_label = QLabel("Select search options", self)
        self.search_options_button = QComboBox(self)
        self.search_options_button.addItems(['Simple Search', 'Parameter Search', 'Combined Search', 'Complete Search'])
        self.help_search_options = QPushButton("help", self)

        self.results_table = QTableWidget(self)

        self.export_button = QPushButton('Export', self)
        self.clipboard_button = QPushButton('Clipboard',self)

        # Create an instance of SearchLogicController
        self.controller = SearchWindowController(self)

        # Get the list of uploaded table names
        table_names = self.controller.get_table_names()

        # Set the number of rows in the table to the number of table names
        self.table_table.setRowCount(len(table_names))

        # For each table name, create a new item in the table
        for i, table_name in enumerate(table_names):
            item = QTableWidgetItem(table_name)
            self.table_table.setItem(i, 0, item)

        # Create a combo box for the table names
        self.table_names_combo_box = QComboBox(self)

        # Add the table names to the combo box
        self.table_names_combo_box.addItems(table_names)

        # Connect combobox signal to controller to update table in search window upon selection in combobox
        self.table_names_combo_box.currentTextChanged.connect(self.controller.update_table_name)

        # Layout
        layout = QGridLayout()

        layout.addWidget(table_table_label, 1,0)
        layout.addWidget(self.table_table,2,0)
        layout.addWidget(self.table_names_combo_box, 3, 0)  # combo box is here
        layout.addWidget(table_label,4,0)
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

        # Show the window
        self.show()

if __name__ == "__main__":
    app = QApplication([])
    search_window = SearchWindow()
    app.exec()