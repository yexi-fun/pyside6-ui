# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'step.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QStackedWidget, QTabWidget, QTextEdit, QVBoxLayout,
    QWidget)
from .resources_rc import *
from .reso import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(980, 575)
        MainWindow.setStyleSheet(u"")
        MainWindow.setAnimated(True)
        MainWindow.setTabShape(QTabWidget.TabShape.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(980, 575))
        self.centralwidget.setStyleSheet(u"#bgApp {	\n"
"	border-radius:5px;\n"
"}\n"
"#contentBox {\n"
"	border-bottom-left-radius:5px;\n"
"	background-color:#212327 ;\n"
"}\n"
"#topBar {\n"
"	background-color:#606266;\n"
"}\n"
"#barRightBox{\n"
"	background-color:transparent;\n"
"}\n"
"#mainContent {\n"
"	border: 2px solid #822e9d;\n"
"}\n"
"#maximizeButton, #minimizeButton,#quitButton{\n"
"	background-color:#17202a;\n"
"}\n"
"#topBarTitle{\n"
" 	color:white;\n"
"}\n"
"#topBar{\n"
"	background-color:#17202a;\n"
"}\n"
"#logo{\n"
"	background-color:transparent;\n"
"}\n"
"#logoLabel{\n"
"	border-radius: 15px;\n"
"	background-image: url(:/logo/images/images/hutao-logo.png);\n"
"	border: 2px solid #822e9d;\n"
"}\n"
"#leftMenu{\n"
"	background-color:#212327 ;\n"
"}\n"
"#leftMenuTop, #spaceFrame{\n"
"	background-color:transparent;\n"
"}\n"
"#rightBox{\n"
"	background-color:#212327;\n"
"}\n"
"#stackedWidget{\n"
"	background-color:#566573;\n"
"}\n"
"#scroll_area{\n"
"	border:2px solid #212f3c;\n"
"}\n"
"#toolBox{\n"
"	\n"
"}\n"
"#textEdit_input{\n"
"	border:1"
                        "px solid  #212f3c;\n"
"	background-color:rgb(255, 255, 255);\n"
"	border-radius:10px;\n"
"}\n"
"QPushButton{\n"
"	background-color:#212327;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:rgb(85, 255, 0);\n"
"}")
        self.verticalLayout_7 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.bgApp = QFrame(self.centralwidget)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setFrameShape(QFrame.Shape.StyledPanel)
        self.bgApp.setFrameShadow(QFrame.Shadow.Raised)
        self.bgApp.setLineWidth(0)
        self.verticalLayout = QVBoxLayout(self.bgApp)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.topBar = QFrame(self.bgApp)
        self.topBar.setObjectName(u"topBar")
        self.topBar.setMinimumSize(QSize(0, 40))
        self.topBar.setMaximumSize(QSize(16777215, 40))
        self.topBar.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.topBar.setStyleSheet(u"")
        self.topBar.setFrameShape(QFrame.Shape.NoFrame)
        self.topBar.setFrameShadow(QFrame.Shadow.Raised)
        self.topBar.setLineWidth(0)
        self.horizontalLayout_4 = QHBoxLayout(self.topBar)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.logo = QFrame(self.topBar)
        self.logo.setObjectName(u"logo")
        self.logo.setMinimumSize(QSize(45, 0))
        self.logo.setMaximumSize(QSize(56, 16777215))
        self.logo.setFrameShape(QFrame.Shape.StyledPanel)
        self.logo.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.logo)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.logoLabel = QLabel(self.logo)
        self.logoLabel.setObjectName(u"logoLabel")
        self.logoLabel.setMinimumSize(QSize(0, 38))
        self.logoLabel.setMaximumSize(QSize(16777215, 38))
        self.logoLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.logoLabel, 0, 0, 1, 1)


        self.horizontalLayout_4.addWidget(self.logo)

        self.topBarTitle = QLabel(self.topBar)
        self.topBarTitle.setObjectName(u"topBarTitle")
        self.topBarTitle.setMinimumSize(QSize(780, 0))
        font = QFont()
        font.setFamilies([u"STCaiyun"])
        font.setPointSize(20)
        font.setBold(True)
        self.topBarTitle.setFont(font)

        self.horizontalLayout_4.addWidget(self.topBarTitle)

        self.barRightBox = QFrame(self.topBar)
        self.barRightBox.setObjectName(u"barRightBox")
        self.barRightBox.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.barRightBox.setFrameShape(QFrame.Shape.StyledPanel)
        self.barRightBox.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.barRightBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.minimizeButton = QPushButton(self.barRightBox)
        self.minimizeButton.setObjectName(u"minimizeButton")
        self.minimizeButton.setMinimumSize(QSize(0, 28))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/cil-minus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minimizeButton.setIcon(icon)
        self.minimizeButton.setIconSize(QSize(16, 16))
        self.minimizeButton.setFlat(False)

        self.horizontalLayout_3.addWidget(self.minimizeButton)

        self.maximizeButton = QPushButton(self.barRightBox)
        self.maximizeButton.setObjectName(u"maximizeButton")
        self.maximizeButton.setMinimumSize(QSize(0, 28))
        self.maximizeButton.setIconSize(QSize(16, 16))

        self.horizontalLayout_3.addWidget(self.maximizeButton)

        self.quitButton = QPushButton(self.barRightBox)
        self.quitButton.setObjectName(u"quitButton")
        self.quitButton.setMinimumSize(QSize(0, 28))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/cil-x.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.quitButton.setIcon(icon1)

        self.horizontalLayout_3.addWidget(self.quitButton)


        self.horizontalLayout_4.addWidget(self.barRightBox)


        self.verticalLayout.addWidget(self.topBar)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.Shape.StyledPanel)
        self.contentBox.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.contentBox)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.leftMenu = QFrame(self.contentBox)
        self.leftMenu.setObjectName(u"leftMenu")
        self.leftMenu.setEnabled(True)
        self.leftMenu.setMinimumSize(QSize(45, 0))
        self.leftMenu.setMaximumSize(QSize(45, 16777215))
        self.leftMenu.setFrameShape(QFrame.Shape.StyledPanel)
        self.leftMenu.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.leftMenu)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.leftMenuTop = QFrame(self.leftMenu)
        self.leftMenuTop.setObjectName(u"leftMenuTop")
        self.leftMenuTop.setMinimumSize(QSize(45, 250))
        self.leftMenuTop.setMaximumSize(QSize(45, 16777215))
        self.leftMenuTop.setFrameShape(QFrame.Shape.StyledPanel)
        self.leftMenuTop.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuTop)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.leftMenuTop)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QSize(45, 45))
        font1 = QFont()
        font1.setKerning(True)
        self.pushButton.setFont(font1)
        self.pushButton.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.pushButton.setAutoFillBackground(False)
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/cil-home.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon2)
        self.pushButton.setAutoDefault(False)

        self.verticalLayout_3.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.leftMenuTop)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(45, 45))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/cil-briefcase.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_2.setIcon(icon3)

        self.verticalLayout_3.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.leftMenuTop)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(45, 45))
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/cil-clipboard.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_3.setIcon(icon4)

        self.verticalLayout_3.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.leftMenuTop)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(45, 45))
        icon5 = QIcon()
        icon5.addFile(u":/icons/images/icons/cil-folder.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_4.setIcon(icon5)

        self.verticalLayout_3.addWidget(self.pushButton_4)

        self.verticalSpacer = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.verticalLayout_4.addWidget(self.leftMenuTop)

        self.spaceFrame = QFrame(self.leftMenu)
        self.spaceFrame.setObjectName(u"spaceFrame")
        self.spaceFrame.setMinimumSize(QSize(45, 200))
        self.spaceFrame.setMaximumSize(QSize(45, 16777215))
        self.spaceFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.spaceFrame.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_4.addWidget(self.spaceFrame)

        self.pushButton_5 = QPushButton(self.leftMenu)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(45, 45))
        self.pushButton_5.setMaximumSize(QSize(53, 50))
        icon6 = QIcon()
        icon6.addFile(u":/icons/images/icons/cil-settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_5.setIcon(icon6)

        self.verticalLayout_4.addWidget(self.pushButton_5)


        self.horizontalLayout_2.addWidget(self.leftMenu)

        self.rightBox = QFrame(self.contentBox)
        self.rightBox.setObjectName(u"rightBox")
        self.rightBox.setFrameShape(QFrame.Shape.StyledPanel)
        self.rightBox.setFrameShadow(QFrame.Shadow.Raised)
        self.rightBox.setLineWidth(1)
        self.rightBox.setMidLineWidth(0)
        self.verticalLayout_2 = QVBoxLayout(self.rightBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.rightBox)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMaximumSize(QSize(16777215, 16777215))
        self.stackedWidget.setFrameShape(QFrame.Shape.StyledPanel)
        self.stackedWidget.setFrameShadow(QFrame.Shadow.Raised)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.lineEdit_3 = QLineEdit(self.page_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(870, 510, 51, 20))
        self.lineEdit_3.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.stackedWidget.addWidget(self.page_2)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.lineEdit_2 = QLineEdit(self.page)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(860, 500, 51, 20))
        self.stackedWidget.addWidget(self.page)
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setEnabled(True)
        self.verticalLayout_5 = QVBoxLayout(self.home)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.scroll_area = QScrollArea(self.home)
        self.scroll_area.setObjectName(u"scroll_area")
        self.scroll_area.setMinimumSize(QSize(913, 432))
        self.scroll_area.setWidgetResizable(True)
        self.chat_widget = QWidget()
        self.chat_widget.setObjectName(u"chat_widget")
        self.chat_widget.setGeometry(QRect(0, 0, 927, 428))
        self.scroll_area.setWidget(self.chat_widget)

        self.verticalLayout_5.addWidget(self.scroll_area)

        self.toolBox = QWidget(self.home)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setMinimumSize(QSize(0, 100))
        self.toolBox.setMaximumSize(QSize(16777215, 100))
        self.verticalLayout_6 = QVBoxLayout(self.toolBox)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.textEdit_input = QTextEdit(self.toolBox)
        self.textEdit_input.setObjectName(u"textEdit_input")

        self.verticalLayout_6.addWidget(self.textEdit_input)

        self.toolBoxSub = QWidget(self.toolBox)
        self.toolBoxSub.setObjectName(u"toolBoxSub")
        self.toolBoxSub.setMinimumSize(QSize(0, 50))
        self.toolBoxSub.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_5 = QHBoxLayout(self.toolBoxSub)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(5, 0, 5, 0)
        self.network = QPushButton(self.toolBoxSub)
        self.network.setObjectName(u"network")
        self.network.setMinimumSize(QSize(40, 40))
        self.network.setMaximumSize(QSize(40, 40))
        icon7 = QIcon()
        icon7.addFile(u":/icons/images/icons/cil-wifi-signal-2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.network.setIcon(icon7)

        self.horizontalLayout_5.addWidget(self.network)

        self.newTitle = QPushButton(self.toolBoxSub)
        self.newTitle.setObjectName(u"newTitle")
        self.newTitle.setMinimumSize(QSize(40, 40))
        self.newTitle.setMaximumSize(QSize(40, 40))
        icon8 = QIcon()
        icon8.addFile(u":/icons/images/icons/cil-plus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.newTitle.setIcon(icon8)

        self.horizontalLayout_5.addWidget(self.newTitle)

        self.cleanMsg = QPushButton(self.toolBoxSub)
        self.cleanMsg.setObjectName(u"cleanMsg")
        self.cleanMsg.setMinimumSize(QSize(40, 40))
        self.cleanMsg.setMaximumSize(QSize(40, 40))
        icon9 = QIcon()
        icon9.addFile(u":/icons/images/icons/cil-account-logout.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.cleanMsg.setIcon(icon9)

        self.horizontalLayout_5.addWidget(self.cleanMsg)

        self.horizontalSpacer_2 = QSpacerItem(742, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.pushButton_Submit = QPushButton(self.toolBoxSub)
        self.pushButton_Submit.setObjectName(u"pushButton_Submit")
        self.pushButton_Submit.setMinimumSize(QSize(40, 40))
        self.pushButton_Submit.setMaximumSize(QSize(40, 40))
        icon10 = QIcon()
        icon10.addFile(u":/icons/images/icons/cil-level-up.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_Submit.setIcon(icon10)

        self.horizontalLayout_5.addWidget(self.pushButton_Submit)


        self.verticalLayout_6.addWidget(self.toolBoxSub)


        self.verticalLayout_5.addWidget(self.toolBox)

        self.stackedWidget.addWidget(self.home)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addWidget(self.rightBox)


        self.verticalLayout.addWidget(self.contentBox)


        self.verticalLayout_7.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.minimizeButton.setDefault(False)
        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logoLabel.setText("")
        self.topBarTitle.setText(QCoreApplication.translate("MainWindow", u"Yexi-ui", None))
        self.minimizeButton.setText("")
        self.maximizeButton.setText("")
        self.quitButton.setText("")
        self.pushButton.setText("")
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
        self.pushButton_4.setText("")
        self.pushButton_5.setText("")
        self.lineEdit_3.setText(QCoreApplication.translate("MainWindow", u"\u7b2c\u4e09\u9875", None))
        self.lineEdit_2.setText(QCoreApplication.translate("MainWindow", u"\u7b2c\u4e8c\u9875", None))
        self.network.setText("")
        self.newTitle.setText("")
        self.cleanMsg.setText("")
        self.pushButton_Submit.setText("")
    # retranslateUi

