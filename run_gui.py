# scripts/run_gui.py

from src.gui.main_window import MainWindow
from PyQt6.QtWidgets import QApplication

def run():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == "__main__":
    run()