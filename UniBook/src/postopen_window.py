from PySide6.QtWidgets import QMainWindow
from postopen_ui import Ui_MainWindow  # Adjust the import based on your UI file

class PostOpenWindow(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.shareButton.clicked.connect(self.reportPost)
        
    def reportPost(self):
        self.controller.show_reportPost()