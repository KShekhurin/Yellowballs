from random import randint
import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class Controller:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.view = View(self)
        self.ball = (0, 0, 0)

    def run(self):
        self.view.show()
        sys.exit(self.app.exec_())

    def gen_ball(self):
        length = randint(0, min(self.view.height(), self.view.width()))

        posx, posy = (
            randint(0, abs(self.view.width() - length)),
            randint(0, abs(self.view.height() - length))
        )

        self.ball = (posx, posy, length)
        self.view.repaint()


class View(QMainWindow):
    def __init__(self, controller: Controller):
        super(QMainWindow, self).__init__()
        uic.loadUi("Ui.ui", self)

        self.controller = controller
        self.init_bindings()

    def init_bindings(self):
        self.genBall_btn.clicked.connect(self.controller.gen_ball)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_balls(None, qp)
        qp.end()

    def draw_balls(self, event, qp):
        posx, posy, length = self.controller.ball
        qp.setBrush(QColor(255, 0, 0))
        qp.drawEllipse(posx, posy, length, length)


if __name__ == "__main__":
    controller = Controller()
    controller.run()