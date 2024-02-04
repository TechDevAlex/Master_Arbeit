# src/gui/controllers/load_data_controller.py
import os
from PyQt6.QtWidgets import QMessageBox
from database.data_insertion import create_table_from_csv
from database.data_conversion import convert_database_to_dataframe
from PyQt6.QtCore import QAbstractListModel
from PyQt6.QtWidgets import QMessageBox, QDialog

class LoadDataController (QAbstractListModel):
    def __init__(self, view, file_dialog, csv_filepath = None, table_name = None):

        self.table_names = []

        super().__init__()
        self.view = view
        self.file_dialog = file_dialog
        self.csv_filepath = csv_filepath
        self.table_name = table_name


        # Connect signals for the Load Data Window widgets
        self.view.load_data_button.clicked.connect(self.load_data)
        self.view.browse_button.clicked.connect(self.browse_csv_file)
        self.view.load_sample_button.clicked.connect(self.load_sample_data)

         # If a CSV file path is provided, load the data automatically
        if self.csv_filepath:
            self.view.csv_filepath_input.setText(self.csv_filepath)
            self.load_data()

    def load_data(self):

        # Action when "Load Data" button git is clicked
        csv_filepath = self.view.csv_filepath_input.text()
        table_name = self.view.table_name_input.text()
        #print(f"Loading data from CSV file: {csv_filepath}") 
        create_table_from_csv(csv_filepath,table_name)
        QMessageBox.information(self.view, "Create Table", f"Table {table_name} created successfully from {csv_filepath}")

        # Store table names in list
        self.table_names.append(table_name)

        print(self.table_names)
    

    def browse_csv_file(self):
        # Action when "Browse" button is clicked
        file_path, _ = self.file_dialog.getOpenFileName(self.view, "Select CSV File", "", "CSV Files (*.csv);;All Files (*)")
        if file_path:
            self.view.csv_filepath_input.setText(file_path)

    def load_sample_data(self):
        # path of sample data
       current_dir = os.path.dirname(os.path.abspath(__file__))
       csv_filepath = os.path.join(current_dir, '..', '..', '..', 'data', 'Sample_Simple_1.csv')
       create_table_from_csv(csv_filepath,'test_data')
       QMessageBox.information(self.view, "Load Sample Data", "Sample data loaded successfully!")

    def update_dataframe(self):
        # action when "update Dataframe" button is clicked
        convert_database_to_dataframe()
        QMessageBox.information(self.view, "Update Dataframe", "Dataframe updated succesfully!")
