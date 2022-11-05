from rate_coefficient import rate_coefficient
from rotation_result import RotationResult

"""
Function for check result of play
Function takes users bet
Bet should be 'red', 'black', or number

Function returns array, 
where first element is result of rotation (int)
and second element is win coefficient (int) or error message for user (String)
"""


def win_lose_check(bet):

    result = RotationResult()
    coefficient = rate_coefficient(bet, result)

    return_arr = [result.get_number(), ]

    if coefficient == "Wrong input":
        return_arr.append("Wrong input")
    elif coefficient == "Wrong number":
        return_arr.append("Number must be in range of 0 and 36")
    else:

        try:
            coefficient = int(coefficient)
            return_arr.append(coefficient)
        except ValueError:
            return_arr.append("Error")

    return return_arr
