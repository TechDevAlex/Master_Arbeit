# scripts/run_gui.py

from gui.screens.main_window import MainWindow
from PyQt6.QtWidgets import QApplication

def run():
    """
    Run the GUI application.

    This function creates a new QApplication, initializes the main window of the
    application, and starts the application's event loop.

    Note:
        This function does not return until the application's event loop has ended.
    """
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == "__main__":
    """Executes the run function if this module is run as the main script."""
    run()
