# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'payment.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QRadioButton, QSizePolicy,
    QTextEdit, QWidget)
import _icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(700, 450)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 70, 70);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(40, 90, 601, 341))
        self.frame_4.setStyleSheet(u"background-color: rgb(12, 126, 124);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.label_18 = QLabel(self.frame_4)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(20, 10, 111, 21))
        self.label_18.setStyleSheet(u"font: 11pt \"Sans Serif\";\n"
"color: rgb(0, 0, 0);")
        self.pushButton_4 = QPushButton(self.frame_4)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(470, 290, 121, 31))
        self.pushButton_4.setStyleSheet(u"background-color: rgb(0, 170, 255);\n"
"color: rgb(0, 0, 0);")
        self.pushButton_5 = QPushButton(self.frame_4)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(330, 290, 121, 31))
        self.pushButton_5.setStyleSheet(u"background-color: rgb(255, 0, 127);")
        self.label_23 = QLabel(self.frame_4)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(290, 340, 151, 41))
        self.label_23.setStyleSheet(u"font: 11pt \"Sans Serif\";\n"
"color: rgb(0, 0, 0);")
        self.widget_5 = QWidget(self.frame_4)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setGeometry(QRect(270, 390, 211, 161))
        self.widget_5.setStyleSheet(u"background-color: rgb(153, 153, 153);")
        self.label_25 = QLabel(self.widget_5)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(10, 10, 151, 31))
        self.label_25.setStyleSheet(u"font: 11pt \"Sans Serif\";\n"
"color: rgb(0, 0, 0);")
        self.label_28 = QLabel(self.widget_5)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(10, 40, 131, 31))
        self.label_28.setStyleSheet(u"font: 11pt \"Sans Serif\";\n"
"color: rgb(0, 0, 0);")
        self.textEdit_2 = QTextEdit(self.widget_5)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(10, 60, 161, 61))
        self.pushButton_7 = QPushButton(self.widget_5)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(40, 130, 111, 31))
        self.pushButton_7.setStyleSheet(u"background-color: rgb(237, 255, 37);\n"
"color: rgb(0, 0, 0);")
        self.widget_6 = QWidget(self.frame_4)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setGeometry(QRect(10, 390, 211, 161))
        self.widget_6.setStyleSheet(u"background-color: rgb(153, 153, 153);")
        self.label_27 = QLabel(self.widget_6)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(10, 10, 151, 31))
        self.label_27.setStyleSheet(u"font: 11pt \"Sans Serif\";\n"
"color: rgb(0, 0, 0);")
        self.label_30 = QLabel(self.widget_6)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(10, 40, 131, 31))
        self.label_30.setStyleSheet(u"font: 11pt \"Sans Serif\";\n"
"color: rgb(0, 0, 0);")
        self.textEdit_4 = QTextEdit(self.widget_6)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setGeometry(QRect(10, 60, 161, 61))
        self.widget_7 = QWidget(self.frame_4)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setGeometry(QRect(520, 390, 211, 161))
        self.widget_7.setStyleSheet(u"background-color: rgb(153, 153, 153);")
        self.label_26 = QLabel(self.widget_7)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(10, 10, 151, 31))
        self.label_26.setStyleSheet(u"font: 11pt \"Sans Serif\";\n"
"color: rgb(0, 0, 0);")
        self.label_29 = QLabel(self.widget_7)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(10, 40, 131, 31))
        self.label_29.setStyleSheet(u"font: 11pt \"Sans Serif\";\n"
"color: rgb(0, 0, 0);")
        self.textEdit_3 = QTextEdit(self.widget_7)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setGeometry(QRect(10, 60, 161, 61))
        self.pushButton_8 = QPushButton(self.widget_7)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(40, 130, 111, 31))
        self.pushButton_8.setStyleSheet(u"background-color: rgb(237, 255, 37);\n"
"color: rgb(0, 0, 0);")
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 100, 91, 17))
        self.lineEdit_6 = QLineEdit(self.frame_4)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(50, 120, 231, 31))
        self.lineEdit_6.setStyleSheet(u"background-color: rgb(6, 154, 156);")
        self.lineEdit_7 = QLineEdit(self.frame_4)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(50, 190, 231, 31))
        self.lineEdit_7.setStyleSheet(u"background-color: rgb(6, 154, 156);")
        self.lineEdit_8 = QLineEdit(self.frame_4)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setGeometry(QRect(340, 190, 231, 31))
        self.lineEdit_8.setStyleSheet(u"background-color: rgb(6, 154, 156);")
        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 170, 101, 17))
        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(340, 170, 91, 17))
        self.widget = QWidget(self.frame_4)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(190, 240, 231, 41))
        self.widget.setStyleSheet(u"background-color: rgb(23, 255, 228);")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(80, 10, 81, 17))
        self.label_4.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.radioButton = QRadioButton(self.frame_4)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(60, 50, 111, 23))
        self.radioButton_2 = QRadioButton(self.frame_4)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(250, 50, 111, 23))
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(10, 59, 681, 21))
        self.line.setLineWidth(2)
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.unibookLabel = QLabel(self.centralwidget)
        self.unibookLabel.setObjectName(u"unibookLabel")
        self.unibookLabel.setGeometry(QRect(90, 30, 91, 31))
        self.unibookLabel.setAutoFillBackground(False)
        self.unibookLabel.setStyleSheet(u"font: italic 9pt \"Sans Serif\";\n"
"color: rgb(255, 255, 255);\n"
"font: 26pt \"Sans Serif\";")
        self.unibookLabel.setScaledContents(True)
        self.logoLabel = QLabel(self.centralwidget)
        self.logoLabel.setObjectName(u"logoLabel")
        self.logoLabel.setGeometry(QRect(20, 20, 51, 41))
        self.logoLabel.setPixmap(QPixmap(u":/font_awesome/regular/icons/font_awesome/regular/money-bill-1.png"))
        self.logoLabel.setScaledContents(True)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Pay with:</span></p><p><span style=\" font-weight:700;\"><br/></span></p></body></html>", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Finish", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Select your plan now!</p></body></html>", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700; font-style:italic;\">Rookie</span></p><p><span style=\" font-size:14pt; font-weight:700; font-style:italic;\"><br/></span></p></body></html>", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt;\">Plan includes</span></p><p><span style=\" font-size:9pt;\"><br/></span></p></body></html>", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&gt;&gt; Analytics</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&gt;&gt; Basic Search Functionality</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Start 30 days trial", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700; font-style:italic;\">Rookie</span></p><p><span style=\" font-size:14pt; font-weight:700; font-style:italic;\"><br/></span></p></body></html>", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt;\">Plan includes</span></p><p><span style=\" font-size:9pt;\"><br/></span></p></body></html>", None))
        self.textEdit_4.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&gt;&gt; Analytics</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&gt;&gt; Basic Search Functionality</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700; font-style:italic;\">Rookie</span></p><p><span style=\" font-size:14pt; font-weight:700; font-style:italic;\"><br/></span></p></body></html>", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt;\">Plan includes</span></p><p><span style=\" font-size:9pt;\"><br/></span></p></body></html>", None))
        self.textEdit_3.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&gt;&gt; Analytics</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&gt;&gt; Basic Search Functionality</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Start 30 days trial", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Card Number:", None))
        self.lineEdit_6.setText("")
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"XXXX XXXX XXXX XXXX", None))
        self.lineEdit_7.setText("")
        self.lineEdit_7.setPlaceholderText(QCoreApplication.translate("MainWindow", u"MM/YY", None))
        self.lineEdit_8.setText("")
        self.lineEdit_8.setPlaceholderText(QCoreApplication.translate("MainWindow", u"***", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Expiration Date:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"CVV:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">PAY 8.99$</span></p></body></html>", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Credit Card", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Paypal", None))
        self.unibookLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">Payment</span></p></body></html>", None))
        self.logoLabel.setText("")
    # retranslateUi

