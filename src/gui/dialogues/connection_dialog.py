from PyQt6.QtWidgets import QDialog, QLineEdit, QVBoxLayout, QPushButton, QLabel

class ConnectionDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Connect to Database")

        layout = QVBoxLayout()

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Username")
        layout.addWidget(self.username_input)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.password_input)

        self.license_input = QLineEdit()
        self.license_input.setPlaceholderText("License Code (optional)")
        layout.addWidget(self.license_input)

        self.connect_button = QPushButton("Connect")
        self.connect_button.clicked.connect(self.accept)
        layout.addWidget(self.connect_button)

        self.setLayout(layout)
