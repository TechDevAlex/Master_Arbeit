# src\gui\controllers\data_entry_window_controller.py
from database.data_insertion import add_single_entry_to_table
from database.data_retrieval import retrieve_column_names_from_table, retrieve_data_from_database
from PyQt6.QtWidgets import QTableWidgetItem
import pandas as pd



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

    def display_table(self):
        # Get the selected table name
        table_name = self.window.table_name_combobox.currentText()

        # Retrieve the data from the database
        data = retrieve_data_from_database(table_name)

       # Convert the data to a DataFrame
        df = pd.DataFrame(data)


        # # Clear the existing table widget
        # self.window.table_widget.setRowCount(0)
        # self.window.table_widget.setColumnCount(len(df.columns))
        # self.window.table_widget.setHorizontalHeaderLabels(df.columns)

        # Get the column names from the DataFrame
        column_names = df.columns.tolist()

        # Set the column names in the QTableWidget
        self.window.table_widget.setHorizontalHeaderLabels(column_names)

        # Display the data in the QTableWidget
        self.window.table_widget.setRowCount(len(df))
        self.window.table_widget.setColumnCount(len(df.columns))
        for i, row in enumerate(df.values):
            for j, item in enumerate(row):
                self.window.table_widget.setItem(i, j, QTableWidgetItem(str(item)))