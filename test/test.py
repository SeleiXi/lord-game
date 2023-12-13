from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtWebEngineWidgets import *

class TabWidget(QTabWidget):
    def __init__(self, *args, **kwargs):
        QTabWidget.__init__(self, *args, **kwargs)
        url = QUrl("https://www.google.com")
        view = HtmlView(self)
        view.load(url)
        ix = self.addTab(view, "加载中 ...")
        self.resize(800, 600)

class HtmlView(QWebEngineView):
    def __init__(self, *args, **kwargs):
        QWebEngineView.__init__(self, *args, **kwargs)
        self.tab = self.parent()


    def createWindow(self, windowType):
        if windowType == QWebEnginePage.WebBrowserTab:
            webView = HtmlView(self.tab)
            ix = self.tab.addTab(webView, "加载中 ...")
            self.tab.setCurrentIndex(ix)
            navigation_bar = QToolBar('Navigation')
        # 设定图标的大小
            navigation_bar.setIconSize(QSize(16, 16))
            #添加导航栏到窗口中
            self.addToolBar(navigation_bar)
            return webView
        return QWebEngineView.createWindow(self, windowType)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    main = TabWidget()
    main.show()
    sys.exit(app.exec_())