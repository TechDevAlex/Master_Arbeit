import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QDialog, QLabel, QLineEdit, QComboBox, QSpinBox

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
        username_label = QLabel("Username:")
        self.username_input = QLineEdit()

        password_label = QLabel("Password:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        login_button = QPushButton("Login")
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
        layout.addWidget(return_to_main_button)

        self.setLayout(layout)


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
