# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'admin_home.ui'
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

        self.verticalLayout_2.addWidget(self.menuBtn, 0, Qt.AlignTop)


        self.verticalLayout.addWidget(self.widget_2, 0, Qt.AlignLeft|Qt.AlignTop)

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

        self.pushButton_5 = QPushButton(self.widget_3)
        self.pushButton_5.setObjectName(u"pushButton_5")
        icon3 = QIcon()
        icon3.addFile(u":/feather/icons/feather/list.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_5.setIcon(icon3)
        self.pushButton_5.setIconSize(QSize(25, 25))

        self.verticalLayout_3.addWidget(self.pushButton_5)


        self.verticalLayout.addWidget(self.widget_3, 0, Qt.AlignLeft|Qt.AlignTop)

        self.widget_5 = QWidget(self.leftMenu)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_4 = QVBoxLayout(self.widget_5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pushButton_3 = QPushButton(self.widget_5)
        self.pushButton_3.setObjectName(u"pushButton_3")
        icon4 = QIcon()
        icon4.addFile(u":/feather/icons/feather/log-out.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_3.setIcon(icon4)
        self.pushButton_3.setIconSize(QSize(25, 25))

        self.verticalLayout_4.addWidget(self.pushButton_3)


        self.verticalLayout.addWidget(self.widget_5, 0, Qt.AlignLeft|Qt.AlignBottom)


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
        icon5 = QIcon()
        icon5.addFile(u":/feather/icons/feather/x-circle.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_4.setIcon(icon5)

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
        icon6 = QIcon()
        icon6.addFile(u":/feather/icons/feather/search.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.searchBtn_2.setIcon(icon6)

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
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 345, 633))
        self.verticalLayout_37 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_37.setSpacing(4)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(5, 0, 0, 0)
        self.pushButton_45 = QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_45.setObjectName(u"pushButton_45")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_45.sizePolicy().hasHeightForWidth())
        self.pushButton_45.setSizePolicy(sizePolicy)
        self.pushButton_45.setMinimumSize(QSize(0, 45))
        self.pushButton_45.setMaximumSize(QSize(500, 45))
        font = QFont()
        font.setPointSize(9)
        font.setStyleStrategy(QFont.PreferDefault)
        self.pushButton_45.setFont(font)
        self.pushButton_45.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_45.setAutoFillBackground(False)
        self.pushButton_45.setStyleSheet(u"background-color: rgb(5, 87, 85);\n"
"text-align: left; padding-left: 5px;\n"
"")
        icon7 = QIcon()
        icon7.addFile(u":/feather/icons/feather/book-open.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_45.setIcon(icon7)
        self.pushButton_45.setIconSize(QSize(20, 20))

        self.verticalLayout_37.addWidget(self.pushButton_45)

        self.pushButton_47 = QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_47.setObjectName(u"pushButton_47")
        sizePolicy.setHeightForWidth(self.pushButton_47.sizePolicy().hasHeightForWidth())
        self.pushButton_47.setSizePolicy(sizePolicy)
        self.pushButton_47.setMinimumSize(QSize(0, 45))
        self.pushButton_47.setMaximumSize(QSize(500, 45))
        self.pushButton_47.setFont(font)
        self.pushButton_47.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_47.setAutoFillBackground(False)
        self.pushButton_47.setStyleSheet(u"background-color: rgb(5, 87, 85);\n"
"text-align: left; padding-left: 5px;\n"
"")
        self.pushButton_47.setIcon(icon7)
        self.pushButton_47.setIconSize(QSize(20, 20))

        self.verticalLayout_37.addWidget(self.pushButton_47)

        self.pushButton_46 = QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_46.setObjectName(u"pushButton_46")
        sizePolicy.setHeightForWidth(self.pushButton_46.sizePolicy().hasHeightForWidth())
        self.pushButton_46.setSizePolicy(sizePolicy)
        self.pushButton_46.setMinimumSize(QSize(0, 45))
        self.pushButton_46.setMaximumSize(QSize(500, 45))
        self.pushButton_46.setFont(font)
        self.pushButton_46.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_46.setAutoFillBackground(False)
        self.pushButton_46.setStyleSheet(u"background-color: rgb(5, 87, 85);\n"
"text-align: left; padding-left: 5px;\n"
"")
        self.pushButton_46.setIcon(icon7)
        self.pushButton_46.setIconSize(QSize(20, 20))

        self.verticalLayout_37.addWidget(self.pushButton_46)

        self.pushButton_44 = QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_44.setObjectName(u"pushButton_44")
        sizePolicy.setHeightForWidth(self.pushButton_44.sizePolicy().hasHeightForWidth())
        self.pushButton_44.setSizePolicy(sizePolicy)
        self.pushButton_44.setMinimumSize(QSize(0, 45))
        self.pushButton_44.setMaximumSize(QSize(500, 45))
        self.pushButton_44.setFont(font)
        self.pushButton_44.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_44.setAutoFillBackground(False)
        self.pushButton_44.setStyleSheet(u"background-color: rgb(5, 87, 85);\n"
"text-align: left; padding-left: 5px;\n"
"")
        self.pushButton_44.setIcon(icon7)
        self.pushButton_44.setIconSize(QSize(20, 20))

        self.verticalLayout_37.addWidget(self.pushButton_44)

        self.pushButton_43 = QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_43.setObjectName(u"pushButton_43")
        sizePolicy.setHeightForWidth(self.pushButton_43.sizePolicy().hasHeightForWidth())
        self.pushButton_43.setSizePolicy(sizePolicy)
        self.pushButton_43.setMinimumSize(QSize(0, 45))
        self.pushButton_43.setMaximumSize(QSize(500, 45))
        self.pushButton_43.setFont(font)
        self.pushButton_43.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_43.setAutoFillBackground(False)
        self.pushButton_43.setStyleSheet(u"background-color: rgb(5, 87, 85);\n"
"text-align: left; padding-left: 5px;\n"
"")
        self.pushButton_43.setIcon(icon7)
        self.pushButton_43.setIconSize(QSize(20, 20))

        self.verticalLayout_37.addWidget(self.pushButton_43)

        self.pushButton_42 = QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_42.setObjectName(u"pushButton_42")
        sizePolicy.setHeightForWidth(self.pushButton_42.sizePolicy().hasHeightForWidth())
        self.pushButton_42.setSizePolicy(sizePolicy)
        self.pushButton_42.setMinimumSize(QSize(0, 45))
        self.pushButton_42.setMaximumSize(QSize(500, 45))
        self.pushButton_42.setFont(font)
        self.pushButton_42.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_42.setAutoFillBackground(False)
        self.pushButton_42.setStyleSheet(u"background-color: rgb(5, 87, 85);\n"
"text-align: left; padding-left: 5px;\n"
"")
        self.pushButton_42.setIcon(icon7)
        self.pushButton_42.setIconSize(QSize(20, 20))

        self.verticalLayout_37.addWidget(self.pushButton_42)

        self.pushButton_41 = QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_41.setObjectName(u"pushButton_41")
        sizePolicy.setHeightForWidth(self.pushButton_41.sizePolicy().hasHeightForWidth())
        self.pushButton_41.setSizePolicy(sizePolicy)
        self.pushButton_41.setMinimumSize(QSize(0, 45))
        self.pushButton_41.setMaximumSize(QSize(500, 45))
        self.pushButton_41.setFont(font)
        self.pushButton_41.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_41.setAutoFillBackground(False)
        self.pushButton_41.setStyleSheet(u"background-color: rgb(5, 87, 85);\n"
"text-align: left; padding-left: 5px;\n"
"")
        self.pushButton_41.setIcon(icon7)
        self.pushButton_41.setIconSize(QSize(20, 20))

        self.verticalLayout_37.addWidget(self.pushButton_41)

        self.pushButton_40 = QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_40.setObjectName(u"pushButton_40")
        sizePolicy.setHeightForWidth(self.pushButton_40.sizePolicy().hasHeightForWidth())
        self.pushButton_40.setSizePolicy(sizePolicy)
        self.pushButton_40.setMinimumSize(QSize(0, 45))
        self.pushButton_40.setMaximumSize(QSize(500, 45))
        self.pushButton_40.setFont(font)
        self.pushButton_40.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_40.setAutoFillBackground(False)
        self.pushButton_40.setStyleSheet(u"background-color: rgb(5, 87, 85);\n"
"text-align: left; padding-left: 5px;\n"
"")
        self.pushButton_40.setIcon(icon7)
        self.pushButton_40.setIconSize(QSize(20, 20))

        self.verticalLayout_37.addWidget(self.pushButton_40)

        self.pushButton_39 = QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_39.setObjectName(u"pushButton_39")
        sizePolicy.setHeightForWidth(self.pushButton_39.sizePolicy().hasHeightForWidth())
        self.pushButton_39.setSizePolicy(sizePolicy)
        self.pushButton_39.setMinimumSize(QSize(0, 45))
        self.pushButton_39.setMaximumSize(QSize(500, 45))
        self.pushButton_39.setFont(font)
        self.pushButton_39.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_39.setAutoFillBackground(False)
        self.pushButton_39.setStyleSheet(u"background-color: rgb(5, 87, 85);\n"
"text-align: left; padding-left: 5px;\n"
"")
        self.pushButton_39.setIcon(icon7)
        self.pushButton_39.setIconSize(QSize(20, 20))

        self.verticalLayout_37.addWidget(self.pushButton_39)

        self.pushButton_48 = QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_48.setObjectName(u"pushButton_48")
        sizePolicy.setHeightForWidth(self.pushButton_48.sizePolicy().hasHeightForWidth())
        self.pushButton_48.setSizePolicy(sizePolicy)
        self.pushButton_48.setMinimumSize(QSize(0, 45))
        self.pushButton_48.setMaximumSize(QSize(500, 45))
        self.pushButton_48.setFont(font)
        self.pushButton_48.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_48.setAutoFillBackground(False)
        self.pushButton_48.setStyleSheet(u"background-color: rgb(5, 87, 85);\n"
"text-align: left; padding-left: 5px;\n"
"")
        self.pushButton_48.setIcon(icon7)
        self.pushButton_48.setIconSize(QSize(20, 20))

        self.verticalLayout_37.addWidget(self.pushButton_48)

        self.pushButton_38 = QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_38.setObjectName(u"pushButton_38")
        sizePolicy.setHeightForWidth(self.pushButton_38.sizePolicy().hasHeightForWidth())
        self.pushButton_38.setSizePolicy(sizePolicy)
        self.pushButton_38.setMinimumSize(QSize(0, 45))
        self.pushButton_38.setMaximumSize(QSize(500, 45))
        self.pushButton_38.setFont(font)
        self.pushButton_38.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_38.setAutoFillBackground(False)
        self.pushButton_38.setStyleSheet(u"background-color: rgb(5, 87, 85);\n"
"text-align: left; padding-left: 5px;\n"
"")
        self.pushButton_38.setIcon(icon7)
        self.pushButton_38.setIconSize(QSize(20, 20))

        self.verticalLayout_37.addWidget(self.pushButton_38)

        self.pushButton_37 = QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_37.setObjectName(u"pushButton_37")
        sizePolicy.setHeightForWidth(self.pushButton_37.sizePolicy().hasHeightForWidth())
        self.pushButton_37.setSizePolicy(sizePolicy)
        self.pushButton_37.setMinimumSize(QSize(0, 45))
        self.pushButton_37.setMaximumSize(QSize(500, 45))
        self.pushButton_37.setFont(font)
        self.pushButton_37.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_37.setAutoFillBackground(False)
        self.pushButton_37.setStyleSheet(u"background-color: rgb(5, 87, 85);\n"
"text-align: left; padding-left: 5px;\n"
"")
        self.pushButton_37.setIcon(icon7)
        self.pushButton_37.setIconSize(QSize(20, 20))

        self.verticalLayout_37.addWidget(self.pushButton_37)

        self.pushButton_36 = QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_36.setObjectName(u"pushButton_36")
        sizePolicy.setHeightForWidth(self.pushButton_36.sizePolicy().hasHeightForWidth())
        self.pushButton_36.setSizePolicy(sizePolicy)
        self.pushButton_36.setMinimumSize(QSize(0, 45))
        self.pushButton_36.setMaximumSize(QSize(500, 45))
        self.pushButton_36.setFont(font)
        self.pushButton_36.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_36.setAutoFillBackground(False)
        self.pushButton_36.setStyleSheet(u"background-color: rgb(5, 87, 85);\n"
"text-align: left; padding-left: 5px;\n"
"")
        self.pushButton_36.setIcon(icon7)
        self.pushButton_36.setIconSize(QSize(20, 20))

        self.verticalLayout_37.addWidget(self.pushButton_36)

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
        self.pushButton = QPushButton(self.widget_11)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 40))
        self.pushButton.setStyleSheet(u"background-color: rgb(188, 17, 74);")

        self.horizontalLayout_8.addWidget(self.pushButton)

        self.pushButton_8 = QPushButton(self.widget_11)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(0, 40))
        self.pushButton_8.setStyleSheet(u"background-color: rgb(17, 171, 188);")

        self.horizontalLayout_8.addWidget(self.pushButton_8)


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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1059, 764))
        self.verticalLayout_7 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(7, 2, 7, 0)
        self.widget_40 = QWidget(self.scrollAreaWidgetContents)
        self.widget_40.setObjectName(u"widget_40")
        self.widget_40.setMinimumSize(QSize(0, 0))
        self.widget_40.setMaximumSize(QSize(16777215, 16777215))
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
        self.pushButton_15 = QPushButton(self.widget_43)
        self.pushButton_15.setObjectName(u"pushButton_15")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_15.sizePolicy().hasHeightForWidth())
        self.pushButton_15.setSizePolicy(sizePolicy1)
        icon8 = QIcon()
        icon8.addFile(u":/feather/icons/feather/arrow-right.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_15.setIcon(icon8)
        self.pushButton_15.setAutoDefault(False)

        self.gridLayout_8.addWidget(self.pushButton_15, 0, 2, 1, 1)

        self.label_35 = QLabel(self.widget_43)
        self.label_35.setObjectName(u"label_35")

        self.gridLayout_8.addWidget(self.label_35, 1, 0, 1, 1)

        self.label_36 = QLabel(self.widget_43)
        self.label_36.setObjectName(u"label_36")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        font1.setKerning(True)
        self.label_36.setFont(font1)
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

        self.widget_35 = QWidget(self.scrollAreaWidgetContents)
        self.widget_35.setObjectName(u"widget_35")
        self.widget_35.setMinimumSize(QSize(0, 0))
        self.widget_35.setMaximumSize(QSize(16777215, 16777215))
        self.widget_35.setStyleSheet(u"background-color: rgb(150, 150, 150);")
        self.horizontalLayout_14 = QHBoxLayout(self.widget_35)
        self.horizontalLayout_14.setSpacing(7)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.widget_36 = QWidget(self.widget_35)
        self.widget_36.setObjectName(u"widget_36")
        self.verticalLayout_31 = QVBoxLayout(self.widget_36)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.label_31 = QLabel(self.widget_36)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMinimumSize(QSize(170, 100))
        self.label_31.setStyleSheet(u"")
        self.label_31.setAlignment(Qt.AlignCenter)

        self.verticalLayout_31.addWidget(self.label_31)


        self.horizontalLayout_14.addWidget(self.widget_36, 0, Qt.AlignLeft)

        self.widget_37 = QWidget(self.widget_35)
        self.widget_37.setObjectName(u"widget_37")
        self.widget_37.setMinimumSize(QSize(0, 0))
        self.verticalLayout_32 = QVBoxLayout(self.widget_37)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(-1, 0, 2, 0)
        self.widget_38 = QWidget(self.widget_37)
        self.widget_38.setObjectName(u"widget_38")
        self.gridLayout_7 = QGridLayout(self.widget_38)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setVerticalSpacing(0)
        self.gridLayout_7.setContentsMargins(0, 0, 0, -1)
        self.label_32 = QLabel(self.widget_38)
        self.label_32.setObjectName(u"label_32")

        self.gridLayout_7.addWidget(self.label_32, 1, 0, 1, 1)

        self.pushButton_14 = QPushButton(self.widget_38)
        self.pushButton_14.setObjectName(u"pushButton_14")
        sizePolicy1.setHeightForWidth(self.pushButton_14.sizePolicy().hasHeightForWidth())
        self.pushButton_14.setSizePolicy(sizePolicy1)
        self.pushButton_14.setIcon(icon8)
        self.pushButton_14.setAutoDefault(False)

        self.gridLayout_7.addWidget(self.pushButton_14, 0, 2, 1, 1)

        self.label_33 = QLabel(self.widget_38)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font1)
        self.label_33.setTextFormat(Qt.AutoText)
        self.label_33.setScaledContents(False)
        self.label_33.setWordWrap(False)

        self.gridLayout_7.addWidget(self.label_33, 0, 0, 1, 2)


        self.verticalLayout_32.addWidget(self.widget_38, 0, Qt.AlignTop)

        self.widget_39 = QWidget(self.widget_37)
        self.widget_39.setObjectName(u"widget_39")
        self.verticalLayout_33 = QVBoxLayout(self.widget_39)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 2, 2)
        self.textBrowser_7 = QTextBrowser(self.widget_39)
        self.textBrowser_7.setObjectName(u"textBrowser_7")

        self.verticalLayout_33.addWidget(self.textBrowser_7)


        self.verticalLayout_32.addWidget(self.widget_39)


        self.horizontalLayout_14.addWidget(self.widget_37)


        self.verticalLayout_7.addWidget(self.widget_35)

        self.widget_30 = QWidget(self.scrollAreaWidgetContents)
        self.widget_30.setObjectName(u"widget_30")
        self.widget_30.setMinimumSize(QSize(0, 0))
        self.widget_30.setMaximumSize(QSize(16777215, 16777215))
        self.widget_30.setStyleSheet(u"background-color: rgb(150, 150, 150);")
        self.horizontalLayout_13 = QHBoxLayout(self.widget_30)
        self.horizontalLayout_13.setSpacing(7)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.widget_31 = QWidget(self.widget_30)
        self.widget_31.setObjectName(u"widget_31")
        self.verticalLayout_28 = QVBoxLayout(self.widget_31)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.label_28 = QLabel(self.widget_31)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMinimumSize(QSize(170, 100))
        self.label_28.setStyleSheet(u"")
        self.label_28.setAlignment(Qt.AlignCenter)

        self.verticalLayout_28.addWidget(self.label_28)


        self.horizontalLayout_13.addWidget(self.widget_31, 0, Qt.AlignLeft)

        self.widget_32 = QWidget(self.widget_30)
        self.widget_32.setObjectName(u"widget_32")
        self.widget_32.setMinimumSize(QSize(0, 0))
        self.verticalLayout_29 = QVBoxLayout(self.widget_32)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(-1, 0, 2, 0)
        self.widget_33 = QWidget(self.widget_32)
        self.widget_33.setObjectName(u"widget_33")
        self.gridLayout_6 = QGridLayout(self.widget_33)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setVerticalSpacing(0)
        self.gridLayout_6.setContentsMargins(0, 0, 0, -1)
        self.label_29 = QLabel(self.widget_33)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout_6.addWidget(self.label_29, 1, 0, 1, 1)

        self.pushButton_13 = QPushButton(self.widget_33)
        self.pushButton_13.setObjectName(u"pushButton_13")
        sizePolicy1.setHeightForWidth(self.pushButton_13.sizePolicy().hasHeightForWidth())
        self.pushButton_13.setSizePolicy(sizePolicy1)
        self.pushButton_13.setIcon(icon8)
        self.pushButton_13.setAutoDefault(False)

        self.gridLayout_6.addWidget(self.pushButton_13, 0, 2, 1, 1)

        self.label_30 = QLabel(self.widget_33)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font1)
        self.label_30.setTextFormat(Qt.AutoText)
        self.label_30.setScaledContents(False)
        self.label_30.setWordWrap(False)

        self.gridLayout_6.addWidget(self.label_30, 0, 0, 1, 2)


        self.verticalLayout_29.addWidget(self.widget_33, 0, Qt.AlignTop)

        self.widget_34 = QWidget(self.widget_32)
        self.widget_34.setObjectName(u"widget_34")
        self.verticalLayout_30 = QVBoxLayout(self.widget_34)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 2, 2)
        self.textBrowser_6 = QTextBrowser(self.widget_34)
        self.textBrowser_6.setObjectName(u"textBrowser_6")

        self.verticalLayout_30.addWidget(self.textBrowser_6)


        self.verticalLayout_29.addWidget(self.widget_34)


        self.horizontalLayout_13.addWidget(self.widget_32)


        self.verticalLayout_7.addWidget(self.widget_30)

        self.widget_25 = QWidget(self.scrollAreaWidgetContents)
        self.widget_25.setObjectName(u"widget_25")
        self.widget_25.setMinimumSize(QSize(0, 0))
        self.widget_25.setMaximumSize(QSize(16777215, 16777215))
        self.widget_25.setStyleSheet(u"background-color: rgb(150, 150, 150);")
        self.horizontalLayout_12 = QHBoxLayout(self.widget_25)
        self.horizontalLayout_12.setSpacing(7)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.widget_26 = QWidget(self.widget_25)
        self.widget_26.setObjectName(u"widget_26")
        self.verticalLayout_25 = QVBoxLayout(self.widget_26)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.label_25 = QLabel(self.widget_26)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(170, 100))
        self.label_25.setStyleSheet(u"")
        self.label_25.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.label_25)


        self.horizontalLayout_12.addWidget(self.widget_26, 0, Qt.AlignLeft)

        self.widget_27 = QWidget(self.widget_25)
        self.widget_27.setObjectName(u"widget_27")
        self.widget_27.setMinimumSize(QSize(0, 0))
        self.verticalLayout_26 = QVBoxLayout(self.widget_27)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(-1, 0, 2, 0)
        self.widget_28 = QWidget(self.widget_27)
        self.widget_28.setObjectName(u"widget_28")
        self.gridLayout_5 = QGridLayout(self.widget_28)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setVerticalSpacing(0)
        self.gridLayout_5.setContentsMargins(0, 0, 0, -1)
        self.label_26 = QLabel(self.widget_28)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_5.addWidget(self.label_26, 1, 0, 1, 1)

        self.pushButton_12 = QPushButton(self.widget_28)
        self.pushButton_12.setObjectName(u"pushButton_12")
        sizePolicy1.setHeightForWidth(self.pushButton_12.sizePolicy().hasHeightForWidth())
        self.pushButton_12.setSizePolicy(sizePolicy1)
        self.pushButton_12.setIcon(icon8)
        self.pushButton_12.setAutoDefault(False)

        self.gridLayout_5.addWidget(self.pushButton_12, 0, 2, 1, 1)

        self.label_27 = QLabel(self.widget_28)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font1)
        self.label_27.setTextFormat(Qt.AutoText)
        self.label_27.setScaledContents(False)
        self.label_27.setWordWrap(False)

        self.gridLayout_5.addWidget(self.label_27, 0, 0, 1, 2)


        self.verticalLayout_26.addWidget(self.widget_28, 0, Qt.AlignTop)

        self.widget_29 = QWidget(self.widget_27)
        self.widget_29.setObjectName(u"widget_29")
        self.verticalLayout_27 = QVBoxLayout(self.widget_29)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 2, 2)
        self.textBrowser_5 = QTextBrowser(self.widget_29)
        self.textBrowser_5.setObjectName(u"textBrowser_5")

        self.verticalLayout_27.addWidget(self.textBrowser_5)


        self.verticalLayout_26.addWidget(self.widget_29)


        self.horizontalLayout_12.addWidget(self.widget_27)


        self.verticalLayout_7.addWidget(self.widget_25)

        self.widget_20 = QWidget(self.scrollAreaWidgetContents)
        self.widget_20.setObjectName(u"widget_20")
        self.widget_20.setMinimumSize(QSize(0, 0))
        self.widget_20.setMaximumSize(QSize(16777215, 16777215))
        self.widget_20.setStyleSheet(u"background-color: rgb(150, 150, 150);")
        self.horizontalLayout_11 = QHBoxLayout(self.widget_20)
        self.horizontalLayout_11.setSpacing(7)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.widget_21 = QWidget(self.widget_20)
        self.widget_21.setObjectName(u"widget_21")
        self.verticalLayout_22 = QVBoxLayout(self.widget_21)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.widget_21)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(170, 100))
        self.label_13.setStyleSheet(u"")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.label_13)


        self.horizontalLayout_11.addWidget(self.widget_21, 0, Qt.AlignLeft)

        self.widget_22 = QWidget(self.widget_20)
        self.widget_22.setObjectName(u"widget_22")
        self.widget_22.setMinimumSize(QSize(0, 0))
        self.verticalLayout_23 = QVBoxLayout(self.widget_22)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(-1, 0, 2, 0)
        self.widget_23 = QWidget(self.widget_22)
        self.widget_23.setObjectName(u"widget_23")
        self.gridLayout_4 = QGridLayout(self.widget_23)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setVerticalSpacing(0)
        self.gridLayout_4.setContentsMargins(0, 0, 0, -1)
        self.pushButton_11 = QPushButton(self.widget_23)
        self.pushButton_11.setObjectName(u"pushButton_11")
        sizePolicy1.setHeightForWidth(self.pushButton_11.sizePolicy().hasHeightForWidth())
        self.pushButton_11.setSizePolicy(sizePolicy1)
        self.pushButton_11.setIcon(icon8)
        self.pushButton_11.setAutoDefault(False)

        self.gridLayout_4.addWidget(self.pushButton_11, 0, 2, 1, 1)

        self.label_24 = QLabel(self.widget_23)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_4.addWidget(self.label_24, 1, 0, 1, 1)

        self.label_14 = QLabel(self.widget_23)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font1)
        self.label_14.setTextFormat(Qt.AutoText)
        self.label_14.setScaledContents(False)
        self.label_14.setWordWrap(False)

        self.gridLayout_4.addWidget(self.label_14, 0, 0, 1, 2)


        self.verticalLayout_23.addWidget(self.widget_23, 0, Qt.AlignTop)

        self.widget_24 = QWidget(self.widget_22)
        self.widget_24.setObjectName(u"widget_24")
        self.verticalLayout_24 = QVBoxLayout(self.widget_24)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 2, 2)
        self.textBrowser_4 = QTextBrowser(self.widget_24)
        self.textBrowser_4.setObjectName(u"textBrowser_4")

        self.verticalLayout_24.addWidget(self.textBrowser_4)


        self.verticalLayout_23.addWidget(self.widget_24)


        self.horizontalLayout_11.addWidget(self.widget_22)


        self.verticalLayout_7.addWidget(self.widget_20)

        self.widget_19 = QWidget(self.scrollAreaWidgetContents)
        self.widget_19.setObjectName(u"widget_19")
        self.widget_19.setMinimumSize(QSize(0, 0))
        self.widget_19.setMaximumSize(QSize(16777215, 16777215))
        self.widget_19.setStyleSheet(u"background-color: rgb(150, 150, 150);")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_19)
        self.horizontalLayout_6.setSpacing(7)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.widget_7 = QWidget(self.widget_19)
        self.widget_7.setObjectName(u"widget_7")
        self.verticalLayout_11 = QVBoxLayout(self.widget_7)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.widget_7)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(170, 100))
        self.label_3.setStyleSheet(u"")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_3)


        self.horizontalLayout_6.addWidget(self.widget_7, 0, Qt.AlignLeft)

        self.widget_8 = QWidget(self.widget_19)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setMinimumSize(QSize(0, 0))
        self.verticalLayout_12 = QVBoxLayout(self.widget_8)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(-1, 0, 2, 0)
        self.widget_10 = QWidget(self.widget_8)
        self.widget_10.setObjectName(u"widget_10")
        self.gridLayout = QGridLayout(self.widget_10)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, -1)
        self.label_6 = QLabel(self.widget_10)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)

        self.pushButton_7 = QPushButton(self.widget_10)
        self.pushButton_7.setObjectName(u"pushButton_7")
        sizePolicy1.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy1)
        self.pushButton_7.setIcon(icon8)
        self.pushButton_7.setAutoDefault(False)

        self.gridLayout.addWidget(self.pushButton_7, 0, 2, 1, 1)

        self.label_4 = QLabel(self.widget_10)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setTextFormat(Qt.AutoText)
        self.label_4.setScaledContents(False)
        self.label_4.setWordWrap(False)

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 2)


        self.verticalLayout_12.addWidget(self.widget_10, 0, Qt.AlignTop)

        self.widget_9 = QWidget(self.widget_8)
        self.widget_9.setObjectName(u"widget_9")
        self.verticalLayout_15 = QVBoxLayout(self.widget_9)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 2, 2)
        self.textBrowser = QTextBrowser(self.widget_9)
        self.textBrowser.setObjectName(u"textBrowser")

        self.verticalLayout_15.addWidget(self.textBrowser)


        self.verticalLayout_12.addWidget(self.widget_9)


        self.horizontalLayout_6.addWidget(self.widget_8)


        self.verticalLayout_7.addWidget(self.widget_19)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_9.addWidget(self.scrollArea)

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
        self.pushButton_5.setToolTip(QCoreApplication.translate("MainWindow", u"Lessons", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_5.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_3.setToolTip(QCoreApplication.translate("MainWindow", u"LogOut", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_3.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Lessons", None))
        self.pushButton_4.setText("")
        self.searchBtn_2.setText("")
        self.searchLine_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search...", None))
        self.pushButton_45.setText(QCoreApplication.translate("MainWindow", u"\u0393\u03c1\u03b1\u03bc\u03bc\u03b9\u03ba\u03ae \u0386\u03bb\u03b3\u03b5\u03b2\u03c1\u03b1", None))
        self.pushButton_47.setText(QCoreApplication.translate("MainWindow", u"\u0395\u03b9\u03c3\u03b1\u03b3\u03c9\u03b3\u03ae \u03c3\u03c4\u03bf\u03c5\u03c2 \u0391\u03bb\u03b3\u03bf\u03c1\u03af\u03b8\u03bc\u03bf\u03c5\u03c2", None))
        self.pushButton_46.setText(QCoreApplication.translate("MainWindow", u"\u0398\u03b5\u03c9\u03c1\u03af\u03b1 \u03a3\u03b7\u03bc\u03ac\u03c4\u03c9\u03bd \u03ba\u03b1\u03b9 \u03a3\u03c5\u03c3\u03c4\u03b7\u03bc\u03ac\u03c4\u03c9\u03bd", None))
        self.pushButton_44.setText(QCoreApplication.translate("MainWindow", u"\u0394\u03b9\u03b1\u03ba\u03c1\u03b9\u03c4\u03ac \u039c\u03b1\u03b8\u03b7\u03bc\u03b1\u03c4\u03b9\u03ba\u03ac", None))
        self.pushButton_43.setText(QCoreApplication.translate("MainWindow", u"\u0393\u03b5\u03bd\u03b9\u03ba\u03ac \u039c\u03b1\u03b8\u03b7\u03bc\u03b1\u03c4\u03b9\u03ba\u03ac \u0399", None))
        self.pushButton_42.setText(QCoreApplication.translate("MainWindow", u"\u0391\u03c1\u03c7\u03b9\u03c4\u03b5\u03ba\u03c4\u03bf\u03bd\u03b9\u03ba\u03ae \u03a5\u03c0\u03bf\u03bb\u03bf\u03b3\u03b9\u03c3\u03c4\u03ce\u03bd", None))
        self.pushButton_41.setText(QCoreApplication.translate("MainWindow", u"\u039b\u03bf\u03b3\u03b9\u03ba\u03ae \u03a3\u03c7\u03b5\u03b4\u03af\u03b1\u03c3\u03b7", None))
        self.pushButton_40.setText(QCoreApplication.translate("MainWindow", u"\u0393\u03b5\u03bd\u03b9\u03ba\u03ac \u039c\u03b1\u03b8\u03b7\u03bc\u03b1\u03c4\u03b9\u03ba\u03ac \u0399\u0399", None))
        self.pushButton_39.setText(QCoreApplication.translate("MainWindow", u"\u0398\u03b5\u03c9\u03c1\u03af\u03b1 \u03a5\u03c0\u03bf\u03bb\u03bf\u03b3\u03b9\u03c3\u03bc\u03bf\u03cd", None))
        self.pushButton_48.setText(QCoreApplication.translate("MainWindow", u"\u0394\u03b9\u03b1\u03ba\u03c1\u03b9\u03c4\u03ac \u039c\u03b1\u03b8\u03b7\u03bc\u03b1\u03c4\u03b9\u03ba\u03ac", None))
        self.pushButton_38.setText(QCoreApplication.translate("MainWindow", u"\u03a4\u03b5\u03c7\u03bd\u03bf\u03bb\u03bf\u03b3\u03af\u03b1 \u039b\u03bf\u03b3\u03b9\u03c3\u03bc\u03b9\u03ba\u03bf\u03cd", None))
        self.pushButton_37.setText(QCoreApplication.translate("MainWindow", u"\u0398\u03b5\u03c9\u03c1\u03af\u03b1 \u0393\u03c1\u03b1\u03c6\u03b7\u03bc\u03ac\u03c4\u03c9\u03bd", None))
        self.pushButton_36.setText(QCoreApplication.translate("MainWindow", u"\u0391\u03c1\u03b9\u03b8\u03bc\u03b7\u03c4\u03b9\u03ba\u03ae \u0391\u03bd\u03ac\u03bb\u03c5\u03c3\u03b7 \u03ba\u03b1\u03b9 \u03a0\u03b5\u03c1\u03b9\u03b2\u03ac\u03bb\u03bb\u03bf\u03bd\u03c4\u03b1 \u03a5\u03c0\u03bf\u03bb\u03bf\u03c0\u03bf\u03af\u03b7\u03c3\u03b7\u03c2", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Reported Posts", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Upload Confirmation", None))
#if QT_CONFIG(whatsthis)
        self.label_34.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/material_design/icons/material_design/unsplash_IyaNci0CyRk.png\"/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_34.setText("")
        self.pushButton_15.setText("")
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
#if QT_CONFIG(whatsthis)
        self.label_31.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/material_design/icons/material_design/unsplash_IyaNci0CyRk.png\"/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_31.setText("")
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"18/04/2025", None))
        self.pushButton_14.setText("")
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"\u0393\u03c1\u03b1\u03bc\u03bc\u03b9\u03ba\u03ae \u0386\u03bb\u03b3\u03b5\u03b2\u03c1\u03b1 \u2013 \u03a0\u03b9\u03b8\u03b1\u03bd\u03ac \u0398\u03ad\u03bc\u03b1\u03c4\u03b1 \u0395\u03be\u03b5\u03c4\u03ac\u03c3\u03b5\u03c9\u03bd", None))
        self.textBrowser_7.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">\u0391\u03bd\u03b1\u03c1\u03c4\u03ae\u03b8\u03b7\u03ba\u03b5 \u03bb\u03af\u03c3\u03c4\u03b1 \u03bc\u03b5 \u03b5\u03bd\u03b4\u03b5\u03b9\u03ba\u03c4\u03b9\u03ba\u03ac \u03b8\u03ad\u03bc\u03b1\u03c4\u03b1 \u03c0\u03bf\u03c5 \u03c0\u03b9\u03b8\u03b1\u03bd\u03cc\u03bd \u03bd\u03b1 \u03b5\u03bc\u03c6\u03b1\u03bd\u03b9\u03c3\u03c4\u03bf\u03cd\u03bd \u03c3\u03c4"
                        "\u03b7\u03bd \u03c4\u03b5\u03bb\u03b9\u03ba\u03ae \u03b5\u03be\u03ad\u03c4\u03b1\u03c3\u03b7 \u03c4\u03bf\u03c5 \u03bc\u03b1\u03b8\u03ae\u03bc\u03b1\u03c4\u03bf\u03c2. \u03a0\u03b5\u03c1\u03b9\u03bb\u03b1\u03bc\u03b2\u03ac\u03bd\u03bf\u03bd\u03c4\u03b1\u03b9 \u03b1\u03c3\u03ba\u03ae\u03c3\u03b5\u03b9\u03c2 \u03c0\u03ac\u03bd\u03c9 \u03c3\u03b5 \u03c3\u03c5\u03c3\u03c4\u03ae\u03bc\u03b1\u03c4\u03b1 \u03b3\u03c1\u03b1\u03bc\u03bc\u03b9\u03ba\u03ce\u03bd \u03b5\u03be\u03b9\u03c3\u03ce\u03c3\u03b5\u03c9\u03bd, \u03b9\u03b4\u03b9\u03bf\u03c4\u03b9\u03bc\u03ad\u03c2 \u03ba\u03b1\u03b9 \u03b9\u03b4\u03b9\u03bf\u03b4\u03b9\u03b1\u03bd\u03cd\u03c3\u03bc\u03b1\u03c4\u03b1, \u03bf\u03c1\u03b8\u03bf\u03b3\u03ce\u03bd\u03b9\u03b5\u03c2 \u03c0\u03c1\u03bf\u03b2\u03bf\u03bb\u03ad\u03c2 \u03ba\u03b1\u03b9 \u03b4\u03b9\u03b1\u03b3\u03c9\u03bd\u03b9\u03bf\u03c0\u03bf\u03af\u03b7\u03c3\u03b7 \u03c0\u03af\u03bd\u03b1\u03ba\u03c9\u03bd. \u0397 \u03b5\u03be\u03ac\u03c3\u03ba\u03b7\u03c3\u03b7 \u03c3\u03b5 \u03b1\u03c5\u03c4\u03ac \u03c4"
                        "\u03b1 \u03b8\u03ad\u03bc\u03b1\u03c4\u03b1 \u03b8\u03b1 \u03b2\u03bf\u03b7\u03b8\u03ae\u03c3\u03b5\u03b9 \u03c3\u03b7\u03bc\u03b1\u03bd\u03c4\u03b9\u03ba\u03ac \u03c3\u03c4\u03b7\u03bd \u03ba\u03b1\u03c4\u03b1\u03bd\u03cc\u03b7\u03c3\u03b7 \u03c4\u03c9\u03bd \u03b2\u03b1\u03c3\u03b9\u03ba\u03ce\u03bd \u03b5\u03bd\u03bd\u03bf\u03b9\u03ce\u03bd \u03ba\u03b1\u03b9 \u03c3\u03c4\u03b7 \u03c3\u03c9\u03c3\u03c4\u03ae \u03c0\u03c1\u03bf\u03b5\u03c4\u03bf\u03b9\u03bc\u03b1\u03c3\u03af\u03b1 \u03b3\u03b9\u03b1 \u03c4\u03b7\u03bd \u03b5\u03be\u03ad\u03c4\u03b1\u03c3\u03b7. \u03a3\u03c5\u03bd\u03b9\u03c3\u03c4\u03ac\u03c4\u03b1\u03b9 \u03b7 \u03c3\u03c5\u03b6\u03ae\u03c4\u03b7\u03c3\u03b7 \u03b1\u03c0\u03bf\u03c1\u03b9\u03ce\u03bd \u03c3\u03c4\u03bf \u03b5\u03c0\u03cc\u03bc\u03b5\u03bd\u03bf \u03b5\u03c1\u03b3\u03b1\u03c3\u03c4\u03ae\u03c1\u03b9\u03bf \u03ae \u03bc\u03ad\u03c3\u03c9 \u03c4\u03bf\u03c5 chat.</span></p></body></html>", None))
#if QT_CONFIG(whatsthis)
        self.label_28.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/material_design/icons/material_design/unsplash_IyaNci0CyRk.png\"/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_28.setText("")
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"18/04/2025", None))
        self.pushButton_13.setText("")
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"\u0393\u03c1\u03b1\u03bc\u03bc\u03b9\u03ba\u03ae \u0386\u03bb\u03b3\u03b5\u03b2\u03c1\u03b1 \u2013 \u03a0\u03bf\u03bb\u03bb\u03b1\u03c0\u03bb\u03b1\u03c3\u03b9\u03b1\u03c3\u03bc\u03cc\u03c2 \u039c\u03b7\u03c4\u03c1\u03c9\u03ce\u03bd", None))
        self.textBrowser_6.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">\u039d\u03ad\u03b1 \u03b4\u03b7\u03bc\u03bf\u03c3\u03af\u03b5\u03c5\u03c3\u03b7 \u03bc\u03b5 \u03b8\u03b5\u03c9\u03c1\u03af\u03b1 \u03ba\u03b1\u03b9 \u03c0\u03b1\u03c1\u03b1\u03b4\u03b5\u03af\u03b3\u03bc\u03b1\u03c4\u03b1 \u03b3\u03b9\u03b1 \u03c4\u03bf\u03bd \u03c0\u03bf\u03bb\u03bb\u03b1\u03c0\u03bb\u03b1\u03c3\u03b9\u03b1\u03c3\u03bc\u03cc \u03bc\u03b7"
                        "\u03c4\u03c1\u03c9\u03ce\u03bd, \u03bc\u03b9\u03b1 \u03b2\u03b1\u03c3\u03b9\u03ba\u03ae \u03ad\u03bd\u03bd\u03bf\u03b9\u03b1 \u03c4\u03b7\u03c2 \u03b3\u03c1\u03b1\u03bc\u03bc\u03b9\u03ba\u03ae\u03c2 \u03ac\u03bb\u03b3\u03b5\u03b2\u03c1\u03b1\u03c2 \u03bc\u03b5 \u03b5\u03c5\u03c1\u03b5\u03af\u03b1 \u03b5\u03c6\u03b1\u03c1\u03bc\u03bf\u03b3\u03ae \u03c3\u03b5 \u03bc\u03b1\u03b8\u03b7\u03bc\u03b1\u03c4\u03b9\u03ba\u03ac, \u03c6\u03c5\u03c3\u03b9\u03ba\u03ae \u03ba\u03b1\u03b9 \u03c5\u03c0\u03bf\u03bb\u03bf\u03b3\u03b9\u03c3\u03c4\u03b9\u03ba\u03ac \u03c3\u03c5\u03c3\u03c4\u03ae\u03bc\u03b1\u03c4\u03b1. \u03a4\u03bf \u03c5\u03bb\u03b9\u03ba\u03cc \u03c0\u03b5\u03c1\u03b9\u03bb\u03b1\u03bc\u03b2\u03ac\u03bd\u03b5\u03b9 \u03bf\u03b4\u03b7\u03b3\u03af\u03b5\u03c2 \u03b3\u03b9\u03b1 \u03c4\u03bf\u03bd \u03c5\u03c0\u03bf\u03bb\u03bf\u03b3\u03b9\u03c3\u03bc\u03cc \u03c4\u03bf\u03c5 \u03b3\u03b9\u03bd\u03bf\u03bc\u03ad\u03bd\u03bf\u03c5 \u03b4\u03cd\u03bf \u03bc\u03b7\u03c4\u03c1\u03c9\u03ce\u03bd, \u03c4\u03b9\u03c2 \u03c3"
                        "\u03c5\u03bd\u03b8\u03ae\u03ba\u03b5\u03c2 \u03c5\u03c0\u03cc \u03c4\u03b9\u03c2 \u03bf\u03c0\u03bf\u03af\u03b5\u03c2 \u03b5\u03af\u03bd\u03b1\u03b9 \u03b4\u03c5\u03bd\u03b1\u03c4\u03cc\u03c2 \u03bf \u03c0\u03bf\u03bb\u03bb\u03b1\u03c0\u03bb\u03b1\u03c3\u03b9\u03b1\u03c3\u03bc\u03cc\u03c2, \u03ba\u03b1\u03b8\u03ce\u03c2 \u03ba\u03b1\u03b9 \u03b1\u03c3\u03ba\u03ae\u03c3\u03b5\u03b9\u03c2 \u03bc\u03b5 \u03bb\u03cd\u03c3\u03b5\u03b9\u03c2 \u03b3\u03b9\u03b1 \u03b5\u03be\u03ac\u03c3\u03ba\u03b7\u03c3\u03b7. \u0395\u03af\u03bd\u03b1\u03b9 \u03b9\u03b4\u03b9\u03b1\u03af\u03c4\u03b5\u03c1\u03b1 \u03c7\u03c1\u03ae\u03c3\u03b9\u03bc\u03bf \u03b3\u03b9\u03b1 \u03c4\u03b7\u03bd \u03ba\u03b1\u03c4\u03b1\u03bd\u03cc\u03b7\u03c3\u03b7 \u03b5\u03bd\u03bd\u03bf\u03b9\u03ce\u03bd \u03cc\u03c0\u03c9\u03c2 \u03bf\u03b9 \u03b3\u03c1\u03b1\u03bc\u03bc\u03b9\u03ba\u03bf\u03af \u03bc\u03b5\u03c4\u03b1\u03c3\u03c7\u03b7\u03bc\u03b1\u03c4\u03b9\u03c3\u03bc\u03bf\u03af \u03ba\u03b1\u03b9 \u03b7 \u03c3\u03cd\u03bd\u03b8\u03b5\u03c3\u03b7"
                        " \u03c0\u03c1\u03ac\u03be\u03b5\u03c9\u03bd.</span></p></body></html>", None))
#if QT_CONFIG(whatsthis)
        self.label_25.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/material_design/icons/material_design/unsplash_IyaNci0CyRk.png\"/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_25.setText("")
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"18/04/2025", None))
        self.pushButton_12.setText("")
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"\u0393\u03c1\u03b1\u03bc\u03bc\u03b9\u03ba\u03ae \u0386\u03bb\u03b3\u03b5\u03b2\u03c1\u03b1 \u2013 \u039c\u03ad\u03b8\u03bf\u03b4\u03bf\u03b9 \u03a0\u03bf\u03bb\u03bb\u03b1\u03c0\u03bb\u03b1\u03c3\u03b9\u03b1\u03c3\u03bc\u03bf\u03cd \u039c\u03b7\u03c4\u03c1\u03c9\u03ce\u03bd", None))
        self.textBrowser_5.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">\u0391\u03bd\u03b1\u03c1\u03c4\u03ae\u03b8\u03b7\u03ba\u03b5 \u03bd\u03ad\u03bf \u03c5\u03bb\u03b9\u03ba\u03cc \u03c0\u03bf\u03c5 \u03c0\u03b1\u03c1\u03bf\u03c5\u03c3\u03b9\u03ac\u03b6\u03b5\u03b9 \u03b1\u03bd\u03b1\u03bb\u03c5\u03c4\u03b9\u03ba\u03ac \u03c4\u03b9\u03c2 \u03b2\u03b1\u03c3\u03b9\u03ba\u03ad\u03c2 \u03bc\u03b5\u03b8\u03cc\u03b4\u03bf\u03c5"
                        "\u03c2 \u03c0\u03bf\u03bb\u03bb\u03b1\u03c0\u03bb\u03b1\u03c3\u03b9\u03b1\u03c3\u03bc\u03bf\u03cd \u03bc\u03b7\u03c4\u03c1\u03c9\u03ce\u03bd, \u03c4\u03cc\u03c3\u03bf \u03c3\u03b5 \u03b8\u03b5\u03c9\u03c1\u03b7\u03c4\u03b9\u03ba\u03cc \u03b5\u03c0\u03af\u03c0\u03b5\u03b4\u03bf \u03cc\u03c3\u03bf \u03ba\u03b1\u03b9 \u03bc\u03b5 \u03c0\u03c1\u03b1\u03ba\u03c4\u03b9\u03ba\u03ac \u03c0\u03b1\u03c1\u03b1\u03b4\u03b5\u03af\u03b3\u03bc\u03b1\u03c4\u03b1. \u03a0\u03b5\u03c1\u03b9\u03bb\u03b1\u03bc\u03b2\u03ac\u03bd\u03bf\u03bd\u03c4\u03b1\u03b9 \u03b7 \u03ba\u03bb\u03b1\u03c3\u03b9\u03ba\u03ae \u03bc\u03ad\u03b8\u03bf\u03b4\u03bf\u03c2 \u03b3\u03c1\u03b1\u03bc\u03bc\u03ce\u03bd-\u03c3\u03c4\u03b7\u03bb\u03ce\u03bd, \u03b7 \u03c7\u03c1\u03ae\u03c3\u03b7 \u03b9\u03b4\u03b9\u03bf\u03c4\u03ae\u03c4\u03c9\u03bd \u03b3\u03b9\u03b1 \u03b1\u03c0\u03bb\u03bf\u03c0\u03bf\u03af\u03b7\u03c3\u03b7 \u03c5\u03c0\u03bf\u03bb\u03bf\u03b3\u03b9\u03c3\u03bc\u03ce\u03bd, \u03ba\u03b1\u03b8\u03ce\u03c2 \u03ba\u03b1\u03b9 \u03bc\u03b9\u03b1"
                        " \u03b5\u03b9\u03c3\u03b1\u03b3\u03c9\u03b3\u03ae \u03c3\u03b5 \u03c0\u03b9\u03bf \u03b1\u03c0\u03bf\u03b4\u03bf\u03c4\u03b9\u03ba\u03bf\u03cd\u03c2 \u03b1\u03bb\u03b3\u03bf\u03c1\u03af\u03b8\u03bc\u03bf\u03c5\u03c2 \u03cc\u03c0\u03c9\u03c2 \u03bf Strassen. \u03a4\u03bf \u03c5\u03bb\u03b9\u03ba\u03cc \u03b5\u03af\u03bd\u03b1\u03b9 \u03b9\u03b4\u03b1\u03bd\u03b9\u03ba\u03cc \u03b3\u03b9\u03b1 \u03c4\u03b7\u03bd \u03b5\u03bc\u03b2\u03ac\u03b8\u03c5\u03bd\u03c3\u03b7 \u03c3\u03c4\u03b7\u03bd \u03ad\u03bd\u03bd\u03bf\u03b9\u03b1 \u03c4\u03bf\u03c5 \u03c0\u03bf\u03bb\u03bb\u03b1\u03c0\u03bb\u03b1\u03c3\u03b9\u03b1\u03c3\u03bc\u03bf\u03cd \u03ba\u03b1\u03b9 \u03c4\u03b7 \u03c3\u03cd\u03bd\u03b4\u03b5\u03c3\u03ae \u03c4\u03bf\u03c5 \u03bc\u03b5 \u03b5\u03c6\u03b1\u03c1\u03bc\u03bf\u03b3\u03ad\u03c2 \u03c3\u03c4\u03b7 \u03b3\u03c1\u03b1\u03bc\u03bc\u03b9\u03ba\u03ae \u03b1\u03c0\u03b5\u03b9\u03ba\u03cc\u03bd\u03b9\u03c3\u03b7 \u03ba\u03b1\u03b9 \u03c4\u03b7\u03bd \u03b1\u03c1\u03b9\u03b8\u03bc\u03b7\u03c4\u03b9\u03ba\u03ae"
                        " \u03b1\u03bd\u03ac\u03bb\u03c5\u03c3\u03b7. \u03a0\u03c1\u03bf\u03c4\u03b5\u03af\u03bd\u03b5\u03c4\u03b1\u03b9 \u03b3\u03b9\u03b1 \u03c0\u03c1\u03bf\u03b5\u03c4\u03bf\u03b9\u03bc\u03b1\u03c3\u03af\u03b1 \u03b5\u03bd\u03cc\u03c8\u03b5\u03b9 \u03c4\u03b7\u03c2 \u03c4\u03b5\u03bb\u03b9\u03ba\u03ae\u03c2 \u03b5\u03be\u03ad\u03c4\u03b1\u03c3\u03b7\u03c2.</span></p></body></html>", None))
#if QT_CONFIG(whatsthis)
        self.label_13.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/material_design/icons/material_design/unsplash_IyaNci0CyRk.png\"/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_13.setText("")
        self.pushButton_11.setText("")
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"18/04/2025", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u0394\u03b9\u03b1\u03b3\u03c9\u03bd\u03bf\u03c0\u03bf\u03af\u03b7\u03c3\u03b7 \u03a0\u03b9\u03bd\u03ac\u03ba\u03c9\u03bd", None))
        self.textBrowser_4.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">\u0394\u03b7\u03bc\u03bf\u03c3\u03b9\u03b5\u03cd\u03c4\u03b7\u03ba\u03b5 \u03bd\u03ad\u03bf \u03c5\u03bb\u03b9\u03ba\u03cc \u03c0\u03bf\u03c5 \u03b1\u03c6\u03bf\u03c1\u03ac \u03c4\u03b7 \u03b4\u03b9\u03b1\u03b4\u03b9\u03ba\u03b1\u03c3\u03af\u03b1 \u03b4\u03b9\u03b1\u03b3\u03c9\u03bd\u03bf\u03c0\u03bf\u03af\u03b7\u03c3\u03b7\u03c2 \u03c0\u03b9\u03bd\u03ac"
                        "\u03ba\u03c9\u03bd, \u03bc\u03b9\u03b1 \u03b1\u03c0\u03cc \u03c4\u03b9\u03c2 \u03c3\u03b7\u03bc\u03b1\u03bd\u03c4\u03b9\u03ba\u03cc\u03c4\u03b5\u03c1\u03b5\u03c2 \u03c4\u03b5\u03c7\u03bd\u03b9\u03ba\u03ad\u03c2 \u03c4\u03b7\u03c2 \u03b3\u03c1\u03b1\u03bc\u03bc\u03b9\u03ba\u03ae\u03c2 \u03ac\u03bb\u03b3\u03b5\u03b2\u03c1\u03b1\u03c2 \u03bc\u03b5 \u03c0\u03bb\u03ae\u03b8\u03bf\u03c2 \u03b5\u03c6\u03b1\u03c1\u03bc\u03bf\u03b3\u03ce\u03bd \u03c3\u03b5 \u03c6\u03c5\u03c3\u03b9\u03ba\u03ad\u03c2 \u03b5\u03c0\u03b9\u03c3\u03c4\u03ae\u03bc\u03b5\u03c2, \u03bc\u03b7\u03c7\u03b1\u03bd\u03b9\u03ba\u03ae \u03ba\u03b1\u03b9 \u03c0\u03bb\u03b7\u03c1\u03bf\u03c6\u03bf\u03c1\u03b9\u03ba\u03ae. \u03a3\u03c4\u03bf \u03c5\u03bb\u03b9\u03ba\u03cc \u03c0\u03b1\u03c1\u03bf\u03c5\u03c3\u03b9\u03ac\u03b6\u03bf\u03bd\u03c4\u03b1\u03b9 \u03bf\u03b9 \u03c3\u03c5\u03bd\u03b8\u03ae\u03ba\u03b5\u03c2 \u03c5\u03c0\u03cc \u03c4\u03b9\u03c2 \u03bf\u03c0\u03bf\u03af\u03b5\u03c2 \u03ad\u03bd\u03b1\u03c2 \u03c0\u03af\u03bd\u03b1\u03ba\u03b1\u03c2"
                        " \u03b5\u03af\u03bd\u03b1\u03b9 \u03b4\u03b9\u03b1\u03b3\u03c9\u03bd\u03bf\u03c0\u03bf\u03b9\u03ae\u03c3\u03b9\u03bc\u03bf\u03c2, \u03bf \u03c1\u03cc\u03bb\u03bf\u03c2 \u03c4\u03c9\u03bd \u03b9\u03b4\u03b9\u03bf\u03c4\u03b9\u03bc\u03ce\u03bd \u03ba\u03b1\u03b9 \u03b9\u03b4\u03b9\u03bf\u03b4\u03b9\u03b1\u03bd\u03c5\u03c3\u03bc\u03ac\u03c4\u03c9\u03bd, \u03ba\u03b1\u03b8\u03ce\u03c2 \u03ba\u03b1\u03b9 \u03c0\u03b1\u03c1\u03b1\u03b4\u03b5\u03af\u03b3\u03bc\u03b1\u03c4\u03b1 \u03b2\u03ae\u03bc\u03b1-\u03b2\u03ae\u03bc\u03b1. \u0395\u03c0\u03b9\u03c0\u03bb\u03ad\u03bf\u03bd, \u03c0\u03b5\u03c1\u03b9\u03bb\u03b1\u03bc\u03b2\u03ac\u03bd\u03bf\u03bd\u03c4\u03b1\u03b9 \u03c3\u03cd\u03bd\u03c4\u03bf\u03bc\u03b5\u03c2 \u03b8\u03b5\u03c9\u03c1\u03b7\u03c4\u03b9\u03ba\u03ad\u03c2 \u03b5\u03c0\u03b1\u03bd\u03b1\u03bb\u03ae\u03c8\u03b5\u03b9\u03c2 \u03ba\u03b1\u03b9 \u03b1\u03c3\u03ba\u03ae\u03c3\u03b5\u03b9\u03c2 \u03b3\u03b9\u03b1 \u03b5\u03be\u03ac\u03c3\u03ba\u03b7\u03c3\u03b7. \u0397 \u03ba\u03b1\u03c4\u03b1\u03bd\u03cc"
                        "\u03b7\u03c3\u03b7 \u03c4\u03b7\u03c2 \u03b4\u03b9\u03b1\u03b3\u03c9\u03bd\u03bf\u03c0\u03bf\u03af\u03b7\u03c3\u03b7\u03c2 \u03b5\u03af\u03bd\u03b1\u03b9 \u03b8\u03b5\u03bc\u03b5\u03bb\u03b9\u03ce\u03b4\u03b7\u03c2 \u03b3\u03b9\u03b1 \u03c4\u03b7\u03bd \u03b1\u03bd\u03ac\u03bb\u03c5\u03c3\u03b7 \u03b4\u03c5\u03bd\u03b1\u03bc\u03b9\u03ba\u03ce\u03bd \u03c3\u03c5\u03c3\u03c4\u03b7\u03bc\u03ac\u03c4\u03c9\u03bd \u03ba\u03b1\u03b9 \u03c4\u03b7 \u03bb\u03cd\u03c3\u03b7 \u03b4\u03b9\u03b1\u03c6\u03bf\u03c1\u03b9\u03ba\u03ce\u03bd \u03b5\u03be\u03b9\u03c3\u03ce\u03c3\u03b5\u03c9\u03bd.</span></p></body></html>", None))
#if QT_CONFIG(whatsthis)
        self.label_3.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/material_design/icons/material_design/unsplash_IyaNci0CyRk.png\"/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_3.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"18/04/2025", None))
        self.pushButton_7.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0393\u03c1\u03b1\u03bc\u03bc\u03b9\u03ba\u03ae \u0386\u03bb\u03b3\u03b5\u03b2\u03c1\u03b1 \u2013 \u0399\u03b4\u03b9\u03bf\u03c4\u03b9\u03bc\u03ad\u03c2 \u03ba\u03b1\u03b9 \u0399\u03b4\u03b9\u03bf\u03b4\u03b9\u03b1\u03bd\u03cd\u03c3\u03bc\u03b1\u03c4\u03b1", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">\u039d\u03ad\u03b1 \u03b1\u03bd\u03ac\u03c1\u03c4\u03b7\u03c3\u03b7 \u03bc\u03b5 \u03b5\u03c0\u03b9\u03ba\u03b5\u03bd\u03c4\u03c1\u03c9\u03bc\u03ad\u03bd\u03b7 \u03c0\u03b1\u03c1\u03bf\u03c5\u03c3\u03af\u03b1\u03c3\u03b7 \u03c3\u03c4\u03b9\u03c2 \u03b9\u03b4\u03b9\u03bf\u03c4\u03b9\u03bc\u03ad\u03c2 \u03ba\u03b1\u03b9 \u03c4\u03b1 \u03b9\u03b4\u03b9\u03bf"
                        "\u03b4\u03b9\u03b1\u03bd\u03cd\u03c3\u03bc\u03b1\u03c4\u03b1, \u03ad\u03bd\u03bd\u03bf\u03b9\u03b5\u03c2-\u03ba\u03bb\u03b5\u03b9\u03b4\u03b9\u03ac \u03b3\u03b9\u03b1 \u03c4\u03b7\u03bd \u03ba\u03b1\u03c4\u03b1\u03bd\u03cc\u03b7\u03c3\u03b7 \u03c4\u03b7\u03c2 \u03c3\u03c5\u03bc\u03c0\u03b5\u03c1\u03b9\u03c6\u03bf\u03c1\u03ac\u03c2 \u03b3\u03c1\u03b1\u03bc\u03bc\u03b9\u03ba\u03ce\u03bd \u03bc\u03b5\u03c4\u03b1\u03c3\u03c7\u03b7\u03bc\u03b1\u03c4\u03b9\u03c3\u03bc\u03ce\u03bd. \u03a3\u03c4\u03bf \u03c5\u03bb\u03b9\u03ba\u03cc \u03c0\u03b5\u03c1\u03b9\u03bb\u03b1\u03bc\u03b2\u03ac\u03bd\u03b5\u03c4\u03b1\u03b9 \u03b8\u03b5\u03c9\u03c1\u03af\u03b1, \u03b3\u03b5\u03c9\u03bc\u03b5\u03c4\u03c1\u03b9\u03ba\u03ae \u03b5\u03c1\u03bc\u03b7\u03bd\u03b5\u03af\u03b1, \u03ba\u03b1\u03b8\u03ce\u03c2 \u03ba\u03b1\u03b9 \u03bf\u03b4\u03b7\u03b3\u03af\u03b5\u03c2 \u03b3\u03b9\u03b1 \u03c4\u03bf\u03bd \u03c5\u03c0\u03bf\u03bb\u03bf\u03b3\u03b9\u03c3\u03bc\u03cc \u03c4\u03bf\u03c5\u03c2 \u03bc\u03ad\u03c3\u03b1 \u03b1\u03c0\u03cc "
                        "\u03c7\u03b1\u03c1\u03b1\u03ba\u03c4\u03b7\u03c1\u03b9\u03c3\u03c4\u03b9\u03ba\u03ac \u03c0\u03bf\u03bb\u03c5\u03ce\u03bd\u03c5\u03bc\u03b1. \u039f\u03b9 \u03b9\u03b4\u03b9\u03bf\u03c4\u03b9\u03bc\u03ad\u03c2 \u03ba\u03b1\u03b9 \u03c4\u03b1 \u03b9\u03b4\u03b9\u03bf\u03b4\u03b9\u03b1\u03bd\u03cd\u03c3\u03bc\u03b1\u03c4\u03b1 \u03ad\u03c7\u03bf\u03c5\u03bd \u03ba\u03c1\u03af\u03c3\u03b9\u03bc\u03b7 \u03c3\u03b7\u03bc\u03b1\u03c3\u03af\u03b1 \u03c3\u03b5 \u03c0\u03bb\u03b7\u03b8\u03ce\u03c1\u03b1 \u03b5\u03c6\u03b1\u03c1\u03bc\u03bf\u03b3\u03ce\u03bd, \u03cc\u03c0\u03c9\u03c2 \u03b7 \u03b4\u03b9\u03b1\u03b3\u03c9\u03bd\u03bf\u03c0\u03bf\u03af\u03b7\u03c3\u03b7, \u03b7 \u03c3\u03c4\u03b1\u03b8\u03b5\u03c1\u03cc\u03c4\u03b7\u03c4\u03b1 \u03c3\u03c5\u03c3\u03c4\u03b7\u03bc\u03ac\u03c4\u03c9\u03bd \u03ba\u03b1\u03b9 \u03b7 \u03b1\u03bd\u03ac\u03bb\u03c5\u03c3\u03b7 \u03b4\u03b5\u03b4\u03bf\u03bc\u03ad\u03bd\u03c9\u03bd (\u03c0.\u03c7. PCA). \u03a0\u03c1\u03bf\u03c4\u03b5\u03af\u03bd\u03b5\u03c4\u03b1\u03b9 \u03b7 \u03bc"
                        "\u03b5\u03bb\u03ad\u03c4\u03b7 \u03c4\u03bf\u03c5\u03c2 \u03c9\u03c2 \u03c0\u03c1\u03bf\u03b5\u03c4\u03bf\u03b9\u03bc\u03b1\u03c3\u03af\u03b1 \u03b3\u03b9\u03b1 \u03c4\u03b9\u03c2 \u03b5\u03be\u03b5\u03c4\u03ac\u03c3\u03b5\u03b9\u03c2 \u03ba\u03b1\u03b9 \u03b3\u03b9\u03b1 \u03c4\u03b7 \u03c3\u03cd\u03bd\u03b4\u03b5\u03c3\u03b7 \u03c4\u03b7\u03c2 \u03b8\u03b5\u03c9\u03c1\u03af\u03b1\u03c2 \u03bc\u03b5 \u03c0\u03c1\u03b1\u03ba\u03c4\u03b9\u03ba\u03ad\u03c2 \u03b5\u03c6\u03b1\u03c1\u03bc\u03bf\u03b3\u03ad\u03c2.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2';\"><br /></p></body></html>", None))
    # retranslateUi

