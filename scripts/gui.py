import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QDialog, QLabel, QLineEdit, QComboBox, QSpinBox, QTextEdit, QMessageBox
from database import connect_to_database, close_connection, execute_query


class MainPage(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the window title
        self.setWindowTitle("Main Page")

        # Create buttons
        self.login_button = QPushButton("Login")
        self.search_button = QPushButton("Search")
        self.manual_entry_button = QPushButton("Manual Data Entry")
        self.import_data_button = QPushButton("Import Data")

        # Set up layout
        layout = QVBoxLayout()
        layout.addWidget(self.login_button)
        layout.addWidget(self.search_button)
        layout.addWidget(self.manual_entry_button)
        layout.addWidget(self.import_data_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

class LoginPage(QDialog):
    def __init__(self):
        super().__init__()

        # Set the window title
        self.setWindowTitle("Login")

        # Create widgets
        username_label = QLabel("Username (Actor First Name):")
        self.username_input = QLineEdit()

        password_label = QLabel("Password (Actor Last Name):")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        login_button = QPushButton("Login")
        login_button.clicked.connect(self.check_login)

        return_to_main_button = QPushButton("Return to Main Page")
        return_to_main_button.clicked.connect(self.close)

        # Set up layout
        layout = QVBoxLayout()
        layout.addWidget(username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(login_button)
        layout.addWidget(return_to_main_button)

        self.setLayout(layout)

    def check_login(self):
        # Get the entered username and password
        entered_username = self.username_input.text()
        entered_password = self.password_input.text()

        # Connect to the database
        connection = connect_to_database()

        if connection:
            try:
                # Execute a query to check if the entered username and password match an actor
                query = f"SELECT actor_id FROM actor WHERE first_name = '{entered_username}' AND last_name = '{entered_password}';"
                cursor = execute_query(connection, query)
                data = cursor.fetchone()

                # Check if a matching actor was found
                if data:
                    # Create a message box for successful login
                    success_message = QMessageBox()
                    success_message.setWindowTitle("Login Successful")
                    success_message.setText("You have successfully logged in.")
                    success_message.exec()

                    # You can add code here to perform actions for a successful login

                else:
                    # Create a message box for failed login
                    error_message = QMessageBox()
                    error_message.setWindowTitle("Login Failed")
                    error_message.setText("Login failed. Invalid username or password.")
                    error_message.exec()
            except Exception as e:
                print("Error:", e)
            finally:
                # Close the database connection
                close_connection(connection)


class SearchPage(QDialog):
    def __init__(self):
        super().__init__()

        # Set the window title
        self.setWindowTitle("Search Parameters")

        # Create widgets
        type_label = QLabel("Type:")
        self.type_input = QLineEdit()

        property_label = QLabel("Property:")
        self.property_combo = QComboBox()
        self.property_combo.addItems(["E-Modulus", "Elongation at Break"])

        min_label = QLabel("Min:")
        self.min_spin = QSpinBox()

        max_label = QLabel("Max:")
        self.max_spin = QSpinBox()

        search_button = QPushButton("Search")

        return_to_main_button = QPushButton("Return to Main Page")
        return_to_main_button.clicked.connect(self.close)

        search_button = QPushButton("Search")
        search_button.clicked.connect(self.search_actors)

        return_to_main_button = QPushButton("Return to Main Page")
        return_to_main_button.clicked.connect(self.close)

        # Create a QTextEdit widget to display search results
        self.results_display = QTextEdit(self)

        # Set up layout
        # Set up layout
        layout = QVBoxLayout()
        layout.addWidget(type_label)
        layout.addWidget(self.type_input)
        layout.addWidget(property_label)
        layout.addWidget(self.property_combo)
        layout.addWidget(min_label)
        layout.addWidget(self.min_spin)
        layout.addWidget(max_label)
        layout.addWidget(self.max_spin)
        layout.addWidget(search_button)
        layout.addWidget(self.results_display)
        layout.addWidget(return_to_main_button)

        self.setLayout(layout)

    def search_actors(self):
        # Get the search term from the input field
        search_term = self.type_input.text()

        # Connect to the database
        connection = connect_to_database()

        if connection:
            try:
                # Execute a query to search for actors by name
                query = f"SELECT first_name, last_name FROM actor WHERE first_name LIKE '%{search_term}%' OR last_name LIKE '%{search_term}%';"
                cursor = execute_query(connection, query)
                data = cursor.fetchall()

                # Display the search results in the QTextEdit
                if data:
                    result_text = "\n".join([f"{row[0]} {row[1]}" for row in data])
                    self.results_display.setPlainText(result_text)
                else:
                    self.results_display.setPlainText("No matching actors found.")
            except Exception as e:
                print("Error:", e)
            finally:
                # Close the database connection
                close_connection(connection)


class DevPage(QDialog):
    def __init__(self, page_name):
        super().__init__()

        # Set the window title
        self.setWindowTitle(f"{page_name} - Currently in Development")

        message_label = QLabel(f"{page_name} is currently in development.")

        return_button = QPushButton("Return to Main Page")
        return_button.clicked.connect(self.close)

        # Set up layout
        layout = QVBoxLayout()
        layout.addWidget(message_label)
        layout.addWidget(return_button)

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_page = MainPage()

    def open_login_page():
        login_page = LoginPage()
        login_page.exec()

    def open_search_page():
        search_page = SearchPage()
        search_page.exec()

    def open_dev_page(page_name):
        dev_page = DevPage(page_name)
        dev_page.exec()

    main_page.login_button.clicked.connect(open_login_page)
    main_page.search_button.clicked.connect(open_search_page)
    main_page.manual_entry_button.clicked.connect(lambda: open_dev_page("Manual Data Entry"))
    main_page.import_data_button.clicked.connect(lambda: open_dev_page("Import Data"))

    main_page.show()
    sys.exit(app.exec())