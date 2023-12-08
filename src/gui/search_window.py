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

            table_label = QLabel("Table Name:", self)
            self.table_input = QLineEdit(self)

            self.search_button = QPushButton("Search", self)
            self.search_button_2 = QPushButton("Search_2", self)


            self.search_options_label = QLabel("Select search options", self)
            self.search_options_button = QComboBox(self)
            self.search_options_button.addItems(['Name'])

            self.results_table = QTableWidget(self)



            # Layout

            layout = QGridLayout()


            layout.addWidget(table_label,2,0)
            layout.addWidget(self.table_input, 3,0)
            layout.addWidget(self.search_button, 4,0)
            layout.addWidget(self.search_button_2, 4,1)
            layout.addWidget(self.search_options_label, 5,0)
            layout.addWidget(self.search_options_button, 6,0)
            layout.addWidget(self.results_table,7,0)


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
