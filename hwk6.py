# Write a recursive function to count all the elements in a list (divide and rule).
from math import floor


# def recursive_count(list):
#     index = 0
#
#
#     if list != []:
#
#         index += 1
#
#         index = recursive_count(list[1::])
#
#         return index
#
#
# print(recursive_count([1, 2, 3, 4, 5]))

# *******************************************

# Find the biggest number in the list(D&R)

# def max_list(list1):
#     mid = floor(len(list1)/2)
#     left = list1[:mid]
#     right = list1[mid:]
#
#     if max(left) > max(right):
#
#         return max(left)
#     else:
#         return max(right)
#
#
# print(max_list([1,51,3,78,5,63,7]))

#****************************************************
# There are two lists that have different length. First has keys and the second has values.
# Create a function, which creates a dictionary of keys and values.
# If the is not enough values to match each key, this key should have value equal to None.
# If the is not enough keys to match each value, this value should be ignored.

names = [
    'Aliza Hulme',
    'Isaiah Mcgill',
    'Keiran Partridge',
    'Michele Wilcox',
    'Jordon Rocha',
    'Shakir Calhoun',
    'Lexi Bob',
    'Nimrah Regan',
    'Scarlet Roberts',
    'Emily-Jane Mejia'
]
jobs = [
    'Speech therapist',
    'Animal breeder',
    'Miner',
    'IT consultant',
    'Butler',
    'Radio presenter',
    'Architect',
    'Police officer',
]

def create_dict(keys, values):
    dictionary = dict()
    if len(keys)-len(values) != 0:

        for i in range(len(keys)-len(values)):

            values.append(None)

    for j in range(len(keys)):

        dictionary[keys[j]] = values[j]

    return dictionary
print(create_dict(names,jobs))

# ******************************************************

#codewar = 7 kyu, Minimize Sum Of Array (Array Series #1)

# minSum({12,6,10,26,3,24}) ==> return (342)
# Explanation: The minimum sum obtained from summing each two integers product , 26*3 + 24*6 + 12*10 = 342

def min_sum(arr):

    ans = 0
    while len(arr)>0:
        ans += max(arr)*min(arr)
        arr.remove(max(arr))
        arr.remove(min(arr))
    return ans
