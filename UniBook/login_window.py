from PySide6.QtWidgets import QMainWindow
from login_ui import Ui_MainWindow  # or whatever the main class is

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)