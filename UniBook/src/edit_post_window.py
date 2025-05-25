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

    def deletePost(self,post):
        if self.controller.queryDeletePost(post):
            QMessageBox.information(self, "Success", f"Post with PostID {post.post_id} deleted successfully!")
            self.close() 



        