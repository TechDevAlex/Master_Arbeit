from database.data_retrieval import retrieve_data_from_database
from search.search_logic import search
from database.data_conversion import convert_table_to_dataframe
from PyQt6.QtWidgets import QTableWidgetItem, QMessageBox, QDialog

class SearchLogicController:
    def __init__(self, view):
        self.view = view
        
        # Connect signals for the Search Window inputs
        self.view.search_button.clicked.connect(self.perform_search)

    def perform_search(self):
        # Action when search button is clicked
        table_name = self.view.table_input.text()


        if not table_name:
            QMessageBox.warning(self.view, "Input Error", "Please enter a table name or a keyword.")
            return
        try:
            data = retrieve_data_from_database(table_name)
        except Exception as e:
            QMessageBox.warning(self.view, "Error", f"Error retrieving data: {e}")
            return
        data = retrieve_data_from_database(table_name)
        df = convert_table_to_dataframe(data)

        result = search(df)
        headers = result.loc[0,:].astype(str).tolist()
        
        
        #display the Result
        self.view.results_table.setRowCount(len(result))
        self.view.results_table.setColumnCount(len(result.columns))
        for i, row in enumerate(result.values):
            for j, item in enumerate(row):
                self.view.results_table.setItem(i, j, QTableWidgetItem(str(item)))

