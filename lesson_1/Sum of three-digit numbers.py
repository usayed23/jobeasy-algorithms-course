# Our code generates a random three-digit number and has to sum up all its digits. For example, if a number is 349,
# the code has to print the number 16, because 3 + 4 + 9 = 16.

from random import randint

n = int(input('Input a number of digits')) # 2

number = randint()

# n = randint(100, 999)
# print(n)
# sum_result = 0
#
# for digit_str in str(n):
#     sum_result += int(digit_str)
#
# print(sum_result)

once = n % 10
# print(once)

n = n // 10
# print(n)

tens = n % 10
# print(tens)

n = n // 10
# print(n)

result = n + tens + once

print(result)

# TODO: Homework: Rewrite a program with any number of digits.
#  Instead of  3 digits, you should sum digits up from n digits number,
#  Where  User enter n manually. n > 0
