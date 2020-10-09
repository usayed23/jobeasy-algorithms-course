# The equation for the Fibonacci sequence:
# φ0 = 0,  φ1 = 1,  φn = φn−1 + φn−2.
#
# The task is to display all the numbers from start to n of the Fibonacci sequence φn

# Equation:
# F0 = 0
# F1 = 1
# F2 = 1
# Fn = Fn-1 + Fn-2


# 1 2 3 4 5 6 7 ...
# 1 1 2 3 5 8 13 ...


def fibonacci(n):
    fibonacci_1 = 1
    fibonacci_2 = 1

    if n < 0:
        print('Wrong value')
    if n == 0:
        print(0)


    if n > 0:
        print(fibonacci_1)
    if n > 1:
        print(fibonacci_2)


    index = 0
    while index < n - 2:
        fibonacci_1, fibonacci_2 = fibonacci_2, fibonacci_1 + fibonacci_2
        index += 1
        print(fibonacci_2)

fibonacci(100)

# TODO: HW: Rewrite code, which will return only needed element of Fib sequence