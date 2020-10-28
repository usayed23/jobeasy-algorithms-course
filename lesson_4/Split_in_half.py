# Given a string. Split it for two same parts. (if the string has odd characters, the first part should
# be greater for one character). Swap this parts and save the result in a new string and return it

from math import floor


def split_in_half(string):
    string_len = len(string)
    half = floor(string_len / 2)
    if string_len % 2 != 0:
        first = string[:half + 1]
        second = string[half + 1:]
    else:
        first = string[:half]
        second = string[half:]
    return f'{second}{first}'


print(split_in_half('bbbbbcaaaaa'))
