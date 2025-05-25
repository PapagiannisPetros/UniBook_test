from datetime import datetime
from PySide6.QtWidgets import QMainWindow, QMessageBox
from payment_ui import Ui_MainWindow  # Adjust the import based on your UI file


class PaymentWindow(QMainWindow):
    def __init__(self, controller, subscription_type):
        super().__init__()
        self.controller = controller
        self.subscription_type = subscription_type
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_5.clicked.connect(self.close)
        self.ui.pushButton_4.clicked.connect(self.finish_payment)

        self.ui.lineEdit_6.textChanged.connect(self.format_card_input)

    def format_card_input(self, text):
        digits_only = ''.join(filter(str.isdigit, text))

        grouped = ' '.join(digits_only[i:i+4] for i in range(0, len(digits_only), 4))
        if text != grouped:
            cursor_pos = self.ui.lineEdit_6.cursorPosition()
            self.ui.lineEdit_6.blockSignals(True)
            self.ui.lineEdit_6.setText(grouped)
            self.ui.lineEdit_6.setCursorPosition(min(cursor_pos + 1, len(grouped)))
            self.ui.lineEdit_6.blockSignals(False)

    def finish_payment(self):
        card_number = self.ui.lineEdit_6.text().replace(" ", "")
        expiry_date = self.ui.lineEdit_7.text()
        cvv = self.ui.lineEdit_8.text()

        if not card_number.isdigit() or len(card_number) != 16:
            QMessageBox.warning(self, "Card Error", "Card number must be 16 digits.")
            return

        if not expiry_date or len(expiry_date) != 5 or expiry_date[2] != "/":
            QMessageBox.warning(self, "Card Error", "Expiry date must be in MM/YY format.")
            return

        try:
            month, year = map(int, expiry_date.split("/"))
            if not (1 <= month <= 12):
                raise ValueError

            now = datetime.now()
            current_year = now.year % 100
            current_month = now.month

            if (year < current_year) or (year == current_year and month < current_month):
                QMessageBox.warning(self, "Card Error", "Card has expired.")
                return
        except ValueError:
            QMessageBox.warning(self, "Card Error", "Invalid expiry date.")
            return

        if not cvv.isdigit() or len(cvv) != 3:
            QMessageBox.warning(self, "Card Error", "CVV must be 3 digits.")
            return

        self.controller.activate_subscription(self.subscription_type)
        self.close()
