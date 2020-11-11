from random import randint

length = int(input('Enter a number of items: '))
list_numbers = []

for _ in range(length):
    list_numbers.append(randint(1, 10))
print(list_numbers)


def two_mins(array):
    min_1 = min(array)
    array.remove(min_1)
    min_2 = min(array)
    return f'min 1 element is {min_1} and min 2 element is {min_2}'


print(two_mins(list_numbers))