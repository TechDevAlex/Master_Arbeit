# src\gui\screens\data_entry_window.py
from PyQt6.QtWidgets import QApplication, QLineEdit, QVBoxLayout, QWidget, QLabel, QPushButton, QComboBox
from src.database.data_insertion import add_single_entry_to_table, type_mapping_StringtoSQL
from src.database.data_retrieval import retrieve_table_names_from_database
import sys

class data_entry_window(QWidget):
    def __init__(self):
        super().__init__()

        # Create a QVBoxLayout to lay out the widgets
        layout = QVBoxLayout()

        # Create QLineEdit widgets for each input field
        self.material_name_field = QLineEdit()
        self.material_class_field = QLineEdit()
        self.trade_name_field = QLineEdit()  # New field for trade name
        self.material_property_field = QLineEdit()

        # Create a QComboBox for the datatype field
        self.datatype_field = QComboBox()

        # Add the datatypes to the QComboBox
        for datatype in type_mapping_StringtoSQL().keys():
            self.datatype_field.addItem(str(datatype))

        self.value_field = QLineEdit()

        # Create a QComboBox for the table names
        self.table_name_combo = QComboBox()

        # Get the table names and add them to the QComboBox
        table_names = retrieve_table_names_from_database()
        for table_name in table_names:
            table_name = table_name.strip('"')
            self.table_name_combo.addItem(table_name)

        # Add the QLineEdit widgets and QComboBox to the layout with labels
        layout.addWidget(QLabel("Table Name"))
        layout.addWidget(self.table_name_combo)

        layout.addWidget(QLabel("Material Name"))
        layout.addWidget(self.material_name_field)

        layout.addWidget(QLabel("Material Class"))
        layout.addWidget(self.material_class_field)

        layout.addWidget(QLabel("Trade Name")) 
        layout.addWidget(self.trade_name_field) 

        layout.addWidget(QLabel("Material Property"))
        layout.addWidget(self.material_property_field)

        layout.addWidget(QLabel("Data Type"))
        layout.addWidget(self.datatype_field)

        layout.addWidget(QLabel("Value"))
        layout.addWidget(self.value_field)

        # Create a QPushButton that will call add_single_entry_to_table when clicked
        submit_button = QPushButton("Submit")
        submit_button.clicked.connect(self.submit_data)
        layout.addWidget(submit_button)

        # Set the window's layout
        self.setLayout(layout)

    def submit_data(self):
        # Call add_single_entry_to_table with the values from the input fields
        print(self.table_name_combo.currentText())
        add_single_entry_to_table(
            self.table_name_combo.currentText().strip(),
            self.material_name_field.text(),
            self.material_class_field.text(),
            self.trade_name_field.text(), 
            self.material_property_field.text(),
            self.datatype_field.currentText(),
            self.value_field.text()
        )

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = data_entry_window()
    window.show()

    sys.exit(app.exec())