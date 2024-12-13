import sys

from PyQt6.QtWidgets import QWidget, QApplication


class PaintСircle(QWidget):
    def __init__(self):
        self.initUI()

    def initUI(self):



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PaintСircle()
    ex.show()
    sys.exit(app.exec())
