# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_LordGame(object):
    def setupUi(self, LordGame):
        if not LordGame.objectName():
            LordGame.setObjectName(u"LordGame")
        LordGame.resize(611, 671)
        LordGame.setStyleSheet(u"#horizontalLayout QPushButton{\n"
"color:blue;\n"
"backgroundcolor:red;\n"
"}\n"
".QDialog .QPushButton{\n"
"color:yellow;\n"
"}\n"
"QCheckBox:hover:checked { color: red }")
        self.action = QAction(LordGame)
        self.action.setObjectName(u"action")
        self.action123 = QAction(LordGame)
        self.action123.setObjectName(u"action123")
        self.action321 = QAction(LordGame)
        self.action321.setObjectName(u"action321")
        self.centralwidget = QWidget(LordGame)
        self.centralwidget.setObjectName(u"centralwidget")
        font = QFont()
        font.setFamily(u"System")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.centralwidget.setFont(font)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(110, -20, 541, 451))
        self.label.setPixmap(QPixmap(u"C:/Users/bzhan/Desktop/test_decompiler/chigua.png"))
        self.keySequenceEdit = QKeySequenceEdit(self.tab)
        self.keySequenceEdit.setObjectName(u"keySequenceEdit")
        self.keySequenceEdit.setGeometry(QRect(80, 480, 113, 20))
        self.toolButton = QToolButton(self.tab)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setGeometry(QRect(290, 480, 37, 18))
        self.comboBox = QComboBox(self.tab)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(20, 180, 69, 22))
        self.radioButton = QRadioButton(self.tab)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(20, 210, 89, 16))
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.horizontalLayout_3 = QHBoxLayout(self.tab_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.checkBox_2 = QCheckBox(self.tab_2)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.horizontalLayout_4.addWidget(self.checkBox_2)

        self.pushButton_4 = QPushButton(self.tab_2)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_4.addWidget(self.pushButton_4)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.listWidget = QListWidget(self.tab_2)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        self.listWidget.setObjectName(u"listWidget")

        self.horizontalLayout_2.addWidget(self.listWidget)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.textEdit = QTextEdit(self.tab_3)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(0, 0, 711, 391))
        self.tabWidget.addTab(self.tab_3, "")

        self.verticalLayout.addWidget(self.tabWidget)

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
        font1 = QFont()
        font1.setFamily(u"MiSans Heavy")
        font1.setBold(True)
        font1.setItalic(False)
        font1.setWeight(75)
        self.pushButton_2.setFont(font1)

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)
        self.pushButton.setFont(font1)
        self.pushButton.setAutoDefault(False)
        self.pushButton.setFlat(False)

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setEnabled(True)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setFont(font1)
        icon = QIcon()
        icon.addFile(u"../../../\u5c01\u9762/chigua.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon)

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(u"checkBox")

        self.horizontalLayout.addWidget(self.checkBox)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMaximum(5)
        self.progressBar.setValue(0)

        self.verticalLayout.addWidget(self.progressBar)

        self.buttonBox = QDialogButtonBox(self.centralwidget)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStyleSheet(u"")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)

        LordGame.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(LordGame)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 611, 23))
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        LordGame.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(LordGame)
        self.statusbar.setObjectName(u"statusbar")
        LordGame.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(LordGame)
        self.toolBar.setObjectName(u"toolBar")
        LordGame.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuHelp.addSeparator()
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.action123)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.action321)
        self.toolBar.addAction(self.action123)
        self.toolBar.addAction(self.action321)

        self.retranslateUi(LordGame)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(LordGame)
    # setupUi

    def retranslateUi(self, LordGame):
        LordGame.setWindowTitle(QCoreApplication.translate("LordGame", u"LordGame", None))
        self.action.setText(QCoreApplication.translate("LordGame", u"\u4f5c\u8005\u806f\u7e6b\u65b9\u5f0f", None))
        self.action123.setText(QCoreApplication.translate("LordGame", u"123", None))
        self.action321.setText(QCoreApplication.translate("LordGame", u"321", None))
        self.label_3.setText(QCoreApplication.translate("LordGame", u"TextLabel", None))
        self.label.setText("")
        self.toolButton.setText(QCoreApplication.translate("LordGame", u"...", None))
        self.radioButton.setText(QCoreApplication.translate("LordGame", u"RadioButton", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("LordGame", u"Tab 1", None))
        self.checkBox_2.setText(QCoreApplication.translate("LordGame", u"CheckBox", None))
        self.pushButton_4.setText(QCoreApplication.translate("LordGame", u"PushButton", None))

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("LordGame", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qlistwidgetitem1 = self.listWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("LordGame", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qlistwidgetitem2 = self.listWidget.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("LordGame", u"\u65b0\u5efa\u9879\u76ee", None));
        self.listWidget.setSortingEnabled(__sortingEnabled)

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("LordGame", u"123", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("LordGame", u"asd", None))
        self.pushButton_2.setText(QCoreApplication.translate("LordGame", u"Oringinal", None))
        self.pushButton.setText(QCoreApplication.translate("LordGame", u"Speed Mode", None))
        self.pushButton_3.setText(QCoreApplication.translate("LordGame", u"Challenge Mode", None))
        self.checkBox.setText(QCoreApplication.translate("LordGame", u"123", None))
        self.menuHelp.setTitle(QCoreApplication.translate("LordGame", u"Made By SeleiXi", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("LordGame", u"toolBar", None))
    # retranslateUi

