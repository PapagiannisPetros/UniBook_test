# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'admin_hometoCJpB.ui'
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
    QLineEdit, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QStackedWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1377, 676)
        MainWindow.setStyleSheet(u"background-color: rgb(5, 87, 85);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMaximumSize(QSize(1920, 1080))
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_10 = QHBoxLayout(self.widget)
        self.horizontalLayout_10.setSpacing(5)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.leftMenu = QFrame(self.widget)
        self.leftMenu.setObjectName(u"leftMenu")
        self.leftMenu.setMaximumSize(QSize(16777215, 16777215))
        self.leftMenu.setStyleSheet(u"background-color: rgb(12, 126, 124);")
        self.verticalLayout = QVBoxLayout(self.leftMenu)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.leftMenu)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_2 = QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.menuBtn = QPushButton(self.widget_2)
        self.menuBtn.setObjectName(u"menuBtn")
        icon = QIcon()
        icon.addFile(u":/material_design/icons/material_design/menu.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.menuBtn.setIcon(icon)
        self.menuBtn.setIconSize(QSize(25, 25))

        self.verticalLayout_2.addWidget(self.menuBtn, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout.addWidget(self.widget_2, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.pushButton_16 = QPushButton(self.leftMenu)
        self.pushButton_16.setObjectName(u"pushButton_16")
        icon1 = QIcon()
        icon1.addFile(u":/material_design/icons/material_design/home.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_16.setIcon(icon1)
        self.pushButton_16.setIconSize(QSize(25, 25))

        self.verticalLayout.addWidget(self.pushButton_16)

        self.widget_3 = QWidget(self.leftMenu)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_3 = QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pushButton_2 = QPushButton(self.widget_3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        icon2 = QIcon()
        icon2.addFile(u":/material_design/icons/material_design/co_present.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QSize(25, 25))

        self.verticalLayout_3.addWidget(self.pushButton_2)


        self.verticalLayout.addWidget(self.widget_3, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.widget_5 = QWidget(self.leftMenu)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_4 = QVBoxLayout(self.widget_5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pushButton_3 = QPushButton(self.widget_5)
        self.pushButton_3.setObjectName(u"pushButton_3")
        icon3 = QIcon()
        icon3.addFile(u":/feather/icons/feather/log-out.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_3.setIcon(icon3)
        self.pushButton_3.setIconSize(QSize(25, 25))

        self.verticalLayout_4.addWidget(self.pushButton_3)


        self.verticalLayout.addWidget(self.widget_5, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignBottom)


        self.horizontalLayout_10.addWidget(self.leftMenu)

        self.centerMenu = QWidget(self.widget)
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

        self.pushButton_4 = QPushButton(self.widget_4)
        self.pushButton_4.setObjectName(u"pushButton_4")
        icon4 = QIcon()
        icon4.addFile(u":/feather/icons/feather/x-circle.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_4.setIcon(icon4)

        self.horizontalLayout_2.addWidget(self.pushButton_4)


        self.verticalLayout_5.addWidget(self.widget_4)

        self.widget_45 = QWidget(self.centerMenu)
        self.widget_45.setObjectName(u"widget_45")
        self.widget_45.setMinimumSize(QSize(0, 600))
        self.verticalLayout_6 = QVBoxLayout(self.widget_45)
        self.verticalLayout_6.setSpacing(7)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 9, 0, 0)
        self.widget_46 = QWidget(self.widget_45)
        self.widget_46.setObjectName(u"widget_46")
        self.horizontalLayout_16 = QHBoxLayout(self.widget_46)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.searchBtn_2 = QPushButton(self.widget_46)
        self.searchBtn_2.setObjectName(u"searchBtn_2")
        self.searchBtn_2.setMaximumSize(QSize(30, 16777215))
        icon5 = QIcon()
        icon5.addFile(u":/feather/icons/feather/search.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.searchBtn_2.setIcon(icon5)

        self.horizontalLayout_16.addWidget(self.searchBtn_2)

        self.searchLine_2 = QLineEdit(self.widget_46)
        self.searchLine_2.setObjectName(u"searchLine_2")
        self.searchLine_2.setMaximumSize(QSize(500, 16777215))

        self.horizontalLayout_16.addWidget(self.searchLine_2)


        self.verticalLayout_6.addWidget(self.widget_46)

        self.scrollArea_2 = QScrollArea(self.widget_45)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 248, 585))
        self.verticalLayout_37 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_37.setSpacing(4)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(5, 0, 0, 0)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_6.addWidget(self.scrollArea_2)


        self.verticalLayout_5.addWidget(self.widget_45)


        self.horizontalLayout_10.addWidget(self.centerMenu)

        self.mainBody = QWidget(self.widget)
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
        self.widget_6 = QWidget(self.header)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_3.setSpacing(7)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, 5, 10, 0)
        self.widget_12 = QWidget(self.widget_6)
        self.widget_12.setObjectName(u"widget_12")
        self.verticalLayout_10 = QVBoxLayout(self.widget_12)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_3.addWidget(self.widget_12)

        self.widget_11 = QWidget(self.widget_6)
        self.widget_11.setObjectName(u"widget_11")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.reportBut = QPushButton(self.widget_11)
        self.reportBut.setObjectName(u"reportBut")
        self.reportBut.setMinimumSize(QSize(0, 40))
        self.reportBut.setStyleSheet(u"background-color: rgb(188, 17, 74);")

        self.horizontalLayout_8.addWidget(self.reportBut)

        self.uploadBut = QPushButton(self.widget_11)
        self.uploadBut.setObjectName(u"uploadBut")
        self.uploadBut.setMinimumSize(QSize(0, 40))
        self.uploadBut.setStyleSheet(u"background-color: rgb(17, 171, 188);")

        self.horizontalLayout_8.addWidget(self.uploadBut)


        self.horizontalLayout_3.addWidget(self.widget_11)


        self.horizontalLayout_4.addWidget(self.widget_6)


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
        self.stackedWidget_2.addWidget(self.homePage)

        self.verticalLayout_8.addWidget(self.stackedWidget_2)


        self.horizontalLayout_5.addWidget(self.mainPagesCont)


        self.horizontalLayout_7.addWidget(self.mainContents)


        self.horizontalLayout_10.addWidget(self.mainBody)


        self.horizontalLayout.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menuBtn.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_16.setToolTip(QCoreApplication.translate("MainWindow", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_16.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_2.setToolTip(QCoreApplication.translate("MainWindow", u"Profile", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_2.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_3.setToolTip(QCoreApplication.translate("MainWindow", u"LogOut", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_3.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Lessons", None))
        self.pushButton_4.setText("")
        self.searchBtn_2.setText("")
        self.searchLine_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search...", None))
        self.reportBut.setText(QCoreApplication.translate("MainWindow", u"Reported Posts", None))
        self.uploadBut.setText(QCoreApplication.translate("MainWindow", u"Upload Confirmation", None))
    # retranslateUi

