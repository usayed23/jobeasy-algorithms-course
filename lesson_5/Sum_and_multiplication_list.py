# Enter elements from a keyboard. Calculate sum and multiplication of elements.
# Print the list, calculated sum, and multiplication of elements

length = int(input(f"Enter a length of a list "))
array_1 = []

for item in range(length):
    number = int(input(f"Enter a value of element "))
    array_1.append(number)


def sum_and_mult(array):
    sum_of_elements = 0
    mult_of_elements = 1
    for item in array:
        sum_of_elements += item
        mult_of_elements *= item
    return {
        'sum': sum_of_elements,
        'mult': mult_of_elements,
        'array': array
    }

print(sum_and_mult(array_1))
