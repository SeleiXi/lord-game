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
        icon.addFile(u"icons/seleixi.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.000000000000000)
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
        self.label.setPixmap(QPixmap(u"icons/seleixi.png"))

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
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line)

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
        icon1.addFile(u"../../../\u5c01\u9762/seleixi.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonChallengeMode.setIcon(icon1)

        self.horizontalLayout.addWidget(self.pushButtonChallengeMode)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_2)


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

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u9748\u9053\u6e90\u5c0a", None))
        self.actionQQ.setText(QCoreApplication.translate("MainWindow", u"QQ:1632845225", None))
        self.actionDiscord.setText(QCoreApplication.translate("MainWindow", u"Discord:SeleiXi", None))
        self.actionEmail.setText(QCoreApplication.translate("MainWindow", u"Email:bzhanthresh@gmail.com", None))
        self.actionGithub.setText(QCoreApplication.translate("MainWindow", u"Github:SeleiXi (\u672c\u9805\u76ee\u5df2\u767c\u4f48\u65bcGithub)", None))
        self.label.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Home Page", None))
        self.textBrowser.setDocumentTitle("")
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MiSans Heavy'; font-size:28pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:400;\">\u6b61\u8fce\u4f86\u5230\u9748\u9053\u6e90\u5c0a\uff01 \u904a\u6232\u6539\u7de8\u81ea\u672c\u4eba\u6240\u8457\u5c0f\u8aaa(\u5df2\u4e0b\u67b6)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:400;\">\u4f60\u53ef\u4ee5\u81e8\u6642\u4ee580\u91d1\u9322\u53ec\u559a\u4e00\u4f4d\u706b\u9d3f\u5b50(\u8840\u91cf\u70ba80)\u4ee5\u53ca\u4ee5100\u91d1\u9322\u96c7\u50ad\u4e00\u4f4d\u4f86\u81ea\u661f"
                        "\u9748\u65cf\u7684Killer(HP\u70ba100)\u3002</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:400;\">\u5728\u524d\u5f80\u57ce\u5821\u7684\u8def\u4e0a\u6709\u5169\u7a2e\u6575\u4eba\uff0c\u5206\u5225\u662f</span><span style=\" font-size:12pt;\">\u5996\u5f2d\u7334</span><span style=\" font-size:12pt; font-weight:400;\">\u548c\u7d05</span><span style=\" font-size:12pt;\">\u7329</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:400;\">\u706b\u9d3f\u5b50\u53ea\u9700\u6d88\u801720HP\u4fbf\u53ef\u64ca\u6bba\u5996\u5f2d\u7334,\u4f46Killer\u5247\u9700\u6d88\u801780HP\u3002Killer\u6d88\u801720HP\u53ef\u64ca\u6bba\u7d05</span><span style=\" font-size:12pt;\">\u7329</span><span style=\" font-size:12pt; font-weight:400;\">,\u800c\u706b\u9d3f\u5b50\u970080HP\u3002</span><"
                        "/p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:400;\">\u5728\u904a\u6232\u4e2d\uff0c\u4f60\u64c1\u6709\u4e00\u6b21\u6a5f\u6703\u4ee5\u8996\u5bdf\u68ee\u6797\u4e2d\u7684\u9748\u7378\u5206\u5e03(\u53ef\u89c0\u5bdf5\u79d2)\u3002</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:400;\">\u4f60\u8eab\u4e0a\u50c5\u6709300\u9748\u77f3,\u8a66\u4ee5\u6700\u4f4e\u7684\u82b1\u92b7\u64ca\u6557\u68ee\u6797\u4e2d\u7684\u6575\u4eba\u4e26\u9032\u5165\u57ce\u5821</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:400;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-inden"
                        "t:0px;\"><span style=\" font-size:12pt; font-weight:400;\">\u6ce8\u610f\uff1a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:400;\">1.\u901a\u95dc\u8a55\u7d1a\u5206\u70ba\u3010\u512a\u79c0\u3011 / \u3010\u826f\u597d\u3011 / \u3010\u4e0d\u932f\u3011 / \u3010\u4e00\u822c\u3011</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:400;\">2.\u5728\u55ae\u4f4d\u79fb\u52d5\u6642,\u9f20\u6a19\u5728\u904a\u6232\u754c\u9762\u4e0d\u65b7\u6ed1\u52d5\u53ef\u4ee5\u52a0\u901f\u79fb\u52d5</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:400;\">3.\u901a\u904e\u8f38\u5165A/D\u9032\u884c\u79fb\u52d5\uff08\u8acb\u6ce8\u610f\uff0c\u672c\u904a\u6232\u7684"
                        "\u6240\u6709\u6d89\u53ca\u5b57\u6bcd\u7684\u8f38\u5165,\u90fd\u9700\u8981\u4ee5\u82f1\u6587\u8f38\u5165\u6cd5\u57f7\u884c\uff09\uff0c\u8f38\u5165\u6578\u5b571/2/3\u4f86\u5207\u63db\u5175\u7a2e</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:400;\">4.\u9078\u5175\u7d50\u675f\u4e26\u9032\u5165\u904a\u6232\u5f8c\uff0c\u9ede\u64caF11\u53ef\u4ee5\u9032\u5165\u5168\u5c4f\u6a21\u5f0f</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Background_Introduction", None))
        self.pushButtonChallengeMode.setText(QCoreApplication.translate("MainWindow", u"\u904a\u6232\u555f\u52d5", None))
        self.menuMade_By_SeleiXI.setTitle(QCoreApplication.translate("MainWindow", u"Made By SeleiXi", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u806f\u7e6b\u4f5c\u8005", None))
    # retranslateUi

