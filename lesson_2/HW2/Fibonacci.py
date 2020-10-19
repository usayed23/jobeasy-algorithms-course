# The equation for the Fibonacci sequence:
# φ0 = 0,  φ1 = 1,  φn = φn−1 + φn−2.
#
# The task is to display element of the Fibonacci sequence φn

# Equation:
# F0 = 0
# F1 = 1
# F2 = 1
# Fn = Fn-1 + Fn-2


def fibonacci(n):
    fibonacci1 = 1
    if n < 0:
        print(f'Wrong value')
        quit()

    elif n == 0:
        print(0)
    elif n == 1 or n == 2:
        print(fibonacci1)
    else:
        fibonacci2 = 1
        i = 0
        while i < n - 2:
            fibonacci1, fibonacci2 = fibonacci2, fibonacci1 + fibonacci2
            i = i + 1
            if i == n - 2:
                print(fibonacci2)

fibonacci(int(input("element of the Fibonacci sequence: ")))
