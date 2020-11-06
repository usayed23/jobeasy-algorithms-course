from random import randint

length = int(input('Enter a number of items: '))
list_numbers = []

for _ in range(length):
    list_numbers.append(randint(1, 10))
print(list_numbers)

def ar_mn(arr):
    result = []
    sum_arr = 0
    for item in arr:
        sum_arr += item

    arithmetical_mean = sum_arr / len(arr)

    for item in arr:
        if item < arithmetical_mean:
            result.append(item)

    print(arithmetical_mean)
    return result


print(ar_mn(list_numbers))