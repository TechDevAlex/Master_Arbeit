# src\gui\controllers\data_entry_window_controller.py
from database.data_insertion import type_mapping_SQLtoPython, type_mapping_StringtoSQL, add_single_entry_to_table



"""
This module defines the functinos for user interaction
with the Data Entry window.
"""
class data_entry_window_controller:
    def __init__(self, window):
        self.window = window



    def submit_data(self, table_name, material_name, material_class, trade_name, material_property, datatype, value, max_min):
        # Call add_single_entry_to_table with the values from the input fields
        add_single_entry_to_table(
            table_name,
            material_name,
            material_class,
            trade_name,
            material_property + max_min + ".",
            datatype,
            value
        )

    def toggle_max_min(self, state):
        # Check the state of the toggle button
        if state:
            # If the toggle button is on, set the label to "max"
            self.window.max_min_label.setText("min")
        else:
            # If the toggle button is off, set the label to "min"
            self.window.max_min_label.setText("max")