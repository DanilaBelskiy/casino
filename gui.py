from PyQt5.QtWidgets import QApplication, QLabel, QHBoxLayout, QVBoxLayout, QPushButton, QWidget, QMainWindow
from color_number_table import color_number_table

app = QApplication([])

vbox = QVBoxLayout()

# Add horizontal axes
layout_1 = QHBoxLayout()
layout_2 = QHBoxLayout()
layout_3 = QHBoxLayout()
layout_4 = QHBoxLayout()

vbox.addLayout(layout_1)
vbox.addLayout(layout_2)
vbox.addLayout(layout_3)
vbox.addLayout(layout_4)

# Create main buttons
main_buttons = []
for i in range(0, 37):
    main_buttons.append(QPushButton(f"{i}"))

# Set style for main buttons
c_n_table = color_number_table()
for i in range(len(main_buttons)):
    if c_n_table[i] == "red":
        main_buttons[i].setStyleSheet("background-color : red")
    elif c_n_table[i] == "black":
        main_buttons[i].setStyleSheet("background-color : black; color : white")
    elif c_n_table[i] == "green":
        main_buttons[i].setStyleSheet("background-color : green")

# Set geometry for main buttons
for i in range(len(main_buttons)):
    main_buttons[i].setGeometry(0+i, 0, 50, 50)

'''# Add main buttons in window
layout_1.addWidget(main_buttons[36])
layout_1.addWidget(main_buttons[33])
layout_1.addWidget(main_buttons[30])
layout_1.addWidget(main_buttons[27])
layout_1.addWidget(main_buttons[24])
layout_1.addWidget(main_buttons[21])
layout_1.addWidget(main_buttons[18])
layout_1.addWidget(main_buttons[15])
layout_1.addWidget(main_buttons[12])
layout_1.addWidget(main_buttons[9])
layout_1.addWidget(main_buttons[6])
layout_1.addWidget(main_buttons[3])

layout_2.addWidget(main_buttons[35])
layout_2.addWidget(main_buttons[32])
layout_2.addWidget(main_buttons[29])
layout_2.addWidget(main_buttons[26])
layout_2.addWidget(main_buttons[23])
layout_2.addWidget(main_buttons[20])
layout_2.addWidget(main_buttons[17])
layout_2.addWidget(main_buttons[14])
layout_2.addWidget(main_buttons[11])
layout_2.addWidget(main_buttons[8])
layout_2.addWidget(main_buttons[5])
layout_2.addWidget(main_buttons[2])

layout_3.addWidget(main_buttons[34])
layout_3.addWidget(main_buttons[31])
layout_3.addWidget(main_buttons[28])
layout_3.addWidget(main_buttons[25])
layout_3.addWidget(main_buttons[22])
layout_3.addWidget(main_buttons[19])
layout_3.addWidget(main_buttons[16])
layout_3.addWidget(main_buttons[13])
layout_3.addWidget(main_buttons[10])
layout_3.addWidget(main_buttons[7])
layout_3.addWidget(main_buttons[4])
layout_3.addWidget(main_buttons[1])'''

win = 1

for i in range(len(main_buttons)):
    pass

app.exec()
