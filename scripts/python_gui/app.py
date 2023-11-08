import sys
from PyQt6.QtWidgets import QApplication
from gui.database import connect_to_database
from gui.layouts.database_viewer import DatabaseViewer
from gui.layouts.welcome_page import WelcomePage

def main():
    # Call the database connection function
    db_connection = connect_to_database()

    if db_connection:
        # Create a PyQt6 application instance
        app = QApplication([])

        # Instantiate the Welcome Window and show it
        Welcome = WelcomePage()
        Welcome.show()

        # Run the application
        app.exec()

        # Close the cursor and connection after the app finishes
        db_connection.close()

if __name__ == "__main__":
    main()
