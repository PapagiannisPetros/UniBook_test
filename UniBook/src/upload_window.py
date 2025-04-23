import fitz  # PyMuPDF

from PySide6.QtWidgets import (
    QApplication, QWidget, QFileDialog, QLabel, QVBoxLayout, QMainWindow
)
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import Qt

from upload_ui import Ui_MainWindow  # Adjust as needed


class UploadWindow(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.pushButtonLoadPDF.clicked.connect(self.load_pdf)
        
    def load_pdf(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Άνοιγμα PDF", "", "PDF Files (*.pdf)"
        )
        if file_path:
            self.display_pdf(file_path)
            
    def display_pdf(self, file_path):
        try:
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

