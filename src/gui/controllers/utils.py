# src\gui\controllers\utils.py


"""
Contains functions used by multiple windows.
"""

from gui.screens.data_entry_window import data_entry_window

def open_data_entry_window(app):
    """
    Opens the data entry window.

    This function creates a new instance of the data entry window and shows it.

    Parameters:
    app (QApplication): The application instance.

    Returns:
    data_entry_window_instance: The instance of the data entry window.
    """
    data_entry_window_instance = data_entry_window()
    data_entry_window_instance.show()
    return data_entry_window_instance