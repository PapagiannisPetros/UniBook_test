# edit_profile_window.py
from PySide6.QtWidgets import QMainWindow
from edit_profile_ui import Ui_MainWindow  # Adjust class name if it's different

class EditProfileWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

