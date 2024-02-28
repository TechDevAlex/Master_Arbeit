# src\gui\screens\data_entry_window.py
from PyQt6.QtWidgets import QApplication, QLineEdit, QWidget, QLabel, QPushButton, QComboBox, QGridLayout, QTableWidget
from PyQt6.QtCore import Qt
from database.data_insertion import type_mapping_StringtoSQL
from database.data_retrieval import retrieve_table_names_from_database
from gui.controllers.data_entry_window_controller import data_entry_window_controller
from gui.widgets.custom_widgets import CustomComboBox, ErrorBox
import sys

class data_entry_window(QWidget):
    def __init__(self):
        super().__init__()

        self.controller = data_entry_window_controller(self)

        # Create QLineEdit widgets for each input field
        self.material_name_field = QLineEdit()
        self.material_name_field.setObjectName("material_name_field")
        self.material_class_field = QLineEdit()
        self.material_class_field.setObjectName("material_class_field")
        self.trade_name_field = QLineEdit() 
        self.trade_name_field.setObjectName("trade_name_field")
        self.material_property_field = QLineEdit()
        self.material_property_field.setObjectName("material_property_field")

        # Create a QComboBox for the datatype field
        self.datatype_field = QComboBox()
        self.datatype_field.setObjectName("datatype_field")

        # Add the datatypes to the QComboBox
        for datatype in type_mapping_StringtoSQL().keys():
            self.datatype_field.addItem(str(datatype))

        self.value_field = QLineEdit()
        self.value_field.setObjectName("value_field")

        # Create a QComboBox for the table names
        self.table_name_combobox = QComboBox()
        self.table_name_combobox.setObjectName("table_names_combobox")

        # Get the table names and add them to the QComboBox
        table_names = retrieve_table_names_from_database()
        for table_name in table_names:
            table_name = table_name.strip('"')
            self.table_name_combobox.addItem(table_name)

        # Create a QPushButton that will call add_single_entry_to_table when clicked
        self.submit_button = QPushButton("Submit")
        self.submit_button.setObjectName("submit_button")
        self.submit_button.clicked.connect(self.submit_data)

        # Create a QLabel for the max/min display
        self.max_min_label = QLabel("max")
        self.max_min_label.setObjectName("max_min_label")
        self.max_min_label.setFixedWidth(30)

        # Create a QCheckBox to determine if the value is a max or min
        self.max_min_toggle = QPushButton("max <-> min")
        self.max_min_toggle.setObjectName("max_min_toggle")
        self.max_min_toggle.setCheckable(True)
        self.max_min_toggle.setFixedWidth(100)
        self.max_min_toggle.clicked.connect(self.toggle_max_min)

        # Create a QComboBox for the material property field
        self.material_property_dropdown = CustomComboBox()
        self.material_property_dropdown.setObjectName("material_property_drowdown")
        self.material_property_dropdown.setFixedWidth(200)
        self.material_property_dropdown.popupShown.connect(self.update_material_property_dropdown)
        self.material_property_dropdown.activated.connect(lambda: self.controller.set_material_property_field(self.material_property_dropdown.currentText()))

        # Create  button to display the current table
        self.display_table_button = QPushButton("Display Table")
        self.display_table_button.setObjectName("display_table_button")
        self.display_table_button.clicked.connect(self.controller.display_table)
   

        # Create a widget to display the table
        self.table_widget = QTableWidget()
        self.table_widget.setObjectName("table_widget")
        self.table_widget.setRowCount(10)
        self.table_widget.setColumnCount(5)

        #Create an undo button to undo the last submitted entry
        self.undo_button = QPushButton("Undo last action")
        self.undo_button.setObjectName("undo_submit_button")
        self.undo_button.clicked.connect(self.undo_last_entry)






        # Create a QGridLayout to lay out the widgets
        layout = QGridLayout()

        # Add the QLineEdit widgets and QComboBox to the layout with labels
        layout.addWidget(QLabel("Table Name"), 0, 0)
        layout.addWidget(self.table_name_combobox, 0, 1)
        layout.addWidget(self.display_table_button, 0, 2)
        layout.addWidget(self.table_widget, 0, 3)

        layout.addWidget(QLabel("Material Name"), 1, 0)
        layout.addWidget(self.material_name_field, 1, 1)

        layout.addWidget(QLabel("Material Class"), 2, 0)
        layout.addWidget(self.material_class_field, 2, 1)

        layout.addWidget(QLabel("Trade Name"), 3, 0)
        layout.addWidget(self.trade_name_field, 3, 1)

        layout.addWidget(QLabel("Material Property"), 4, 0)
        layout.addWidget(self.material_property_field, 4, 1)
        layout.addWidget(self.material_property_dropdown, 4, 3)

        layout.addWidget(QLabel("Data Type"), 5, 0)
        layout.addWidget(self.datatype_field, 5, 1)

        layout.addWidget(QLabel("Value"), 6, 0)
        layout.addWidget(self.value_field, 6, 1)
        layout.addWidget(self.max_min_label, 6, 2)
        layout.addWidget(self.max_min_toggle, 6, 3)

        layout.addWidget(self.submit_button, 7, 1)
        layout.addWidget(self.undo_button, 7, 2)

        # Set the window's layout
        self.setLayout(layout)


    def submit_data(self):
        # Call the controller's submit_data method
        try:
            self.controller.submit_data(
                self.table_name_combobox.currentText().strip(),
                self.material_name_field.text(),
                self.material_class_field.text(),
                self.trade_name_field.text(),
                self.material_property_field.text(),
                self.datatype_field.currentText(),
                self.value_field.text(),
                self.max_min_label.text()
            )
        except ValueError as e:
            errorbox = ErrorBox(str(e))
            errorbox.exec()


    def toggle_max_min(self):
        # Call the controller's toggle_max_min method
        self.controller.toggle_max_min(self.max_min_toggle.isChecked())

    def update_material_property_dropdown(self):
        # Update the material property dropdown
        column_names = self.controller.update_column_names(self.table_name_combobox.currentText(), self.material_property_field.text())

        
        # Clear the QComboBox
        self.material_property_dropdown.clear()

        # Add the column names to the QComboBox
        for column_name in column_names:
            self.material_property_dropdown.addItem(column_name)

    def undo_last_entry(self):
        # Call the controller's undo_last_entry method
        try:
            self.controller.undo()
        except Exception as e:
            errorbox = ErrorBox(str(e))
            errorbox.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = data_entry_window()
    window.show()

    sys.exit(app.exec())