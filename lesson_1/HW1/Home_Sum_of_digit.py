# TODO: Homework: Rewrite a program with any number of digits.
#  Instead of  3 digits, you should sum digits up from n digits number,
#  Where User enter n manually. n > 0

from random import randint

n = int(input("Enter a number of digits "))
# n = 5
# digits = 84621
# (10000, 99999)
# (1000, 9999)
# (100, 999)



def sum_of_digits(digits):
    down = 10 ** (digits - 1)
    up = (10 ** digits) - 1

    number = randint(down, up)
    print(f' {number} is our random {n} digits number')

    result = 0
    while number > 0:
        digit = number % 10
        result += digit
        number //= 10
    print(f'Sum of digits is {result}')


sum_of_digits(n)
