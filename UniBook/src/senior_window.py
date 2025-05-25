from PySide6.QtWidgets import QMainWindow
from senior_ui import Ui_MainWindow  # Adjust the import based on your UI file


class SeniorWindow(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.continueBut.clicked.connect(self.show_payment_senior)
        self.ui.cancelBut.clicked.connect(self.close)

    def show_payment_senior(self):
        self.controller.show_payment("Senior")
