import sys
from threading import Thread
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPainter, QBrush, QImage, QFont
from PyQt5.QtCore import Qt
from definitions import *
from wall import *

from PyQt5.QtWidgets import*
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QPainter, QBrush, QImage, QFont

#Matrix = [[0 for x in range(width)] for y in range(height)]
Matrix=make_matrix()
#Matrix=makeDestructableWall()

class ViewWindow (QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()

    def initUI(self):
        self.resize(600,600)
        self.setWindowTitle('Dyna Blaster')
        self.setWindowIcon(QIcon('projakat_slika1.jpg'))


        palette = QPalette()
        palette.setBrush(10, Qt.darkGray)
        self.setPalette(palette)

        self.show()

    def closeEvent(self,event):
        reply = QMessageBox.question(self, 'Dyna Blaster', 'Are you sure you want to exit?',QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawBrushes(qp)
        qp.end()


    def drawBrushes(self,qp):
        nullbrush = QBrush()
        emptybrush = QBrush(Qt.darkGreen)
        wallImage = QImage("IndestructableWall.jpg")
        wallbrush = QBrush()
        wallbrush.setTextureImage(wallImage)

        wallImage2 = QImage("Wall.jpg")
        wallbrush2 = QBrush()
        wallbrush2.setTextureImage(wallImage2)

        bombImage = QImage("Bomb.jpg")
        bombBrush = QBrush()
        bombBrush.setTextureImage(bombImage)






#iscrtevanje na tabli
        w=0
        h=0
        offset=40
        for i in range(0,height):
            for j in range(0,width):
                if(Kind(Matrix[i][j])==Kind.Empty):
                        qp.setBrush(emptybrush)
                elif(Kind(Matrix[i][j])==Kind.IndestructibleWall):
                    qp.setBrush(wallbrush)
                elif(Kind(Matrix[i][j])==Kind.Wall):
                    qp.setBrush(wallbrush2)
                qp.drawRect(w, h, 40, 40)
                w = w + offset
            w = 0
            h = h + offset

if  __name__ =='__main__':
    app=QApplication(sys.argv)
    ex= ViewWindow()
    sys.exit(app.exec_())