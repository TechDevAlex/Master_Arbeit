from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
from scripts.data_conversion import convert_to_dataframe
from scripts.data_retrieval import retrieve_data_from_database
from scripts.db_connection import create_connection

class SustainableMaterialsDatabaseApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sustainable Materials Database")
        self.setGeometry(100, 100, 400, 200)

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

        # Initialize the SearchLogic instance
        self.search_logic = SearchLogic(dataframe=None)  # Replace None with your actual DataFrame

    def search_material(self):
        # Get the search keyword from the input field
        search_keyword = self.search_input.text()

        # Create a database connection
        connection = create_connection(database_name="your_database_name")  # Replace with your actual database name

        # Perform data retrieval
        data = retrieve_data(connection, search_keyword)  # Update this based on your data_retrieval implementation

        # Perform data conversion
        df = create_dataframe(data)  # Update this based on your data_conversion implementation

        # Display the result in the output field
        self.output_field.setText(str(df))

if __name__ == "__main__":
    app = QApplication([])
    mainWin = SustainableMaterialsDatabaseApp()
    mainWin.show()
    app.exec()
