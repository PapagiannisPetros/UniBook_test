# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rookie.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QTextEdit, QWidget)
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
        self.frame_4.setGeometry(QRect(70, 110, 531, 321))
        self.frame_4.setStyleSheet(u"background-color: rgb(12, 126, 124);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.label_18 = QLabel(self.frame_4)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(140, 20, 251, 31))
        self.label_18.setStyleSheet(u"font: 11pt \"Sans Serif\";\n"
"color: rgb(0, 0, 0);")
        self.continueBut = QPushButton(self.frame_4)
        self.continueBut.setObjectName(u"continueBut")
        self.continueBut.setGeometry(QRect(390, 270, 121, 31))
        self.continueBut.setStyleSheet(u"background-color: rgb(0, 170, 255);\n"
"color: rgb(0, 0, 0);")
        self.cancelBut = QPushButton(self.frame_4)
        self.cancelBut.setObjectName(u"cancelBut")
        self.cancelBut.setGeometry(QRect(240, 270, 121, 31))
        self.cancelBut.setStyleSheet(u"background-color: rgb(255, 0, 127);")
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
        self.widget_8 = QWidget(self.frame_4)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setGeometry(QRect(110, 70, 301, 161))
        self.widget_8.setStyleSheet(u"background-color: rgb(153, 153, 153);")
        self.label_31 = QLabel(self.widget_8)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(10, 10, 151, 31))
        self.label_31.setStyleSheet(u"font: 11pt \"Sans Serif\";\n"
"color: rgb(0, 0, 0);")
        self.label_32 = QLabel(self.widget_8)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(10, 40, 131, 31))
        self.label_32.setStyleSheet(u"font: 11pt \"Sans Serif\";\n"
"color: rgb(0, 0, 0);")
        self.textEdit_5 = QTextEdit(self.widget_8)
        self.textEdit_5.setObjectName(u"textEdit_5")
        self.textEdit_5.setGeometry(QRect(10, 60, 281, 91))
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(10, 59, 681, 21))
        self.line.setLineWidth(2)
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.unibookLabel = QLabel(self.centralwidget)
        self.unibookLabel.setObjectName(u"unibookLabel")
        self.unibookLabel.setGeometry(QRect(90, 20, 131, 41))
        self.unibookLabel.setAutoFillBackground(False)
        self.unibookLabel.setStyleSheet(u"font: italic 9pt \"Sans Serif\";\n"
"color: rgb(255, 255, 255);\n"
"font: 26pt \"Sans Serif\";")
        self.unibookLabel.setScaledContents(True)
        self.logoLabel = QLabel(self.centralwidget)
        self.logoLabel.setObjectName(u"logoLabel")
        self.logoLabel.setGeometry(QRect(20, 10, 61, 51))
        self.logoLabel.setPixmap(QPixmap(u"../images/logo.png"))
        self.logoLabel.setScaledContents(True)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Become a senior from now on!</span></p></body></html>", None))
        self.continueBut.setText(QCoreApplication.translate("MainWindow", u"Continue", None))
        self.cancelBut.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
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
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700; font-style:italic;\">Rookie</span></p><p><span style=\" font-size:14pt; font-weight:700; font-style:italic;\"><br/></span></p></body></html>", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt;\">Plan includes</span></p><p><span style=\" font-size:9pt;\"><br/></span></p></body></html>", None))
        self.textEdit_5.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&gt;&gt; Analytics</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&gt;&gt; Basic Search Functionality</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.unibookLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:22pt; font-weight:700; font-style:italic;\">UniBook.</span></p></body></html>", None))
        self.logoLabel.setText("")
    # retranslateUi

