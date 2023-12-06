from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QFileDialog, QTableWidget, QComboBox
from src.gui.controllers.search_logic_controller import SearchLogicController



class SearchWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Search Window")
        self.setGeometry(100, 100, 400, 200)

        # Widgets
        search_label = QLabel("Search Query:", self)
        self.query_input = QLineEdit(self)

        table_label = QLabel("Table Name:", self)
        self.table_input = QLineEdit(self)

        self.search_button = QPushButton("Search", self)

        self.search_options_label = QLabel("Select search options", self)
        self.search_options_button = QComboBox(self)
        self.search_options_button.addItems(['Name'])

        self.results_table = QTableWidget(self)
       
        

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(search_label)
        layout.addWidget(self.query_input)
        layout.addWidget(table_label)
        layout.addWidget(self.table_input)
        layout.addWidget(self.search_button)
        layout.addWidget(self.search_options_label)
        layout.addWidget(self.search_options_button)
        layout.addWidget(self.results_table)
        

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Keep a reference to the QFileDialog to prevent it from being garbage-collected
        file_dialog = QFileDialog()
        self.file_dialog = file_dialog

        # Create an instance of SearchLogicController
        self.controller = SearchLogicController(self)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    search_window = SearchWindow()
    search_window.show()
    app.exec()
