# profile_window.py
from PySide6.QtWidgets import QMainWindow
from profile_ui import Ui_MainWindow  # or whatever class name your profile_ui.py has from edit_profile_window import EditProfileWindow

class ProfileWindow(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connect button to open edit profile
        self.ui.editProfBut.clicked.connect(self.open_edit_profile)

        self.ui.homeBut.clicked.connect(self.open_home)

        self.ui.logoutBut.clicked.connect(self.logout)

    def open_edit_profile(self):
        self.controller.show_edit_profile()
        
    def open_home(self):
        self.controller.show_home()
        self.close()
        
    def logout(self):
        self.controller.show_login()
        self.close()

    def set_profile_data(self, data):
        self.ui.label_5.setText(f"<b>{data['name']}</b><br>@{data['am']}")
        self.ui.label_7.setText(data['gender'])
        self.ui.label_8.setText(f"Born {data['birth_date']}")
        self.ui.label_9.setText(data['address'])
        self.ui.label_10.setText(data['university'])
        self.ui.label_11.setText(str(data['phone']))
        self.ui.label_12.setText(data['email'])
