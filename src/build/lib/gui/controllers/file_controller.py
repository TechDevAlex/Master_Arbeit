# src/gui/controllers/button_controller.py

from src.gui.utils.gui_utils import show_info_dialog


class ButtonController:
    def handle_button_click(self):
        show_info_dialog("Button Clicked", "The button was clicked!")
