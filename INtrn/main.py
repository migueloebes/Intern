from PyQt5.QtCore import *
from qtpy.QtCore import QUrl
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QAction
from PyQt5.QtWebEngineWidgerts import QWebEngineView

class MainWindow(QMainWindow):
     super().__init__()
self.setWindowTitle("Intrn")
self.setWindowIcon(QIcon('icon./https://media.discordapp.net/attachments/1466835985911386458/1492275825377017936/intern-removebg-preview.png?ex=69dcb7e9&is=69db6669&hm=15b201cbc2295ba184ad02eba6d5ae45d4e5f7aff90da787e9695eb9a35547b3&=&format=webp&quality=lossless'))  
self.setWindowFlags(Qt.Window)
     
def __init__(self):
        super(MainWindow, self).__int__()
        self.Brownser = QWebEngineView()
        self.brownser.setUrl (QUrl('https//google.com'))
        self.setCentralWidget(self.browser)
        self.showNormal()
# central
        ncentral_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

# voltar
        back_btn = QAction('back', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

# avançar

        forward_btn = QAction('Advance', self)  
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

# recarregar

        reload_btn = QAction('Recharge', self)  
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

# home

        home_btn = QAction('Home', self)  
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

def navigate_home(self):
        self.browser.setUrl(QUrl('https://duckduckgo.com'))  # Define a URL inicial

# Navegur com url 
def navigate_to_url(self):  
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

# atualize a url
def update_url(self):  
        self.url_bar.setText(self.browser.url().toString())

        
       # Favoritos
        self.bookmark_button = QPushButton("Bookmark")
        self.bookmark_button.setIcon(QIcon('icon/bookmark_icon.png'))  # Icon for the bookmark button
        self.bookmark_button.setIconSize(QSize(32, 32))
        nav_layout.addWidget(self.bookmark_button)

        # menu de favoritos
        self.bookmark_menu = QMenu("Bookmarks", self)
        self.bookmark_button.setMenu(self.bookmark_menu)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    QApplication.setApplicationName('Intrn')
    window = MainWindow()
    app.exec_()

