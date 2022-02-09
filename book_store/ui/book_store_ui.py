# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'book_store_uipgzXBP.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from Custom_Widgets.Widgets import QCustomSlideMenu

import qt_resources_rc
import qt_resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(619, 420)
        MainWindow.setMinimumSize(QSize(0, 0))
        font = QFont()
        font.setFamily(u"Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"* { border: none; }")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        font1 = QFont()
        font1.setFamily(u"Noto Sans")
        font1.setBold(True)
        font1.setItalic(False)
        font1.setWeight(75)
        self.centralwidget.setFont(font1)
        self.centralwidget.setStyleSheet(u"background-color: rgb(13, 25, 16);\n"
"color: rgb(255, 255, 255);\n"
"font-family: \"Noto Sans\";")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.nav_container = QCustomSlideMenu(self.centralwidget)
        self.nav_container.setObjectName(u"nav_container")
        self.nav_container.setMinimumSize(QSize(0, 0))
        self.nav_container.setMaximumSize(QSize(0, 16777215))
        self.nav_container.setStyleSheet(u"background-color: rgb(36, 36, 36);\n"
"color: rgb(255, 255, 255);\n"
"padding: 5px 5px;")
        self.verticalLayout_2 = QVBoxLayout(self.nav_container)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.nav_header = QFrame(self.nav_container)
        self.nav_header.setObjectName(u"nav_header")
        font2 = QFont()
        font2.setFamily(u"Noto Sans")
        font2.setPointSize(10)
        self.nav_header.setFont(font2)
        self.nav_header.setFrameShape(QFrame.StyledPanel)
        self.nav_header.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.nav_header)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.nav_header_icon = QLabel(self.nav_header)
        self.nav_header_icon.setObjectName(u"nav_header_icon")
        self.nav_header_icon.setMinimumSize(QSize(40, 40))
        self.nav_header_icon.setMaximumSize(QSize(40, 40))
        self.nav_header_icon.setFont(font2)
        self.nav_header_icon.setStyleSheet(u"border-radius: 20px;\n"
"border: 2px solid rgb(3, 218, 197);\n"
"")
        self.nav_header_icon.setPixmap(QPixmap(u":/icons/icons/book-open.svg"))
        self.nav_header_icon.setScaledContents(False)
        self.nav_header_icon.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.nav_header_icon, 0, Qt.AlignHCenter)


        self.verticalLayout_2.addWidget(self.nav_header, 0, Qt.AlignTop)

        self.nav = QFrame(self.nav_container)
        self.nav.setObjectName(u"nav")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nav.sizePolicy().hasHeightForWidth())
        self.nav.setSizePolicy(sizePolicy)
        self.nav.setStyleSheet(u"QPushButton {\n"
"	text-align: left;\n"
"	padding: 10px 10px;\n"
"	border: 1px solid rgb(58, 58, 58);\n"
"	border-radius: 5px;\n"
"}")
        self.nav.setFrameShape(QFrame.StyledPanel)
        self.nav.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.nav)
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.inventory_nav_btn = QPushButton(self.nav)
        self.inventory_nav_btn.setObjectName(u"inventory_nav_btn")
        self.inventory_nav_btn.setFont(font2)
        icon = QIcon()
        icon.addFile(u":/icons/icons/package.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.inventory_nav_btn.setIcon(icon)
        self.inventory_nav_btn.setIconSize(QSize(20, 20))

        self.verticalLayout_3.addWidget(self.inventory_nav_btn)

        self.billing_nav_btn = QPushButton(self.nav)
        self.billing_nav_btn.setObjectName(u"billing_nav_btn")
        self.billing_nav_btn.setFont(font2)
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/file-text.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.billing_nav_btn.setIcon(icon1)
        self.billing_nav_btn.setIconSize(QSize(20, 20))

        self.verticalLayout_3.addWidget(self.billing_nav_btn)

        self.analytics_nav_btn = QPushButton(self.nav)
        self.analytics_nav_btn.setObjectName(u"analytics_nav_btn")
        self.analytics_nav_btn.setFont(font2)
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/bar-chart-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.analytics_nav_btn.setIcon(icon2)
        self.analytics_nav_btn.setIconSize(QSize(20, 20))

        self.verticalLayout_3.addWidget(self.analytics_nav_btn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.verticalLayout_2.addWidget(self.nav)

        self.nav_footer = QFrame(self.nav_container)
        self.nav_footer.setObjectName(u"nav_footer")
        self.nav_footer.setFrameShape(QFrame.StyledPanel)
        self.nav_footer.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.nav_footer, 0, Qt.AlignBottom)


        self.horizontalLayout.addWidget(self.nav_container)

        self.body = QFrame(self.centralwidget)
        self.body.setObjectName(u"body")
        self.body.setFrameShape(QFrame.StyledPanel)
        self.body.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.body)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header = QFrame(self.body)
        self.header.setObjectName(u"header")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.header.sizePolicy().hasHeightForWidth())
        self.header.setSizePolicy(sizePolicy1)
        self.header.setStyleSheet(u"background-color: rgb(36, 36, 36);")
        self.header.setFrameShape(QFrame.StyledPanel)
        self.header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.header_left = QFrame(self.header)
        self.header_left.setObjectName(u"header_left")
        self.header_left.setFrameShape(QFrame.StyledPanel)
        self.header_left.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.header_left)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.menu_btn = QPushButton(self.header_left)
        self.menu_btn.setObjectName(u"menu_btn")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_btn.setIcon(icon3)
        self.menu_btn.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.menu_btn, 0, Qt.AlignLeft)


        self.horizontalLayout_2.addWidget(self.header_left, 0, Qt.AlignLeft)

        self.header_center = QFrame(self.header)
        self.header_center.setObjectName(u"header_center")
        self.header_center.setFrameShape(QFrame.StyledPanel)
        self.header_center.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.header_center)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.header_title = QLabel(self.header_center)
        self.header_title.setObjectName(u"header_title")

        self.horizontalLayout_5.addWidget(self.header_title, 0, Qt.AlignHCenter)


        self.horizontalLayout_2.addWidget(self.header_center)

        self.header_right = QFrame(self.header)
        self.header_right.setObjectName(u"header_right")
        self.header_right.setFrameShape(QFrame.StyledPanel)
        self.header_right.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.header_right)


        self.verticalLayout.addWidget(self.header)

        self.main = QStackedWidget(self.body)
        self.main.setObjectName(u"main")
        sizePolicy.setHeightForWidth(self.main.sizePolicy().hasHeightForWidth())
        self.main.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setFamily(u"Noto Sans")
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setWeight(75)
        self.main.setFont(font3)
        self.main.setStyleSheet(u"")
        self.main.setFrameShape(QFrame.StyledPanel)
        self.main.setFrameShadow(QFrame.Raised)
        self.inventory_page = QWidget()
        self.inventory_page.setObjectName(u"inventory_page")
        self.verticalLayout_5 = QVBoxLayout(self.inventory_page)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.inventory_title = QLabel(self.inventory_page)
        self.inventory_title.setObjectName(u"inventory_title")
        self.inventory_title.setFont(font3)

        self.verticalLayout_5.addWidget(self.inventory_title, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.main.addWidget(self.inventory_page)
        self.billing_page = QWidget()
        self.billing_page.setObjectName(u"billing_page")
        self.verticalLayout_6 = QVBoxLayout(self.billing_page)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.billing_title = QLabel(self.billing_page)
        self.billing_title.setObjectName(u"billing_title")
        self.billing_title.setFont(font3)

        self.verticalLayout_6.addWidget(self.billing_title, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.main.addWidget(self.billing_page)
        self.analytics_page = QWidget()
        self.analytics_page.setObjectName(u"analytics_page")
        self.verticalLayout_7 = QVBoxLayout(self.analytics_page)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.analytics_title = QLabel(self.analytics_page)
        self.analytics_title.setObjectName(u"analytics_title")
        self.analytics_title.setFont(font3)

        self.verticalLayout_7.addWidget(self.analytics_title, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.main.addWidget(self.analytics_page)

        self.verticalLayout.addWidget(self.main)

        self.footer = QFrame(self.body)
        self.footer.setObjectName(u"footer")
        self.footer.setFrameShape(QFrame.StyledPanel)
        self.footer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.footer)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.size_grip = QFrame(self.footer)
        self.size_grip.setObjectName(u"size_grip")
        self.size_grip.setFrameShape(QFrame.StyledPanel)
        self.size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.size_grip)


        self.verticalLayout.addWidget(self.footer)


        self.horizontalLayout.addWidget(self.body)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.main.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.nav_header_icon.setText("")
        self.inventory_nav_btn.setText(QCoreApplication.translate("MainWindow", u"Inventory", None))
        self.billing_nav_btn.setText(QCoreApplication.translate("MainWindow", u"Billing", None))
        self.analytics_nav_btn.setText(QCoreApplication.translate("MainWindow", u"Analytics", None))
        self.menu_btn.setText("")
        self.header_title.setText(QCoreApplication.translate("MainWindow", u"Inventory", None))
        self.inventory_title.setText(QCoreApplication.translate("MainWindow", u"Inventory", None))
        self.billing_title.setText(QCoreApplication.translate("MainWindow", u"Billing", None))
        self.analytics_title.setText(QCoreApplication.translate("MainWindow", u"Analytics", None))
    # retranslateUi

