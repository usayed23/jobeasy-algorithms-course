# Count odd and even numbers.  Count odd and even digits of the whole number.
# E.g, if entered number 34560, then 3 digits will be even (4, 6, and 0)  and  2 odd digits (3 and 5).


number = int(input(f"Enter a number: "))


def count_odd_even(n):
    even_counter = 0
    odd_counter = 0
    # while n > 0:
    #     digit = n % 10
    #     if digit % 2 == 0:
    #         even_counter += 1
    #     else:
    #         odd_counter += 1
    #     n //= 10

    # for digit in str(n):
    #     if int(digit) % 2 == 0:
    #         even_counter += 1
    #     else:
    #         odd_counter += 1
    # return {
    #     'odd': odd_counter,
    #     'even': even_counter
    # }


print(count_odd_even(number))
