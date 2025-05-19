# home_window.py
from PySide6.QtWidgets import QMainWindow
from home_ui import Ui_MainWindow
from PySide6.QtWidgets import QPushButton
from PySide6.QtGui import QIcon, QFont
from PySide6.QtCore import QSize
from PySide6.QtWidgets import QMessageBox


class HomeWindow(QMainWindow):
    def __init__(self, controller, courses):
        super().__init__()
        self.controller = controller
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.profileBut.clicked.connect(self.show_profile)
        self.ui.logoutBut.clicked.connect(self.logout)
        self.ui.sendBut.clicked.connect(self.send_message)
        self.ui.newBut.clicked.connect(self.upload_file)

        self.display_message("System", "Welcome to the chat!")
        self.add_course_buttons(courses)
        
        self.ui.rightMenu.hide()
        self.ui.lessonsBut.clicked.connect(self.requestDisplayChatWindow)
        
        
        
    def add_course_buttons(self, courses):
        for course in courses:
            course_id = course.course_id  # Accessing attribute directly
            course_name = course.course_name

            button = QPushButton(course_name, self.ui.scrollAreaWidgetContents_2)
            button.setMinimumSize(QSize(0, 45))
            button.setMaximumSize(QSize(500, 45))
            font = QFont()
            font.setPointSize(9)
            button.setFont(font)
            button.setStyleSheet("background-color: rgb(5, 87, 85); text-align: left; padding-left: 5px;")
            icon = QIcon(":/feather/icons/feather/book-open.png")
            button.setIcon(icon)
            button.setIconSize(QSize(20, 20))

            # Connect button click to controller method
            button.clicked.connect(lambda _, cid=course_id: self.controller.course_selected(cid,1))

            self.ui.verticalLayout_37.addWidget(button)
    
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
            self.handleNewMessage(message)
            self.display_message("You", message)
            self.ui.chatInput.clear()
    
    def handleNewMessage(self, message):
        self.controller.querySaveMessage(message)
            
    def upload_file(self):
        self.controller.show_upload()
        
    def post_open(self):
        self.controller.open_post()
        
    def requestDisplayChatWindow(self):
        self.controller.queryFetchChat(self.controller.selected_course_id)