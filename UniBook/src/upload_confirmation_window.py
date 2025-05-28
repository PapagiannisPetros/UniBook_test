from PySide6.QtWidgets import QMainWindow,QMessageBox
from upload_confirmation_ui import Ui_MainWindow  # Adjust the import based on your UI file

class UploadConfirmationWindow(QMainWindow):
    def __init__(self, controller ,post_id):
        super().__init__()
        self.controller = controller
        self.post_id = post_id
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_2.clicked.connect(lambda: self.approveUploadPost(post_id))
        self.ui.pushButton_4.clicked.connect(lambda: self.approveUploadPost(post_id))

    def approveUploadPost(self,post_id):
        if self.controller.queryApproveUploadPost(post_id):
            self.showConfirmationWindowUpload(post_id)
            self.close() 

    def showConfirmationWindowUpload(self,post_id):
        QMessageBox.information(self, "Success", f"Post with PostID {post_id} uploaded successfully!")

    #def displayCommentWindow(self):
