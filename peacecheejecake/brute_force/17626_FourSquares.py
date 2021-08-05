# https://www.acmicpc.net/problem/17626
# Four Squares
# 31312


from math import sqrt


def rrange(n):
    return (q ** 2 for q in range(int(sqrt(n // 2)), int(sqrt(n)) + 1))


def simulate(n):
    squares = [rn ** 2 for rn in range(1, int(sqrt(n)) + 1)]

    if n in squares:
        return 1
    
    for s in rrange(n):
        if n - s in squares:
            return 2
            
    for s in rrange(n):
        for t in rrange(n - s):
            if n - s - t in squares:
                return 3

    return 4


n = int(input())

print(simulate(n))
