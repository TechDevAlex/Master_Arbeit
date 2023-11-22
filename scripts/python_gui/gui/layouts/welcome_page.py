from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton
from .database_viewer import DatabaseViewer  # Import the DatabaseViewer class

class WelcomePage(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Welcome to the Sustainable Materials Database")
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout()

        # Welcome label
        welcome_label = QLabel("Welcome to the Sustainable Materials Database")
        layout.addWidget(welcome_label)

        # Button to open the Database Viewer
        db_viewer_button = QPushButton("Open Database Viewer")
        db_viewer_button.clicked.connect(self.open_database_viewer)
        layout.addWidget(db_viewer_button)

        self.central_widget.setLayout(layout)

    def open_database_viewer(self):
        # Instantiate the DatabaseViewer and show it
        self.viewer = DatabaseViewer()
        self.viewer.show()

def main():
    app = QApplication([])

    # Create an instance of the WelcomePage and show it
    welcome_page = WelcomePage()
    welcome_page.show()

    app.exec()

if __name__ == "__main__":
    main()
