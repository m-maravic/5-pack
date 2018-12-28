import sys
from PyQt5.QtWdgets import*
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class ViewWindow (QWidget):
    def _init_(self):
        super()._init_()

        self.initUI()

    def initUI(self):
        self.resize(800,800)
        self.setWindowlitle('Dyna Blaster ')
        self.setWindowIcon(QIcon('icon.png'))


        palette = QPalette()
        palette.setBrush(10, Qt.black)
        self.setPalette(palette)

        self.show()

    def closeEvent(self,event):

        reply =QMessageBox.question(self, 'Dyna Blaster')
          if reply == QMessageBox.Yes:
              event.accept()
         else
              event.ignore()