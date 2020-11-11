# In a list find continuous sublist which has the greater sum of elements
from random import randint

length = int(input('Enter a number of items: '))
list_numbers = []

for _ in range(length):
    list_numbers.append(randint(-20, 20))
print(list_numbers)

def largest_sum_contiguous_sublist(array):
    best_sum = array[0]
    best_sublist = []
    index_1 = 0
    while index_1 < len(array):
        index_2 = index_1 + 1
        current_sum = array[index_1]
        current_sublist = [array[index_1]]
        if current_sum >= best_sum:
            best_sum = current_sum
            best_sublist = current_sublist.copy()
        while index_2 < len(array):
            current_sum += array[index_2]
            current_sublist.append(array[index_2])
            if current_sum >= best_sum:
                best_sum = current_sum
                best_sublist = current_sublist.copy()
            index_2 += 1
        index_1 += 1
    return {
        'best sum': best_sum,
        'best sublist': best_sublist
    }



print(largest_sum_contiguous_sublist(list_numbers))
