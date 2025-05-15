import fitz

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
        file_path = self.controller.load_pdf()
        self.display_pdf(file_path)
        
    def display_pdf(self, file_path):
        try:
            print(f"Loading PDF from: {file_path}")
            doc = fitz.open(file_path)

            # Καθαρίζουμε το scroll area
            layout = self.ui.scrollAreaWidgetContents_4.layout()
            if layout is None:
                layout = QVBoxLayout(self.ui.scrollAreaWidgetContents_4)
            else:
                while layout.count():
                    child = layout.takeAt(0)
                    if child.widget():
                        child.widget().deleteLater()

            # Προσθέτουμε κάθε σελίδα
            for page_num in range(len(doc)):
                page = doc.load_page(page_num)
                pix = page.get_pixmap()
                image = QImage(pix.samples, pix.width, pix.height, pix.stride, QImage.Format.Format_RGB888)
                pixmap = QPixmap.fromImage(image)

                label = QLabel()
                label.setMinimumHeight(800)  # or any value you prefer

                label.setPixmap(pixmap)
                layout.addWidget(label)

        except Exception as e:
            print(f"Σφάλμα κατά τη φόρτωση PDF: {e}")
        
    def reportPost(self):
        self.controller.show_reportPost()
        
    def requestDownloadPost(self):
        self.controller.download_post()