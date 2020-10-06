# #
# # Sum of 3 modified
# # TODO: Homework: Rewrite a program with any number of digits.
# # Instead of  3 digits, you should sum digits up from n digits number,\
# #
# #  Where User enter n manually. n > 0
# from random import randint
#
from random import randint

n = (input('Input a number of digits'))

z = len(n)
print(z)


def limit(z):
    lower_limit = 0
    upper_limit = 0
    if z >= 0:
        lower_limit = 10 ** (z - 1)
        upper_limit = ((10 ** (z - 1)) * 10) - 1

    return lower_limit, upper_limit


num_digit = limit(z)
print(num_digit[0])
print(num_digit[1])

sum_of_all = randint(num_digit[0], num_digit[1])

sum_all_string = str(sum_of_all)
print(sum_all_string)


def string_to_digits(str1):
    sum_of_int_digit = 0
    for int_1 in str1:
        if int_1.isdigit():
            x = int(int_1)
            sum_of_int_digit = sum_of_int_digit + x

    return sum_of_int_digit


print(string_to_digits(sum_all_string))
#
# # Find max number from 3 values, entered manually from a keyboard
#
num_1 = int(input("Please Enter the first value"))
num_2 = int(input("please Enter the Second value"))
num_3 = int(input("please Enter the Third value"))

three_values = [num_1, num_2, num_3]

print(max(three_values))
#
# # Count odd and even numbers.  Count odd and even digits of the whole number. E.g, if entered number 34560, then 3 digits will be even (4, 6, and 0)  and  2 odd digits (3 and 5).

number = "45547811"


def odd_even(number):
    odd_number = 0
    even_number = 0
    for odd in number:
        if odd.isdigit():
            x = int(odd)
            if (x % 2) == 0:
                even_number = even_number + 1

            else:
                odd_number = odd_number + 1

    return odd_number, even_number


even_odd_list = odd_even(number)
print("Number of Odd are",even_odd_list[0])
print("Number of Even are",even_odd_list[1])
