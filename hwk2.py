# # ****************************************************************************************************
# # TODO: HW: Rewrite code, which will return only needed element of Fib sequence
#
# def fibonacci(n):
#     fibonacci_1 = 1
#     fibonacci_2 = 1
#
#     if n < 0:
#         print('Wrong value')
#     if n == 0:
#         print(0)
#
#     index = 0
#     while index < n - 2:
#         fibonacci_1, fibonacci_2 = fibonacci_2, fibonacci_1 + fibonacci_2
#         index += 1
#
#     return fibonacci_2
#
#
# print(fibonacci(4))
#
# # ****************************************************************************************************************************
# # Zeros not for Heros
# # Numbers ending with zeros are boring. They might be fun in your world, but not here. Get rid of them. Only the ending ones.
#
# # 1450 -> 145
# # 960000 -> 96
# # 1050 -> 105
# # -1050 -> -105
# # Zero alone is fine, don't worry about it. Poor guy anyway
#
number = 560987000
string_num = str(number)
string_num = string_num.strip("0")
print(string_num)
#
# # *******************************************************************************************************
#
# # Digital root is the recursive sum of all the digits in a number.
# # Given n, take the sum of the digits of n.
# # If that value has more than one digit, continue reducing in this way until a single-digit number is produced.
# # This is only applicable to the natural numbers.
#
# # 16  -->  1 + 6 = 7
# # 942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
# # 132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
# # 493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2


n = 15498


def digital_root(y):
    sum_of_all_1 = 0
    k=str(y)
    for x in k:
        if x.isdigit():
            single_int = int(x)
            sum_of_all_1 = sum_of_all_1 + single_int

    if len(str(sum_of_all_1)) > 1:
        sum_of_all_1 = digital_root(sum_of_all_1)

    return (sum_of_all_1)

print(digital_root(n))


