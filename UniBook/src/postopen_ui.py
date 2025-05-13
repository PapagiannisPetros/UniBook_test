# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'postopen.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
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
        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(10, 0, 1066, 211))
        self.widget_4.setStyleSheet(u"background-color: rgb(183, 177, 191);")
        self.verticalLayout_3 = QVBoxLayout(self.widget_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 0, -1, 5)
        self.widget_6 = QWidget(self.widget_4)
        self.widget_6.setObjectName(u"widget_6")
        self.formLayout = QFormLayout(self.widget_6)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(-1, 0, -1, -1)
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
        self.post_title = QLabel(self.widget_43)
        self.post_title.setObjectName(u"post_title")
        self.post_title.setMaximumSize(QSize(16777215, 51))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.post_title.setFont(font)
        self.post_title.setTextFormat(Qt.AutoText)
        self.post_title.setScaledContents(False)
        self.post_title.setWordWrap(False)

        self.verticalLayout_6.addWidget(self.post_title, 0, Qt.AlignVCenter)

        self.post_date = QLabel(self.widget_43)
        self.post_date.setObjectName(u"post_date")
        self.post_date.setMaximumSize(QSize(16777215, 34))
        font1 = QFont()
        font1.setPointSize(9)
        self.post_date.setFont(font1)

        self.verticalLayout_6.addWidget(self.post_date)


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
        self.post_text = QTextBrowser(self.widget_44)
        self.post_text.setObjectName(u"post_text")
        self.post_text.setMaximumSize(QSize(16777215, 150))

        self.verticalLayout_36.addWidget(self.post_text, 0, Qt.AlignBottom)


        self.verticalLayout_35.addWidget(self.widget_44)


        self.verticalLayout_3.addWidget(self.widget_42)

        self.widget1 = QWidget(self.widget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(10, 210, 1066, 41))
        self.horizontalLayout_stats = QHBoxLayout(self.widget1)
        self.horizontalLayout_stats.setObjectName(u"horizontalLayout_stats")
        self.horizontalLayout_stats.setContentsMargins(0, 0, 0, 0)
        self.likeButton = QPushButton(self.widget1)
        self.likeButton.setObjectName(u"likeButton")
        icon = QIcon()
        icon.addFile(u":/feather/icons/feather/thumbs-up.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.likeButton.setIcon(icon)

        self.horizontalLayout_stats.addWidget(self.likeButton)

        self.commentButton = QPushButton(self.widget1)
        self.commentButton.setObjectName(u"commentButton")
        icon1 = QIcon()
        icon1.addFile(u":/font_awesome/regular/icons/font_awesome/regular/comment-dots.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.commentButton.setIcon(icon1)

        self.horizontalLayout_stats.addWidget(self.commentButton)

        self.downloadButton = QPushButton(self.widget1)
        self.downloadButton.setObjectName(u"downloadButton")
        icon2 = QIcon()
        icon2.addFile(u":/feather/icons/feather/arrow-down-circle.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.downloadButton.setIcon(icon2)

        self.horizontalLayout_stats.addWidget(self.downloadButton)

        self.likeButton_2 = QPushButton(self.widget1)
        self.likeButton_2.setObjectName(u"likeButton_2")
        icon3 = QIcon()
        icon3.addFile(u":/feather/icons/feather/bookmark.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.likeButton_2.setIcon(icon3)

        self.horizontalLayout_stats.addWidget(self.likeButton_2)

        self.shareButton = QPushButton(self.widget1)
        self.shareButton.setObjectName(u"shareButton")
        icon4 = QIcon()
        icon4.addFile(u":/feather/icons/feather/flag.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.shareButton.setIcon(icon4)

        self.horizontalLayout_stats.addWidget(self.shareButton)

        self.rightMenu = QWidget(self.widget)
        self.rightMenu.setObjectName(u"rightMenu")
        self.rightMenu.setGeometry(QRect(340, 350, 350, 521))
        self.rightMenu.setMinimumSize(QSize(300, 0))
        self.rightMenu.setMaximumSize(QSize(350, 16777215))
        self.rightMenu.setStyleSheet(u"background-color: rgb(12, 126, 124);")
        self.verticalLayout_13 = QVBoxLayout(self.rightMenu)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 3)
        self.widget_47 = QWidget(self.widget)
        self.widget_47.setObjectName(u"widget_47")
        self.widget_47.setGeometry(QRect(10, 270, 1051, 381))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_47.sizePolicy().hasHeightForWidth())
        self.widget_47.setSizePolicy(sizePolicy)
        self.widget_47.setMinimumSize(QSize(0, 0))
        self.verticalLayout_14 = QVBoxLayout(self.widget_47)
        self.verticalLayout_14.setSpacing(7)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(3, 0, 3, 0)
        self.widget_8 = QWidget(self.widget_47)
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


        self.verticalLayout_14.addWidget(self.widget_8)

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


        self.verticalLayout.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText("")
        self.post_title.setText(QCoreApplication.translate("MainWindow", u"\u0393\u03c1\u03b1\u03bc\u03bc\u03b9\u03ba\u03ae \u0386\u03bb\u03b3\u03b5\u03b2\u03c1\u03b1 \u2013 \u039d\u03ad\u03b1 \u0394\u03b7\u03bc\u03bf\u03c3\u03af\u03b5\u03c5\u03c3\u03b7", None))
        self.post_date.setText(QCoreApplication.translate("MainWindow", u"18/04/2025", None))
        self.post_text.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">\u03bd\u03ad\u03bf \u03c5\u03bb\u03b9\u03ba\u03cc \u03bc\u03b5 \u03c0\u03b1\u03c1\u03b1\u03b4\u03b5\u03af\u03b3\u03bc\u03b1\u03c4\u03b1 \u03b5\u03c6\u03b1\u03c1\u03bc\u03bf\u03b3\u03ae\u03c2 \u03c0\u03af\u03bd\u03b1\u03ba\u03c9\u03bd \u03ba\u03b1\u03b9 \u03b4\u03b9\u03b1\u03bd\u03c5\u03c3\u03bc\u03ac\u03c4\u03c9\u03bd \u03c3\u03c4\u03b7\u03bd \u03b5\u03c0"
                        "\u03af\u03bb\u03c5\u03c3\u03b7 \u03c3\u03c5\u03c3\u03c4\u03b7\u03bc\u03ac\u03c4\u03c9\u03bd \u03b3\u03c1\u03b1\u03bc\u03bc\u03b9\u03ba\u03ce\u03bd \u03b5\u03be\u03b9\u03c3\u03ce\u03c3\u03b5\u03c9\u03bd. \u03a0\u03c1\u03bf\u03c4\u03b5\u03af\u03bd\u03b5\u03c4\u03b1\u03b9 \u03b7 \u03bc\u03b5\u03bb\u03ad\u03c4\u03b7 \u03c0\u03c1\u03b9\u03bd \u03c4\u03bf \u03b5\u03c0\u03cc\u03bc\u03b5\u03bd\u03bf \u03bc\u03ac\u03b8\u03b7\u03bc\u03b1 \u03ba\u03b1\u03b8\u03ce\u03c2 \u03c0\u03b5\u03c1\u03b9\u03bb\u03b1\u03bc\u03b2\u03ac\u03bd\u03b5\u03b9 \u03b2\u03b1\u03c3\u03b9\u03ba\u03ad\u03c2 \u03ad\u03bd\u03bd\u03bf\u03b9\u03b5\u03c2 \u03b3\u03b9\u03b1 \u03c4\u03b9\u03c2 \u03b5\u03bd\u03b4\u03b9\u03ac\u03bc\u03b5\u03c3\u03b5\u03c2 \u03b5\u03be\u03b5\u03c4\u03ac\u03c3\u03b5\u03b9\u03c2.</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.likeButton.setToolTip(QCoreApplication.translate("MainWindow", u"Like", None))
#endif // QT_CONFIG(tooltip)
        self.likeButton.setText(QCoreApplication.translate("MainWindow", u"129", None))
#if QT_CONFIG(tooltip)
        self.commentButton.setToolTip(QCoreApplication.translate("MainWindow", u"Comments", None))
#endif // QT_CONFIG(tooltip)
        self.commentButton.setText(QCoreApplication.translate("MainWindow", u"54", None))
#if QT_CONFIG(tooltip)
        self.downloadButton.setToolTip(QCoreApplication.translate("MainWindow", u"Download", None))
#endif // QT_CONFIG(tooltip)
        self.downloadButton.setText("")
#if QT_CONFIG(tooltip)
        self.likeButton_2.setToolTip(QCoreApplication.translate("MainWindow", u"Pin", None))
#endif // QT_CONFIG(tooltip)
        self.likeButton_2.setText("")
#if QT_CONFIG(tooltip)
        self.shareButton.setToolTip(QCoreApplication.translate("MainWindow", u"Report", None))
#endif // QT_CONFIG(tooltip)
        self.shareButton.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:700; font-style:italic;\">Comments</span></p></body></html>", None))
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

