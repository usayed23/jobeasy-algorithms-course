# User enter a string from a keyboard. Result for return - inverted string

from math import acos


def reversed_string(string):
    # option 1
    return string[::-1]
    # option 2
    # return ''.join(reversed(string))
    # option 3
    # result = ''
    # index = len(string) - 1
    # while index >= 0:
    #     result += string[index]
    #     index -= 1
    # return result



