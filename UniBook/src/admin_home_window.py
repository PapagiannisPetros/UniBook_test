from PySide6.QtWidgets import QMainWindow,QPushButton
from PySide6.QtGui import QIcon, QFont
from PySide6.QtCore import QSize
from admin_home_ui import Ui_MainWindow  # Adjust the import based on your UI file

class AdminReportsWindow(QMainWindow):
    def __init__(self, controller, courses):
        super().__init__()
        self.controller = controller
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_3.clicked.connect(self.logout)
        #self.ui.reportBut.connect(self.add_course_buttons)

        self.add_course_buttons(courses)

    def logout(self):
        self.controller.show_login()
        self.close()

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
            button.clicked.connect(lambda _, cid=course_id: self.controller.course_selected(cid,2))

            self.ui.verticalLayout_37.addWidget(button)

    def displayPostInfo(self):
        self.controller.open_not_uploaded_post()