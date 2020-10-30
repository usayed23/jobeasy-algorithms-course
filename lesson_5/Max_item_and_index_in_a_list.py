# Populate a list of random numbers. Find and print the max element and the index of this element


from random import randint
lowest = int(input('From number'))
greatest = int(input('To number'))


length = int(input(f"Enter a list length "))
array_1 = []

for i in range(length):
    item = randint(lowest, greatest)
    array_1.append(item)


def find_max_item_and_its_index_in_list(array):
    if len(array) <= 0:
        return 'List should have 1 element'
    maximum = array[0]
    max_index = 0
    index = 0
    while index < len(array):
        if array[index] > maximum:
            maximum = array[index]
            max_index = index
        index += 1
    return {
        'max element': maximum,
        'max index': max_index,
        'array': array
    }


print(find_max_item_and_its_index_in_list(array_1))
