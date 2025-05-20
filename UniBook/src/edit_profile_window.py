# edit_profile_window.py
from PySide6.QtWidgets import QMainWindow
from edit_profile_ui import Ui_MainWindow  # Adjust class name if it's different

class EditProfileWindow(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.rookieBut.clicked.connect(self.show_rookie)
        
        self.ui.seniorBut.clicked.connect(self.show_senior)
        
        self.ui.cancelBut.clicked.connect(self.cancel)

        self.ui.savechangesBut.clicked.connect(self.save_changes)

    def show_rookie(self):
        self.controller.show_rookie()
        
    def show_senior(self):
        self.controller.show_senior()
        
    def cancel(self):
        self.controller.cancel()

    def save_changes(self):
        self.controller.save_profile_changes()