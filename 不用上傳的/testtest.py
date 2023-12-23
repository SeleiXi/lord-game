from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader

class Stats:
    # 治療面板
    def __init__(self):
        self.ui = QUiLoader().load('cure.ui')
        self.ui.pushButton.clicked.connect(self.cure)
    def cure(self):
        global money,character_dict
        number  = self.ui.spinBox.value()
        if number<=money:
            pass


app = QApplication([])
stats = Stats()
stats.ui.show()
app.exec_()