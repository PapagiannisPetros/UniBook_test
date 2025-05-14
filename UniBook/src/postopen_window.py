from PySide6.QtWidgets import QMainWindow
from postopen_ui import Ui_MainWindow  # Adjust the import based on your UI file
from PySide6.QtWidgets import QFileDialog, QVBoxLayout, QLabel
from PySide6.QtGui import QPixmap, QImage

class PostOpenWindow(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.load_pdf()
        
        self.ui.shareButton.clicked.connect(self.reportPost)
        
        self.ui.downloadButton.clicked.connect(self.requestDownloadPost)
    
    def load_pdf(self):
        self.controller.load_pdf()
        
    def reportPost(self):
        self.controller.show_reportPost()
        
    def requestDownloadPost(self):
        self.controller.download_post()