import fitz  # PyMuPDF

from PySide6.QtWidgets import (
    QApplication, QWidget, QFileDialog, QLabel, QVBoxLayout, QMainWindow
)
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFileDialog, QMessageBox
from PySide6.QtWidgets import QSizePolicy

from upload_ui import Ui_MainWindow  # Adjust as needed


class UploadWindow(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.pushButtonLoadPDF.clicked.connect(self.displayFilePreview)
        self.ui.pushButton_2.clicked.connect(self.uploadPost)
        self.ui.pushButton_3.clicked.connect(self.displayCancelWindow)
        print("Upload window initialized")
        
    def displayFilePreview(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Άνοιγμα PDF", "", "PDF Files (*.pdf)"
        )
        if file_path:
            if self.check_type(file_path):
                self.ui.textBrowser_3.setPlainText(file_path)
                self.display_pdf(file_path)
            else:
                QMessageBox.warning(self, "Error Window", "Παρακαλώ επιλέξτε ένα αρχείο PDF.")
        else:
            self.displayCancelWindow(self)
            
    def displayCancelWindow(self, parent):
        QMessageBox.information(self, "Cancel Window", "Action Canceled", QMessageBox.Ok)
        self.close()
           
    def check_type(self,file_path):
        # Check if the file is a PDF
        return file_path.lower().endswith('.pdf')
             
    def display_pdf(self, file_path):
        try:
            doc = fitz.open(file_path)

            layout = self.ui.scrollAreaWidgetContents_4.layout()
            if layout is None:
                layout = QVBoxLayout(self.ui.scrollAreaWidgetContents_4)
            else:
                while layout.count():
                    child = layout.takeAt(0)
                    if child.widget():
                        child.widget().deleteLater()

            for page_num in range(len(doc)):
                page = doc.load_page(page_num)
                pix = page.get_pixmap()
                image = QImage(pix.samples, pix.width, pix.height, pix.stride, QImage.Format.Format_RGB888)
                pixmap = QPixmap.fromImage(image)

                label = QLabel()
                label.setPixmap(pixmap)
                label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)

                layout.addWidget(label)

        except Exception as e:
            print(f"Error loading PDF: {e}")


    def uploadPost(self):
        # Get the post details from the UI
        title = self.ui.textEdit_2.toPlainText()
        description = self.ui.textEdit.toPlainText()
        file_name = self.ui.textBrowser_3.toPlainText()

        
            # Optional: Load the file data as bytes
        file_data = None
        if file_name:
            try:
                with open(file_name, "rb") as f:
                    file_data = f.read()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to read file:\n{str(e)}")
                return

        # Call the controller method
        self.controller.queryUploadPost(title, description, file_data, file_name)
        self.close()

