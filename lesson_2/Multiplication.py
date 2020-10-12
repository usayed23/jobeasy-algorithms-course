# Write a Python program to multiply two integers without using the * operator in python

# 5 * 3 = 15
# 5 + 5 + 5 = 15
# 3 + 3 + 3 + 3 + 3 = 15

def multiplication(number_1, number_2):
    min_number = min((number_1, number_2))
    max_number = max((number_1, number_2))
    result = 0

    for _ in range(min_number):
        result += max_number
    return result

print(multiplication(1000, 2))