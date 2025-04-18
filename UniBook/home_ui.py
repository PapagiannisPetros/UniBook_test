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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QStackedWidget, QVBoxLayout, QWidget)
import _icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1146, 641)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMaximumSize(QSize(1920, 1080))
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.leftMenu = QFrame(self.centralwidget)
        self.leftMenu.setObjectName(u"leftMenu")
        self.leftMenu.setMaximumSize(QSize(380, 636))
        self.verticalLayout = QVBoxLayout(self.leftMenu)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, -1, 0)
        self.widget = QWidget(self.leftMenu)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.menuBtn = QPushButton(self.widget)
        self.menuBtn.setObjectName(u"menuBtn")
        icon = QIcon()
        icon.addFile(u":/material_design/icons/material_design/menu.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.menuBtn.setIcon(icon)

        self.verticalLayout_2.addWidget(self.menuBtn, 0, Qt.AlignTop)


        self.verticalLayout.addWidget(self.widget, 0, Qt.AlignLeft|Qt.AlignTop)

        self.widget_2 = QWidget(self.leftMenu)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_3 = QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, -1, 0, -1)
        self.pushButton = QPushButton(self.widget_2)
        self.pushButton.setObjectName(u"pushButton")
        font = QFont()
        font.setKerning(True)
        self.pushButton.setFont(font)
        icon1 = QIcon()
        icon1.addFile(u"../Qss/icons/Icons/feather/home.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon1)

        self.verticalLayout_3.addWidget(self.pushButton)

        self.profileBut = QPushButton(self.widget_2)
        self.profileBut.setObjectName(u"profileBut")
        icon2 = QIcon()
        icon2.addFile(u":/material_design/icons/material_design/co_present.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.profileBut.setIcon(icon2)

        self.verticalLayout_3.addWidget(self.profileBut)

        self.pushButton_5 = QPushButton(self.widget_2)
        self.pushButton_5.setObjectName(u"pushButton_5")
        icon3 = QIcon()
        icon3.addFile(u":/feather/icons/feather/list.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_5.setIcon(icon3)

        self.verticalLayout_3.addWidget(self.pushButton_5)


        self.verticalLayout.addWidget(self.widget_2, 0, Qt.AlignLeft|Qt.AlignTop)

        self.widget_3 = QWidget(self.leftMenu)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_4 = QVBoxLayout(self.widget_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pushButton_3 = QPushButton(self.widget_3)
        self.pushButton_3.setObjectName(u"pushButton_3")
        icon4 = QIcon()
        icon4.addFile(u":/feather/icons/feather/log-out.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_3.setIcon(icon4)

        self.verticalLayout_4.addWidget(self.pushButton_3)


        self.verticalLayout.addWidget(self.widget_3, 0, Qt.AlignLeft|Qt.AlignBottom)


        self.horizontalLayout.addWidget(self.leftMenu, 0, Qt.AlignLeft)

        self.centerMenu = QWidget(self.centralwidget)
        self.centerMenu.setObjectName(u"centerMenu")
        self.centerMenu.setMaximumSize(QSize(200, 16777215))
        self.verticalLayout_5 = QVBoxLayout(self.centerMenu)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 0, -1, 0)
        self.widget_4 = QWidget(self.centerMenu)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget_4)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.pushButton_4 = QPushButton(self.widget_4)
        self.pushButton_4.setObjectName(u"pushButton_4")
        icon5 = QIcon()
        icon5.addFile(u":/feather/icons/feather/x-circle.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_4.setIcon(icon5)

        self.horizontalLayout_2.addWidget(self.pushButton_4, 0, Qt.AlignRight)


        self.verticalLayout_5.addWidget(self.widget_4)

        self.stackedWidget = QStackedWidget(self.centerMenu)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.lessonsPage = QWidget()
        self.lessonsPage.setObjectName(u"lessonsPage")
        self.verticalLayout_6 = QVBoxLayout(self.lessonsPage)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_2 = QLabel(self.lessonsPage)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_2, 0, Qt.AlignVCenter)

        self.stackedWidget.addWidget(self.lessonsPage)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.centerMenu)

        self.mainBody = QWidget(self.centralwidget)
        self.mainBody.setObjectName(u"mainBody")
        self.verticalLayout_7 = QVBoxLayout(self.mainBody)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, 0, 0, 0)
        self.mainContents = QWidget(self.mainBody)
        self.mainContents.setObjectName(u"mainContents")
        self.horizontalLayout_5 = QHBoxLayout(self.mainContents)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 0, 0, 0)
        self.mainPagesCont = QWidget(self.mainContents)
        self.mainPagesCont.setObjectName(u"mainPagesCont")
        self.verticalLayout_8 = QVBoxLayout(self.mainPagesCont)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(-1, 0, -1, 0)
        self.header = QWidget(self.mainPagesCont)
        self.header.setObjectName(u"header")
        self.horizontalLayout_4 = QHBoxLayout(self.header)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.widget_5 = QWidget(self.header)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.searchBtn = QPushButton(self.widget_5)
        self.searchBtn.setObjectName(u"searchBtn")
        self.searchBtn.setMaximumSize(QSize(30, 16777215))
        icon6 = QIcon()
        icon6.addFile(u":/feather/icons/feather/search.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.searchBtn.setIcon(icon6)

        self.horizontalLayout_3.addWidget(self.searchBtn, 0, Qt.AlignRight|Qt.AlignVCenter)

        self.searchLine = QLineEdit(self.widget_5)
        self.searchLine.setObjectName(u"searchLine")
        self.searchLine.setMaximumSize(QSize(500, 16777215))

        self.horizontalLayout_3.addWidget(self.searchLine, 0, Qt.AlignVCenter)

        self.pushButton_6 = QPushButton(self.widget_5)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMaximumSize(QSize(70, 16777215))
        icon7 = QIcon()
        icon7.addFile(u"../Qss/icons/Icons/feather/plus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_6.setIcon(icon7)

        self.horizontalLayout_3.addWidget(self.pushButton_6, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_4.addWidget(self.widget_5)


        self.verticalLayout_8.addWidget(self.header)

        self.stackedWidget_2 = QStackedWidget(self.mainPagesCont)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.homePage = QWidget()
        self.homePage.setObjectName(u"homePage")
        self.verticalLayout_9 = QVBoxLayout(self.homePage)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_4 = QLabel(self.homePage)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_4)

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
        self.rightMenu.setMinimumSize(QSize(200, 0))
        self.rightMenu.setMaximumSize(QSize(300, 16777215))
        self.verticalLayout_11 = QVBoxLayout(self.rightMenu)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(-1, 0, 0, 0)
        self.widget_7 = QWidget(self.rightMenu)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.widget_7)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_6.addWidget(self.label_6)

        self.pushButton_7 = QPushButton(self.widget_7)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setIcon(icon5)

        self.horizontalLayout_6.addWidget(self.pushButton_7, 0, Qt.AlignRight)


        self.verticalLayout_11.addWidget(self.widget_7)

        self.stackedWidget_3 = QStackedWidget(self.rightMenu)
        self.stackedWidget_3.setObjectName(u"stackedWidget_3")
        self.chatPage = QWidget()
        self.chatPage.setObjectName(u"chatPage")
        self.verticalLayout_12 = QVBoxLayout(self.chatPage)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_7 = QLabel(self.chatPage)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_7)

        self.stackedWidget_3.addWidget(self.chatPage)

        self.verticalLayout_11.addWidget(self.stackedWidget_3)


        self.horizontalLayout_5.addWidget(self.rightMenu)


        self.verticalLayout_7.addWidget(self.mainContents)


        self.horizontalLayout.addWidget(self.mainBody)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.pushButton, self.profileBut)
        QWidget.setTabOrder(self.profileBut, self.pushButton_3)

        self.retranslateUi(MainWindow)

        self.stackedWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menuBtn.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.profileBut.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Lessons", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Log Out", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Center Menu", None))
        self.pushButton_4.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Lessons", None))
        self.searchBtn.setText("")
        self.searchLine.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search...", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Home Page", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Profile Page", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Right Menu", None))
        self.pushButton_7.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Chat", None))
    # retranslateUi

