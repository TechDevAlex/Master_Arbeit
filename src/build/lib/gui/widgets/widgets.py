# src/gui/widgets.py
from PyQt6.QtWidgets import QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout


def label(text):
    return QLabel(text)

def small_button(text):
    button = QPushButton(text)
    button.setFixedSize(100, 30)
    return button

def data_button(text):
    button = QPushButton(text)
    button.setStyleSheet("background-color: lightgray;") 
    return button

from PyQt6.QtWidgets import QLabel, QLineEdit, QPushButton

# src/gui/widgets.py
from PyQt6.QtWidgets import QLabel, QLineEdit, QPushButton

def load_data_window_widgets():
    label = QLabel("Load Data Window")
    load_sample_button = QPushButton("Load Sample Data")
    csv_filepath_label = QLabel("CSV File Path:")
    csv_filepath_input = QLineEdit()
    browse_button = QPushButton("Browse")
    load_data_button = QPushButton("Load Data")

    return label, load_sample_button, csv_filepath_label, csv_filepath_input, browse_button, load_data_button

def connect_load_data_signals(load_sample_button, browse_button, load_data_button, load_sample_data_func, browse_csv_file_func, load_data_func):
    # Connect signals for the Load Data Window widgets
    load_sample_button.clicked.connect(load_sample_data_func)
    browse_button.clicked.connect(browse_csv_file_func)
    load_data_button.clicked.connect(load_data_func)
