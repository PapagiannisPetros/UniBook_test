from PySide6.QtWidgets import QMainWindow,QMessageBox,QInputDialog
from upload_confirmation_ui import Ui_MainWindow  # Adjust the import based on your UI file

class UploadConfirmationWindow(QMainWindow):
    def __init__(self, controller ,post_id):
        super().__init__()
        self.controller = controller
        self.post_id = post_id
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_2.clicked.connect(lambda: self.approveUploadPost(post_id))
        self.ui.pushButton_4.clicked.connect(lambda: self.displayCommentWindow(post_id))
        self.ui.pushButton_3.clicked.connect(lambda: self.closeWindow())

    def closeWindow(self):
        self.close()
    
    def approveUploadPost(self,post_id):
        if self.controller.queryApproveUploadPost(post_id):
            self.showConfirmationWindowUpload(post_id)
            self.close() 

    def showConfirmationWindowUpload(self,post_id):
        QMessageBox.information(self, "Success", f"Post with PostID {post_id} uploaded successfully!")

    def displayCommentWindow(self,post_id):
        text, ok = QInputDialog.getText(None, "Post Comment", "Enter your comment:")
        if ok:
            print(f"The comment: {text}")
            self.rejectPost(post_id)

    def rejectPost(self,post_id):
        if self.controller.queryRejectPost(post_id):
            self.showRejectionWindow(post_id)

    def showRejectionWindow(self,post_id):
        QMessageBox.information(self, "Post Rejected for Upload", f"Post with PostID {post_id} got rejected!")
