# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'profile.ui'
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
    QPushButton, QSizePolicy, QTextBrowser, QVBoxLayout,
    QWidget)

from widget import Widget
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
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(180, 10, 851, 131))
        self.label_3.setPixmap(QPixmap(u"../../../../../../../Downloads/image 3.png"))
        self.label_3.setScaledContents(True)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(180, 10, 851, 201))
        self.frame_2.setStyleSheet(u"background-color: rgb(3, 255, 217);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(150, 150, 121, 41))
        self.label_5.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.editProfBut = QPushButton(self.frame_2)
        self.editProfBut.setObjectName(u"editProfBut")
        self.editProfBut.setGeometry(QRect(730, 150, 91, 31))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(220, 90, 81, 81))
        self.label_4.setPixmap(QPixmap(u"../../../../../../../Downloads/Profile Image.png"))
        self.label_4.setScaledContents(True)
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(180, 220, 171, 411))
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
        self.frame_4.setGeometry(QRect(360, 220, 671, 411))
        self.frame_4.setStyleSheet(u"background-color: rgb(3, 255, 217);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.label_18 = QLabel(self.frame_4)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(20, 0, 81, 21))
        self.label_18.setStyleSheet(u"font: 11pt \"Sans Serif\";")
        self.label_19 = QLabel(self.frame_4)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(50, 30, 54, 21))
        self.label_19.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_20 = QLabel(self.frame_4)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(10, 30, 31, 17))
        self.label_20.setPixmap(QPixmap(u":/material_design/icons/material_design/sticky_note_2.png"))
        self.label_21 = QLabel(self.frame_4)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(370, 30, 81, 17))
        self.label_21.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_23 = QLabel(self.frame_4)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(340, 30, 21, 17))
        self.label_23.setPixmap(QPixmap(u":/material_design/icons/material_design/sticky_note_2.png"))
        self.scrollArea_2 = Widget(self.frame_4)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setGeometry(QRect(340, 50, 321, 351))
        self.scrollArea_2.setStyleSheet(u"background-color: rgb(22, 150, 122);")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 319, 349))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget_2 = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMaximumSize(QSize(300, 125))
        self.widget_2.setStyleSheet(u"background-color: rgb(106, 106, 106);")
        self.label_26 = QLabel(self.widget_2)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(0, 0, 61, 125))
        self.label_26.setMinimumSize(QSize(0, 125))
        self.label_26.setPixmap(QPixmap(u"../../../../../../../Downloads/Mask Group.png"))
        self.label_26.setScaledContents(True)
        self.label_27 = QLabel(self.widget_2)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(70, 0, 231, 31))
        self.label_27.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.textBrowser_2 = QTextBrowser(self.widget_2)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        self.textBrowser_2.setGeometry(QRect(70, 50, 201, 61))
        self.label_28 = QLabel(self.widget_2)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(70, 30, 71, 17))

        self.verticalLayout_3.addWidget(self.widget_2)

        self.widget = QWidget(self.scrollAreaWidgetContents_2)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(300, 125))
        self.widget.setStyleSheet(u"background-color: rgb(106, 106, 106);")
        self.label_22 = QLabel(self.widget)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(0, 0, 61, 125))
        self.label_22.setMinimumSize(QSize(0, 125))
        self.label_22.setPixmap(QPixmap(u"../../../../../../../Downloads/Mask Group.png"))
        self.label_22.setScaledContents(True)
        self.label_24 = QLabel(self.widget)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(70, 0, 231, 31))
        self.label_24.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.textBrowser = QTextBrowser(self.widget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(70, 50, 201, 61))
        self.label_25 = QLabel(self.widget)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(70, 30, 71, 17))

        self.verticalLayout_3.addWidget(self.widget)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.scrollArea_3 = Widget(self.frame_4)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setGeometry(QRect(10, 50, 321, 351))
        self.scrollArea_3.setStyleSheet(u"background-color: rgb(22, 150, 122);")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 319, 349))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.widget_3 = QWidget(self.scrollAreaWidgetContents_3)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMaximumSize(QSize(300, 125))
        self.widget_3.setStyleSheet(u"background-color: rgb(106, 106, 106);")
        self.label_29 = QLabel(self.widget_3)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(0, 0, 61, 125))
        self.label_29.setMinimumSize(QSize(0, 125))
        self.label_29.setPixmap(QPixmap(u"../../../../../../../Downloads/Mask Group.png"))
        self.label_29.setScaledContents(True)
        self.label_30 = QLabel(self.widget_3)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(70, 0, 231, 31))
        self.label_30.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.textBrowser_3 = QTextBrowser(self.widget_3)
        self.textBrowser_3.setObjectName(u"textBrowser_3")
        self.textBrowser_3.setGeometry(QRect(70, 50, 201, 61))
        self.label_31 = QLabel(self.widget_3)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(70, 30, 71, 17))

        self.verticalLayout_4.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.scrollAreaWidgetContents_3)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMaximumSize(QSize(300, 125))
        self.widget_4.setStyleSheet(u"background-color: rgb(106, 106, 106);")
        self.label_32 = QLabel(self.widget_4)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(0, 0, 61, 125))
        self.label_32.setMinimumSize(QSize(0, 125))
        self.label_32.setPixmap(QPixmap(u"../../../../../../../Downloads/Mask Group.png"))
        self.label_32.setScaledContents(True)
        self.label_33 = QLabel(self.widget_4)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(70, 0, 231, 31))
        self.label_33.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.textBrowser_4 = QTextBrowser(self.widget_4)
        self.textBrowser_4.setObjectName(u"textBrowser_4")
        self.textBrowser_4.setGeometry(QRect(70, 50, 201, 61))
        self.label_34 = QLabel(self.widget_4)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(70, 30, 71, 17))

        self.verticalLayout_4.addWidget(self.widget_4)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.frame_2.raise_()
        self.frame.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
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
        self.label_3.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Petros Papagiannis\n"
"@1100658", None))
        self.editProfBut.setText(QCoreApplication.translate("MainWindow", u"Edit Profile", None))
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
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">NoteBook</span></p></body></html>", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"My Notes", None))
        self.label_20.setText("")
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Pinned Notes", None))
        self.label_23.setText("")
        self.label_26.setText("")
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"\u0393\u03c1\u03b1\u03bc\u03bc\u03b9\u03ba\u03ae \u0386\u03bb\u03b3\u03b5\u03b2\u03c1\u03b1 : \u0398\u03ad\u03bc\u03b1\u03c4\u03b1 \u0395\u03be\u03b5\u03c4\u03ac\u03c3\u03b5\u03c9\u03bd", None))
        self.textBrowser_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u03a4\u03b1 \u03c0\u03b5\u03c1\u03c3\u03b9\u03bd\u03ac \u03b8\u03ad\u03bc\u03b1\u03c4\u03b1 \u03c4\u03c9\u03bd \u03b5\u03be\u03b5\u03c4\u03ac\u03c3\u03b5\u03c9\u03bd \u03c3\u03c4\u03b7\u03bd \u0393\u03c1\u03b1\u03bc\u03bc\u03b9\u03ba\u03ae \u0386\u03bb\u03b3\u03b5\u03b2\u03c1\u03b1</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt"
                        "-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"18/04/2025\u00b4", None))
        self.label_22.setText("")
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"\u0393\u03c1\u03b1\u03bc\u03bc\u03b9\u03ba\u03ae \u0386\u03bb\u03b3\u03b5\u03b2\u03c1\u03b1 : \u0398\u03ad\u03bc\u03b1\u03c4\u03b1 \u0395\u03be\u03b5\u03c4\u03ac\u03c3\u03b5\u03c9\u03bd", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u03a4\u03b1 \u03c0\u03b5\u03c1\u03c3\u03b9\u03bd\u03ac \u03b8\u03ad\u03bc\u03b1\u03c4\u03b1 \u03c4\u03c9\u03bd \u03b5\u03be\u03b5\u03c4\u03ac\u03c3\u03b5\u03c9\u03bd \u03c3\u03c4\u03b7\u03bd \u0393\u03c1\u03b1\u03bc\u03bc\u03b9\u03ba\u03ae \u0386\u03bb\u03b3\u03b5\u03b2\u03c1\u03b1</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt"
                        "-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"18/04/2025\u00b4", None))
        self.label_29.setText("")
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"\u0393\u03c1\u03b1\u03bc\u03bc\u03b9\u03ba\u03ae \u0386\u03bb\u03b3\u03b5\u03b2\u03c1\u03b1 : \u0398\u03ad\u03bc\u03b1\u03c4\u03b1 \u0395\u03be\u03b5\u03c4\u03ac\u03c3\u03b5\u03c9\u03bd", None))
        self.textBrowser_3.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u03a4\u03b1 \u03c0\u03b5\u03c1\u03c3\u03b9\u03bd\u03ac \u03b8\u03ad\u03bc\u03b1\u03c4\u03b1 \u03c4\u03c9\u03bd \u03b5\u03be\u03b5\u03c4\u03ac\u03c3\u03b5\u03c9\u03bd \u03c3\u03c4\u03b7\u03bd \u0393\u03c1\u03b1\u03bc\u03bc\u03b9\u03ba\u03ae \u0386\u03bb\u03b3\u03b5\u03b2\u03c1\u03b1</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt"
                        "-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"18/04/2025\u00b4", None))
        self.label_32.setText("")
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"\u0393\u03c1\u03b1\u03bc\u03bc\u03b9\u03ba\u03ae \u0386\u03bb\u03b3\u03b5\u03b2\u03c1\u03b1 : \u0398\u03ad\u03bc\u03b1\u03c4\u03b1 \u0395\u03be\u03b5\u03c4\u03ac\u03c3\u03b5\u03c9\u03bd", None))
        self.textBrowser_4.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u03a4\u03b1 \u03c0\u03b5\u03c1\u03c3\u03b9\u03bd\u03ac \u03b8\u03ad\u03bc\u03b1\u03c4\u03b1 \u03c4\u03c9\u03bd \u03b5\u03be\u03b5\u03c4\u03ac\u03c3\u03b5\u03c9\u03bd \u03c3\u03c4\u03b7\u03bd \u0393\u03c1\u03b1\u03bc\u03bc\u03b9\u03ba\u03ae \u0386\u03bb\u03b3\u03b5\u03b2\u03c1\u03b1</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt"
                        "-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"18/04/2025\u00b4", None))
    # retranslateUi

