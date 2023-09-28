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
