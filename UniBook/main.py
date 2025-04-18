import sys
from PySide6.QtWidgets import QApplication
from login_window import LoginWindow
from home_window import HomeWindow


class Controller:
    def __init__(self):
        self.login = LoginWindow()
        self.home = None

        # Connect login button to handler
        self.login.ui.loginBut.clicked.connect(self.show_home)

    def show_login(self):
        self.login.show()

    def show_home(self):
        self.home = HomeWindow()
        self.login.close()  # or self.login.hide()
        self.home.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = Controller()
    controller.show_login()
    sys.exit(app.exec())
