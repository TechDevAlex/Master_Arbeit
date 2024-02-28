from PyQt6.QtWidgets import QComboBox, QMessageBox
from PyQt6.QtCore import pyqtSignal

class CustomComboBox(QComboBox):
    
    popupShown = pyqtSignal()

    def showPopup(self):
        super().showPopup()
        # Call the method to update the dropdown here
        self.popupShown.emit()


class ErrorBox(QMessageBox):
    def __init__(self, message):
        super().__init__()
        self.setText(message)
        self.setWindowTitle("Error")
