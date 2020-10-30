# Function has given a list of integer numbers and k integer number.
# It returns all pairs of numbers from the list which equal to k.
# E.g. pair_sum([1, 3, 4, 6, 8, 2, 2], 4) returns (1,3) and (2,2)


def pair_sum(arr, k):
    result = []
    index_1 = 0
    while index_1 < len(arr) - 1:
        index_2 = index_1 + 1
        while index_2 < len(arr):
            if arr[index_1] + arr[index_2] == k:
                pair = (arr[index_1], arr[index_2])
                pair = sorted(pair)
                if pair not in result:
                    result.append(pair)
                    break
            index_2 += 1
        index_1 += 1
    return result


print(pair_sum([1, -1, 3, 4, 2, 2, 0, 5], 4))
