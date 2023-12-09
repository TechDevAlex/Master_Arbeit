from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout, QGridLayout, QWidget, QFileDialog, QTableWidget, QComboBox
from src.gui.controllers.search_logic_controller import SearchLogicController



class SearchWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initializeSearchWindow()



    def initializeSearchWindow(self):

            self.setWindowTitle("Search Window")
            self.setGeometry(100, 100, 400, 200)

            # Widgets
            #search_label = QLabel("Search Query:", self)
            #self.query_input = QLineEdit(self)

            table_table_label = QLabel("Names of uploaded tables:", self)
            self.table_table = QTableWidget(self) #TODO: should list the uploaded table names

            table_label = QLabel("Insert table name", self)
            self.table_input = QLineEdit(self)

            self.search_button = QPushButton("Display Table", self)
            self.help_search = QPushButton("help", self) #TODO: Help menu should pop up


            self.search_options_label = QLabel("Select search options", self)
            self.search_options_button = QComboBox(self) #TODO: Click on option should pop up another window for further search refinement
            self.search_options_button.addItems(['Simple Search', 'Parameter Search', 'Combined Search', 'Complete Search'])
            self.help_search_options = QPushButton("help", self) #TODO: Help menu should pop up

            self.results_table = QTableWidget(self) #TODO: Is it possible to click into the components of a table?

            self.export_button = QPushButton('Export', self) #TODO: Export menu should pop up
            self.clipboard_button = QPushButton('Clipboard',self) #TODO: Results should be stored at a clipboard



            # Layout

            layout = QGridLayout()

            layout.addWidget(table_table_label, 1,0)
            layout.addWidget(self.table_table,2,0)
            layout.addWidget(table_label,3,0)
            layout.addWidget(self.table_input, 4,0)
            layout.addWidget(self.search_button, 5,0)
            layout.addWidget(self.help_search, 5,1)
            layout.addWidget(self.search_options_label, 6,0)
            layout.addWidget(self.search_options_button, 7,0)
            layout.addWidget(self.help_search_options, 7,1)
            layout.addWidget(self.results_table,8,0)
            layout.addWidget(self.export_button, 9,0)
            layout.addWidget(self.clipboard_button, 9,1)


            container = QWidget()
            container.setLayout(layout)
            self.setCentralWidget(container)

            # Keep a reference to the QFileDialog to prevent it from being garbage-collected
            file_dialog = QFileDialog()
            self.file_dialog = file_dialog

            # Create an instance of SearchLogicController
            self.controller = SearchLogicController(self)
            self.show()
        

if __name__ == "__main__":
    app = QApplication([])
    search_window = SearchWindow()
    app.exec()
