from itertools import combinations


def factorial(n):
    c = 1
    for i in range(1, n + 1):
        c *= i
    return c


def comb(n, k):
    t = 0
    c = combinations(range(n), k)
    while True:
        try:
            next(c)
            t += 1
        except StopIteration:
            break
    return t
