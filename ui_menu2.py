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
        MainWindow.resize(561, 677)
        icon = QIcon()
        icon.addFile(u"chigua.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QPushButton{\n"
"color:Red}\n"
"QMainWindow{\n"
"background-color:white\n"
"}")
        self.actionQQ1632845225 = QAction(MainWindow)
        self.actionQQ1632845225.setObjectName(u"actionQQ1632845225")
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
        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setFamily(u"MiSans")
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(Qt.RichText)

        self.verticalLayout_2.addWidget(self.label_2)

        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u"C:/Users/bzhan/Desktop/test_decompiler/chigua.png"))

        self.verticalLayout_2.addWidget(self.label)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_3 = QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.textBrowser = QTextBrowser(self.tab_2)
        self.textBrowser.setObjectName(u"textBrowser")
        font1 = QFont()
        font1.setFamily(u"MiSans Heavy")
        font1.setPointSize(28)
        font1.setBold(True)
        font1.setWeight(75)
        self.textBrowser.setFont(font1)
        self.textBrowser.setLineWrapMode(QTextEdit.WidgetWidth)

        self.verticalLayout_3.addWidget(self.textBrowser)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 30, -1, 30)
        self.pushButtonOringinal = QPushButton(self.centralwidget)
        self.pushButtonOringinal.setObjectName(u"pushButtonOringinal")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonOringinal.sizePolicy().hasHeightForWidth())
        self.pushButtonOringinal.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setFamily(u"MiSans Heavy")
        font2.setBold(True)
        font2.setItalic(False)
        font2.setWeight(75)
        self.pushButtonOringinal.setFont(font2)

        self.horizontalLayout.addWidget(self.pushButtonOringinal)

        self.pushButtonChallengeMode = QPushButton(self.centralwidget)
        self.pushButtonChallengeMode.setObjectName(u"pushButtonChallengeMode")
        self.pushButtonChallengeMode.setEnabled(True)
        sizePolicy.setHeightForWidth(self.pushButtonChallengeMode.sizePolicy().hasHeightForWidth())
        self.pushButtonChallengeMode.setSizePolicy(sizePolicy)
        self.pushButtonChallengeMode.setFont(font2)
        icon1 = QIcon()
        icon1.addFile(u"../../../\u5c01\u9762/chigua.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonChallengeMode.setIcon(icon1)

        self.horizontalLayout.addWidget(self.pushButtonChallengeMode)

        self.pushButtonSpeedMode = QPushButton(self.centralwidget)
        self.pushButtonSpeedMode.setObjectName(u"pushButtonSpeedMode")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButtonSpeedMode.sizePolicy().hasHeightForWidth())
        self.pushButtonSpeedMode.setSizePolicy(sizePolicy1)
        self.pushButtonSpeedMode.setFont(font2)
        self.pushButtonSpeedMode.setAutoDefault(False)
        self.pushButtonSpeedMode.setFlat(False)

        self.horizontalLayout.addWidget(self.pushButtonSpeedMode)


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
        self.menu.addAction(self.actionQQ1632845225)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u7075\u9053\u6e90\u5c0a", None))
        self.actionQQ1632845225.setText(QCoreApplication.translate("MainWindow", u"QQ1632845225", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">\u8239\u65b0Version\uff0c\u9707\u64bc\u4f86\u8972\uff01</span></p></body></html>", None))
        self.label.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Home Page", None))
        self.textBrowser.setDocumentTitle("")
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MiSans Heavy'; font-size:28pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'SimSun'; font-size:16pt;\">\u6b22\u8fce\u6765\u5230\u7075\u9053\u6e90\u5c0a\uff01 </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'SimSun'; font-size:10pt;\">\u6e38\u620f\u6539\u7f16\u81ea\u5c0f\u8bf4(\u540c\u672c\u7a0b\u5e8f\u4f5c\u8005\u6240\u8457)\uff1ahttps://book.qidian.com/info/1030712451/</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-rig"
                        "ht:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'SimSun'; font-size:12pt;\">\u5929\u5143\u5e9c\u906d\u5230\u7075\u517d\u4fb5\u5360\u540e,\u5e9c\u5185\u56db\u5904\u72fc\u85c9,\u4e2b\u9b1f\u4e0e\u5e9c\u4e3b\u7686\u88ab\u62d0\u53bb,\u56da\u7981\u5728\u9b54\u708e\u68ee\u6df1\u5904\u3002\u4ec5\u6709\u7075\u738b\u5883\u754c\u7684\u4f60\u65e0\u529b\u62b5\u6297,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'SimSun'; font-size:12pt;\">\u4f46\u5728\u7075\u754c\u5929\u5730\u4e2d,\u4f60\u53ef\u4ee5\u4e34\u65f6\u4ee580\u7075\u77f3\u4ece\u6e90\u754c\u9886\u57df\u53ec\u5524\u4e00\u4f4d\u706b\u9e3d\u5b50(\u8840\u91cf\u4e3a80)\u4ee5\u53ca\u4ee5100\u7075\u77f3\u96c7\u4f63\u4e00\u4f4d\u6765\u81ea\u661f\u7075\u65cf\u7684\u7384\u8005(\u8840\u91cf\u4e3a100)\u3002</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:"
                        "0px;\"><span style=\" font-family:'SimSun'; font-size:12pt;\">\u5728\u9b54\u708e\u68ee\u5de1\u903b\u5b88\u536b\u7684\u901a\u5e38\u53ea\u6709\u5996\u5f2d\u7334\u4e0e\u95ea\u7535\u7329,\u5996\u5f2d\u7334\u751f\u6027\u6015\u706b,\u800c\u661f\u7075\u65cf\u7684\u6218\u58eb\u4eec\u62e5\u6709\u7075\u80fd\u62a4\u7532\u800c\u65e0\u60e7\u95ea\u7535\u3002</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'SimSun'; font-size:12pt;\">\u6545\u6b64\u706b\u9e3d\u5b50\u53ea\u9700\u6d88\u801730\u8840\u4fbf\u53ef\u51fb\u6740\u5996\u5f2d\u7334,\u4f46\u7384\u8005\u5219\u9700\u6d88\u801750\u8840\u3002\u7384\u8005\u6d88\u801730\u8840\u53ef\u51fb\u6740\u95ea\u7535\u7329,\u800c\u706b\u9e3d\u5b50\u970050\u8840\u3002</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'SimSun'; font-size:12pt;\">\u5728\u5168\u5c40\u6e38"
                        "\u620f\u4e2d,\u4f60\u62e5\u6709\u4e00\u6b21\u673a\u4f1a\u4ee5\u5929\u773c\u89c6\u5bdf\u9b54\u708e\u68ee\u4e2d\u7684\u7075\u517d\u5206\u5e03\u3002</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'SimSun'; font-size:12pt;\">\u4ee5\u53ca\u4f60\u62e5\u6709\u65e0\u6570\u6b21\u673a\u4f1a,\u4ee5\u7075\u77f3\u8fdc\u7a0b\u6cbb\u6108\u6218\u6597\u540e\u7684\u706b\u9e3d\u5b50\u53ca\u7384\u8005\u3002\u7075\u77f3\u4e0e\u751f\u547d\u7684\u5151\u6362\u6bd4\u4f8b\u4e3a1:1</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'SimSun'; font-size:12pt;\">\u4f60\u8eab\u4e0a\u4ec5\u6709400\u7075\u77f3,\u4ecb\u4e8e\u96c7\u4f63\u7684\u53cb\u519b\u5728\u6218\u6597\u540e\u7686\u4f1a\u6d88\u5931,\u8bd5\u4ee5\u6700\u4f4e\u7684\u82b1\u9500\u51fb\u8d25\u9b54\u708e\u68ee\u4e2d\u7684\u7075\u517d\u5e76\u62ef\u6551\u906d\u5230"
                        "\u4fd8\u864f\u7684\u4eba\u4eec\u3002</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'SimSun'; font-size:12pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'SimSun'; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'SimSun'; font-size:12pt; font-style:italic;\">\u6ce8\u610f\uff1a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'SimSun'; font-size:12pt; font-style:italic;\">1.\u4f60\u9700\u8981\u5728\u6e38\u620f\u5f00\u59cb\u65f6\u4fbf\u96c7\u4f63\u4f60\u9700\u8981\u96c7\u4f63\u7684\u53cb\u519b\u3002</span></p>\n"
"<p styl"
                        "e=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'SimSun'; font-size:12pt; font-style:italic;\">2.\u8fdb\u5165\u6e38\u620f\u540e\u70b9\u51fbF11\u5373\u53ef\u8fdb\u5165\u5168\u5c4f</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'SimSun'; font-size:12pt; font-style:italic;\">3.\u901a\u5173\u8bc4\u7ea7\u5206\u4e3a\u3010\u6781\u5176\u5b8c\u7f8e\u3011 / \u3010\u5b8c\u7f8e\u3011 / \u3010\u4f18\u79c0\u3011 / \u3010\u4e0d\u9519\u3011 / \u3010\u4e00\u822c\u3011</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Background_Introduction", None))
        self.pushButtonOringinal.setText(QCoreApplication.translate("MainWindow", u"Oringinal", None))
        self.pushButtonChallengeMode.setText(QCoreApplication.translate("MainWindow", u"Challenge Mode", None))
        self.pushButtonSpeedMode.setText(QCoreApplication.translate("MainWindow", u"Speedrun Mode", None))
        self.menuMade_By_SeleiXI.setTitle(QCoreApplication.translate("MainWindow", u"Made By SeleiXI", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u8054\u7cfb\u4f5c\u8005", None))
    # retranslateUi

