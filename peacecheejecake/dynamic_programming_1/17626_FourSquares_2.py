# https://www.acmicpc.net/problem/17626
# Four Squares
# 31312 KB / 72 ms


from math import sqrt


def find_min(n):
    squares = [i ** 2 for i in range(int(sqrt(n)) + 1)]

    if n in squares:
        return 1

    for r in range(int(sqrt(n)), int(sqrt(n // 2) - 1), -1):
        if n - r ** 2 in squares:
            return 2

    for r in range(int(sqrt(n)), int(sqrt(n // 2) - 1), -1):
        nn = n - r ** 2
        for rr in range(int(sqrt(nn)), int(sqrt(nn // 2) - 1), -1):
            if nn - rr ** 2 in squares:
                return 3
    
    return 4


print(find_min(int(input())))
