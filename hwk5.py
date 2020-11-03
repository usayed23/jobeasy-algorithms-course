#Write a Python program to remove duplicates from a list.

def remove_duplicates(list1):

    for x in list1:
        if list1.count(x) >= 2:
            list1.remove(x)

    return list1


print(remove_duplicates([1,1,2,3,5,4,6,9,7,8,4,5,2]))


# Given the triangle of consecutive odd numbers:
#          	     1
#             3      5
#         7      9	  11
#    13	 15    17    19
# 21    23    25     27     29
# ...
# Calculate the row sums of this triangle from the row index (starting at index 1) e.g.:
#
# row_sum_odd_numbers(1); # 1
# row_sum_odd_numbers(2); # 3 + 5 = 8
# row_sum_odd_numbers(3); # 7 + 9 + 11 = 27
# row_sum_odd_numbers(4); # 13 + 15 + 17 + 19 = 64


def sum_of_odds(index):

    return index*index*index

print(sum_of_odds(4))


#When given a list, the program should return a list of all the elements that are below the arithmetical mean of the original list.
# The arithmetical mean is the sum of all elements divided by the number of elements.

def below_avg(list2):
    x = sum(list2)/ len(list2)
    index= -1
    for y in list2:
        index += 1
        if x <= y:
          list2.pop(index)

    return list2

print(below_avg([1,5,3,5,2]))


#When given a list of elements find the two lowest elements. They can be equal to each other or different.

def low_two(list3):
    index = -1
    index1 = -1
    min = list3[0]
    min2 = list3[0]

    for x in list3:
        if x < min:
            min = x


    for y in list3:
        if y < min2 and y > min:
            min2 = y



    return f'The two lowest value from the string are {min} and {min2}'



print(low_two([4,3,4,9,1,10,5,6,7]))


#CodeWAR = (7 kyu) ,Sum of array singles
#
# In this Kata, you will be given an array of numbers in which two numbers occur once and the rest occur only twice.
# Your task will be to return the sum of the numbers that occur only once.
# For example, repeats([4,5,7,5,4,8]) = 15 because only the numbers 7 and 8 occur once, and their sum is 15. Every other number occurs twice.

# Test.it("Basic tests")
# Test.assert_equals(repeats([4,5,7,5,4,8]),15)
# Test.assert_equals(repeats([9, 10, 19, 13, 19, 13]),19)
# Test.assert_equals(repeats([16, 0, 11, 4, 8, 16, 0, 11]),12)
# Test.assert_equals(repeats([5, 17, 18, 11, 13, 18, 11, 13]),22)
# Test.assert_equals(repeats([5, 10, 19, 13, 10, 13]),24)


def repeats(arr):
    index = -1
    index2 = -1
    for x in arr:
        index += 1
        if arr.count(x) == 1:
            y = arr[index]

    for i in arr:
        index2 += 1
        if arr.count(i) == 1 and i != y:
            z = arr[index2]

    return z + y

print(repeats([4,5,7,5,4,8]))


# Codewar = (8 kyu),Invert values
# Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.
#
# invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
# invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5]
# invert([]) == []
# You can assume that all values are integers. Do not mutate the input array/list.

def invert(lst):
    final_list = []
    for x in lst:
        y = x * -1
        final_list.append(y)
    return final_list

print(invert([1,2,3,4,5]))

# CODEWAR= (7 kyu), Descending Order

# Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order.
# Essentially, rearrange the digits to create the highest possible number.#
# Examples:
# Input: 42145 Output: 54421
# Input: 145263 Output: 654321
# Input: 123456789 Output: 987654321


def descending_order(num):
    number = str(num)
    list1 = list(number)
    list1.sort()
    list_to_string = "".join(map(str, list1))

    return int(list_to_string[::-1])

print(descending_order(78951133))

