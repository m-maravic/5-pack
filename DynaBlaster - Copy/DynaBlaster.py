import sys
from PyQt5.QtWidgets import*
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class ViewWindow (QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()

    def initUI(self):
        self.resize(800,800)
        self.setWindowTitle('Dyna Blaster')
        self.setWindowIcon(QIcon('projekat_slika1.jpg'))


        palette = QPalette()
        palette.setBrush(10, Qt.black)
        self.setPalette(palette)

        self.show()

    def closeEvent(self,event):
        reply = QMessageBox.question(self, 'Dyna Blaster', 'Are you sure you want to exit?',QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()



if  __name__ =='__main__':
    app=QApplication(sys.argv)
    ex= ViewWindow()
    sys.exit(app.exec_())