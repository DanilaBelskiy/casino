from PyQt5.QtWidgets import QApplication
from gui import Window

import sys


def application():
    app = QApplication(sys.argv)
    win = Window()

    win.show()
    sys.exit(app.exec_())
