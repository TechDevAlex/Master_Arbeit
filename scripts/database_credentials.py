import json
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

class DatabaseConfigDialog(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Database Configuration")
        self.setGeometry(100, 100, 400, 200)

        self.host_label = QLabel("Database Host:")
        self.database_label = QLabel("Database Name:")
        self.user_label = QLabel("Database Username:")
        self.password_label = QLabel("Database Password:")

        self.host_input = QLineEdit()
        self.database_input = QLineEdit()
        self.user_input = QLineEdit()
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)

        self.save_button = QPushButton("Save Configuration")
        self.save_button.clicked.connect(self.save_configuration)

        layout = QVBoxLayout()
        layout.addWidget(self.host_label)
        layout.addWidget(self.host_input)
        layout.addWidget(self.database_label)
        layout.addWidget(self.database_input)
        layout.addWidget(self.user_label)
        layout.addWidget(self.user_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.save_button)

        self.setLayout(layout)

    def save_configuration(self):
        host = self.host_input.text()
        database = self.database_input.text()
       
