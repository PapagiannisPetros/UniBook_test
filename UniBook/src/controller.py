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
from report_check_window import ReportCheckWindow
from datetime import datetime
from models import Message
from models import Report
from models import Comment
from upload_confirmation_window import UploadConfirmationWindow

from PySide6.QtWidgets import QWidget, QLabel, QTextBrowser, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout, QSizePolicy
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QFont, QIcon
from PySide6.QtWidgets import QFileDialog, QMessageBox
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import QSize, QRect

class Controller:
    def __init__(self):
        self.db = DatabaseManager()
        try:
            self.db.create_tables()
        except Exception as e:
            print(f"Error creating tables: {e}")
        self.db.insert_sample_data()
        
        self.selected_course_id =  None
        self.chat_id = None
        self.current_profile = None
        self.penalty = None

        self.login = LoginWindow(self)
        
        self.comments_cache = {}
        
    def display_comment(self, author, text, timestamp):
        comment_display = self.post_open_window.ui.chatDisplay
        comment_display.append(f"<b>{author}</b> ({timestamp}):<br>{text}<br><br>")
        
    def saveComment(self, comment_text):
        
        from datetime import datetime
        post_id = self.current_post.post_id
        self.student_id = self.db.student.student_id
        send_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Create Comment object
        comment = Comment(
            comment_id=None,  # Let DB assign it
            post_id=post_id,
            student_id=student_id,
            comment_text=comment_text,
            upload_time=send_time
        )

        # Cache it
        if post_id not in self.comments_cache:
            self.comments_cache[post_id] = []
        self.comments_cache[post_id].append(comment)

        # Save to DB
        self.db.insert_comment(comment.post_id, comment.student_id, comment.comment_text, comment.upload_time)
        
        
        self.display_comment("You", comment_text, send_time)
    
    def queryFetchComments(self):
    
        comments = self.db.get_comments_by_post_id(self.current_post.post_id)
        self.comments_cache[self.current_post.post_id] = comments
        self.displayComments(comments)
            
    def displayComments(self, comments):
        if self.post_open_window.ui.widget_2.isVisible():
            self.post_open_window.ui.widget_2.hide()
        else:
            comment_display = self.post_open_window.ui.chatDisplay
            comment_display.clear()

            for comment in comments:
                time_str = comment.upload_time  # Format if needed
                comment_display.append(
                    f"<b>Student {comment.student_id}</b> ({time_str}):<br>{comment.comment_text}<br><br>"
                )

            self.post_open_window.ui.widget_2.show()
            
        
    def querySaveMessage(self, message_text):

        message = Message(
            message_id=None,
            chat_id=self.chat_id,
            student_id=self.db.student.student_id,
            message_text=message_text,
            send_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )

        self.db.insert_message(message)
        self.displaySuccessWindow(self)
        
    def displaySuccessWindow(self):
        QMessageBox.information(None, "Success", "Message sent successfully.")
        
    def queryFetchChat(self, course_id):
        if self.selected_course_id is None:
            QMessageBox.warning(None, "Error", "No course selected.")
            return
        chat = self.db.get_or_create_chat_by_course_id(course_id)
        self.chat_id = chat.chat_id
        messages = self.db.get_messages_by_chat_id(chat.chat_id)
        self.displayChatWindow(chat, messages)
        
    def displayChatWindow(self, chat, messages):
        if self.home_window.ui.rightMenu.isVisible():
            self.home_window.ui.rightMenu.hide()
        else:
            chat_screen = self.home_window.ui.chatDisplay 
            chat_screen.clear()

            for message in messages:
                time_str = message.send_time  # or format it with datetime
                chat_screen.append(f"<b>Student {message.student_id}</b> ({time_str}):<br>{message.message_text}<br><br>")

            self.home_window.ui.rightMenu.show()
            
    def load_pdf(self):
        print("")
        return self.current_post.post_file  # assuming it's already in memory

        
    def queryUploadPost(self, title, description, file_data, file_name):
        from datetime import datetime
        post_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        print("!!!!!!!! file_name: ", file_name)
        
        if self.selected_course_id is None:
            QMessageBox.warning(None, "Error", "No course selected.")
            return
        course_id = self.selected_course_id
        student_id = self.db.student.student_id # Assuming student_id is 1 for now, you might want to change this based on your logic #TODO 

        self.db.create_post(course_id, student_id, title, description, post_time, 0, 0, file_data, file_name)

        QMessageBox.information(self.home_window, "Success", "Post uploaded successfully.")
        
    def download_post(self):
        self.checkSubscription()
    
        file_data = self.current_post.post_file
        file_name = self.current_post.file_name
        print (f"File name: {file_name}")
        if file_data:
            self.displaySelectFolderWindow(f"{file_name}.pdf", file_data)
        else:
            QMessageBox.warning(self.home_window, "Error", "Subscription not found.")
            
    def displaySelectFolderWindow(self, filename, filedata):
        file_path, _ = QFileDialog.getSaveFileName(
            parent=self.home_window,  # or another QWidget like self.main_window
            caption="Save PDF",
            dir=filename,
            filter="PDF Files (*.pdf)"
        )

        print(f"Selected file path: {file_path}")
        if file_path:
            try:
                with open(file_path, "wb") as f:
                    f.write(filedata)
                QMessageBox.information(self.home_window, "Success", f"Downloaded to:\n{file_path}")
            except Exception as e:
                QMessageBox.critical(self.home_window, "Error", f"Failed to save file:\n{str(e)}")
        else:
            print("User canceled the save dialog.") 
            
    def checkSubscription(self):
        subscription_type = self.db.get_subscription_type_by_student_id(self.current_post.student_id)
        print(f"Subscription type: {subscription_type}")
        if not subscription_type:
            QMessageBox.warning(self.home_window, "Error", "Subscription not found.")
            return

        if subscription_type.lower() not in ['rookie', 'premium']:
            QMessageBox.warning(self.home_window, "Error", f"Invalid subscription type: {subscription_type}")
            return
        return subscription_type

    def dIsplayCancelWIndow(self):
        QMessageBox.information(self.post_open_window, "Cancelled", "You have cancelled the report submission.")
    
    def querySaveReport(self, report_type, report_time):
        
         # Create the Report object
        report = Report(
            report_id=None,  # Assuming it's auto-incremented in DB
            post_id=self.current_post.post_id,
            reporter_id=1,  # Replace with actual student/user ID
            report_type=report_type,
            status='Not Checked',
            report_time=report_time
        )
        self.student_reports_cache = report
        
        # Save the report details to the database
        self.db.save_report(self.current_post.post_id, self.db.student.student_id, report_type, 'Not Checked',report_time)
        QMessageBox.information(self.home_window, "Success", "Report submitted successfully.")
        
    def show_reportPost(self):
        if self.queryStudentValidation():
            
           self.displayReportWindow()
        else:
            QMessageBox.warning(self.home_window, "Error", "You cannot report posts as your account is not validated.")
    
    def displayReportWindow(self):
        self.report_post_window = ReportPostWindow(self)
        self.report_post_window.ui.post_title.setText(self.current_post.title)
        self.report_post_window.ui.post_time.setText(self.current_post.date)
        self.report_post_window.ui.post_text.setText(self.current_post.description)
            
        self.report_post_window.show()
        
            
    def queryStudentValidation(self):
        # Check if the student is validated
        if self.db.student.validation_status == 1:
            QMessageBox.warning(self.home_window, "Error", "Your account is not validated. Please contact an admin.")
            return False
        return True
        
    def _create_post_widget(self, post, is_uploaded=True):
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
        if is_uploaded:
            open_button.clicked.connect(lambda _, pid=post.post_id: self.post_selected(pid))
        else:
            open_button.clicked.connect(lambda _, pid=post.post_id: self.nu_post_selected(pid))

        horizontalLayout.addWidget(info_container)

        return post_widget
    
    def create_report_widget(self, report, is_checked=True):
        # Retrieve the related post using the post_id in the report
        post = self.db.get_post_by_id(report.post_id)

        report_widget = QWidget()
        report_widget.setMinimumSize(QSize(0, 0))
        report_widget.setMaximumSize(QSize(16777215, 200))
        report_widget.setStyleSheet("background-color: rgb(200, 100, 100);")

        horizontalLayout = QHBoxLayout(report_widget)
        horizontalLayout.setContentsMargins(0, 0, 0, 0)
        horizontalLayout.setSpacing(7)

        # Left side: Image placeholder
        image_container = QWidget(report_widget)
        image_layout = QVBoxLayout(image_container)
        image_layout.setContentsMargins(0, 0, 0, 0)
        post_image = QLabel(image_container)
        post_image.setMinimumSize(QSize(170, 100))
        post_image.setAlignment(Qt.AlignCenter)
        post_image.setText("Image")
        image_layout.addWidget(post_image)
        horizontalLayout.addWidget(image_container, 0, Qt.AlignLeft)

        # Right side: Info
        info_container = QWidget(report_widget)
        info_layout = QVBoxLayout(info_container)
        info_layout.setContentsMargins(0, 0, 2, 0)

        top_info = QWidget(info_container)
        grid = QGridLayout(top_info)
        grid.setContentsMargins(0, 0, 0, -1)

        title_label = QLabel(f"Report: {report.report_type} | Post: {post.title}", top_info)
        title_label.setFont(QFont('', 10))
        grid.addWidget(title_label, 0, 0, 1, 2)

        date_label = QLabel(f"Reported on: {report.report_time}", top_info)
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
        desc_browser.setText(f"{post.description}\n\nStatus: {report.status}")
        bottom_layout.addWidget(desc_browser)

        info_layout.addWidget(bottom_info)

        # Connect open button to the appropriate handler
        if  not is_checked:
            open_button.clicked.connect(lambda _, rid=report.report_id: self.report_selected(rid))
    

        horizontalLayout.addWidget(info_container)

        return report_widget
    
    def post_selected(self, post_id):
        # Find the selected post from the cached posts
        post = next((p for p in self.posts_cache if p.post_id == post_id), None)
        self.current_post=post

        if post:
            self.show_post_window(post)

    def nu_post_selected(self, post_id):
        # Find the selected non-uploaded post
        post = next((p for p in self.nu_posts_cache if p.post_id == post_id), None)

        if post:
            self.current_post = post
            self.show_upload_confirmation(post)

    def report_selected(self,report_id):
        report = next((p for p in self.reports_cache if p.report_id == report_id), None)

        if report:
            self.current_report = report
            self.show_report_check_window(report)

    
    def show_post_window(self, post):
        self.current_post = post
        self.post_open_window = PostOpenWindow(self)
        self.post_open_window.ui.post_title.setText(post.title)
        self.post_open_window.ui.post_date.setText(post.date)
        self.post_open_window.ui.post_text.setText(post.description)
        self.post_open_window.ui.likeButton.setText(str(post.likes))

        self.post_open_window.show()

    def show_upload_confirmation(self, post):
        self.nu_post_open = UploadConfirmationWindow(self, post.post_id)
        self.nu_post_open.ui.textBrowser_2.setText(post.title)
        self.nu_post_open.ui.textBrowser.setText(post.description)
        
        self.nu_post_open.show()

    def show_report_check_window(self,report):
        post = self.db.get_post_by_id(report.post_id)

        self.report_open = ReportCheckWindow(self,report.report_id)
        self.report_open.ui.textBrowser_2.setText(post.title)
        self.report_open.ui.textBrowser.setText(post.description)
        self.report_open.ui.textBrowser_3.setText(str(post.post_file))
        self.report_open.ui.textBrowserUsername.setText(self.db.getPostUsername(post.post_id))
        self.report_open.ui.textBrowser_6.setText(str(post.date))
        self.report_open.ui.textBrowser_7.setText(report.report_type)
        self.penalty = self.report_open.ui.textEdit_9.toPlainText()

        self.report_open.show()

    def show_login(self):
        #self.home.hide()
       # self.rookie.hide()
        #self.admin_home.hide()
        self.login.show()
        
    def show_home(self):
        self.login.hide()
        self.queryFetchCourses()
        self.displayCourses()

    def show_admin_window(self):
        self.login.hide()
        self.queryFetchCourses()
        self.admin_window = AdminReportsWindow(self, self.courses_cache)
        self.admin_window.show()
        
    def queryFetchCourses(self):
        self.db.get_all_courses()
        self.courses_cache = self.db.get_all_courses()
    
    def displayCourses(self):
        self.home_window = HomeWindow(self, self.courses_cache)
        self.home_window.show()
        
    def course_selected(self, course_id, window):
        # Store selected course if needed
        self.selected_course_id = course_id

        if(window==1):
            self.queryFetchPosts(course_id)
        elif(window==2):
            self.display_not_uploaded_posts_for_course(course_id)
        
    def queryFetchPosts(self, course_id):
        posts = self.db.get_posts_by_course(course_id)
        self.posts_cache = posts  # Cache the posts in the controller
        
        # Clear previous posts
        layout = self.home_window.ui.verticalLayout_7 # POST WALL
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

        for post in posts:
            layout.addWidget(self._create_post_widget(post))

    def display_not_uploaded_posts_for_course(self, course_id):
        nu_posts = self.db.get_not_uploaded_posts_by_course(course_id)
        self.nu_posts_cache = nu_posts  # Cache the posts in the controller
        
        # Clear previous posts
        layout = self.admin_window.ui.verticalLayout_8
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
        if widget:                    
            widget.deleteLater()

        for post in nu_posts:
            layout.addWidget(self._create_post_widget(post,is_uploaded = False))

    def display_reports(self):
        reports = self.db.getReports()

        if not reports:
            QMessageBox.information(None," ","No reports to check!")
        else:
            self.reports_cache = reports

            layout = self.admin_window.ui.verticalLayout_8
            for report in reports:
                layout.addWidget(self.create_report_widget(report,is_checked = False))
        
    def show_rookie(self):
        #self.home.hide()
        self.rookie = RookieWindow(self)
        self.rookie.show()
        
    def show_senior(self):
        self.senior = SeniorWindow(self)
        self.senior.show()

    def show_profile(self):
        self.home_window.hide()
        profile = self.db.query_fetch_profile()
        self.students_posts = self.db.get_students_posts_by_student_id(self.db.student.student_id)
        if profile:
            self.current_profile = profile
            self.display_profile(profile)
            self.displayStudentPosts()
            self.profile.show()
        else:
            QMessageBox.warning(None, "Error", "No profile information found.")

    def displayStudentPosts(self):
        layout = self.profile.ui.scrollAreaWidgetContents_3.layout()
        
        # Clear existing posts
        if layout is None:
            layout = QVBoxLayout(self.home_window.ui.scrollAreaWidgetContents_3)
        else:
            while layout.count():
                child = layout.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()

        for post in self.students_posts:
            post_widget = QWidget()
            post_widget.setMinimumSize(QSize(450, 140))
            post_widget.setMaximumSize(QSize(300, 125))
            post_widget.setStyleSheet("background-color: rgb(150, 150, 150);")

            # Post Image
            postimg = QLabel(post_widget)
            postimg.setGeometry(QRect(0, 0, 61, 141))
            postimg.setMinimumSize(QSize(0, 125))
            postimg.setPixmap(QPixmap(":/img/default_post.png"))  # Provide a default image path or load dynamically
            postimg.setScaledContents(True)

            # Title
            title_label = QLabel(post_widget)
            title_label.setGeometry(QRect(70, 0, 351, 41))
            title_label.setStyleSheet("color: rgb(0, 0, 0);")
            title_label.setText(post.title)

            # Author Label
            date_label = QLabel(post_widget)
            date_label.setGeometry(QRect(70, 30, 71, 17))
            date_label.setText(f" {post.date}")

            # Description
            text_browser = QTextBrowser(post_widget)
            text_browser.setGeometry(QRect(70, 50, 371, 81))
            text_browser.setText(post.description)

            # View Button
            view_button = QPushButton(post_widget)
            view_button.setGeometry(QRect(420, 0, 28, 24))
            icon = QIcon(":/feather/icons/feather/arrow-right.png")
            view_button.setIcon(icon)
            view_button.setAutoDefault(False)
            view_button.clicked.connect(lambda _, p=post: self.show_post_window(p))

            # Comment Button
            comment_button = QPushButton(post_widget)
            comment_button.setGeometry(QRect(370, 20, 80, 25))
            comment_button.setText("Edit")
            comment_button.clicked.connect(lambda _, p=post: self.handleCommentPost(p))

            layout.addWidget(post_widget)


    def display_profile(self, profile):
        self.profile = ProfileWindow(self)
        self.profile.ui.label_5.setText(f"<b>{profile.name}</b><br>@{profile.am}")
        self.profile.ui.label_7.setText(profile.gender)
        self.profile.ui.label_8.setText(f"Born {profile.birth_date}")
        self.profile.ui.label_9.setText(profile.address)
        self.profile.ui.label_10.setText(self.db.student.university)
        self.profile.ui.label_11.setText(str(profile.tel_num))
        self.profile.ui.label_12.setText(profile.email)

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
        if not self.current_profile:
            QMessageBox.warning(None, "Error", "Profile information is unavailable.")
            return

        profile = self.current_profile
        self.edit_profile = EditProfileWindow(self)

        name_parts = profile.name.split()
        first_name = name_parts[0] if len(name_parts) > 0 else ""
        last_name = name_parts[1] if len(name_parts) > 1 else ""

        self.edit_profile.ui.lineEdit.setText(first_name)
        self.edit_profile.ui.lineEdit_2.setText(last_name)
        self.edit_profile.ui.lineEdit_3.setText(str(profile.tel_num))
        self.edit_profile.ui.lineEdit_4.setText(profile.birth_date)
        self.edit_profile.ui.lineEdit_5.setText(profile.email)
        self.edit_profile.ui.lineEdit_6.setText(profile.address)

        self.edit_profile.ui.label_5.setText(f"<b>{profile.name}</b><br>@{profile.am}")
        self.edit_profile.ui.label_7.setText(str(profile.gender))
        self.edit_profile.ui.label_8.setText(f"Born {profile.birth_date}")
        self.edit_profile.ui.label_10.setText(str(profile.address))
        self.edit_profile.ui.label_11.setText(str(profile.tel_num))
        self.edit_profile.ui.label_12.setText(str(profile.email))

        self.edit_profile.show()

    def save_profile_changes(self):
        first_name = self.edit_profile.ui.lineEdit.text()
        last_name = self.edit_profile.ui.lineEdit_2.text()
        tel_num = self.edit_profile.ui.lineEdit_3.text()
        birth_date = self.edit_profile.ui.lineEdit_4.text()
        email = self.edit_profile.ui.lineEdit_5.text()
        address = self.edit_profile.ui.lineEdit_6.text()
        full_name = f"{first_name} {last_name}"

        success = self.db.update_profile(
            am=self.db.student.am,
            name=full_name,
            email=email,
            birth_date=birth_date,
            address=address,
            tel_num=tel_num
        )
        if success:
            self.current_profile.name = full_name
            self.current_profile.email = email
            self.current_profile.birth_date = birth_date
            self.current_profile.address = address
            self.current_profile.tel_num = int(tel_num)

            self.edit_profile.hide()
            self.display_profile(self.current_profile)
            QMessageBox.information(None, "Success", "Profile updated successfully.")
        else:
            QMessageBox.critical(None, "Error", "Update failed.")

    def show_upload(self):
        if self.selected_course_id is None:
            QMessageBox.warning(None, "Error", "No course selected.")
            return
        self.upload = UploadWindow(self)
        self.upload.show()
        
    def open_post(self):
        self.post_open = PostOpenWindow(self)
        self.post_open.show()

    def open_not_uploaded_post(self):
        self.nu_post_open = UploadConfirmationWindow(self)
        self.nu_post_open.show()

    def student_authentication(self, username, password):
        return self.db.is_valid_student(username, password)

    def admin_authentication(self, username, password):
        return self.db.is_valid_admin(username, password)
    
    def queryApproveUploadPost(self,post_id):
        return self.db.uploadPost(post_id)
    
    def queryRejectReport(self,report_id):
        return self.db.rejectReport(report_id)
    
    def queryApplyPenalty(self,report_id):
        self.db.querySendPenaltyMessage(report_id,self.penalty)
        print(self.penalty)
        self.penalty = None
        return True