number_1 = 10
index_1 = 5


result_1 = number_1 ** index_1


def power(number, index):
    if index == 0:
        return 1
    elif index == 1:
        return number
    elif index > 1:
        result = power(number, index - 1) * number
        return result
    else:
        print('Error message!!!')


result_3 = power(number_1, index_1)

print(result_1)
print(result_3)
