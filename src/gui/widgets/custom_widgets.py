from PyQt6.QtWidgets import QComboBox
from PyQt6.QtCore import pyqtSignal

class CustomComboBox(QComboBox):
    
    popupShown = pyqtSignal()

    def showPopup(self):
        super().showPopup()
        # Call the method to update the dropdown here
        self.popupShown.emit()