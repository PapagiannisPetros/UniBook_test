# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QWidget)
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1138, 639)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 255));")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.logoLabel = QLabel(self.centralwidget)
        self.logoLabel.setObjectName(u"logoLabel")
        self.logoLabel.setGeometry(QRect(480, 80, 161, 151))
        
        # Get the absolute path to the directory this file is in
        base_dir = os.path.dirname(os.path.abspath(__file__))
        
                # Build absolute path
        image_path = os.path.join(os.path.dirname(__file__), "../images/logo.png")
        self.logoLabel.setPixmap(QPixmap(image_path))
        
        self.logoLabel.setScaledContents(True)
        self.unibookLabel = QLabel(self.centralwidget)
        self.unibookLabel.setObjectName(u"unibookLabel")
        self.unibookLabel.setGeometry(QRect(490, 30, 161, 51))
        self.unibookLabel.setAutoFillBackground(False)
        self.unibookLabel.setStyleSheet(u"color: rgb(0, 255, 255);\n"
"font: italic 9pt \"Sans Serif\";\n"
"font: 26pt \"Sans Serif\";")
        self.unibookLabel.setScaledContents(True)
        self.loginLabel = QLabel(self.centralwidget)
        self.loginLabel.setObjectName(u"loginLabel")
        self.loginLabel.setGeometry(QRect(460, 260, 211, 21))
        self.loginLabel.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"Sans Serif\";")
        self.backgrounrLabel = QLabel(self.centralwidget)
        self.backgrounrLabel.setObjectName(u"backgrounrLabel")
        self.backgrounrLabel.setGeometry(QRect(0, 270, 1141, 371))
        
                # Build absolute path
        image_path = os.path.join(os.path.dirname(__file__), "../images/rectangle.png")
        self.backgrounrLabel.setPixmap(QPixmap(image_path))
        
        self.backgrounrLabel.setScaledContents(True)
        self.loginBut = QPushButton(self.centralwidget)
        self.loginBut.setObjectName(u"loginBut")
        self.loginBut.setGeometry(QRect(480, 470, 151, 37))
        self.loginBut.setStyleSheet(u"background-color: rgb(0, 144, 255);")
        icon = QIcon()
        icon.addFile(u":/feather/i cons/feather/airplay.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.loginBut.setIcon(icon)
        self.loginBut.setIconSize(QSize(32, 32))
        self.usernameIn = QLineEdit(self.centralwidget)
        self.usernameIn.setObjectName(u"usernameIn")
        self.usernameIn.setGeometry(QRect(440, 350, 261, 31))
        self.usernameIn.setStyleSheet(u"background-color: rgb(170, 255, 255);\n"
"color: rgb(57, 57, 57);")
        self.passwordIn = QLineEdit(self.centralwidget)
        self.passwordIn.setObjectName(u"passwordIn")
        self.passwordIn.setGeometry(QRect(440, 410, 261, 31))
        self.passwordIn.setStyleSheet(u"background-color: rgb(170, 255, 255);\n"
"color: rgb(57, 57, 57);")
        self.loginAdmBut = QPushButton(self.centralwidget)
        self.loginAdmBut.setObjectName(u"loginAdmBut")
        self.loginAdmBut.setGeometry(QRect(480, 530, 151, 37))
        self.loginAdmBut.setStyleSheet(u"background-color: rgb(0, 144, 255);")
        self.loginAdmBut.setIcon(icon)
        self.loginAdmBut.setIconSize(QSize(32, 32))
        MainWindow.setCentralWidget(self.centralwidget)
        self.backgrounrLabel.raise_()
        self.logoLabel.raise_()
        self.unibookLabel.raise_()
        self.loginLabel.raise_()
        self.loginBut.raise_()
        self.usernameIn.raise_()
        self.passwordIn.raise_()
        self.loginAdmBut.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("Login Page", u"Login Page", None))
        self.logoLabel.setText("")
        self.unibookLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700; font-style:italic;\">UniBook.</span></p></body></html>", None))
        self.loginLabel.setText(QCoreApplication.translate("MainWindow", u"Log in with your Academic ID", None))
        self.backgrounrLabel.setText("")
        self.loginBut.setText(QCoreApplication.translate("MainWindow", u"Log in", None))
        self.usernameIn.setText("")
        self.usernameIn.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u038c\u03bd\u03bf\u03bc\u03b1 \u03a7\u03c1\u03ae\u03c3\u03c4\u03b7 (username)", None))
        self.passwordIn.setText("")
        self.passwordIn.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u039a\u03c9\u03b4\u03b9\u03ba\u03cc\u03c2 \u03a7\u03c1\u03ae\u03c3\u03c4\u03b7 (password)", None))
        self.loginAdmBut.setText(QCoreApplication.translate("MainWindow", u"Log in as an Admin", None))
    # retranslateUi

