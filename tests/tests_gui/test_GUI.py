# \src\gui\tests\tests_gui\test_main_window.py

import unittest
from PyQt6.QtWidgets import QApplication
from PyQt6.QtTest import QTest
from PyQt6.QtCore import Qt
from gui.screens.main_window import MainWindow
from PyQt6.QtWidgets import QPushButton, QComboBox, QLineEdit

app = None  # Global QApplication instance

class MainWindowTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Initialize QApplication once for all tests."""
        global app
        app = QApplication.instance()
        if app is None:
            app = QApplication([])

    def setUp(self):
        """Set up method to prepare the test environment for each test."""
        # Pass the shared QApplication instance to MainWindow
        self.window = MainWindow(app)

    def tearDown(self):
        """Tear down method to clean up after each test."""
        self.window.close()

    def value_exists_in_table(self, value):
        # Helper function to check if a value exists in the table widget in the data entry window
        for i in range(self.window.main_window_controller.data_entry_window.table_widget.rowCount()):
            for j in range(self.window.main_window_controller.data_entry_window.table_widget.columnCount()):
                item = self.window.main_window_controller.data_entry_window.table_widget.item(i, j)
                if item is not None and item.text() == value:
                    return True

    def test_user_navigation(self):
        """
        Test the user navigation through the GUI.
        This test emulates a user clicking on the connect button, then the load data button, and so on.
        """

        # -------------------------
        # Testing Main Window
        # -------------------------

        # Emulate a user clicking on the connect button
        self.window.main_window_controller.toggle_connection()
        # Check if the status label is updated correctly
        self.assertEqual(self.window.status_label.text(), "Status: Connected")   

        # Check if the load data button is enabled
        self.assertTrue(self.window.load_data_button.isEnabled())
        # Emulate a user clicking on the load data button
        QTest.mouseClick(self.window.findChild(QPushButton, "Load_Data_Button"), Qt.MouseButton.LeftButton)
        # Check if the load data window is open
        self.assertTrue(self.window.main_window_controller.load_data_window.isVisible())
        # Emulate a user closing the load data window
        self.window.main_window_controller.load_data_window.close()
        # Check if the load data window is closed
        self.assertFalse(self.window.main_window_controller.load_data_window.isVisible())

        # Emulate a user clicking on the search button
        QTest.mouseClick(self.window.findChild(QPushButton, "Search_Button"), Qt.MouseButton.LeftButton)
        # Check if the search window is open
        self.assertTrue(self.window.main_window_controller.search_window.isVisible())

        # -------------------------
        # Testing Search Window
        # -------------------------

        # Emulate a user selecting "test_table" in the combo box
        combo_box = self.window.main_window_controller.search_window.findChild(QComboBox, "table_names_combo_box")


        # Check if the combo_box is not None
        
        if combo_box is not None:
            index = None
            #print(combo_box.count())
            # Iterate over the items in the combo_box
            for i in range(combo_box.count()):
                # Check if the item text contains "test_table"
                if "test_table" in combo_box.itemText(i):
                    # Set the index to the current iteration value
                    index = i
                    #print(combo_box.itemText(i))
                    break
            if index is None:
                # Fail the test if the index is not found
                self.fail("Could not find index of 'test_table' in combo box 'table_names_combo_box'")
                
            # ---- 
            #    Check later
            # Make sure the combobox has a different text in it, so the currentTextChanged signal is emitted, error handling for the case that test_table index is the last item in the combobox
            # combo_box.setCurrentIndex((index + 1) % combo_box.count())
            # ----
            # Set the combo_box's current index to 1 in case the index is the first item in the combo_box, as this does not trigger the currentTextChanged signal
            if index == 0:
                combo_box.setCurrentIndex(1)
          
            # Set the combo_box's current index to the found index
            combo_box.setCurrentIndex(index) 

            # Assert that the input field text is "test_table", it should change automatically upon currentTextChanged calling update_table_name in the search controller
            self.assertEqual(self.window.main_window_controller.search_window.findChild(QLineEdit, "table_input").text(), '"test_table"')
        else:
            # Fail the test if the combo_box is not found
            self.fail("Could not find combo box 'table_names_combo_box'")


        # Emulate a user closing the search window
        self.window.main_window_controller.search_window.close()
        # Check if the search window is closed
        self.assertFalse(self.window.main_window_controller.search_window.isVisible())

        # -------------------------
        # Testing Personal Workspace Window
        # -------------------------

        # Emulate a user clicking on the personal workspace button
        QTest.mouseClick(self.window.findChild(QPushButton, "Personal_Workspace_Button"), Qt.MouseButton.LeftButton)
        # Check if the personal workspace window is open
        self.assertTrue(self.window.main_window_controller.personal_workspace_window.isVisible())

        # Emulate a user clicking on the data entry button from the personal workspace window
        QTest.mouseClick(self.window.main_window_controller.personal_workspace_window.findChild(QPushButton, "Data_Entry_Button"), Qt.MouseButton.LeftButton)
        # Check if the data entry window is open
        self.assertTrue(self.window.main_window_controller.personal_workspace_window.workspace_controller.data_entry_window.isVisible())
        # Emulate a user closing the data entry window
        self.window.main_window_controller.personal_workspace_window.workspace_controller.data_entry_window.close()
        # Check if the data entry window is closed
        self.assertFalse(self.window.main_window_controller.personal_workspace_window.workspace_controller.data_entry_window.isVisible())


        # Emulate a user closing the personal workspace window
        self.window.main_window_controller.personal_workspace_window.close()
        # Check if the personal workspace window is closed
        self.assertFalse(self.window.main_window_controller.personal_workspace_window.isVisible())

        # -------------------------
        # Testing Data Entry Window
        # -------------------------

        TestEntryValues = {
            "table_name": "test_table",
            "material_name": "Test_Material",
            "material_class": "Test_Class",
            "trade_name": "Test_Trade Name",
            "material_property": "Test_Property min.",
            "value": "100"
        }


        # Emulate a user clicking on the data entry button from the main window
        QTest.mouseClick(self.window.findChild(QPushButton, "Data_Entry_Button"), Qt.MouseButton.LeftButton)
        # Check if the data entry window is open
        self.assertTrue(self.window.main_window_controller.data_entry_window.isVisible())

        # Emulate a user selecting a table name in the table_name_combo
        table_name_combo = self.window.main_window_controller.data_entry_window.findChild(QComboBox, "table_names_combobox")
        table_name_combo.setCurrentText(TestEntryValues["table_name"])
        self.assertEqual(table_name_combo.currentText(), TestEntryValues["table_name"])

        # Emulate a user entering text into the material_name_field
        material_name_field = self.window.main_window_controller.data_entry_window.findChild(QLineEdit, "material_name_field")

        QTest.keyClicks(material_name_field, TestEntryValues["material_name"])
        self.assertEqual(material_name_field.text(), TestEntryValues["material_name"])

        # Emulate a user entering text into the material_class_field
        material_class_field = self.window.main_window_controller.data_entry_window.findChild(QLineEdit, "material_class_field")
        QTest.keyClicks(material_class_field, TestEntryValues["material_class"])
        self.assertEqual(material_class_field.text(), TestEntryValues["material_class"])
     
        # Emulate a user entering text into the trade_name_field
        trade_name_field = self.window.main_window_controller.data_entry_window.findChild(QLineEdit, "trade_name_field")
        QTest.keyClicks(trade_name_field, TestEntryValues["trade_name"])
        self.assertEqual(trade_name_field.text(), TestEntryValues["trade_name"])
        
        # Emulate a user entering text into the material_property_field
        material_property_field = self.window.main_window_controller.data_entry_window.findChild(QLineEdit, "material_property_field")
        QTest.keyClicks(material_property_field, TestEntryValues["material_property"])
        self.assertEqual(material_property_field.text(), TestEntryValues["material_property"])
        
        # Emulate a user entering text into the value_field
        value_field = self.window.main_window_controller.data_entry_window.findChild(QLineEdit, "value_field")
        QTest.keyClicks(value_field, "100")
        self.assertEqual(value_field.text(), "100")
   
        # Emulate a user clicking on the max_min_toggle button
        max_min_toggle = self.window.main_window_controller.data_entry_window.findChild(QPushButton, "max_min_toggle")
        QTest.mouseClick(max_min_toggle, Qt.MouseButton.LeftButton)
        self.assertTrue(max_min_toggle.isChecked())

        # Emulate a user clicking on the submit button
        submit_button = self.window.main_window_controller.data_entry_window.findChild(QPushButton, "submit_button")
        QTest.mouseClick(submit_button, Qt.MouseButton.LeftButton)

        # Emulate the popupShown signal of the material_property_dropdown
        self.window.main_window_controller.data_entry_window.update_material_property_dropdown()

        # Emulate a user selecting a material property in the material_property_dropdown
        material_property_dropdown = self.window.main_window_controller.data_entry_window.findChild(QComboBox, "material_property_drowdown")
        material_property_dropdown.setCurrentText(TestEntryValues["material_property"])
        self.assertEqual(material_property_dropdown.currentText(), TestEntryValues["material_property"])
        # Assert that the material_property_field text is "Test_Property min."
        self.assertEqual(material_property_field.text(), TestEntryValues["material_property"])
        
        # Emulate a user clicking on the display table button
        display_table_button = self.window.main_window_controller.data_entry_window.findChild(QPushButton, "display_table_button")
        QTest.mouseClick(display_table_button, Qt.MouseButton.LeftButton)

        # Check if any cell in the table widget contains a value
        has_value = False
        for i in range(self.window.main_window_controller.data_entry_window.table_widget.rowCount()):
            for j in range(self.window.main_window_controller.data_entry_window.table_widget.columnCount()):
                if self.window.main_window_controller.data_entry_window.table_widget.item(i, j) is not None:
                    has_value = True
                    break
            if has_value:
                break
        self.assertTrue(has_value)

        # Emulate a user undoing the last entry
        undo_button = self.window.main_window_controller.data_entry_window.findChild(QPushButton, "undo_submit_button")
        QTest.mouseClick(undo_button, Qt.MouseButton.LeftButton)
        # Check if the last entry is undone
        self.assertEqual(self.window.main_window_controller.data_entry_window.controller.last_entry, None)

        # -- testing deletion --

        # Emulate a user clicking on the deletion toggle button    
        self.window.main_window_controller.data_entry_window.delete_toggle.click()
        
        # Check if the layout changed
        self.assertEqual(self.window.main_window_controller.data_entry_window.material_class_field.styleSheet(), "border: 1px solid red;")

        # Emulate a user clicking on the submit button again
        QTest.mouseClick(submit_button, Qt.MouseButton.LeftButton)

        # Emulate a user clicking on the display table button
        QTest.mouseClick(display_table_button, Qt.MouseButton.LeftButton)
        
        # Check if the value is in the table widget again
        has_value = False
        for i in range(self.window.main_window_controller.data_entry_window.table_widget.rowCount()):
            for j in range(self.window.main_window_controller.data_entry_window.table_widget.columnCount()):
                if self.window.main_window_controller.data_entry_window.table_widget.item(i, j) is not None:
                    if self.window.main_window_controller.data_entry_window.table_widget.item(i, j).text() == TestEntryValues["value"]:
                        has_value = True
                        break
            if has_value:
                break

        # Emulate a user clicking on the delete button
        delete_button = self.window.main_window_controller.data_entry_window.findChild(QPushButton, "delete_button")
        QTest.mouseClick(delete_button, Qt.MouseButton.LeftButton)

        # Check if the value is not in the table widget
        has_value = False
        for i in range(self.window.main_window_controller.data_entry_window.table_widget.rowCount()):
            for j in range(self.window.main_window_controller.data_entry_window.table_widget.columnCount()):
                if self.window.main_window_controller.data_entry_window.table_widget.item(i, j) is not None:
                    if self.window.main_window_controller.data_entry_window.table_widget.item(i, j).text() == TestEntryValues["value"]:
                        has_value = True
                        break
            if has_value:
                break


        # Emulate a user closing the data entry window
        self.window.main_window_controller.data_entry_window.close()
        # Check if the data entry window is closed
        self.assertFalse(self.window.main_window_controller.data_entry_window.isVisible())
  



        


if __name__ == '__main__':
    unittest.main()