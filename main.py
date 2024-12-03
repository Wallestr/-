import sys
import random

from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QPainter, QPen, QColor, QPolygonF
from PyQt6.QtCore import Qt, QPointF, QRectF, QSizeF
from PyQt6 import uic 


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self) 
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(
            QColor(
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255),
                )
            )
        hh = random.randint(20, 100)
        painter.drawEllipse(QPointF(self.width() / 2, self.height() / 2), hh, hh)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())