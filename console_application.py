from rotation_result import RotationResult
from rate_coefficient import rate_coefficient


"""
Start console application
Application is game in roulette
User have capital
He can bet money on number or color
He can win money or lose
"""


def console_application(capital=100, ):
    while capital > 0:
        print(f"Your current capital = {capital}")

        inp = input("Input your bet and your bet type: ")
        inp = inp.split(' ')

        if len(inp) != 2:
            print("Input 2 words\n")
            continue

        rate = inp[0]
        rate_type = inp[1]

        try:
            rate = int(rate)
        except ValueError:
            print("Input {bet} {type of your bet}\n")
            continue

        if rate > capital:
            print("You haven't those money\n")
            continue

        rotation = RotationResult()

        coefficient = rate_coefficient(rate_type, rotation)

        try:
            coefficient = int(coefficient)
        except ValueError:
            if coefficient == "Wrong number":
                print("Number must be in range of 0 and 36")
            if coefficient == "Wrong input":
                print("Try input 'red', 'black' or number\n")
            continue

        capital -= rate

        if coefficient > 0:
            capital += rate * (coefficient + 1)
        rotation.print()

        if capital > 0:
            print("-------------------Next try--------------------------")

    print("Capital = 0")
    print("You a bankrupt")
