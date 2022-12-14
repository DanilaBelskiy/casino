import random
from color_number_table import color_number_table

"""
The class is one rotation of the roulette
It have number and color
Number is random
"""


class RotationResult:

    def __init__(self):
        self.number = random.randint(0, 36)
        self.color = color_number_table()[self.number]

    def print(self):
        print(f"{self.number} : {self.color}")

    def get_number(self):
        return self.number

    def get_color(self):
        return self.color
