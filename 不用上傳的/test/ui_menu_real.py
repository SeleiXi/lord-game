# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu_real.ui'
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
        MainWindow.resize(758, 699)
        MainWindow.setStyleSheet(u"QPushButton{\n"
"color:Red}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u"C:/Users/bzhan/Desktop/test_decompiler/chigua.png"))

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignHCenter)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 30, -1, 30)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily(u"MiSans Heavy")
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_2.setFont(font)

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)
        self.pushButton.setFont(font)
        self.pushButton.setAutoDefault(False)
        self.pushButton.setFlat(False)

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setEnabled(True)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setFont(font)
        icon = QIcon()
        icon.addFile(u"../../../\u5c01\u9762/chigua.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon)

        self.horizontalLayout.addWidget(self.pushButton_3)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMaximum(5)
        self.progressBar.setValue(0)

        self.verticalLayout.addWidget(self.progressBar)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 758, 23))
        self.menuMade_By_SeleiXI = QMenu(self.menubar)
        self.menuMade_By_SeleiXI.setObjectName(u"menuMade_By_SeleiXI")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMade_By_SeleiXI.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Lord_Game", None))
        self.label.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Oringinal", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Speed Mode", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Challenge Mode", None))
        self.menuMade_By_SeleiXI.setTitle(QCoreApplication.translate("MainWindow", u"Made By SeleiXI", None))
    # retranslateUi

