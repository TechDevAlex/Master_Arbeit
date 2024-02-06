# src\gui\screens\help_window.py

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit

class SearchHelpWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Create widgets
        self.search_label = QLabel("Search Documentation:")
        self.search_input = QLineEdit()
        self.open_doc_button = QPushButton("Open Documentation")
        self.contact_support_button = QPushButton("Contact Support")
        self.faq_button = QPushButton("FAQs")
        self.tutorial_button = QPushButton("Tutorials")

        # Set up layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.search_label)
        layout.addWidget(self.search_input)
        layout.addWidget(self.open_doc_button)
        layout.addWidget(self.contact_support_button)
        layout.addWidget(self.faq_button)
        layout.addWidget(self.tutorial_button)

        # Set window title
        self.setWindowTitle("Help Window")

        # Set window size
        self.resize(400, 300)

    def open_help_search_window(self):
        self.help_window = HelpWindow()
        self.help_window.show()