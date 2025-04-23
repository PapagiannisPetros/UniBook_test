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
        MainWindow.resize(1359, 734)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 70, 70);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(90, 10, 1211, 201))
        self.frame_2.setStyleSheet(u"background-color: rgb(12, 126, 124);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(280, 140, 131, 51))
        self.label_5.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.editProfBut = QPushButton(self.frame_2)
        self.editProfBut.setObjectName(u"editProfBut")
        self.editProfBut.setGeometry(QRect(860, 140, 151, 51))
        self.editProfBut.setStyleSheet(u"font: 11pt \"Sans Serif\";\n"
"background-color: rgb(8, 89, 82);")
        self.beyourself = QLabel(self.frame_2)
        self.beyourself.setObjectName(u"beyourself")
        self.beyourself.setGeometry(QRect(160, 0, 851, 131))
        self.beyourself.setPixmap(QPixmap(u"../images/beyourself.png"))
        self.beyourself.setScaledContents(True)
        self.profimage = QLabel(self.centralwidget)
        self.profimage.setObjectName(u"profimage")
        self.profimage.setGeometry(QRect(270, 90, 81, 81))
        self.profimage.setPixmap(QPixmap(u"../images/ProfileImage.png"))
        self.profimage.setScaledContents(True)
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(90, 220, 181, 501))
        self.frame_3.setStyleSheet(u"background-color: rgb(12, 126, 124);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 30, 91, 21))
        self.label_6.setStyleSheet(u"font: 10pt \"Sans Serif\";")
        self.label_7 = QLabel(self.frame_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(40, 80, 54, 17))
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
        self.label_12.setGeometry(QRect(40, 270, 141, 17))
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
        self.frame_4.setGeometry(QRect(280, 220, 1021, 501))
        self.frame_4.setStyleSheet(u"background-color: rgb(12, 126, 124);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.label_18 = QLabel(self.frame_4)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(20, 0, 111, 21))
        self.label_18.setStyleSheet(u"font: 11pt \"Sans Serif\";")
        self.label_19 = QLabel(self.frame_4)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(40, 30, 71, 21))
        self.label_19.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_20 = QLabel(self.frame_4)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(10, 30, 31, 17))
        self.label_20.setPixmap(QPixmap(u":/material_design/icons/material_design/sticky_note_2.png"))
        self.label_21 = QLabel(self.frame_4)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(560, 30, 81, 17))
        self.label_21.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_23 = QLabel(self.frame_4)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(530, 30, 21, 17))
        self.label_23.setPixmap(QPixmap(u":/material_design/icons/material_design/sticky_note_2.png"))
        self.scrollArea_3 = Widget(self.frame_4)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setGeometry(QRect(10, 50, 481, 441))
        self.scrollArea_3.setStyleSheet(u"background-color: rgb(0, 70, 70);")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, -25, 468, 450))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.widget_6 = QWidget(self.scrollAreaWidgetContents_3)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMinimumSize(QSize(450, 140))
        self.widget_6.setMaximumSize(QSize(300, 125))
        self.widget_6.setStyleSheet(u"background-color: rgb(150, 150, 150);")
        self.postimg3_6 = QLabel(self.widget_6)
        self.postimg3_6.setObjectName(u"postimg3_6")
        self.postimg3_6.setGeometry(QRect(0, 0, 61, 141))
        self.postimg3_6.setMinimumSize(QSize(0, 125))
        self.postimg3_6.setPixmap(QPixmap(u"../../../../../../../Downloads/Mask Group.png"))
        self.postimg3_6.setScaledContents(True)
        self.label_37 = QLabel(self.widget_6)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(70, 0, 351, 41))
        self.label_37.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.textBrowser_7 = QTextBrowser(self.widget_6)
        self.textBrowser_7.setObjectName(u"textBrowser_7")
        self.textBrowser_7.setGeometry(QRect(70, 50, 371, 81))
        self.label_38 = QLabel(self.widget_6)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setGeometry(QRect(70, 30, 71, 17))
        self.pushButton_14 = QPushButton(self.widget_6)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setGeometry(QRect(420, 0, 28, 24))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_14.sizePolicy().hasHeightForWidth())
        self.pushButton_14.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u":/feather/icons/feather/arrow-right.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_14.setIcon(icon)
        self.pushButton_14.setAutoDefault(False)

        self.verticalLayout_4.addWidget(self.widget_6)

        self.widget_7 = QWidget(self.scrollAreaWidgetContents_3)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMinimumSize(QSize(450, 140))
        self.widget_7.setMaximumSize(QSize(300, 125))
        self.widget_7.setStyleSheet(u"background-color: rgb(150, 150, 150);")
        self.postimg3_7 = QLabel(self.widget_7)
        self.postimg3_7.setObjectName(u"postimg3_7")
        self.postimg3_7.setGeometry(QRect(0, 0, 61, 141))
        self.postimg3_7.setMinimumSize(QSize(0, 125))
        self.postimg3_7.setPixmap(QPixmap(u"../../../../../../../Downloads/Mask Group.png"))
        self.postimg3_7.setScaledContents(True)
        self.label_39 = QLabel(self.widget_7)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setGeometry(QRect(70, 0, 351, 41))
        self.label_39.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.textBrowser_8 = QTextBrowser(self.widget_7)
        self.textBrowser_8.setObjectName(u"textBrowser_8")
        self.textBrowser_8.setGeometry(QRect(70, 50, 371, 81))
        self.label_40 = QLabel(self.widget_7)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setGeometry(QRect(70, 30, 71, 17))
        self.pushButton_15 = QPushButton(self.widget_7)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setGeometry(QRect(420, 0, 28, 24))
        sizePolicy.setHeightForWidth(self.pushButton_15.sizePolicy().hasHeightForWidth())
        self.pushButton_15.setSizePolicy(sizePolicy)
        self.pushButton_15.setIcon(icon)
        self.pushButton_15.setAutoDefault(False)

        self.verticalLayout_4.addWidget(self.widget_7)

        self.widget_5 = QWidget(self.scrollAreaWidgetContents_3)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMinimumSize(QSize(450, 140))
        self.widget_5.setMaximumSize(QSize(300, 125))
        self.widget_5.setStyleSheet(u"background-color: rgb(150, 150, 150);")
        self.postimg3_4 = QLabel(self.widget_5)
        self.postimg3_4.setObjectName(u"postimg3_4")
        self.postimg3_4.setGeometry(QRect(0, 0, 61, 141))
        self.postimg3_4.setMinimumSize(QSize(0, 125))
        self.postimg3_4.setPixmap(QPixmap(u"../../../../../../../Downloads/Mask Group.png"))
        self.postimg3_4.setScaledContents(True)
        self.label_33 = QLabel(self.widget_5)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(70, 0, 351, 41))
        self.label_33.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.textBrowser_5 = QTextBrowser(self.widget_5)
        self.textBrowser_5.setObjectName(u"textBrowser_5")
        self.textBrowser_5.setGeometry(QRect(70, 50, 371, 81))
        self.label_34 = QLabel(self.widget_5)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(70, 30, 71, 17))
        self.pushButton_16 = QPushButton(self.widget_5)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setGeometry(QRect(420, 0, 28, 24))
        sizePolicy.setHeightForWidth(self.pushButton_16.sizePolicy().hasHeightForWidth())
        self.pushButton_16.setSizePolicy(sizePolicy)
        self.pushButton_16.setIcon(icon)
        self.pushButton_16.setAutoDefault(False)

        self.verticalLayout_4.addWidget(self.widget_5)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.scrollArea_4 = Widget(self.frame_4)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setGeometry(QRect(530, 50, 481, 441))
        self.scrollArea_4.setStyleSheet(u"background-color: rgb(0, 70, 70);")
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, -25, 468, 450))
        self.verticalLayout_7 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.widget_8 = QWidget(self.scrollAreaWidgetContents_4)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setMinimumSize(QSize(450, 140))
        self.widget_8.setMaximumSize(QSize(300, 125))
        self.widget_8.setStyleSheet(u"background-color: rgb(150, 150, 150);")
        self.postimg3_8 = QLabel(self.widget_8)
        self.postimg3_8.setObjectName(u"postimg3_8")
        self.postimg3_8.setGeometry(QRect(0, 0, 61, 141))
        self.postimg3_8.setMinimumSize(QSize(0, 125))
        self.postimg3_8.setPixmap(QPixmap(u"../../../../../../../Downloads/Mask Group.png"))
        self.postimg3_8.setScaledContents(True)
        self.label_41 = QLabel(self.widget_8)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setGeometry(QRect(70, 0, 351, 41))
        self.label_41.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.textBrowser_9 = QTextBrowser(self.widget_8)
        self.textBrowser_9.setObjectName(u"textBrowser_9")
        self.textBrowser_9.setGeometry(QRect(70, 50, 371, 81))
        self.label_42 = QLabel(self.widget_8)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(70, 30, 71, 17))
        self.pushButton_17 = QPushButton(self.widget_8)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setGeometry(QRect(420, 0, 28, 24))
        sizePolicy.setHeightForWidth(self.pushButton_17.sizePolicy().hasHeightForWidth())
        self.pushButton_17.setSizePolicy(sizePolicy)
        self.pushButton_17.setIcon(icon)
        self.pushButton_17.setAutoDefault(False)

        self.verticalLayout_7.addWidget(self.widget_8)

        self.widget_9 = QWidget(self.scrollAreaWidgetContents_4)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setMinimumSize(QSize(450, 140))
        self.widget_9.setMaximumSize(QSize(300, 125))
        self.widget_9.setStyleSheet(u"background-color: rgb(150, 150, 150);")
        self.postimg3_9 = QLabel(self.widget_9)
        self.postimg3_9.setObjectName(u"postimg3_9")
        self.postimg3_9.setGeometry(QRect(0, 0, 61, 141))
        self.postimg3_9.setMinimumSize(QSize(0, 125))
        self.postimg3_9.setPixmap(QPixmap(u"../../../../../../../Downloads/Mask Group.png"))
        self.postimg3_9.setScaledContents(True)
        self.label_43 = QLabel(self.widget_9)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setGeometry(QRect(70, 0, 351, 41))
        self.label_43.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.textBrowser_10 = QTextBrowser(self.widget_9)
        self.textBrowser_10.setObjectName(u"textBrowser_10")
        self.textBrowser_10.setGeometry(QRect(70, 50, 371, 81))
        self.label_44 = QLabel(self.widget_9)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setGeometry(QRect(70, 30, 71, 17))
        self.pushButton_18 = QPushButton(self.widget_9)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setGeometry(QRect(420, 0, 28, 24))
        sizePolicy.setHeightForWidth(self.pushButton_18.sizePolicy().hasHeightForWidth())
        self.pushButton_18.setSizePolicy(sizePolicy)
        self.pushButton_18.setIcon(icon)
        self.pushButton_18.setAutoDefault(False)

        self.verticalLayout_7.addWidget(self.widget_9)

        self.widget_10 = QWidget(self.scrollAreaWidgetContents_4)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setMinimumSize(QSize(450, 140))
        self.widget_10.setMaximumSize(QSize(300, 125))
        self.widget_10.setStyleSheet(u"background-color: rgb(150, 150, 150);")
        self.postimg3_5 = QLabel(self.widget_10)
        self.postimg3_5.setObjectName(u"postimg3_5")
        self.postimg3_5.setGeometry(QRect(0, 0, 61, 141))
        self.postimg3_5.setMinimumSize(QSize(0, 125))
        self.postimg3_5.setPixmap(QPixmap(u"../../../../../../../Downloads/Mask Group.png"))
        self.postimg3_5.setScaledContents(True)
        self.textBrowser_6 = QTextBrowser(self.widget_10)
        self.textBrowser_6.setObjectName(u"textBrowser_6")
        self.textBrowser_6.setGeometry(QRect(70, 50, 371, 81))
        self.label_36 = QLabel(self.widget_10)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(70, 30, 71, 17))
        self.pushButton_19 = QPushButton(self.widget_10)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setGeometry(QRect(420, 0, 28, 24))
        sizePolicy.setHeightForWidth(self.pushButton_19.sizePolicy().hasHeightForWidth())
        self.pushButton_19.setSizePolicy(sizePolicy)
        self.pushButton_19.setIcon(icon)
        self.pushButton_19.setAutoDefault(False)
        self.label_45 = QLabel(self.widget_10)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setGeometry(QRect(70, 0, 351, 41))
        self.label_45.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_7.addWidget(self.widget_10)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)
        self.leftMenu = QFrame(self.centralwidget)
        self.leftMenu.setObjectName(u"leftMenu")
        self.leftMenu.setGeometry(QRect(0, 0, 37, 734))
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
        self.menuBtn = QPushButton(self.widget)
        self.menuBtn.setObjectName(u"menuBtn")
        icon1 = QIcon()
        icon1.addFile(u":/material_design/icons/material_design/menu.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.menuBtn.setIcon(icon1)
        self.menuBtn.setIconSize(QSize(25, 25))

        self.verticalLayout_2.addWidget(self.menuBtn, 0, Qt.AlignTop)


        self.verticalLayout.addWidget(self.widget, 0, Qt.AlignLeft|Qt.AlignTop)

        self.homeBut = QPushButton(self.leftMenu)
        self.homeBut.setObjectName(u"homeBut")
        icon2 = QIcon()
        icon2.addFile(u":/material_design/icons/material_design/home.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.homeBut.setIcon(icon2)
        self.homeBut.setIconSize(QSize(25, 25))

        self.verticalLayout.addWidget(self.homeBut)

        self.widget_2 = QWidget(self.leftMenu)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_5 = QVBoxLayout(self.widget_2)
        self.verticalLayout_5.setSpacing(15)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.profileBut = QPushButton(self.widget_2)
        self.profileBut.setObjectName(u"profileBut")
        icon3 = QIcon()
        icon3.addFile(u":/material_design/icons/material_design/co_present.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.profileBut.setIcon(icon3)
        self.profileBut.setIconSize(QSize(25, 25))

        self.verticalLayout_5.addWidget(self.profileBut)

        self.lessonsBut = QPushButton(self.widget_2)
        self.lessonsBut.setObjectName(u"lessonsBut")
        icon4 = QIcon()
        icon4.addFile(u":/feather/icons/feather/list.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.lessonsBut.setIcon(icon4)
        self.lessonsBut.setIconSize(QSize(25, 25))

        self.verticalLayout_5.addWidget(self.lessonsBut)


        self.verticalLayout.addWidget(self.widget_2, 0, Qt.AlignLeft|Qt.AlignTop)

        self.widget_3 = QWidget(self.leftMenu)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_6 = QVBoxLayout(self.widget_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.logoutBut = QPushButton(self.widget_3)
        self.logoutBut.setObjectName(u"logoutBut")
        icon5 = QIcon()
        icon5.addFile(u":/feather/icons/feather/log-out.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.logoutBut.setIcon(icon5)
        self.logoutBut.setIconSize(QSize(25, 25))

        self.verticalLayout_6.addWidget(self.logoutBut)


        self.verticalLayout.addWidget(self.widget_3, 0, Qt.AlignLeft|Qt.AlignBottom)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700;\">Petros Papagiannis</span></p><p><span style=\" font-size:10pt; font-weight:700;\">@1100658</span></p></body></html>", None))
        self.editProfBut.setText(QCoreApplication.translate("MainWindow", u"Edit Profile", None))
        self.beyourself.setText("")
        self.profimage.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:700;\">About me</span></p></body></html>", None))
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
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">My NoteBook</span></p></body></html>", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">My Notes</span></p></body></html>", None))
        self.label_20.setText("")
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Pinned Notes</span></p></body></html>", None))
        self.label_23.setText("")
        self.postimg3_6.setText("")
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"\u0393\u03c1\u03b1\u03bc\u03bc\u03b9\u03ba\u03ae \u0386\u03bb\u03b3\u03b5\u03b2\u03c1\u03b1 : \u0398\u03ad\u03bc\u03b1\u03c4\u03b1 \u0395\u03be\u03b5\u03c4\u03ac\u03c3\u03b5\u03c9\u03bd", None))
        self.textBrowser_7.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u03a4\u03b1 \u03c0\u03b5\u03c1\u03c3\u03b9\u03bd\u03ac \u03b8\u03ad\u03bc\u03b1\u03c4\u03b1 \u03c4\u03c9\u03bd \u03b5\u03be\u03b5\u03c4\u03ac\u03c3\u03b5\u03c9\u03bd \u03c3\u03c4\u03b7\u03bd \u0393\u03c1\u03b1\u03bc\u03bc\u03b9\u03ba\u03ae \u0386\u03bb\u03b3\u03b5\u03b2\u03c1\u03b1</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt"
                        "-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt;\">18/04/2025</span></p></body></html>", None))
        self.pushButton_14.setText("")
        self.postimg3_7.setText("")
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"\u0393\u03c1\u03b1\u03bc\u03bc\u03b9\u03ba\u03ae \u0386\u03bb\u03b3\u03b5\u03b2\u03c1\u03b1 : \u0398\u03ad\u03bc\u03b1\u03c4\u03b1 \u0395\u03be\u03b5\u03c4\u03ac\u03c3\u03b5\u03c9\u03bd", None))
        self.textBrowser_8.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u03a4\u03b1 \u03c0\u03b5\u03c1\u03c3\u03b9\u03bd\u03ac \u03b8\u03ad\u03bc\u03b1\u03c4\u03b1 \u03c4\u03c9\u03bd \u03b5\u03be\u03b5\u03c4\u03ac\u03c3\u03b5\u03c9\u03bd \u03c3\u03c4\u03b7\u03bd \u0393\u03c1\u03b1\u03bc\u03bc\u03b9\u03ba\u03ae \u0386\u03bb\u03b3\u03b5\u03b2\u03c1\u03b1</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt"
                        "-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt;\">18/04/2025</span></p></body></html>", None))
        self.pushButton_15.setText("")
        self.postimg3_4.setText("")
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"\u0393\u03c1\u03b1\u03bc\u03bc\u03b9\u03ba\u03ae \u0386\u03bb\u03b3\u03b5\u03b2\u03c1\u03b1 : \u0398\u03ad\u03bc\u03b1\u03c4\u03b1 \u0395\u03be\u03b5\u03c4\u03ac\u03c3\u03b5\u03c9\u03bd", None))
        self.textBrowser_5.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u03a4\u03b1 \u03c0\u03b5\u03c1\u03c3\u03b9\u03bd\u03ac \u03b8\u03ad\u03bc\u03b1\u03c4\u03b1 \u03c4\u03c9\u03bd \u03b5\u03be\u03b5\u03c4\u03ac\u03c3\u03b5\u03c9\u03bd \u03c3\u03c4\u03b7\u03bd \u0393\u03c1\u03b1\u03bc\u03bc\u03b9\u03ba\u03ae \u0386\u03bb\u03b3\u03b5\u03b2\u03c1\u03b1</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt"
                        "-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt;\">18/04/2025</span></p></body></html>", None))
        self.pushButton_16.setText("")
        self.postimg3_8.setText("")
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"\u0393\u03c1\u03b1\u03bc\u03bc\u03b9\u03ba\u03ae \u0386\u03bb\u03b3\u03b5\u03b2\u03c1\u03b1 : \u0398\u03ad\u03bc\u03b1\u03c4\u03b1 \u0395\u03be\u03b5\u03c4\u03ac\u03c3\u03b5\u03c9\u03bd", None))
        self.textBrowser_9.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u03a4\u03b1 \u03c0\u03b5\u03c1\u03c3\u03b9\u03bd\u03ac \u03b8\u03ad\u03bc\u03b1\u03c4\u03b1 \u03c4\u03c9\u03bd \u03b5\u03be\u03b5\u03c4\u03ac\u03c3\u03b5\u03c9\u03bd \u03c3\u03c4\u03b7\u03bd \u0393\u03c1\u03b1\u03bc\u03bc\u03b9\u03ba\u03ae \u0386\u03bb\u03b3\u03b5\u03b2\u03c1\u03b1</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt"
                        "-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt;\">18/04/2025</span></p></body></html>", None))
        self.pushButton_17.setText("")
        self.postimg3_9.setText("")
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"\u0393\u03c1\u03b1\u03bc\u03bc\u03b9\u03ba\u03ae \u0386\u03bb\u03b3\u03b5\u03b2\u03c1\u03b1 : \u0398\u03ad\u03bc\u03b1\u03c4\u03b1 \u0395\u03be\u03b5\u03c4\u03ac\u03c3\u03b5\u03c9\u03bd", None))
        self.textBrowser_10.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u03a4\u03b1 \u03c0\u03b5\u03c1\u03c3\u03b9\u03bd\u03ac \u03b8\u03ad\u03bc\u03b1\u03c4\u03b1 \u03c4\u03c9\u03bd \u03b5\u03be\u03b5\u03c4\u03ac\u03c3\u03b5\u03c9\u03bd \u03c3\u03c4\u03b7\u03bd \u0393\u03c1\u03b1\u03bc\u03bc\u03b9\u03ba\u03ae \u0386\u03bb\u03b3\u03b5\u03b2\u03c1\u03b1</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt"
                        "-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt;\">18/04/2025</span></p></body></html>", None))
        self.pushButton_18.setText("")
        self.postimg3_5.setText("")
        self.textBrowser_6.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u03a4\u03b1 \u03c0\u03b5\u03c1\u03c3\u03b9\u03bd\u03ac \u03b8\u03ad\u03bc\u03b1\u03c4\u03b1 \u03c4\u03c9\u03bd \u03b5\u03be\u03b5\u03c4\u03ac\u03c3\u03b5\u03c9\u03bd \u03c3\u03c4\u03b7\u03bd \u0393\u03c1\u03b1\u03bc\u03bc\u03b9\u03ba\u03ae \u0386\u03bb\u03b3\u03b5\u03b2\u03c1\u03b1</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt"
                        "-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt;\">18/04/2025</span></p></body></html>", None))
        self.pushButton_19.setText("")
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"\u0393\u03c1\u03b1\u03bc\u03bc\u03b9\u03ba\u03ae \u0386\u03bb\u03b3\u03b5\u03b2\u03c1\u03b1 : \u0398\u03ad\u03bc\u03b1\u03c4\u03b1 \u0395\u03be\u03b5\u03c4\u03ac\u03c3\u03b5\u03c9\u03bd", None))
        self.menuBtn.setText("")
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
    # retranslateUi

