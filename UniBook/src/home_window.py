# home_window.py
from PySide6.QtWidgets import QMainWindow
from home_ui import Ui_MainWindow

class HomeWindow(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.profileBut.clicked.connect(self.show_profile)
        self.ui.logoutBut.clicked.connect(self.logout)
        
        # Initial chat message
        self.display_message("System", "Welcome to the chat!")

        # Connect the send button
        self.ui.sendBut.clicked.connect(self.send_message)
        
        self.ui.newBut.clicked.connect(self.upload_file)

    def show_profile(self):
        self.controller.show_profile()


    def logout(self):
        self.controller.show_login()
        self.close()

    def display_message(self, sender, message):
        formatted = f"<b>{sender}:</b> {message}<br>"
        self.ui.chatDisplay.append(formatted)

    def send_message(self):
        message = self.ui.chatInput.text()
        if message:
            self.display_message("You", message)
            self.ui.chatInput.clear()
            
    def upload_file(self):
        self.controller.show_upload()
