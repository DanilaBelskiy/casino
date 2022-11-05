from rotation_result import RotationResult
from rate_coefficient import rate_coefficient


def app(capital=100, ):
    while capital > 0:
        print(f"Your current capital = {capital}")

        inp = input("Input your rate and your rate type: ")
        inp = inp.split(' ')

        if len(inp) != 2:
            print("Input 2 words\n")
            continue

        rate = inp[0]
        rate_type = inp[1]

        try:
            rate = int(rate)
        except ValueError:
            print("Input {rate} {type of your rate}\n")
            continue

        if rate > capital:
            print("You haven't those money\n")
            continue

        capital -= rate

        rotation = RotationResult()

        rotation.print()
        coefficient = rate_coefficient(rate_type, rotation)

        try:
            coefficient = int(coefficient)
        except ValueError:
            if coefficient == "Wrong number":
                print("Number must be in range of 0 and 36")
            if coefficient == "Wrong input":
                print("Try input 'red', 'black' or number\n")
            continue

        if coefficient > 0:
            capital += rate * (coefficient + 1)

        print()

    print("Capital = 0")
    print("You a bankrupt")
