from PyQt5 import QtWidgets, QtGui, Qt
from PyQt5.QtWidgets import QMainWindow, QLineEdit
from color_number_table import color_number_table
from win_lose_check import win_lose_check

import time

"""
Graphical user interface class
"""


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.c_n_table = color_number_table()

        self.setWindowTitle("Casino")
        self.setFixedSize(1500, 610)
        self.setStyleSheet("background-image : url(resources/background_big.png)")

        # Create main buttons
        self.main_buttons = []
        for i in range(0, 37):
            self.main_buttons.append(QtWidgets.QPushButton(self))
            self.main_buttons[i].setText(f"{i}")

        # Set style for main buttons
        for i in range(len(self.main_buttons)):
            if self.c_n_table[i] == "red":
                self.main_buttons[i].setStyleSheet(
                    "background-color : red; color : white; background-image : url()")
            elif self.c_n_table[i] == "black":
                self.main_buttons[i].setStyleSheet(
                    "background-color : black; color : white; background-image : url();")
            elif self.c_n_table[i] == "green":
                self.main_buttons[i].setStyleSheet("background-color : green; background-image : url()")

        # Set font for main buttons
        for i in range(len(self.main_buttons)):
            self.main_buttons[i].setFont(QtGui.QFont("Comic Sans", 12))

        self.main_size = 100

        # Set geometry for main buttons
        for i in range(1, len(self.main_buttons)):
            if i % 3 == 0:
                self.main_buttons[i].setGeometry(0 + (36-i) // 3 * self.main_size, 0, self.main_size, self.main_size)
            elif i % 3 == 1:
                self.main_buttons[i].setGeometry(0 + (36-i) // 3 * self.main_size, self.main_size * 2, self.main_size, self.main_size)
            else:
                self.main_buttons[i].setGeometry(0 + (36-i) // 3 * self.main_size, self.main_size, self.main_size, self.main_size)
        self.main_buttons[0].setGeometry(self.main_size * 12, 0, self.main_size, self.main_size * 3)

        # Set actions for main buttons
        self.main_buttons[0].clicked.connect(lambda: main_button_click(self, 0))
        self.main_buttons[1].clicked.connect(lambda: main_button_click(self, 1))
        self.main_buttons[2].clicked.connect(lambda: main_button_click(self, 2))
        self.main_buttons[3].clicked.connect(lambda: main_button_click(self, 3))
        self.main_buttons[4].clicked.connect(lambda: main_button_click(self, 4))
        self.main_buttons[5].clicked.connect(lambda: main_button_click(self, 5))
        self.main_buttons[6].clicked.connect(lambda: main_button_click(self, 6))
        self.main_buttons[7].clicked.connect(lambda: main_button_click(self, 7))
        self.main_buttons[8].clicked.connect(lambda: main_button_click(self, 8))
        self.main_buttons[9].clicked.connect(lambda: main_button_click(self, 9))
        self.main_buttons[10].clicked.connect(lambda: main_button_click(self, 10))
        self.main_buttons[11].clicked.connect(lambda: main_button_click(self, 11))
        self.main_buttons[12].clicked.connect(lambda: main_button_click(self, 12))
        self.main_buttons[13].clicked.connect(lambda: main_button_click(self, 13))
        self.main_buttons[14].clicked.connect(lambda: main_button_click(self, 14))
        self.main_buttons[15].clicked.connect(lambda: main_button_click(self, 15))
        self.main_buttons[16].clicked.connect(lambda: main_button_click(self, 16))
        self.main_buttons[17].clicked.connect(lambda: main_button_click(self, 17))
        self.main_buttons[18].clicked.connect(lambda: main_button_click(self, 18))
        self.main_buttons[19].clicked.connect(lambda: main_button_click(self, 19))
        self.main_buttons[20].clicked.connect(lambda: main_button_click(self, 20))
        self.main_buttons[21].clicked.connect(lambda: main_button_click(self, 21))
        self.main_buttons[22].clicked.connect(lambda: main_button_click(self, 22))
        self.main_buttons[23].clicked.connect(lambda: main_button_click(self, 23))
        self.main_buttons[24].clicked.connect(lambda: main_button_click(self, 24))
        self.main_buttons[25].clicked.connect(lambda: main_button_click(self, 25))
        self.main_buttons[26].clicked.connect(lambda: main_button_click(self, 26))
        self.main_buttons[27].clicked.connect(lambda: main_button_click(self, 27))
        self.main_buttons[28].clicked.connect(lambda: main_button_click(self, 28))
        self.main_buttons[29].clicked.connect(lambda: main_button_click(self, 29))
        self.main_buttons[30].clicked.connect(lambda: main_button_click(self, 30))
        self.main_buttons[31].clicked.connect(lambda: main_button_click(self, 31))
        self.main_buttons[32].clicked.connect(lambda: main_button_click(self, 32))
        self.main_buttons[33].clicked.connect(lambda: main_button_click(self, 33))
        self.main_buttons[34].clicked.connect(lambda: main_button_click(self, 34))
        self.main_buttons[35].clicked.connect(lambda: main_button_click(self, 35))
        self.main_buttons[36].clicked.connect(lambda: main_button_click(self, 36))

        # Create color buttons
        self.red_button = QtWidgets.QPushButton(self)
        self.black_button = QtWidgets.QPushButton(self)

        # Create style for color buttons
        self.red_button.setStyleSheet("background-color : red; color : white; background-image : url()")
        self.black_button.setStyleSheet("background-color : black; color : white; background-image : url()")

        # Set geometry for color buttons
        self.red_button.setGeometry(0, self.main_size * 3, self.main_size * 6, self.main_size)
        self.black_button.setGeometry(self.main_size * 6, self.main_size * 3, self.main_size * 6, self.main_size)

        # Set text for color buttons
        self.red_button.setText("Red color")
        self.black_button.setText("Black color")

        # Set font for color buttons
        self.red_button.setFont(QtGui.QFont("Comic Sans", 20))
        self.black_button.setFont(QtGui.QFont("Comic Sans", 20))

        # Set actions for color buttons
        self.red_button.clicked.connect(lambda: color_button_click(self, "red"))
        self.black_button.clicked.connect(lambda: color_button_click(self, "black"))

        # Create rate-interface
        self.rate_text = QtWidgets.QLabel(self)
        self.rate_text.setText("Chose your bet:")
        self.rate_line = QLineEdit(self)

        # Set geometry for rate-interface
        self.rate_text.setGeometry(0, self.main_size * 4.1, self.main_size * 2.5, 60)
        self.rate_line.setGeometry(0, self.main_size * 5, self.main_size * 2, 60)

        # Set font for rate interface
        self.rate_text.setFont(QtGui.QFont("Comic Sans", 20))
        self.rate_line.setFont(QtGui.QFont("Comic Sans", 20))

        # Set style for rate-interface
        self.rate_text.setStyleSheet("color : white; background-image : url()")
        self.rate_line.setStyleSheet("color : white")

        # Create play button
        self.play_button = QtWidgets.QPushButton(self)

        # Set style for play button
        self.play_button.setStyleSheet("background-color : green; color : white; background-image : url(resources/play_button_small.jpg)")

        # Set font for play button
        self.play_button.setFont(QtGui.QFont("Comic Sans", 20))

        # Set geometry for play button
        self.play_button.setGeometry(self.main_size * 3, self.main_size * 4.1, self.main_size * 2, self.main_size * 2)

        # Set text for play button
        self.play_button.setText("")

        # Create progress_bar
        self.pbar = QtWidgets.QProgressBar(self)
        self.pbar.setHidden(True)
        self.pbar.setGeometry(self.main_size * 5.5, self.main_size * 4.8, self.main_size * 3, self.main_size * 0.4)

        # Set action for play button
        self.play_button.clicked.connect(lambda: play_button_click(self))

        # Create capital variable
        self.capital = 100

        # Create capital label
        self.capital_label = QtWidgets.QLabel(self)
        self.capital_label.setText(f"Money:\n{self.capital}")
        self.capital_label.setGeometry(self.main_size * 13, 0, self.main_size * 2, self.main_size * 2)
        self.capital_label.setStyleSheet("color : yellow;") #background-image : url(resources/capital_small.jpg)")
        self.capital_label.setFont(QtGui.QFont("Comic Sans", 25))
        self.capital_label.setAlignment(Qt.Qt.AlignCenter)

        # Create message label
        self.message_label = QtWidgets.QLabel(self)
        self.message_label.setGeometry(self.main_size * 11, self.main_size * 4, self.main_size * 3, self.main_size)
        self.message_label.setStyleSheet("color : white; background-image : url()")
        self.message_label.setFont(QtGui.QFont("Comic Sans", 20))
        self.message_label.setText("")

        # Create bet variables
        self.bet = 0
        self.bet_type = ""
        self.drawn_number = 0
        self.coefficient = []

        # Create drawn number label
        self.drawn_number_label = QtWidgets.QLabel(self)
        self.drawn_number_label.setGeometry(self.main_size * 9, self.main_size * 4.5, self.main_size, self.main_size)
        self.drawn_number_label.setStyleSheet("background-image : url()")
        self.drawn_number_label.setFont(QtGui.QFont("Comic Sans", 12))
        self.drawn_number_label.setAlignment(Qt.Qt.AlignCenter)

        def main_button_click(self, number):

            set_standard_style(self)

            self.main_buttons[number].setStyleSheet("background-color : grey; background-image : url()")

            self.bet_type = f"{number}"

            print(f'main button clicked: {number}')

        def color_button_click(self, color):

            set_standard_style(self)

            if color == "red":
                self.red_button.setStyleSheet("background-color : grey; background-image : url()")
            elif color == "black":
                self.black_button.setStyleSheet("background-color : grey; background-image : url()")

            self.bet_type = f"{color}"

            print(f"color button clicked : {color}")

        def play_button_click(self):

            try:
                self.bet = int(self.rate_line.text())

                if self.bet > self.capital:
                    user_message(self, "You haven't \nthose money")
                elif self.bet == 0:
                    user_message(self, "You can't put 0")
                elif self.bet_type == "":
                    user_message(self, "Choose your bet")
                else:

                    user_message(self, "")
                    self.rate_line.clear()
                    set_standard_style(self)

                    self.pbar.setHidden(False)
                    for i in range(101):
                        self.pbar.setValue(i)
                        time.sleep(0.02)
                    self.pbar.setHidden(True)

                    self.coefficient = win_lose_check(self.bet_type)
                    self.drawn_number = self.coefficient[0]

                    try:
                        self.coefficient[1] = int(self.coefficient[1])
                        capital_change(self, self.bet, self.coefficient[1])
                    except ValueError:
                        user_message(self, f"{self.coefficient[1]}")

                    drawn_number_label_change(self.drawn_number)
                    self.bet_type = ""
            except ValueError:
                user_message(self, "Wrong bet input")
                self.rate_line.setText("")

        def set_standard_style(self):
            for i in range(len(self.main_buttons)):
                if self.c_n_table[i] == "red":
                    self.main_buttons[i].setStyleSheet(
                        "background-color : red; color : white; background-image : url()")
                elif self.c_n_table[i] == "black":
                    self.main_buttons[i].setStyleSheet(
                        "background-color : black; color : white; background-image : url();")
                elif self.c_n_table[i] == "green":
                    self.main_buttons[i].setStyleSheet("background-color : green; background-image : url()")
            self.black_button.setStyleSheet("background-color : black; color : white; background-image : url()")
            self.red_button.setStyleSheet("background-color : red; color : white; background-image : url()")

        def capital_change(self, bet, coefficient):

            self.capital = self.capital - bet
            if coefficient > 0:
                self.capital = self.capital + (coefficient + 1) * bet
            self.capital_label.setText(f"Money:\n{self.capital}")

        def user_message(self, string):
            self.message_label.setText(string)

        def drawn_number_label_change(number):
            color = self.c_n_table[number]
            self.drawn_number_label.setText(f"{number}")
            self.drawn_number_label.setStyleSheet(f"background-color : {color}; background-image : url(); color : white")
            self.setHidden(False)
