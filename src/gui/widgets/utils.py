# src/gui/widgets/utils.py
from PyQt6.QtWidgets import QLabel, QVBoxLayout

def create_main_layout(title):
    # Create a main layout, currently only defining the title
    main_layout = QVBoxLayout()

    # Add a title label to the main layout
    title_label = QLabel(title)
    main_layout.addWidget(title_label)

    return main_layout
