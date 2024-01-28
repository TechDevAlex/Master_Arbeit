# src/gui/screens/transport_map_window.py
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLineEdit, QPushButton, QLabel
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
from gui.controllers.transport_map_controller import TransportMapController
import os

class TransportMapWindow(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.setWindowTitle("Transport Map")
        self.setGeometry(100, 100, 800, 600)
        self.create_widgets()

    def create_widgets(self):
        # Create QWebEngineView widget for the map
        self.web_view = QWebEngineView()

        # Create QLineEdit widgets for the coordinates
        self.coord1_input = QLineEdit(self)
        self.coord2_input = QLineEdit(self)

        # Create a QPushButton
        self.button = QPushButton('Calculate Distance and Update Map', self)
        self.button.clicked.connect(self.update_map)

        # Create a QLabel for the distance
        self.distance_label = QLabel(self)

        vbox = QVBoxLayout()
        vbox.addWidget(self.web_view)
        vbox.addWidget(self.coord1_input)
        vbox.addWidget(self.coord2_input)
        vbox.addWidget(self.button)
        vbox.addWidget(self.distance_label)  # Add the QLabel to the layout

        widget = QWidget()
        widget.setLayout(vbox)
        self.setCentralWidget(widget)

    def update_map(self):
        # Get the coordinates from the QLineEdit widgets and convert them to tuples of floats
        coord1 = tuple(map(float, self.coord1_input.text().split(',')))
        coord2 = tuple(map(float, self.coord2_input.text().split(',')))

        # Calculate the distance and update the map
        distance = self.controller.calculate_distance(coord1, coord2)
        map_file = self.controller.create_map(coord1, coord2)

        # Update the QLabel with the calculated distance
        self.distance_label.setText(f"Distance: {distance} km")

        # Update the map in the QWebEngineView
        self.web_view.load(QUrl.fromLocalFile(os.path.abspath(map_file)))

def main():
    app = QApplication([])
    controller = TransportMapController()
    window = TransportMapWindow(controller)
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()