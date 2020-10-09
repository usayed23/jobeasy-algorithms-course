# Find max number from 3 values, entered manually from a keyboard.


num1 = int(input(f"First number "))
num2 = int(input(f"Second number "))
num3 = int(input(f"Third number "))


def max_of_three(number_1, number_2, number_3):
    # return max([number_1, number_2, number_3])
    # if number_1 > number_2:
    #     if number_1 > number_3:
    #         return number_1
    #     else:
    #         return number_3
    # else:
    #     if number_2 > number_3:
    #         return number_2
    #     else:
    #         return number_3

    # if number_1 >= number_2 and number_1 >= number_3:
    #     return number_1
    # elif number_2 >= number_1 and number_2 >= number_3:
    #     return number_2
    # elif number_3 >= number_1 and number_3 >= number_2:
    #     return number_3

    # max_number = number_1
    # if max_number < number_2:
    #     max_number = number_2
    # if max_number < number_3:
    #     max_number = number_3
    # return max_number

print(max_of_three(num1, num2, num3))
