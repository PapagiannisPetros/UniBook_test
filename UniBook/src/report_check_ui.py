# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'report_checkvGlnTQ.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QTextBrowser, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1116, 699)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 70, 70);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 20, 475, 601))
        self.groupBox.setMaximumSize(QSize(500, 16777215))
        font = QFont()
        font.setPointSize(8)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet(u"background-color: rgb(114, 140, 135);")
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, -1, -1, 0)
        self.widget = QWidget(self.groupBox)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.textBrowser_2 = QTextBrowser(self.widget)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        self.textBrowser_2.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout_2.addWidget(self.textBrowser_2)


        self.verticalLayout.addWidget(self.widget, 0, Qt.AlignmentFlag.AlignTop)

        self.widget_4 = QWidget(self.groupBox)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(self.widget_4)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_5.addWidget(self.label_4, 0, Qt.AlignmentFlag.AlignTop)

        self.textBrowser = QTextBrowser(self.widget_4)
        self.textBrowser.setObjectName(u"textBrowser")

        self.horizontalLayout_5.addWidget(self.textBrowser)


        self.verticalLayout.addWidget(self.widget_4)

        self.widget_2 = QWidget(self.groupBox)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.textBrowser_21 = QTextBrowser(self.widget_2)
        self.textBrowser_21.setObjectName(u"textBrowser_21")
        self.textBrowser_21.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout_3.addWidget(self.textBrowser_21)

        self.pushButton = QPushButton(self.widget_2)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_3.addWidget(self.pushButton)


        self.verticalLayout.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.groupBox)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.widget_3)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.textBrowser_3 = QTextBrowser(self.widget_3)
        self.textBrowser_3.setObjectName(u"textBrowser_3")
        self.textBrowser_3.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout_4.addWidget(self.textBrowser_3)

        self.pushButtonLoadPDF = QPushButton(self.widget_3)
        self.pushButtonLoadPDF.setObjectName(u"pushButtonLoadPDF")

        self.horizontalLayout_4.addWidget(self.pushButtonLoadPDF)


        self.verticalLayout.addWidget(self.widget_3, 0, Qt.AlignmentFlag.AlignTop)

        self.widget_9 = QWidget(self.groupBox)
        self.widget_9.setObjectName(u"widget_9")
        self.horizontalLayout = QHBoxLayout(self.widget_9)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_11 = QLabel(self.widget_9)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout.addWidget(self.label_11)

        self.textBrowserUsername = QTextBrowser(self.widget_9)
        self.textBrowserUsername.setObjectName(u"textBrowserUsername")
        self.textBrowserUsername.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout.addWidget(self.textBrowserUsername)


        self.verticalLayout.addWidget(self.widget_9)

        self.widget_10 = QWidget(self.groupBox)
        self.widget_10.setObjectName(u"widget_10")
        self.horizontalLayout_10 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_12 = QLabel(self.widget_10)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_10.addWidget(self.label_12)

        self.textBrowser_6 = QTextBrowser(self.widget_10)
        self.textBrowser_6.setObjectName(u"textBrowser_6")
        self.textBrowser_6.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout_10.addWidget(self.textBrowser_6)


        self.verticalLayout.addWidget(self.widget_10)

        self.widget_11 = QWidget(self.groupBox)
        self.widget_11.setObjectName(u"widget_11")
        self.horizontalLayout_11 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_13 = QLabel(self.widget_11)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_11.addWidget(self.label_13)

        self.textBrowser_7 = QTextBrowser(self.widget_11)
        self.textBrowser_7.setObjectName(u"textBrowser_7")
        self.textBrowser_7.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout_11.addWidget(self.textBrowser_7)


        self.verticalLayout.addWidget(self.widget_11)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(489, 9, 621, 651))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 619, 649))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.scrollAreaWidgetContents_4 = QWidget(self.scrollAreaWidgetContents_3)
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setMinimumSize(QSize(550, 0))
        self.scrollAreaWidgetContents_4.setStyleSheet(u"background-color: rgb(114, 140, 135);")

        self.verticalLayout_2.addWidget(self.scrollAreaWidgetContents_4)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_3)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(940, 660, 171, 31))
        self.pushButton_2.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(19, 163, 171);")
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(540, 660, 171, 31))
        self.pushButton_3.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(740, 660, 171, 31))
        self.pushButton_4.setStyleSheet(u"background-color: rgb(188, 17, 74);\n"
"color: rgb(0, 0, 0);")
        self.widget_12 = QWidget(self.centralwidget)
        self.widget_12.setObjectName(u"widget_12")
        self.widget_12.setGeometry(QRect(10, 620, 471, 59))
        self.horizontalLayout_13 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_15 = QLabel(self.widget_12)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_13.addWidget(self.label_15)

        self.textEdit_9 = QTextEdit(self.widget_12)
        self.textEdit_9.setObjectName(u"textEdit_9")
        self.textEdit_9.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout_13.addWidget(self.textEdit_9)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Post Details", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Title:              ", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Description:  ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Image:          ", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Download", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"File:               ", None))
        self.pushButtonLoadPDF.setText(QCoreApplication.translate("MainWindow", u"Download", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Username:    ", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Date:             ", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Reported for:", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Apply Penalty", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Invalid Report", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Penalty:", None))
    # retranslateUi