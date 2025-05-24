from PySide6.QtWidgets import QMainWindow
from reportpost_ui import Ui_MainWindow  # Adjust the import based on your UI file
from datetime import datetime


class ReportPostWindow(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.submitBut.clicked.connect(self.send_report_details)
        
        self.ui.cancelBut.clicked.connect(self.requestDisplayCancelWIndow)  # Close the window without action
    
    
    def requestDisplayCancelWIndow(self):
        # Override close method to ensure proper cleanup if needed
        super().close()
        self.controller.dIsplayCancelWIndow()
        
    def send_report_details(self):
        # Collect report details
        checked_items = []

        for checkbox in [
            self.ui.checkBox, self.ui.checkBox_2, self.ui.checkBox_3,
            self.ui.checkBox_4, self.ui.checkBox_5
        ]:
            if checkbox.isChecked():
                checked_items.append(checkbox.text())

        result_string = ", ".join(checked_items)
        print(result_string)

        report_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Send the report details to the controller
        self.controller.querySaveReport(result_string, report_time)
        
        # Close the window after sending the report
        self.close()