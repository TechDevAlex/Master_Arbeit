# src\gui\controllers\profile_window_controller.py

"""
This module defines the controller for the Profile window. It handles user interactions, 
responds to user actions, and updates the view accordingly.
"""

from src.gui.controllers.utils import open_data_entry_window

class Workspace:
    def __init__(self, app):
        self.app = app
        self.data_entry_window = None

    def open_data_entry_window(self):   
        self.data_entry_window = open_data_entry_window(self.app)