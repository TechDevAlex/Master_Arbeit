# test_load_media_controller.py
# todo fix bug, test is generating error: QApplication::regClass: Registering window class 'Qt661ScreenChangeObserverWindow' failed. (Klasse ist bereits vorhanden)

import unittest
import sys, os
from PyQt6.QtWidgets import QApplication, QLabel
from PyQt6.QtGui import QPixmap
from gui.controllers.load_media_controller import MediaController

class TestMediaController(unittest.TestCase):
    def setUp(self):
        self.app = QApplication.instance()
        if self.app is None:
           self.app = QApplication(sys.argv)
           print ("Created QApplication")
        self.controller = MediaController()

    def test_insert_image(self):
        label = QLabel()
        
        # Construct the path to the image
        base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
        image_path = os.path.join(base_dir, "src", "gui", "resources", "pictures", "unittest_image.png")

        self.controller.insert_image(label, image_path)

        # Check if the pixmap was correctly set
        self.assertIsInstance(label.pixmap(), QPixmap)

        # Check if the pixmap is not null (i.e., the image was loaded correctly)
        self.assertIsNotNone(label.pixmap())


    def tearDown(self):
        # Quit the QApplication
        self.app.quit()
        # Delete the QApplication instance
        self.app = None
        print("tearDown executed")

if __name__ == "__main__":
    unittest.main()