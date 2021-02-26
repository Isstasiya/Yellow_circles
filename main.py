import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QFrame
from PyQt5 import uic, QtWidgets
from PyQt5.QtGui import QPainter, QColor
from random import randint


class MyWidget(QFrame):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.t = False
        self.r = []
        self.pushButton.clicked.connect(self.run)
        self.show()

    def run(self):
        self.t = True
        self.update()
    
    def paintEvent(self, event):
        if self.t:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()
        
    def draw(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        x = randint(0, 100)
        self.r.append([randint(0, 380), randint(0, 320), x, x])
        for i in self.r:
            qp.drawEllipse(*i)
        self.t = False

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())