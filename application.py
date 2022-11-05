from PyQt5.QtWidgets import QApplication
from gui import Window

import sys

"""
Start application with interface
Application is game in roulette
User have capital
He can bet money on number or color
He can win money or lose
"""


def application():
    app = QApplication(sys.argv)
    win = Window()

    win.show()
    sys.exit(app.exec_())
