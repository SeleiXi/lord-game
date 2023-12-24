from time import sleep
import time
# import challenge_mode.ifdeath
from PySide2.QtWidgets import *
from PySide2.QtUiTools import *
from threading import Thread
import os,winshell
from PySide2.QtCore import Signal,QObject
import webbrowser

i = 1
shortcut = os.path.join(winshell.desktop(), "Lord_Game" + ".lnk") #設置lnk的目的路徑
now = os.getcwd()
winshell.CreateShortcut(
        Path=shortcut,   # lnk的路徑
        Target=f"{now}/run.exe", # 欲覆制的目標文件路徑
        Icon=(f"{now}/icons/chigua.ico", 0), 
        Description="Lord_Game", #lnk的描述
        StartIn = now
        
    )
class signals(QObject):
    set_value = Signal()    
signal_object = signals()    
class window():
    def __init__(self) -> None:
        self.ui = QUiLoader().load("menu2.ui")
        x = self.ui
        # self.ui.pushButtonOringinal.clicked.connect(self.oringinal_version)
        self.ui.pushButtonChallengeMode.clicked.connect(self.challenge_mode)
        # self.ui.pushButtonSpeedMode.clicked.connect(self.speed_mode)
        signal_object.set_value.connect(self.set_value_func)
        # x.action123.triggered.connect(self.menuClick)
        i = "Normal"
        self.ui.statusbar.showMessage(f'Status = {i}')

        # 鏈接【聯繫作者】中的各個項目
        actionDiscord = self.ui.actionDiscord
        self.ui.menu.addAction(actionDiscord)  
        actionDiscord.triggered.connect(self.discord_link)

        actionQQ = self.ui.actionQQ
        self.ui.menu.addAction(actionQQ)  
        actionQQ.triggered.connect(self.QQ_link)

        actionEmail = self.ui.actionEmail
        self.ui.menu.addAction(actionEmail)  
        actionEmail.triggered.connect(self.mailto_me)

        actionGithub = self.ui.actionGithub
        self.ui.menu.addAction(actionGithub)  
        actionGithub.triggered.connect(self.github_link)

    def menuClick(self):
        global i 
        i +=1
        # self.ui.statusbar.showMessage(f'Status = {i}')
        print("Clicked!")        
    # def oringinal_version(self):
        # def func1():
        #     import Oringinal_Version
        # signal_object.set_value.emit()
        # thread = Thread(target=func1)
        
        # thread.start()
        
        # self.ui.progressBar.setValue(100)
        # self.ui.label.setEnabled(False)
        # self.ui.pushButton_2.setEnabled(False)
    def set_value_func(self):
        self.ui.progressBar.setValue(70)
    def discord_link(self):
        webbrowser.open("https://discord.com/users/700623146197450855")
    def QQ_link(self):
        webbrowser.open("tencent://message/?uin=1632845225&Site=&Menu=yes")
    def mailto_me(self):
        webbrowser.open("mailto:SeleiXi<bzhanthresh@gmail.com>")
    def github_link(self):
        webbrowser.open("github.com/seleixi")


        
    def challenge_mode(self):
        def func1():
            import main
        thread = Thread(target=func1)
        thread.start()
        self.ui.progressBar.setValue(100)             
        # self.ui.label.setEnabled(False)
        # self.ui.pushButton_2.setEnabled(False)
    # def speed_mode(self):
    #     def func1():
    #         import Speed_mode
    #     thread = Thread(target=func1)
    #     thread.start()
    #     self.ui.progressBar.setValue(100)
app = QApplication([])
stats = window()
stats.ui.show()
app.exec_()    