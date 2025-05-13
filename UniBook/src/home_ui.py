# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QScrollArea, QSizePolicy, QStackedWidget,
    QTextBrowser, QVBoxLayout, QWidget)
import _icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1359, 734)
        MainWindow.setStyleSheet(u"background-color: rgb(5, 87, 85);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMaximumSize(QSize(1920, 1080))
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenu = QFrame(self.centralwidget)
        self.leftMenu.setObjectName(u"leftMenu")
        self.leftMenu.setMaximumSize(QSize(16777215, 16777215))
        self.leftMenu.setStyleSheet(u"background-color: rgb(12, 126, 124);")
        self.verticalLayout = QVBoxLayout(self.leftMenu)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.leftMenu)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout.addWidget(self.widget, 0, Qt.AlignLeft|Qt.AlignTop)

        self.homeBut = QPushButton(self.leftMenu)
        self.homeBut.setObjectName(u"homeBut")
        icon = QIcon()
        icon.addFile(u":/material_design/icons/material_design/home.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.homeBut.setIcon(icon)
        self.homeBut.setIconSize(QSize(25, 25))

        self.verticalLayout.addWidget(self.homeBut)

        self.widget_2 = QWidget(self.leftMenu)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_3 = QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.profileBut = QPushButton(self.widget_2)
        self.profileBut.setObjectName(u"profileBut")
        icon1 = QIcon()
        icon1.addFile(u":/material_design/icons/material_design/co_present.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.profileBut.setIcon(icon1)
        self.profileBut.setIconSize(QSize(25, 25))

        self.verticalLayout_3.addWidget(self.profileBut)

        self.lessonsBut = QPushButton(self.widget_2)
        self.lessonsBut.setObjectName(u"lessonsBut")
        icon2 = QIcon()
        icon2.addFile(u":/feather/icons/feather/list.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.lessonsBut.setIcon(icon2)
        self.lessonsBut.setIconSize(QSize(25, 25))

        self.verticalLayout_3.addWidget(self.lessonsBut)


        self.verticalLayout.addWidget(self.widget_2, 0, Qt.AlignLeft|Qt.AlignTop)

        self.widget_3 = QWidget(self.leftMenu)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_4 = QVBoxLayout(self.widget_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.logoutBut = QPushButton(self.widget_3)
        self.logoutBut.setObjectName(u"logoutBut")
        icon3 = QIcon()
        icon3.addFile(u":/feather/icons/feather/log-out.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.logoutBut.setIcon(icon3)
        self.logoutBut.setIconSize(QSize(25, 25))

        self.verticalLayout_4.addWidget(self.logoutBut)


        self.verticalLayout.addWidget(self.widget_3, 0, Qt.AlignLeft|Qt.AlignBottom)


        self.horizontalLayout.addWidget(self.leftMenu, 0, Qt.AlignLeft)

        self.centerMenu = QWidget(self.centralwidget)
        self.centerMenu.setObjectName(u"centerMenu")
        self.centerMenu.setMinimumSize(QSize(250, 0))
        self.centerMenu.setMaximumSize(QSize(200, 16777215))
        self.centerMenu.setStyleSheet(u"background-color: rgb(12, 126, 124);")
        self.verticalLayout_5 = QVBoxLayout(self.centerMenu)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.widget_4 = QWidget(self.centerMenu)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(0, 24))
        self.widget_4.setStyleSheet(u"background-color: rgb(6, 71, 69);\n"
"")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget_4)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout_5.addWidget(self.widget_4)

        self.widget_45 = QWidget(self.centerMenu)
        self.widget_45.setObjectName(u"widget_45")
        self.widget_45.setMinimumSize(QSize(0, 600))
        self.verticalLayout_6 = QVBoxLayout(self.widget_45)
        self.verticalLayout_6.setSpacing(7)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 9, 0, 0)
        self.scrollArea_2 = QScrollArea(self.widget_45)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 248, 699))
        self.verticalLayout_37 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_37.setSpacing(4)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(5, 0, 0, 0)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_6.addWidget(self.scrollArea_2)


        self.verticalLayout_5.addWidget(self.widget_45)


        self.horizontalLayout.addWidget(self.centerMenu)

        self.mainBody = QWidget(self.centralwidget)
        self.mainBody.setObjectName(u"mainBody")
        self.mainBody.setMinimumSize(QSize(800, 0))
        self.mainBody.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_7 = QHBoxLayout(self.mainBody)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.mainContents = QWidget(self.mainBody)
        self.mainContents.setObjectName(u"mainContents")
        self.horizontalLayout_5 = QHBoxLayout(self.mainContents)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.mainPagesCont = QWidget(self.mainContents)
        self.mainPagesCont.setObjectName(u"mainPagesCont")
        self.mainPagesCont.setMinimumSize(QSize(500, 0))
        self.verticalLayout_8 = QVBoxLayout(self.mainPagesCont)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 5, 0)
        self.header = QWidget(self.mainPagesCont)
        self.header.setObjectName(u"header")
        self.horizontalLayout_4 = QHBoxLayout(self.header)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 5)
        self.widget_5 = QWidget(self.header)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_3.setSpacing(7)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, 5, 10, 0)
        self.searchBtn = QPushButton(self.widget_5)
        self.searchBtn.setObjectName(u"searchBtn")
        self.searchBtn.setMaximumSize(QSize(30, 16777215))
        icon4 = QIcon()
        icon4.addFile(u":/feather/icons/feather/search.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.searchBtn.setIcon(icon4)

        self.horizontalLayout_3.addWidget(self.searchBtn, 0, Qt.AlignRight|Qt.AlignVCenter)

        self.searchLine = QLineEdit(self.widget_5)
        self.searchLine.setObjectName(u"searchLine")
        self.searchLine.setMaximumSize(QSize(500, 16777215))

        self.horizontalLayout_3.addWidget(self.searchLine, 0, Qt.AlignVCenter)

        self.newBut = QPushButton(self.widget_5)
        self.newBut.setObjectName(u"newBut")
        self.newBut.setMaximumSize(QSize(70, 16777215))
        self.newBut.setStyleSheet(u"background-color: rgb(17, 188, 185);")
        icon5 = QIcon()
        icon5.addFile(u":/feather/icons/feather/plus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.newBut.setIcon(icon5)

        self.horizontalLayout_3.addWidget(self.newBut, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_4.addWidget(self.widget_5)


        self.verticalLayout_8.addWidget(self.header)

        self.stackedWidget_2 = QStackedWidget(self.mainPagesCont)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setAutoFillBackground(False)
        self.stackedWidget_2.setLineWidth(1)
        self.homePage = QWidget()
        self.homePage.setObjectName(u"homePage")
        self.verticalLayout_9 = QVBoxLayout(self.homePage)
        self.verticalLayout_9.setSpacing(7)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 6, 0, 0)
        self.scrollArea = QScrollArea(self.homePage)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.StyledPanel)
        self.scrollArea.setFrameShadow(QFrame.Raised)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 705, 691))
        self.verticalLayout_7 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(7, 2, 7, 0)
        self.widget_40 = QWidget(self.scrollAreaWidgetContents)
        self.widget_40.setObjectName(u"widget_40")
        self.widget_40.setMinimumSize(QSize(0, 0))
        self.widget_40.setMaximumSize(QSize(16777215, 200))
        self.widget_40.setStyleSheet(u"background-color: rgb(150, 150, 150);")
        self.horizontalLayout_15 = QHBoxLayout(self.widget_40)
        self.horizontalLayout_15.setSpacing(7)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.widget_41 = QWidget(self.widget_40)
        self.widget_41.setObjectName(u"widget_41")
        self.verticalLayout_34 = QVBoxLayout(self.widget_41)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.label_34 = QLabel(self.widget_41)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMinimumSize(QSize(170, 100))
        self.label_34.setStyleSheet(u"")
        self.label_34.setAlignment(Qt.AlignCenter)

        self.verticalLayout_34.addWidget(self.label_34)


        self.horizontalLayout_15.addWidget(self.widget_41, 0, Qt.AlignLeft)

        self.widget_42 = QWidget(self.widget_40)
        self.widget_42.setObjectName(u"widget_42")
        self.widget_42.setMinimumSize(QSize(0, 0))
        self.verticalLayout_35 = QVBoxLayout(self.widget_42)
        self.verticalLayout_35.setSpacing(0)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(-1, 0, 2, 0)
        self.widget_43 = QWidget(self.widget_42)
        self.widget_43.setObjectName(u"widget_43")
        self.gridLayout_8 = QGridLayout(self.widget_43)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setVerticalSpacing(0)
        self.gridLayout_8.setContentsMargins(0, 0, 0, -1)
        self.postBut = QPushButton(self.widget_43)
        self.postBut.setObjectName(u"postBut")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.postBut.sizePolicy().hasHeightForWidth())
        self.postBut.setSizePolicy(sizePolicy)
        icon6 = QIcon()
        icon6.addFile(u":/feather/icons/feather/arrow-right.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.postBut.setIcon(icon6)
        self.postBut.setAutoDefault(False)

        self.gridLayout_8.addWidget(self.postBut, 0, 2, 1, 1)

        self.label_35 = QLabel(self.widget_43)
        self.label_35.setObjectName(u"label_35")

        self.gridLayout_8.addWidget(self.label_35, 1, 0, 1, 1)

        self.label_36 = QLabel(self.widget_43)
        self.label_36.setObjectName(u"label_36")
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_36.setFont(font)
        self.label_36.setTextFormat(Qt.AutoText)
        self.label_36.setScaledContents(False)
        self.label_36.setWordWrap(False)

        self.gridLayout_8.addWidget(self.label_36, 0, 0, 1, 2)


        self.verticalLayout_35.addWidget(self.widget_43, 0, Qt.AlignTop)

        self.widget_44 = QWidget(self.widget_42)
        self.widget_44.setObjectName(u"widget_44")
        self.verticalLayout_36 = QVBoxLayout(self.widget_44)
        self.verticalLayout_36.setSpacing(0)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 2, 2)
        self.textBrowser_8 = QTextBrowser(self.widget_44)
        self.textBrowser_8.setObjectName(u"textBrowser_8")

        self.verticalLayout_36.addWidget(self.textBrowser_8)


        self.verticalLayout_35.addWidget(self.widget_44)


        self.horizontalLayout_15.addWidget(self.widget_42)


        self.verticalLayout_7.addWidget(self.widget_40)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_9.addWidget(self.scrollArea)

        self.stackedWidget_2.addWidget(self.homePage)
        self.profilePage = QWidget()
        self.profilePage.setObjectName(u"profilePage")
        self.verticalLayout_10 = QVBoxLayout(self.profilePage)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_5 = QLabel(self.profilePage)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_5)

        self.stackedWidget_2.addWidget(self.profilePage)

        self.verticalLayout_8.addWidget(self.stackedWidget_2)


        self.horizontalLayout_5.addWidget(self.mainPagesCont)

        self.rightMenu = QWidget(self.mainContents)
        self.rightMenu.setObjectName(u"rightMenu")
        self.rightMenu.setMinimumSize(QSize(300, 0))
        self.rightMenu.setMaximumSize(QSize(350, 16777215))
        self.rightMenu.setStyleSheet(u"background-color: rgb(12, 126, 124);")
        self.verticalLayout_13 = QVBoxLayout(self.rightMenu)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 3)
        self.widget_8 = QWidget(self.rightMenu)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setMinimumSize(QSize(0, 24))
        self.widget_8.setStyleSheet(u"background-color: rgb(6, 71, 69);")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.widget_8)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(0, 24))

        self.horizontalLayout_8.addWidget(self.label_8)

        self.pushButton_8 = QPushButton(self.widget_8)
        self.pushButton_8.setObjectName(u"pushButton_8")
        icon7 = QIcon()
        icon7.addFile(u":/feather/icons/feather/x-circle.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_8.setIcon(icon7)

        self.horizontalLayout_8.addWidget(self.pushButton_8, 0, Qt.AlignRight)


        self.verticalLayout_13.addWidget(self.widget_8)

        self.widget_47 = QWidget(self.rightMenu)
        self.widget_47.setObjectName(u"widget_47")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_47.sizePolicy().hasHeightForWidth())
        self.widget_47.setSizePolicy(sizePolicy1)
        self.widget_47.setMinimumSize(QSize(0, 0))
        self.verticalLayout_14 = QVBoxLayout(self.widget_47)
        self.verticalLayout_14.setSpacing(7)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(3, 0, 3, 0)
        self.chatDisplay = QTextBrowser(self.widget_47)
        self.chatDisplay.setObjectName(u"chatDisplay")

        self.verticalLayout_14.addWidget(self.chatDisplay)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.chatInput = QLineEdit(self.widget_47)
        self.chatInput.setObjectName(u"chatInput")

        self.horizontalLayout_9.addWidget(self.chatInput)

        self.sendBut = QPushButton(self.widget_47)
        self.sendBut.setObjectName(u"sendBut")

        self.horizontalLayout_9.addWidget(self.sendBut)


        self.verticalLayout_14.addLayout(self.horizontalLayout_9)


        self.verticalLayout_13.addWidget(self.widget_47)


        self.horizontalLayout_5.addWidget(self.rightMenu)


        self.horizontalLayout_7.addWidget(self.mainContents)


        self.horizontalLayout.addWidget(self.mainBody)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.profileBut, self.logoutBut)

        self.retranslateUi(MainWindow)

        self.stackedWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.homeBut.setToolTip(QCoreApplication.translate("MainWindow", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.homeBut.setText("")
#if QT_CONFIG(tooltip)
        self.profileBut.setToolTip(QCoreApplication.translate("MainWindow", u"Profile", None))
#endif // QT_CONFIG(tooltip)
        self.profileBut.setText("")
#if QT_CONFIG(tooltip)
        self.lessonsBut.setToolTip(QCoreApplication.translate("MainWindow", u"Lessons", None))
#endif // QT_CONFIG(tooltip)
        self.lessonsBut.setText("")
#if QT_CONFIG(tooltip)
        self.logoutBut.setToolTip(QCoreApplication.translate("MainWindow", u"LogOut", None))
#endif // QT_CONFIG(tooltip)
        self.logoutBut.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:700; font-style:italic;\">Lessons</span></p></body></html>", None))
        self.searchBtn.setText("")
        self.searchLine.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search...", None))
        self.newBut.setText(QCoreApplication.translate("MainWindow", u"New", None))
#if QT_CONFIG(whatsthis)
        self.label_34.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/material_design/icons/material_design/unsplash_IyaNci0CyRk.png\"/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_34.setText("")
        self.postBut.setText("")
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"18/04/2025", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"\u0393\u03c1\u03b1\u03bc\u03bc\u03b9\u03ba\u03ae \u0386\u03bb\u03b3\u03b5\u03b2\u03c1\u03b1 \u2013 \u039d\u03ad\u03b1 \u0394\u03b7\u03bc\u03bf\u03c3\u03af\u03b5\u03c5\u03c3\u03b7", None))
        self.textBrowser_8.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">\u03bd\u03ad\u03bf \u03c5\u03bb\u03b9\u03ba\u03cc \u03bc\u03b5 \u03c0\u03b1\u03c1\u03b1\u03b4\u03b5\u03af\u03b3\u03bc\u03b1\u03c4\u03b1 \u03b5\u03c6\u03b1\u03c1\u03bc\u03bf\u03b3\u03ae\u03c2 \u03c0\u03af\u03bd\u03b1\u03ba\u03c9\u03bd \u03ba\u03b1\u03b9 \u03b4\u03b9\u03b1\u03bd\u03c5\u03c3\u03bc\u03ac\u03c4\u03c9\u03bd \u03c3\u03c4\u03b7\u03bd \u03b5\u03c0"
                        "\u03af\u03bb\u03c5\u03c3\u03b7 \u03c3\u03c5\u03c3\u03c4\u03b7\u03bc\u03ac\u03c4\u03c9\u03bd \u03b3\u03c1\u03b1\u03bc\u03bc\u03b9\u03ba\u03ce\u03bd \u03b5\u03be\u03b9\u03c3\u03ce\u03c3\u03b5\u03c9\u03bd. \u03a0\u03c1\u03bf\u03c4\u03b5\u03af\u03bd\u03b5\u03c4\u03b1\u03b9 \u03b7 \u03bc\u03b5\u03bb\u03ad\u03c4\u03b7 \u03c0\u03c1\u03b9\u03bd \u03c4\u03bf \u03b5\u03c0\u03cc\u03bc\u03b5\u03bd\u03bf \u03bc\u03ac\u03b8\u03b7\u03bc\u03b1 \u03ba\u03b1\u03b8\u03ce\u03c2 \u03c0\u03b5\u03c1\u03b9\u03bb\u03b1\u03bc\u03b2\u03ac\u03bd\u03b5\u03b9 \u03b2\u03b1\u03c3\u03b9\u03ba\u03ad\u03c2 \u03ad\u03bd\u03bd\u03bf\u03b9\u03b5\u03c2 \u03b3\u03b9\u03b1 \u03c4\u03b9\u03c2 \u03b5\u03bd\u03b4\u03b9\u03ac\u03bc\u03b5\u03c3\u03b5\u03c2 \u03b5\u03be\u03b5\u03c4\u03ac\u03c3\u03b5\u03b9\u03c2.</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Profile Page", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Chat", None))
        self.pushButton_8.setText("")
        self.chatDisplay.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:7.8pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:7.8pt;\"><br /></p></body></html>", None))
        self.chatInput.setText("")
        self.chatInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Write a message...", None))
        self.sendBut.setText(QCoreApplication.translate("MainWindow", u"\u0391\u03c0\u03bf\u03c3\u03c4\u03bf\u03bb\u03ae", None))
    # retranslateUi

