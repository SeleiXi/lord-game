# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu2.ui'
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
        MainWindow.resize(561, 683)
        icon = QIcon()
        icon.addFile(u"chigua.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QPushButton{\n"
"color:Red}\n"
"QMainWindow{\n"
"background-color:white\n"
"}")
        self.actionQQ = QAction(MainWindow)
        self.actionQQ.setObjectName(u"actionQQ")
        self.actionDiscord = QAction(MainWindow)
        self.actionDiscord.setObjectName(u"actionDiscord")
        self.actionEmail = QAction(MainWindow)
        self.actionEmail.setObjectName(u"actionEmail")
        self.actionGithub = QAction(MainWindow)
        self.actionGithub.setObjectName(u"actionGithub")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_4 = QVBoxLayout(self.tab)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u"icons/chigua.png"))

        self.verticalLayout_2.addWidget(self.label)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_3 = QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.textBrowser = QTextBrowser(self.tab_2)
        self.textBrowser.setObjectName(u"textBrowser")
        font = QFont()
        font.setFamily(u"MiSans Heavy")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser.setFont(font)
        self.textBrowser.setLineWrapMode(QTextEdit.WidgetWidth)

        self.verticalLayout_3.addWidget(self.textBrowser)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 30, -1, 30)
        self.pushButtonChallengeMode = QPushButton(self.centralwidget)
        self.pushButtonChallengeMode.setObjectName(u"pushButtonChallengeMode")
        self.pushButtonChallengeMode.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonChallengeMode.sizePolicy().hasHeightForWidth())
        self.pushButtonChallengeMode.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamily(u"MiSans Heavy")
        font1.setBold(True)
        font1.setItalic(False)
        font1.setWeight(75)
        self.pushButtonChallengeMode.setFont(font1)
        icon1 = QIcon()
        icon1.addFile(u"../../../\u5c01\u9762/chigua.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonChallengeMode.setIcon(icon1)

        self.horizontalLayout.addWidget(self.pushButtonChallengeMode)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.verticalLayout.addWidget(self.progressBar)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 561, 23))
        self.menuMade_By_SeleiXI = QMenu(self.menubar)
        self.menuMade_By_SeleiXI.setObjectName(u"menuMade_By_SeleiXI")
        self.menu = QMenu(self.menuMade_By_SeleiXI)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMade_By_SeleiXI.menuAction())
        self.menuMade_By_SeleiXI.addAction(self.menu.menuAction())
        self.menu.addAction(self.actionDiscord)
        self.menu.addAction(self.actionEmail)
        self.menu.addAction(self.actionGithub)
        self.menu.addAction(self.actionQQ)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u9748\u9053\u6e90\u5c0a", None))
        self.actionQQ.setText(QCoreApplication.translate("MainWindow", u"QQ:1632845225", None))
        self.actionDiscord.setText(QCoreApplication.translate("MainWindow", u"Discord:SeleiXi", None))
        self.actionEmail.setText(QCoreApplication.translate("MainWindow", u"Email:bzhanthresh@gmail.com", None))
        self.actionGithub.setText(QCoreApplication.translate("MainWindow", u"Github:SeleiXi", None))
        self.label.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Home Page", None))
        self.textBrowser.setDocumentTitle("")
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MiSans Heavy'; font-size:28pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:400;\">\u6b61\u8fce\u4f86\u5230\u9748\u9053\u6e90\u5c0a\uff01 </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:400;\">\u904a\u6232\u6539\u7de8\u81ea\u5c0f\u8aaa(\u540c\u672c\u7a0b\u5e8f\u4f5c\u8005\u6240\u8457)\uff1ahttps://book.qidian.com/info/1030712451/</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"
                        "\"><span style=\" font-size:12pt; font-weight:400;\">\u5929\u5143\u5e9c\u906d\u5230\u9748\u7378\u4fb5\u5360\u5f8c,\u5e9c\u5167\u56db\u8655\u72fc\u85c9,\u4e2b\u9b1f\u8207\u5e9c\u4e3b\u7686\u88ab\u62d0\u53bb,\u56da\u7981\u5728\u9b54\u708e\u68ee\u6df1\u8655\u3002\u50c5\u6709\u9748\u738b\u5883\u754c\u7684\u4f60\u7121\u529b\u62b5\u6297,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:400;\">\u4f46\u5728\u9748\u754c\u5929\u5730\u4e2d,\u4f60\u53ef\u4ee5\u81e8\u6642\u4ee580\u9748\u77f3\u5f9e\u6e90\u754c\u9818\u57df\u53ec\u559a\u4e00\u4f4d\u706b\u9d3f\u5b50(\u8840\u91cf\u70ba80)\u4ee5\u53ca\u4ee5100\u9748\u77f3\u96c7\u50ad\u4e00\u4f4d\u4f86\u81ea\u661f\u9748\u65cf\u7684\u7384\u8005(\u8840\u91cf\u70ba100)\u3002</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:400;"
                        "\">\u5728\u9b54\u708e\u68ee\u5de1\u908f\u5b88\u885b\u7684\u901a\u5e38\u53ea\u6709\u5996\u5f2d\u7334\u8207\u9583\u96fb\u7329,\u5996\u5f2d\u7334\u751f\u6027\u6015\u706b,\u800c\u661f\u9748\u65cf\u7684\u6230\u58eb\u5011\u64c1\u6709\u9748\u80fd\u8b77\u7532\u800c\u7121\u61fc\u9583\u96fb\u3002</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:400;\">\u6545\u6b64\u706b\u9d3f\u5b50\u53ea\u9700\u6d88\u801720\u8840\u4fbf\u53ef\u64ca\u6bba\u5996\u5f2d\u7334,\u4f46\u7384\u8005\u5247\u9700\u6d88\u801780\u8840\u3002\u7384\u8005\u6d88\u801720\u8840\u53ef\u64ca\u6bba\u9583\u96fb\u7329,\u800c\u706b\u9d3f\u5b50\u970080\u8840\u3002</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:400;\">\u5728\u5168\u5c40\u904a\u6232\u4e2d,\u4f60\u64c1\u6709\u4e00\u6b21\u6a5f\u6703\u4ee5\u5929"
                        "\u773c\u8996\u5bdf\u9b54\u708e\u68ee\u4e2d\u7684\u9748\u7378\u5206\u5e03\u3002</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:400;\">\u4ee5\u53ca\u4f60\u64c1\u6709\u7121\u6578\u6b21\u6a5f\u6703,\u4ee5\u9748\u77f3\u9060\u7a0b\u6cbb\u6108\u6230\u9b25\u5f8c\u7684\u706b\u9d3f\u5b50\u53ca\u7384\u8005\u3002\u9748\u77f3\u8207\u751f\u547d\u7684\u514c\u63db\u6bd4\u4f8b\u70ba1:1</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:400;\">\u4f60\u8eab\u4e0a\u50c5\u6709400\u9748\u77f3,\u4ecb\u65bc\u96c7\u50ad\u7684\u53cb\u8ecd\u5728\u6230\u9b25\u5f8c\u7686\u6703\u6d88\u5931,\u8a66\u4ee5\u6700\u4f4e\u7684\u82b1\u92b7\u64ca\u6557\u9b54\u708e\u68ee\u4e2d\u7684\u9748\u7378\u4e26\u62ef\u6551\u906d\u5230\u4fd8\u865c\u7684\u4eba\u5011\u3002</span></p>\n"
"<p style=\"-qt-parag"
                        "raph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:400;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:400;\">\u6ce8\u610f\uff1a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:400;\">1.\u4f60\u9700\u8981\u5728\u904a\u6232\u958b\u59cb\u6642\u4fbf\u96c7\u50ad\u4f60\u9700\u8981\u96c7\u50ad\u7684\u53cb\u8ecd\u3002</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:400;\">2.\u9032\u5165\u904a\u6232\u5f8c\u9ede\u64caF11\u5373\u53ef\u9032\u5165\u5168\u5c4f</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0p"
                        "x; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:400;\">3.\u901a\u95dc\u8a55\u7d1a\u5206\u70ba\u3010\u6975\u5176\u5b8c\u7f8e\u3011 / \u3010\u5b8c\u7f8e\u3011 / \u3010\u512a\u79c0\u3011 / \u3010\u4e0d\u932f\u3011 / \u3010\u4e00\u822c\u3011</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Background_Introduction", None))
        self.pushButtonChallengeMode.setText(QCoreApplication.translate("MainWindow", u"\u904a\u6232\u555f\u52d5", None))
        self.menuMade_By_SeleiXI.setTitle(QCoreApplication.translate("MainWindow", u"Made By SeleiXi", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u806f\u7e6b\u4f5c\u8005", None))
    # retranslateUi
