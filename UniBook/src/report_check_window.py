from PySide6.QtWidgets import QMainWindow,QMessageBox
from report_check_ui import Ui_MainWindow  # Adjust the import based on your UI file
from datetime import datetime


class ReportCheckWindow(QMainWindow):
    def __init__(self, controller, report_id):
        super().__init__()
        self.controller = controller
        self.report_id = report_id
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_4.clicked.connect(lambda: self.rejectReport(report_id))
        self.ui.pushButton_2.clicked.connect(lambda: self.applyPenalty(report_id))
        self.ui.pushButton_3.clicked.connect(lambda: self.closeWindow())

    def closeWindow(self):
        self.close()
    
    def rejectReport(self,report_id):
        if self.controller.queryRejectReport(report_id):
            self.displayRejectionMessage(report_id)
            self.close() 

    def displayRejectionMessage(self,report_id):
        QMessageBox.information(self, "Reject Report", f"Report with ReportID {report_id} got rejected!")

    def applyPenalty(self,report_id):
        if self.controller.queryApplyPenalty(report_id):
            self.displayConfirmationWindow(report_id)
            self.close()

    def displayConfirmationWindow(self,report_id):
        QMessageBox.information(self, "Penalty Applied", f"Author of report with ReportID {report_id} got penalized!")