#\src\gui\controllers\load_media_controller.py

from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QLabel

class MediaController:
    def __init__(self):
        pass

    def insert_image(self, label: QLabel, image_path: str):
        
        # Create a QPixmap object
        pixmap = QPixmap(image_path)

        # Set the QPixmap object as the picture for the QLabel
        label.setPixmap(pixmap)
        label.setScaledContents(True)