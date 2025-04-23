from PySide6.QtWidgets import QApplication
from controller import Controller  # ✅ import the controller normally

if __name__ == "__main__":
    app = QApplication([])
    controller = Controller()
    controller.show_login()
    app.exec()
