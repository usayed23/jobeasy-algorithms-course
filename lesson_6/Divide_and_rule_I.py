# You have a list of numbers. You should sum up all numbers and output their sum.

from random import randint
from math import floor

length = int(input('Enter a number of items: '))
list_numbers = []

for _ in range(length):
    list_numbers.append(randint(0, 20))
print(list_numbers)


def summ(array: list):
    if len(array) == 1:
        return array[0]
    else:
        mid = floor(len(array) / 2)
        left = array[:mid]
        right = array[mid:]
        return summ(left) + summ(right)


print(summ(list_numbers))
