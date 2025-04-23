from PySide6.QtWidgets import QMainWindow
from payment_ui import Ui_MainWindow  # Adjust the import based on your UI file

class PaymentWindow(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)