import sys
print(sys.executable)

from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
from src.data_conversion import convert_to_dataframe
from src.data_retrieval import retrieve_data_from_database
from src.db_connection import create_connection
from src.search.search_logic import SearchLogic


class SustainableMaterialsDatabaseApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sustainable Materials Database")
        self.setGeometry(500, 500, 1000, 800)

        # Widgets
        welcome_label = QLabel("Welcome to Sustainable Materials Database", self)
        search_label = QLabel("Search Material:", self)
        self.search_input = QLineEdit(self)
        self.output_label = QLabel("Output:", self)
        self.output_field = QLabel(self)
        search_button = QPushButton("Search", self)
        search_button.clicked.connect(self.search_material)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(welcome_label)
        layout.addWidget(search_label)
        layout.addWidget(self.search_input)
        layout.addWidget(self.output_label)
        layout.addWidget(self.output_field)
        layout.addWidget(search_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Create a database connection
        connection = create_connection()  

        # Perform data retrieval
        data = retrieve_data_from_database()  

        # Perform data conversion
        self.df = convert_to_dataframe(data)

        # Initialize the SearchLogic instance with the DataFrame
        self.search_logic = SearchLogic(self.df) 

    def search_material(self):
        # Get the search keyword from the input field
        search_keyword = self.search_input.text()

        # Perform search using SearchLogic
        result = self.search_logic.search(keyword=search_keyword)

        # Display the result in the output field
        self.output_field.setText(str(result))


if __name__ == "__main__":
    app = QApplication([])
    mainWin = SustainableMaterialsDatabaseApp()
    mainWin.show()
    app.exec()
