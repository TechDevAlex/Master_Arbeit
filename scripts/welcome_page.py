from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
from src.data_conversion import convert_to_dataframe
from src.data_retrieval import retrieve_data_from_database
from src.search.search_logic import SearchLogic
from src.create_session import create_session
from sqlalchemy import text

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

        # Create a database connection
        session = create_session()

        # Retrieve all table names from the database
        table_names_query = text("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';")
        result = session.execute(table_names_query)
        all_table_names = [row[0] for row in result.fetchall()]

        # Retrieve and convert data for each table
        self.dataframes = {}
        for table_name in all_table_names:
            data = retrieve_data_from_database(table_name)
            df = convert_to_dataframe(data)
            self.dataframes[table_name] = df

        # Initialize a SearchLogic instance for each DataFrame
        self.search_logics = {table_name: SearchLogic(df) for table_name, df in self.dataframes.items()}

    def search_material(self):
        # Get the search keyword from the input field
        search_keyword = self.search_input.text()

        # Perform search for each table 
        results = {table_name: logic.search(keyword=search_keyword) for table_name, logic in self.search_logics.items()}

        # Display the results in the output field
        self.output_field.setText(str(results))

if __name__ == "__main__":
    app = QApplication([])
    mainWin = SustainableMaterialsDatabaseApp()
    mainWin.show()
    app.exec()
