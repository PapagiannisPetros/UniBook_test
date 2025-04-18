# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'editprofile.ui'
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
    QMainWindow, QPushButton, QSizePolicy, QTextEdit,
    QWidget)
import _icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1038, 639)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 70, 70);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-1, -1, 171, 641))
        self.frame.setStyleSheet(u"background-color: rgb(3, 255, 217);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(0, 170, 171, 25))
        self.pushButton.setStyleSheet(u"font: 11pt \"Sans Serif\";")
        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(0, 190, 171, 25))
        self.pushButton_2.setStyleSheet(u"font: 11pt \"Sans Serif\";")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 30, 81, 31))
        self.label.setStyleSheet(u"font: italic 14pt \"Sans Serif\";")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 10, 51, 51))
        self.label_2.setPixmap(QPixmap(u"../../../../../../../Downloads/image 1.png"))
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(190, 30, 171, 181))
        self.frame_2.setStyleSheet(u"background-color: rgb(3, 255, 217);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 140, 121, 41))
        self.label_5.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.pushButton_3 = QPushButton(self.frame_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(730, 150, 91, 31))
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 30, 111, 111))
        self.label_4.setPixmap(QPixmap(u"../../../../../../../Downloads/Profile Image.png"))
        self.label_4.setScaledContents(True)
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(190, 240, 171, 371))
        self.frame_3.setStyleSheet(u"background-color: rgb(3, 255, 217);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 30, 71, 21))
        self.label_6.setStyleSheet(u"font: 10pt \"Sans Serif\";")
        self.label_7 = QLabel(self.frame_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(40, 90, 54, 17))
        self.label_8 = QLabel(self.frame_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(40, 130, 121, 41))
        self.label_9 = QLabel(self.frame_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(40, 200, 81, 17))
        self.label_10 = QLabel(self.frame_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(40, 220, 54, 17))
        self.label_11 = QLabel(self.frame_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(40, 330, 101, 17))
        self.label_12 = QLabel(self.frame_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(30, 270, 141, 17))
        self.label_13 = QLabel(self.frame_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(10, 80, 20, 21))
        self.label_13.setPixmap(QPixmap(u":/font_awesome/regular/icons/font_awesome/regular/user.png"))
        self.label_13.setScaledContents(True)
        self.label_14 = QLabel(self.frame_3)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(10, 140, 20, 21))
        self.label_14.setPixmap(QPixmap(u":/font_awesome/solid/icons/font_awesome/solid/cake-candles.png"))
        self.label_14.setScaledContents(True)
        self.label_15 = QLabel(self.frame_3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(10, 200, 20, 21))
        self.label_15.setPixmap(QPixmap(u":/font_awesome/solid/icons/font_awesome/solid/location-pin.png"))
        self.label_15.setScaledContents(True)
        self.label_16 = QLabel(self.frame_3)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(10, 270, 20, 21))
        self.label_16.setPixmap(QPixmap(u":/font_awesome/solid/icons/font_awesome/solid/folder-open.png"))
        self.label_16.setScaledContents(True)
        self.label_17 = QLabel(self.frame_3)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(10, 330, 20, 21))
        self.label_17.setPixmap(QPixmap(u":/font_awesome/solid/icons/font_awesome/solid/phone-flip.png"))
        self.label_17.setScaledContents(True)
        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(380, 30, 611, 581))
        self.frame_4.setStyleSheet(u"background-color: rgb(3, 255, 217);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.label_18 = QLabel(self.frame_4)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(20, 10, 131, 31))
        self.label_18.setStyleSheet(u"font: 11pt \"Sans Serif\";\n"
"color: rgb(0, 0, 0);")
        self.lineEdit = QLineEdit(self.frame_4)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(30, 70, 231, 31))
        self.lineEdit.setStyleSheet(u"background-color: rgb(6, 154, 156);")
        self.lineEdit_2 = QLineEdit(self.frame_4)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(320, 70, 231, 31))
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(6, 154, 156);")
        self.lineEdit_3 = QLineEdit(self.frame_4)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(30, 150, 231, 31))
        self.lineEdit_3.setStyleSheet(u"background-color: rgb(6, 154, 156);")
        self.lineEdit_4 = QLineEdit(self.frame_4)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(320, 150, 231, 31))
        self.lineEdit_4.setStyleSheet(u"background-color: rgb(6, 154, 156);")
        self.lineEdit_5 = QLineEdit(self.frame_4)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(30, 230, 231, 31))
        self.lineEdit_5.setStyleSheet(u"background-color: rgb(6, 154, 156);")
        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 210, 54, 17))
        self.label_3.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_19 = QLabel(self.frame_4)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(30, 130, 121, 17))
        self.label_19.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_20 = QLabel(self.frame_4)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(320, 130, 71, 17))
        self.label_20.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_21 = QLabel(self.frame_4)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(320, 50, 71, 17))
        self.label_21.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_22 = QLabel(self.frame_4)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(30, 50, 54, 17))
        self.label_22.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.pushButton_4 = QPushButton(self.frame_4)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(50, 290, 121, 31))
        self.pushButton_4.setStyleSheet(u"background-color: rgb(0, 170, 255);\n"
"color: rgb(0, 0, 0);")
        self.pushButton_5 = QPushButton(self.frame_4)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(210, 290, 121, 31))
        self.pushButton_5.setStyleSheet(u"background-color: rgb(255, 0, 127);")
        self.label_23 = QLabel(self.frame_4)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(220, 350, 151, 31))
        self.label_23.setStyleSheet(u"font: 11pt \"Sans Serif\";\n"
"color: rgb(0, 0, 0);")
        self.widget_3 = QWidget(self.frame_4)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(10, 390, 191, 181))
        self.widget_3.setStyleSheet(u"background-color: rgb(153, 153, 153);")
        self.label_24 = QLabel(self.widget_3)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(10, 10, 161, 31))
        self.label_24.setStyleSheet(u"font: 11pt \"Sans Serif\";\n"
"color: rgb(0, 0, 0);")
        self.label_27 = QLabel(self.widget_3)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(10, 40, 131, 31))
        self.label_27.setStyleSheet(u"font: 11pt \"Sans Serif\";\n"
"color: rgb(0, 0, 0);")
        self.textEdit = QTextEdit(self.widget_3)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(10, 70, 171, 71))
        self.widget_5 = QWidget(self.frame_4)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setGeometry(QRect(210, 390, 191, 181))
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
        self.pushButton_7 = QPushButton(self.widget_5)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(40, 150, 121, 31))
        self.pushButton_7.setStyleSheet(u"background-color: rgb(237, 255, 37);\n"
"color: rgb(0, 0, 0);")
        self.textEdit_2 = QTextEdit(self.widget_5)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(10, 70, 171, 71))
        self.widget_4 = QWidget(self.frame_4)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(410, 390, 191, 181))
        self.widget_4.setStyleSheet(u"background-color: rgb(153, 153, 153);")
        self.label_26 = QLabel(self.widget_4)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(10, 10, 151, 31))
        self.label_26.setStyleSheet(u"font: 11pt \"Sans Serif\";\n"
"color: rgb(0, 0, 0);")
        self.label_29 = QLabel(self.widget_4)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(10, 40, 131, 31))
        self.label_29.setStyleSheet(u"font: 11pt \"Sans Serif\";\n"
"color: rgb(0, 0, 0);")
        self.pushButton_8 = QPushButton(self.widget_4)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(40, 150, 121, 31))
        self.pushButton_8.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(224, 255, 21);")
        self.textEdit_3 = QTextEdit(self.widget_4)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setGeometry(QRect(10, 70, 171, 71))
        MainWindow.setCentralWidget(self.centralwidget)
        self.frame_2.raise_()
        self.frame.raise_()
        self.frame_3.raise_()
        self.frame_4.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">UniBook.</span></p></body></html>", None))
        self.label_2.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Petros Papagiannis\n"
"@1100658", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Edit Profile", None))
        self.label_4.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"About me", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Male", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Born 18/02/2004 ", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u0393\u03b1\u03bc\u03b2\u03ad\u03c4\u03c4\u03b1 16,", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u03a0\u03ac\u03c4\u03c1\u03b1", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"+306981810174", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"up1100658@upatras.gr", None))
        self.label_13.setText("")
        self.label_14.setText("")
        self.label_15.setText("")
        self.label_16.setText("")
        self.label_17.setText("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">User Settings</span></p></body></html>", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"Petros", None))
        self.lineEdit_2.setText(QCoreApplication.translate("MainWindow", u"Papagiannis", None))
        self.lineEdit_3.setText(QCoreApplication.translate("MainWindow", u"+30 6981810174", None))
        self.lineEdit_4.setText(QCoreApplication.translate("MainWindow", u"@petrospap", None))
        self.lineEdit_5.setText(QCoreApplication.translate("MainWindow", u"up1100658@ac.upatras.gr", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Telephone Number", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"UserName", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Last Name", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Save Changes", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Select your plan now!</p></body></html>", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700; font-style:italic;\">Basic</span></p></body></html>", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Plan includes</p><p><br/></p></body></html>", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&gt;&gt; Analytics</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&gt;&gt; Basic Search Functionality</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700; font-style:italic;\">Rookie</span></p><p><span style=\" font-size:14pt; font-weight:700; font-style:italic;\"><br/></span></p></body></html>", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Plan includes</p><p><br/></p></body></html>", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Start 30 days trial", None))
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
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700; font-style:italic;\">Senior</span></p></body></html>", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Plan includes</p><p><br/></p></body></html>", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Start 30 days trial", None))
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
    # retranslateUi

