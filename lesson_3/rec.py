def rec(n):
    if n > 0:
        rec(n - 1)
    print(n)

rec(3)