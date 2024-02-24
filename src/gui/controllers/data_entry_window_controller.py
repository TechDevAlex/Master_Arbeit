# src\gui\controllers\data_entry_window_controller.py
from database.data_insertion import add_single_entry_to_table
from database.data_retrieval import retrieve_column_names_from_table



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
            material_property + " " + max_min + ".",
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

    def set_material_property_field(self, material_property):
        # Set the material_property_field to the selected material_property
        self.window.material_property_field.setText(material_property)

    def update_column_names(self, table, property_text_input=None):
        # Get the column names from the specified table
        column_names = retrieve_column_names_from_table(table)

        # Filter the column names based on the property text
        filtered_column_names = [name for name in column_names if property_text_input.lower() in name.lower()]

        return filtered_column_names

