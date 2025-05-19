# edit_profile_window.py
from PySide6.QtWidgets import QMainWindow
from edit_profile_ui import Ui_MainWindow  # Adjust class name if it's different

class EditProfileWindow(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.rookieBut.clicked.connect(self.show_rookie)
        
        self.ui.seniorBut.clicked.connect(self.show_senior)
        
        self.ui.cancelBut.clicked.connect(self.cancel)
    
    def show_rookie(self):
        self.controller.show_rookie()
        
    def show_senior(self):
        self.controller.show_senior()
        
    def cancel(self):
        self.controller.cancel()

    def set_profile_data(self, data):
        self.ui.lineEdit.setText(data.get("name", ""))
        self.ui.lineEdit_2.setText(data.get("name", ""))
        self.ui.lineEdit_3.setText(str(data.get("phone", "")))
        self.ui.lineEdit_4.setText(data.get("birth_date", ""))
        self.ui.lineEdit_5.setText(data.get("email", ""))
        self.ui.lineEdit_6.setText(data.get("address", ""))
        self.ui.label_5.setText(f"<b>{data['name']}</b><br>@{data['am']}")
        self.ui.label_7.setText(data['gender'])
        self.ui.label_8.setText(f"Born {data['birth_date']}")
        self.ui.label_10.setText(data['address'])
        self.ui.label_11.setText(str(data['phone']))
        self.ui.label_12.setText(data['email'])