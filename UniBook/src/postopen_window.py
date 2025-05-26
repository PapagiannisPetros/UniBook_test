import fitz

from PySide6.QtWidgets import QMainWindow
from postopen_ui import Ui_MainWindow  # Adjust the import based on your UI file
from PySide6.QtWidgets import QFileDialog, QVBoxLayout, QLabel
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import Qt
from datetime import datetime
from PySide6.QtWidgets import QMessageBox

class PostOpenWindow(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.load_pdf()
        self.ui.widget_2.hide()
        
        self.ui.shareButton.clicked.connect(self.reportPost)
        
        self.ui.downloadButton.clicked.connect(self.requestDownloadPost)
        
        self.ui.commentButton.clicked.connect(self.show_commentWindow)
        
        self.ui.sendBut.clicked.connect(self.newComment)
        
    def newComment(self):
        comment_text = self.ui.chatInput.text()
        check = self.checkComment(comment_text)
        if check is not None:
            if comment_text:
                self.controller.querySaveComment(comment_text)
                self.ui.chatInput.clear()
            
    def displayErrorWindow(self):
        QMessageBox.warning(self, "Error Window", "Please enter a valid comment.")
    
    def checkComment(self, comment_text):
        if not comment_text.strip():
            QMessageBox.warning(self, "Warning", "Comment cannot be empty.")
            return
        
        if len(comment_text) > 100:
            self.displayErrorWindow()
            return
        return 1
            
    def display_comment(self, author, text):
        comment_display = self.ui.commentDisplay
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        comment_display.append(
            f"<b>{author}</b> ({current_time}):<br>{text}<br><br>"
        )
    
    def load_pdf(self):
        file_data = self.controller.load_pdf()
        self.display_pdf(file_data)

        
    def display_pdf(self, file_data: bytes):
        try:
            doc = fitz.open(stream=file_data, filetype="pdf")

            # Clear the scroll area layout
            layout = self.ui.scrollAreaWidgetContents_4.layout()
            if layout is None:
                layout = QVBoxLayout(self.ui.scrollAreaWidgetContents_4)
            else:
                while layout.count():
                    child = layout.takeAt(0)
                    if child.widget():
                        child.widget().deleteLater()

            # Add each page to the layout
            for page_num in range(len(doc)):
                page = doc.load_page(page_num)
                pix = page.get_pixmap()
                image = QImage(pix.samples, pix.width, pix.height, pix.stride, QImage.Format.Format_RGB888)
                pixmap = QPixmap.fromImage(image)

                label = QLabel()
                label.setPixmap(pixmap)
                label.setAlignment(Qt.AlignCenter)
                layout.addWidget(label)

        except Exception as e:
            print(f"Σφάλμα κατά τη φόρτωση PDF: {e}")

        
    def reportPost(self):
        self.controller.show_reportPost()
        
    def requestDownloadPost(self):
        self.controller.download_post()
        
    def show_commentWindow(self):
        self.controller.queryFetchComments()