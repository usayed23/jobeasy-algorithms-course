# When User enters a number, its factorial is displayed.
import math

n = int(input('Input a number '))


# def factorial(number):
#     if number < 0:
#         print('I don\'t like Gamma functions')
#     elif number == 0:
#         return 1
#     else:
#         result = 1
#         for num in range(1, number + 1):
#             result *= num
#         return result


print(math.factorial(n))

# print(factorial(n))
