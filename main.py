import sys

from PyQt5 import uic
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QPen, QColor, QPolygon
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QMainWindow
from random import randint
from Ui import Ui_MainWindow


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.do_paint = False
        self.a = 3
        self.x = 100
        self.y = 100
        self.a = 0
        self.pushButton.clicked.connect(self.pa)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        if self.a == 1:
            self.draw_ellipse(qp)
            self.a = 0
        qp.end()

    def pa(self):
        self.a = 1
        self.repaint()

    def draw_ellipse(self, qp):
        qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        x = randint(50, 150)
        qp.drawEllipse(150, 150, x, x)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
