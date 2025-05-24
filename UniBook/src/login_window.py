from PySide6.QtWidgets import QMainWindow,QMessageBox
from login_ui import Ui_MainWindow  # or whatever the main class is

class LoginWindow(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.loginBut.clicked.connect(self.request_student_home)
        self.ui.loginAdmBut.clicked.connect(self.request_admin_home)
        
    def request_student_home(self):
        username = self.ui.usernameIn.text()
        password = self.ui.passwordIn.text()

        if self.controller.student_authentication(username, password):
            self.controller.show_home()
            self.close()
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid username or password for student login.")

    def request_admin_home(self):
        username = self.ui.usernameIn.text()
        password = self.ui.passwordIn.text()

        if self.controller.admin_authentication(username, password):
            self.controller.show_admin_window()
            QMessageBox.information(self," ","Admin Login Succesful!\n\nWelcome to UniBook, " + username)
            self.close()
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid username or password for admin login.")