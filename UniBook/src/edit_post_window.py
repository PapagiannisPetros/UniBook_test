from PySide6.QtWidgets import QMainWindow,QMessageBox
from edit_post_ui import Ui_MainWindow

class EditPostWindow(QMainWindow):
    def __init__(self, controller, post):
        super().__init__()
        self.controller = controller
        self.post = post
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_4.clicked.connect(lambda :self.deletePost(post))
        self.ui.pushButton_2.clicked.connect(lambda :self.checkFileTypeSize(post))

    def deletePost(self,post):
        if self.controller.queryDeletePost(post):
            self.displayDeleteConfirmationWindow(post)
            self.close() 

    def checkFileTypeSize(self,post):
        #if post.file_name.lower().endswith(".pdf"):
            self.permanentSave(post)
        #else:
            #displayFileErrorMessage(post)

    def permanentSave(self,post):
        example_title = self.ui.textEdit_2.toPlainText()
        example_description = self.ui.textEdit.toPlainText()
        if self.controller.saveEditPost(post,example_title,example_description):
             self.displayConfirmationWindow(post)
             self.close()

    def displayDeleteConfirmationWindow(self,post):
         QMessageBox.information(self, "Success", f"Post with PostID {post.post_id} deleted successfully!")

    def displayFileErrorMessage(self,post):
         QMessageBox.information(self, "Warning", f"Post with PostID {post.post_id} does not have a file in PDF form!")

    def displayConfirmationWindow(self,post):
         QMessageBox.information(self, "Success", f"Post with PostID {post.post_id} edited successfully!")