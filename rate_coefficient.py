from rotation_result import RotationResult

"""
Function takes bet and result of rotation
Bet should be 'red', 'black', or number

Returns coefficient how many money user wins (int), or error message (String)
"""


def rate_coefficient(rate, result: RotationResult):
    number = result.get_number()
    color = result.get_color()

    try:
        rate = int(rate)
    except ValueError:
        pass

    if rate == "red":
        if color == "red":
            return 1
        else:
            return 0

    elif rate == "black":
        if color == "black":
            return 1
        else:
            return 0

    elif rate == "green":
        if color == "green":
            return 35
        else:
            return 0

    elif type(rate) == int:
        if (rate >= 0) and (rate <= 36):
            if rate == number:
                return 35
            else:
                return 0
        else:
            return "Wrong number"

    else:
        return "Wrong input"
