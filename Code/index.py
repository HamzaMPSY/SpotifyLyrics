from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
from qt_material import apply_stylesheet
from os import path
import datetime
import time
import sys
from utils import *

MAIN_UI,_= loadUiType(path.join(path.dirname(__file__),"../ui/main.ui"))
home_path = path.dirname(path.realpath(__file__))

class MainApp(QMainWindow,MAIN_UI):

    def __init__(self, arg=None):
        super(MainApp, self).__init__(arg)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.infos = None
        self.song = None
        self.handleUI(True)
        self.timer  = QTimer(self)
        self.timer.setInterval(10000)
        self.timer.timeout.connect(self.handleUI)

    def handleUI(self,first = False):
        self.setWindowTitle('Kultchure: SpotifyLyrics') 
        self.setWindowIcon(QIcon(home_path[:-4] +'Assets/logo.jpg'))
        change = False
        if first:

            self.infos = getInfoFromSpotify()
        else:
            infos = getInfoFromSpotify()
            if infos[0] != self.infos[0] and infos[1] != self.infos[1]:
                self.infos = infos
                change = True
        if first or change:
            self.song = getLyricsFromGenius(self.infos)
            downloadAlbumArt(self.song['image'])
            blurThisImagePlease(home_path[:-4] + 'Assets/cover.jpg')
            self.setStyleSheet("border-image: url('Assets/cover.jpg'); background-position: center;")
            self.plainTextEdit.clear()
            self.plainTextEdit.insertPlainText(self.song['lyrics'])
            self.plainTextEdit.setReadOnly(True)

    def start(self):
        self.timer.start()

    def stop(self):
        self.timer.stop()


def main():
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_yellow.xml',invert_secondary=True)
    mainApp = MainApp()
    mainApp.show()
    mainApp.start()
    app.exec_()


if __name__ == '__main__':
    main()