import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)pip install PyQt5 PyQtWebEngine
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class MyBrowser(QMainWindow):
    def __init__(self):
        super(MyBrowser, self).__init__()
        
        # Set up the web view (the part that shows the website)
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://www.google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # Create a navigation bar
        navbar = QToolBar()
        self.addToolBar(navbar)

        # Back Button
        back_btn = QAction('Back', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        # Forward Button
        forward_btn = QAction('Forward', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        # Reload Button
        reload_btn = QAction('Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        # Home Button
        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        # URL Bar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        # Update the URL bar text when the page changes
        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(QUrl('https://www.google.com'))

    def navigate_to_url(self):
        url = self.url_bar.text()
        if not url.startswith('http'):
            url = 'http://' + url
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())

# Execute the application
app = QApplication(sys.argv)
QApplication.setApplicationName('My Python Browser')
window = MyBrowser()
app.exec_()
