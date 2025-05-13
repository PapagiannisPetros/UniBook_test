from login_window import LoginWindow
from home_window import HomeWindow
from admin_home_window import AdminReportsWindow  
from profile_window import ProfileWindow
from rookie_window import RookieWindow
from senior_window import SeniorWindow
from payment_window import PaymentWindow
from edit_profile_window import EditProfileWindow
from upload_window import UploadWindow
from postopen_window import PostOpenWindow
from db_manager import DatabaseManager
from reportpost_window import ReportPostWindow

from PySide6.QtWidgets import QWidget, QLabel, QTextBrowser, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout, QSizePolicy
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QFont, QIcon

class Controller:
    def __init__(self):
        self.db = DatabaseManager()
        try:
            self.db.create_tables()
        except Exception as e:
            print(f"Error creating tables: {e}")
        self.db.insert_sample_data()

        self.login = LoginWindow(self)
        
        self.admin_home = AdminReportsWindow(self)
        self.upload = UploadWindow(self)

        self.login.ui.loginAdmBut.clicked.connect(self.show_admin_reports)
        
    def show_reportPost(self):
        self.report_open = ReportPostWindow(self)
        self.report_open.show()
        
    def _create_post_widget(self, post):
        post_widget = QWidget()
        post_widget.setMinimumSize(QSize(0, 0))
        post_widget.setMaximumSize(QSize(16777215, 200))
        post_widget.setStyleSheet("background-color: rgb(150, 150, 150);")

        horizontalLayout = QHBoxLayout(post_widget)
        horizontalLayout.setContentsMargins(0, 0, 0, 0)
        horizontalLayout.setSpacing(7)

        # Left side: Image (placeholder)
        image_container = QWidget(post_widget)
        image_layout = QVBoxLayout(image_container)
        image_layout.setContentsMargins(0, 0, 0, 0)
        post_image = QLabel(image_container)
        post_image.setMinimumSize(QSize(170, 100))
        post_image.setAlignment(Qt.AlignCenter)
        # You can set post_image.setPixmap(QPixmap(post.image_path)) if available
        post_image.setText("Image")
        image_layout.addWidget(post_image)
        horizontalLayout.addWidget(image_container, 0, Qt.AlignLeft)

        # Right side: Info
        info_container = QWidget(post_widget)
        info_layout = QVBoxLayout(info_container)
        info_layout.setContentsMargins(0, 0, 2, 0)

        top_info = QWidget(info_container)
        grid = QGridLayout(top_info)
        grid.setContentsMargins(0, 0, 0, -1)

        title_label = QLabel(post.title, top_info)
        title_label.setFont(QFont('', 10))
        grid.addWidget(title_label, 0, 0, 1, 2)

        date_label = QLabel(post.date, top_info)
        grid.addWidget(date_label, 1, 0, 1, 1)

        open_button = QPushButton(top_info)
        open_button.setIcon(QIcon(":/feather/icons/feather/arrow-right.png"))
        open_button.setAutoDefault(False)
        grid.addWidget(open_button, 0, 2, 1, 1)

        info_layout.addWidget(top_info, 0, Qt.AlignTop)

        bottom_info = QWidget(info_container)
        bottom_layout = QVBoxLayout(bottom_info)
        bottom_layout.setContentsMargins(0, 0, 2, 2)
        desc_browser = QTextBrowser(bottom_info)
        desc_browser.setText(post.description)
        bottom_layout.addWidget(desc_browser)
        info_layout.addWidget(bottom_info)
        
        # Connect button click to controller method
        open_button.clicked.connect(lambda _, pid=post.post_id: self.post_selected(pid))

        horizontalLayout.addWidget(info_container)

        return post_widget
    
    def post_selected(self, post_id):
        # Find the selected post from the cached posts
        post = next((p for p in self.posts_cache if p.post_id == post_id), None)

        if post:
            self.show_post_window(post)

    
    def show_post_window(self, post):
        self.post_open_window = PostOpenWindow(self)
        self.post_open_window.ui.post_title.setText(post.title)
        self.post_open_window.ui.post_date.setText(post.date)
        self.post_open_window.ui.post_text.setText(post.description)
        self.post_open_window.ui.likeButton.setText(str(post.likes))
        

        self.post_open_window.show()


    def show_login(self):
        #self.home.hide()
       # self.rookie.hide()
        self.admin_home.hide()
        self.login.show()
        
    def show_home(self):
        self.login.hide()
        self.queryFetchCourses()
        self.displayCourses()
        
    def queryFetchCourses(self):
        self.db.get_all_courses()
        self.courses_cache = self.db.get_all_courses()
    
    def displayCourses(self):
        self.home_window = HomeWindow(self, self.courses_cache)
        self.home_window.show()
        
    def course_selected(self, course_id):
        # Store selected course if needed
        self.selected_course_id = course_id
        self.display_posts_for_course(course_id)
        
    def display_posts_for_course(self, course_id):
        posts = self.db.get_posts_by_course(course_id)
        self.posts_cache = posts  # Cache the posts in the controller

        # Clear previous posts
        layout = self.home_window.ui.verticalLayout_7
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

        for post in posts:
            layout.addWidget(self._create_post_widget(post))

    def show_admin_reports(self):
        self.login.hide()
        self.admin_home.show()
        
    def show_rookie(self):
        #self.home.hide()
        self.rookie = RookieWindow(self)
        self.rookie.show()
        
    def show_senior(self):
        self.senior = SeniorWindow(self)
        self.senior.show()
        
    def show_profile(self):
        self.home.hide()
        self.profile = ProfileWindow(self)
        self.profile.show()
        
    def show_payment_rookie(self):
        self.rookie.hide()
        self.payment = PaymentWindow(self)
        self.payment.show()
        
    def show_payment_senior(self):
        self.senior.hide()
        self.payment = PaymentWindow(self)
        self.payment.show()

    def cancel(self):
        self.edit_profile.hide()
        self.profile.show()
        
    def show_edit_profile(self):
        self.edit_profile = EditProfileWindow(self)
        self.edit_profile.show()
    
    def show_upload(self):
        self.upload = UploadWindow(self)
        self.upload.show()
        
    def open_post(self):
        self.post_open = PostOpenWindow(self)
        self.post_open.show()
