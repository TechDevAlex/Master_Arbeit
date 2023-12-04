# src/gui/controllers/load_data_controller.py
import os
from PyQt6.QtWidgets import QMessageBox
from src.data_insertion import create_table_from_csv
from src.data_conversion import convert_database_to_dataframe

class LoadDataController:
    def __init__(self, view, file_dialog):
        self.view = view
        self.file_dialog = file_dialog

        # Connect signals for the Load Data Window widgets
        self.view.load_data_button.clicked.connect(self.load_data)
        self.view.browse_button.clicked.connect(self.browse_csv_file)
        self.view.load_sample_button.clicked.connect(self.load_sample_data)

    def load_data(self):
        # Action when "Load Data" button is clicked
        csv_filepath = self.view.csv_filepath_input.text()
        table_name = self.view.table_name_input.text()
        print(f"Loading data from CSV file: {csv_filepath}") 
        create_table_from_csv(csv_filepath,table_name)
        QMessageBox.information(self.view, "Create Table", f"Table {table_name} created successfully from {csv_filepath}")

    def browse_csv_file(self):
        # Action when "Browse" button is clicked
        file_path, _ = self.file_dialog.getOpenFileName(self.view, "Select CSV File", "", "CSV Files (*.csv);;All Files (*)")
        if file_path:
            self.view.csv_filepath_input.setText(file_path)

    def load_sample_data(self):
        # path of sample data
       csv_filepath = os.path.join(os.path.dirname(__file__),r'..\\..\\..\\init_scripts\sample_data.csv')
       normalized_path = os.path.normpath(csv_filepath)
       create_table_from_csv(normalized_path,'test_data')
       QMessageBox.information(self.view, "Load Sample Data", "Sample data loaded successfully!")

    def update_dataframe(self):
        # action when "update Dataframe" button is clicked
        convert_database_to_dataframe()
        QMessageBox.information(self.view, "Update Dataframe", "Dataframe updated succesfully!")