# src\gui\controllers\data_entry_window_controller.py
from database.data_manipulation import add_single_entry_to_table, delete_single_entry_from_table, delete_rows_from_table, delete_table
from database.data_retrieval import retrieve_column_names_from_table, retrieve_data_from_database
from PyQt6.QtWidgets import QTableWidgetItem, QAbstractItemView
import pandas as pd




"""
This module defines the functinos for user interaction
with the Data Entry window.
"""
class data_entry_window_controller:
    def __init__(self, window):
        self.window = window
        self.last_entry = None
        self.deleted_table = None

        # Create an undo stack
        self.undo_stack = []

    def submit_data(self, table_name, material_name, material_class, trade_name, material_property, datatype, value, max_min):

           # Check if all fields are filled
        if not all([table_name, material_name, material_class, trade_name, material_property, datatype, value, max_min]):
            raise ValueError("All fields must be filled")


        # Call add_single_entry_to_table with the values from the input fields
        if "max." in material_property or "min." in material_property:
            column_name = material_property
        else:
            column_name = material_property + " " + max_min + "."
        add_single_entry_to_table(
            table_name,
            material_name,
            material_class,
            trade_name,
            column_name,
            datatype,
            value
        )
        self.last_entry = {
            'table_name': table_name,
            'material_name': material_name,
            'material_class': material_class,
            'trade_name': trade_name,
            'material_property': column_name,
            'value': value
        }

        # Add the button to the undo stack
        self.undo_stack.append(self.undo_submit_data)


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

        # Make the table widget editable
        self.window.table_widget.setEditTriggers(QAbstractItemView.EditTrigger.AllEditTriggers)

    def delete_data(self):
        # Getting the selected deletion options
        combo_delete_selection = self.window.delete_combobox.currentText()
        delete_toggle = self.window.delete_toggle.isChecked()

        table_name = self.window.table_name_combobox.currentText()


        if delete_toggle:
            # Choose the appropriate function based on the selected deletion option
            if combo_delete_selection == "single entry":
                delete_single_entry_from_table()
            elif combo_delete_selection == "row":
                delete_rows_from_table()
            elif combo_delete_selection == "column":
                # TODO: delete_column_from_table()
                return
            elif combo_delete_selection == "table":
                delete_table(table_name)

        else:
            #TODO: delete_selected_data in table
            return


        self.undo_stack.append(self.undo_delete_data)


    # -----------------------------------------------------
    # Undo functionality
    # -----------------------------------------------------
        

    def undo(self):
        # Check if the undo stack is empty
        if not self.undo_stack:
            raise Exception("No actions")


        # Pop the last button from the undo stack
        undo_button = self.undo_stack.pop()

        # Call the button and get the return value
        return_of_undo_function = undo_button()

        # If the return value is None print an error message
        if return_of_undo_function is None:
            raise Exception("No further undo possible")



    def undo_submit_data(self):
        
        if self.last_entry is None:
            return

        # Delete the last entry from the database
        # keeping "value" despite only indices being necessary, to assert that the correct entry is deleted
        deleted_data = delete_single_entry_from_table(
            self.last_entry['table_name'],
            self.last_entry['material_name'],
            self.last_entry['material_class'],
            self.last_entry['trade_name'],
            self.last_entry['material_property'],
            self.last_entry['value']
        )

        # Set the last_entry to None
        self.last_entry = None

        # Return the last entry as a DataFrame
        return deleted_data

    def undo_delete_data(self):
        if self.delete_table is None:
            return
        
        # Get the last deleted data