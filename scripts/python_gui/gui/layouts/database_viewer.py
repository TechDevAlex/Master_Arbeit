from PyQt6 import QtWidgets
from gui.database import connect_to_database  # Import the database connection function

class DatabaseViewer(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Database Tables Viewer")
        self.central_widget = QtWidgets.QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QtWidgets.QVBoxLayout()

        # Call the database connection function
        self.db_connection = connect_to_database()
        self.sub_window = None  # Initialize the sub_window variable

        if self.db_connection:
            # Fetch table names from the database
            cursor = self.db_connection.cursor()
            cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
            tables = cursor.fetchall()

            # Display the table names in a QTableWidget
            table_widget = QtWidgets.QTableWidget()
            table_widget.setColumnCount(1)
            table_widget.setRowCount(len(tables))

            for row, table in enumerate(tables):
                table_widget.setItem(row, 0, QtWidgets.QTableWidgetItem(table[0]))

            # Connect cellClicked signal to a slot (function) to show table contents
            table_widget.cellClicked.connect(self.show_table_contents)

            layout.addWidget(table_widget)
            cursor.close()

        self.central_widget.setLayout(layout)

    def show_table_contents(self, row, col):
        table_name = self.sender().item(row, col).text()
        cursor = self.db_connection.cursor()
        cursor.execute(f"SELECT * FROM {table_name}")
        data = cursor.fetchall()
        cursor.close()

        # Show the table contents in a new window
        self.sub_window = QtWidgets.QMainWindow()
        self.sub_window.setWindowTitle(f"Contents of {table_name}")
        table_widget = QtWidgets.QTableWidget()
        self.sub_window.setCentralWidget(table_widget)

        table_widget.setRowCount(len(data))
        table_widget.setColumnCount(len(data[0]))

        for row_num, row_data in enumerate(data):
            for col_num, col_data in enumerate(row_data):
                item = QtWidgets.QTableWidgetItem(str(col_data))
                table_widget.setItem(row_num, col_num, item)

        self.sub_window.show()  # Show the sub_window