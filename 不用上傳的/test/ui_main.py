# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(745, 476)
        MainWindow.setStyleSheet(u"")
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, -1, 0, -1)
        self.startDateEdit = QDateEdit(self.centralwidget)
        self.startDateEdit.setObjectName(u"startDateEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startDateEdit.sizePolicy().hasHeightForWidth())
        self.startDateEdit.setSizePolicy(sizePolicy)
        self.startDateEdit.setDateTime(QDateTime(QDate(2019, 1, 1), QTime(0, 0, 10)))

        self.horizontalLayout.addWidget(self.startDateEdit)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        self.endDateEdit = QDateEdit(self.centralwidget)
        self.endDateEdit.setObjectName(u"endDateEdit")
        sizePolicy.setHeightForWidth(self.endDateEdit.sizePolicy().hasHeightForWidth())
        self.endDateEdit.setSizePolicy(sizePolicy)
        self.endDateEdit.setDateTime(QDateTime(QDate(2019, 1, 14), QTime(0, 0, 0)))

        self.horizontalLayout.addWidget(self.endDateEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.crawl = QPushButton(self.centralwidget)
        self.crawl.setObjectName(u"crawl")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.crawl.sizePolicy().hasHeightForWidth())
        self.crawl.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.crawl)

        self.exportToExcel = QPushButton(self.centralwidget)
        self.exportToExcel.setObjectName(u"exportToExcel")

        self.horizontalLayout_2.addWidget(self.exportToExcel)

        self.exportToDB = QPushButton(self.centralwidget)
        self.exportToDB.setObjectName(u"exportToDB")

        self.horizontalLayout_2.addWidget(self.exportToDB)

        self.analyze = QPushButton(self.centralwidget)
        self.analyze.setObjectName(u"analyze")

        self.horizontalLayout_2.addWidget(self.analyze)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.textBrowser = QTextEdit(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setAcceptRichText(True)

        self.verticalLayout.addWidget(self.textBrowser)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 745, 23))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.crawl.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u722c\u53d6", None))
        self.crawl.setProperty("myclass", QCoreApplication.translate("MainWindow", u"bar2btn", None))
        self.exportToExcel.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165Excel", None))
        self.exportToExcel.setProperty("myclass", QCoreApplication.translate("MainWindow", u"bar2btn", None))
        self.exportToDB.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165\u6570\u636e\u5e93", None))
        self.exportToDB.setProperty("myclass", QCoreApplication.translate("MainWindow", u"bar2btn", None))
        self.analyze.setText(QCoreApplication.translate("MainWindow", u"\u5206\u6790\u6570\u636e", None))
        self.analyze.setProperty("myclass", QCoreApplication.translate("MainWindow", u"bar2btn", None))
        self.textBrowser.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u4f60\u597d\uff0c\u767d\u6708\u9ed1\u7fbd", None))
    # retranslateUi

