# Find a sum of elements between min and max elements. Min and max elements are not included

def sum_between_min_and_max(array):
    if len(array) <= 1:
        return 'Array must have at least 2 element'
    maximum = array[0]
    minimum = array[0]
    max_index = 0
    min_index = 0
    sum_of_subarray = 0
    index = 0
    while index < len(array):
        if array[index] > maximum:
            maximum = array[index]
            max_index = index
        if array[index] < minimum:
            minimum = array[index]
            min_index = index
        index += 1
    if min_index < max_index:
        subarray = array[min_index + 1:max_index]
    else:
        subarray = array[max_index + 1:min_index]
    for item in subarray:
        sum_of_subarray += item
    return sum_of_subarray



print(sum_between_min_and_max([6, 3, 5, 1]))
