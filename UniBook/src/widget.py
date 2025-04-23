# widget.py
from PySide6.QtWidgets import QScrollArea

class Widget(QScrollArea):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Add custom behavior if needed
