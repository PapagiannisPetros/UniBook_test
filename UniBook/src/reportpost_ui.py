# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'reportpost.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFormLayout, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QTextBrowser, QVBoxLayout, QWidget)
import _icons_rc
import _icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1116, 699)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 70, 70);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(25, 25, 25, 25)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color: rgb(5, 87, 85);")
        self.verticalLayout_5 = QVBoxLayout(self.widget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(20, 2, 20, 5)
        self.widget_5 = QWidget(self.widget)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.widget_5)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(15)
        font.setBold(False)
        self.label.setFont(font)

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout_5.addWidget(self.widget_5, 0, Qt.AlignHCenter)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_7 = QVBoxLayout(self.widget_3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 11)
        self.widget_4 = QWidget(self.widget_3)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setStyleSheet(u"background-color: rgb(183, 177, 191);")
        self.verticalLayout_3 = QVBoxLayout(self.widget_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget_6 = QWidget(self.widget_4)
        self.widget_6.setObjectName(u"widget_6")
        self.formLayout = QFormLayout(self.widget_6)
        self.formLayout.setObjectName(u"formLayout")
        self.widget_7 = QWidget(self.widget_6)
        self.widget_7.setObjectName(u"widget_7")
        self.verticalLayout_4 = QVBoxLayout(self.widget_7)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_3 = QLabel(self.widget_7)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setPixmap(QPixmap(u"../24-design/Qss/icons/black/feather/align-left.png"))

        self.verticalLayout_4.addWidget(self.label_3)


        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.widget_7)

        self.widget_43 = QWidget(self.widget_6)
        self.widget_43.setObjectName(u"widget_43")
        self.verticalLayout_6 = QVBoxLayout(self.widget_43)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_36 = QLabel(self.widget_43)
        self.label_36.setObjectName(u"label_36")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        font1.setKerning(True)
        self.label_36.setFont(font1)
        self.label_36.setTextFormat(Qt.AutoText)
        self.label_36.setScaledContents(False)
        self.label_36.setWordWrap(False)

        self.verticalLayout_6.addWidget(self.label_36)

        self.label_35 = QLabel(self.widget_43)
        self.label_35.setObjectName(u"label_35")
        font2 = QFont()
        font2.setPointSize(9)
        self.label_35.setFont(font2)

        self.verticalLayout_6.addWidget(self.label_35)


        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.widget_43)


        self.verticalLayout_3.addWidget(self.widget_6)

        self.widget_42 = QWidget(self.widget_4)
        self.widget_42.setObjectName(u"widget_42")
        self.widget_42.setMinimumSize(QSize(0, 0))
        self.verticalLayout_35 = QVBoxLayout(self.widget_42)
        self.verticalLayout_35.setSpacing(0)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(-1, 0, 2, 0)
        self.widget_44 = QWidget(self.widget_42)
        self.widget_44.setObjectName(u"widget_44")
        self.verticalLayout_36 = QVBoxLayout(self.widget_44)
        self.verticalLayout_36.setSpacing(0)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 2, 2)
        self.textBrowser_8 = QTextBrowser(self.widget_44)
        self.textBrowser_8.setObjectName(u"textBrowser_8")
        self.textBrowser_8.setMaximumSize(QSize(16777215, 180))

        self.verticalLayout_36.addWidget(self.textBrowser_8, 0, Qt.AlignBottom)


        self.verticalLayout_35.addWidget(self.widget_44)


        self.verticalLayout_3.addWidget(self.widget_42)


        self.verticalLayout_7.addWidget(self.widget_4)


        self.verticalLayout_5.addWidget(self.widget_3)

        self.widget_8 = QWidget(self.widget)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setStyleSheet(u"background-color: rgb(12, 126, 124);")
        self.verticalLayout_2 = QVBoxLayout(self.widget_8)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.checkBox = QCheckBox(self.widget_8)
        self.checkBox.setObjectName(u"checkBox")
        font3 = QFont()
        font3.setPointSize(10)
        self.checkBox.setFont(font3)

        self.verticalLayout_2.addWidget(self.checkBox)

        self.checkBox_2 = QCheckBox(self.widget_8)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setFont(font3)

        self.verticalLayout_2.addWidget(self.checkBox_2)

        self.checkBox_4 = QCheckBox(self.widget_8)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setFont(font3)

        self.verticalLayout_2.addWidget(self.checkBox_4)

        self.checkBox_3 = QCheckBox(self.widget_8)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setFont(font3)

        self.verticalLayout_2.addWidget(self.checkBox_3)

        self.checkBox_5 = QCheckBox(self.widget_8)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setFont(font3)

        self.verticalLayout_2.addWidget(self.checkBox_5)


        self.verticalLayout_5.addWidget(self.widget_8)

        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_3 = QPushButton(self.widget_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(self.widget_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 0))
        self.pushButton_2.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(19, 163, 171);")

        self.horizontalLayout.addWidget(self.pushButton_2)


        self.verticalLayout_5.addWidget(self.widget_2, 0, Qt.AlignRight|Qt.AlignBottom)


        self.verticalLayout.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Report Post", None))
        self.label_3.setText("")
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"\u0393\u03c1\u03b1\u03bc\u03bc\u03b9\u03ba\u03ae \u0386\u03bb\u03b3\u03b5\u03b2\u03c1\u03b1 \u2013 \u039d\u03ad\u03b1 \u0394\u03b7\u03bc\u03bf\u03c3\u03af\u03b5\u03c5\u03c3\u03b7", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"18/04/2025", None))
        self.textBrowser_8.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">\u03bd\u03ad\u03bf \u03c5\u03bb\u03b9\u03ba\u03cc \u03bc\u03b5 \u03c0\u03b1\u03c1\u03b1\u03b4\u03b5\u03af\u03b3\u03bc\u03b1\u03c4\u03b1 \u03b5\u03c6\u03b1\u03c1\u03bc\u03bf\u03b3\u03ae\u03c2 \u03c0\u03af\u03bd\u03b1\u03ba\u03c9\u03bd \u03ba\u03b1\u03b9 \u03b4\u03b9\u03b1\u03bd\u03c5\u03c3\u03bc\u03ac\u03c4\u03c9\u03bd \u03c3\u03c4\u03b7\u03bd \u03b5\u03c0\u03af\u03bb\u03c5\u03c3\u03b7 \u03c3\u03c5\u03c3\u03c4\u03b7\u03bc\u03ac\u03c4\u03c9\u03bd \u03b3\u03c1\u03b1\u03bc\u03bc\u03b9\u03ba\u03ce\u03bd \u03b5\u03be\u03b9\u03c3\u03ce"
                        "\u03c3\u03b5\u03c9\u03bd. \u03a0\u03c1\u03bf\u03c4\u03b5\u03af\u03bd\u03b5\u03c4\u03b1\u03b9 \u03b7 \u03bc\u03b5\u03bb\u03ad\u03c4\u03b7 \u03c0\u03c1\u03b9\u03bd \u03c4\u03bf \u03b5\u03c0\u03cc\u03bc\u03b5\u03bd\u03bf \u03bc\u03ac\u03b8\u03b7\u03bc\u03b1 \u03ba\u03b1\u03b8\u03ce\u03c2 \u03c0\u03b5\u03c1\u03b9\u03bb\u03b1\u03bc\u03b2\u03ac\u03bd\u03b5\u03b9 \u03b2\u03b1\u03c3\u03b9\u03ba\u03ad\u03c2 \u03ad\u03bd\u03bd\u03bf\u03b9\u03b5\u03c2 \u03b3\u03b9\u03b1 \u03c4\u03b9\u03c2 \u03b5\u03bd\u03b4\u03b9\u03ac\u03bc\u03b5\u03c3\u03b5\u03c2 \u03b5\u03be\u03b5\u03c4\u03ac\u03c3\u03b5\u03b9\u03c2.</span></p></body></html>", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"I don't like it", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"Spam", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"Abuse or harassment", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"Harmful misinformation or glorifying violence", None))
        self.checkBox_5.setText(QCoreApplication.translate("MainWindow", u"Exposing private identifying information", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Sumbit", None))
    # retranslateUi

