# Find the maximal sequence of consecutive zeros that surrounded by ones
# at both ends in the binary representation of a number entered by User.

number = int(input('Enter a number: '))
#
# print(str(bin(number))[2:])
#
#

def to_bin(n):
    bin_string = ''
    while n > 0:
        bin_string += str(n % 2)
        n = n // 2
    return bin_string[::-1]

print(to_bin(number))

def binary_gap(bin_number):
    max_gap = 0
    counter = 0
    for digit in bin_number:
        if digit == '1':
            if max_gap < counter:
                max_gap = counter
            counter = 0
        else:
            counter += 1
    return max_gap


print(binary_gap(to_bin(number)))
