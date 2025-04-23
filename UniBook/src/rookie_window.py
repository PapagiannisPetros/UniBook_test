from PySide6.QtWidgets import QMainWindow
from rookie_ui import Ui_MainWindow  # Adjust the import based on your UI file

class RookieWindow(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.continueBut.clicked.connect(self.show_payment_rookie)
        
    def show_payment_rookie(self):
        self.controller.show_payment_rookie()