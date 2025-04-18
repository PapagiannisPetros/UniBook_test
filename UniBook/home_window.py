# home_window.py
from PySide6.QtWidgets import QMainWindow
from home_ui import Ui_MainWindow
from profile_window import ProfileWindow  # ⬅️ import it

class HomeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connect button
        self.ui.profileBut.clicked.connect(self.show_profile)

    def show_profile(self):
        self.profile = ProfileWindow()
        self.profile.show() 
