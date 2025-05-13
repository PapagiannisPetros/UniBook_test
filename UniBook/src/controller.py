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

    def show_login(self):
        #self.home.hide()
       # self.rookie.hide()
        self.admin_home.hide()
        self.login.show()
        
    def show_home(self):
        self.login.hide()
        courses = self.db.get_all_courses()
        self.home_window = HomeWindow(self, courses)
        self.home_window.show()
        
    def course_selected(self, course_id):
        print("Course selected:", course_id)
    # Here, you could load posts for that course, open a course view, etc.



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
