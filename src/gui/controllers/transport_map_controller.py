# src/controllers/transport_map_controller.py

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
from geopy.distance import geodesic
import folium
import sys

class TransportMapController:
    def __init__(self):
        self.view = None  # Initialize view as None

    def calculate_distance(self, coords_1, coords_2):
        # Calculate the distance between the coordinates
        distance = geodesic(coords_1, coords_2).km  # You can also use .km for kilometers
        return distance

    def create_map(self, coords_1, coords_2):
        # Create a map centered at the average of the coordinates
        map = folium.Map(location=((coords_1[0]+coords_2[0])/2, (coords_1[1]+coords_2[1])/2), zoom_start=6)

        # Add markers for the coordinates
        folium.Marker(location=coords_1, popup='Point 1').add_to(map)
        folium.Marker(location=coords_2, popup='Point 2').add_to(map)

        # Save the map as an HTML file
        map_file = 'map.html'
        map.save(map_file)

        # Return the file path of the saved map
        return map_file