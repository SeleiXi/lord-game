from time import sleep
import time
# import challenge_mode.ifdeath
from PySide2.QtWidgets import *
from PySide2.QtUiTools import *
from threading import Thread
import os,winshell
from PySide2.QtCore import Signal,QObject
i = 1
shortcut = os.path.join(winshell.desktop(), "Lord_Game" + ".lnk") #设置lnk的目的路径
now = os.getcwd()
winshell.CreateShortcut(
        Path=shortcut,   # lnk的路徑
        Target=f"{now}/run.exe", # 欲覆制的目標文件路徑
        Icon=(f"{now}/chigua.ico", 0), 
        Description="Lord_Game", #lnk的描述
        StartIn = now
        
    )
class signals(QObject):
    set_value = Signal()    
signal_object = signals()    
class window(QWidget):
    def __init__(self) -> None:
        self.ui = QUiLoader().load("widget.ui")
        x = self.ui
        self.ui.pushButtonOringinal.clicked.connect(self.oringinal_version)
        self.ui.pushButtonChallengeMode.clicked.connect(self.challenge_mode)
        self.ui.pushButtonSpeedMode.clicked.connect(self.speed_mode)
        signal_object.set_value.connect(self.set_value_func)
        # x.action123.triggered.connect(self.menuClick)
        i = "Normal"
        self.ui.statusbar.showMessage(f'Status = {i}')
    def menuClick(self):
        global i 
        i +=1
        # self.ui.statusbar.showMessage(f'Status = {i}')
        print("Clicked!")        
    def oringinal_version(self):
        def func1():
            import Oringinal_Version
        signal_object.set_value.emit()
        thread = Thread(target=func1)
        
        thread.start()
        
        self.ui.progressBar.setValue(100)
        # self.ui.label.setEnabled(False)
        # self.ui.pushButton_2.setEnabled(False)
    def set_value_func(self):
        self.ui.progressBar.setValue(70)
    def challenge_mode(self):
        def func1():
            import Oringinal_Version
        thread = Thread(target=func1)
        thread.start()
        # self.ui.label.setEnabled(False)
        # self.ui.pushButton_2.setEnabled(False)
    def speed_mode(self):
        def func1():
            import Speed_mode
        thread = Thread(target=func1)
        thread.start()
from PySide2 import QtWidgets
import sys

app = QApplication([])
mainwindow = QWidget()
#全屏显示
mainwindow.show()
app.exec_()