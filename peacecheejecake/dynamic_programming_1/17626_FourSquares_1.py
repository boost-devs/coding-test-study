# https://www.acmicpc.net/problem/17626
# Four Squares
# 125720 KB / 140 ms (PyPy3)

from math import sqrt

n = int(input())

table = [0] * (n + 1)
for k in range(1, n + 1):
    cands = [
        table[k - r ** 2] 
        for r in range(int(sqrt(k)), int(sqrt(k // 2) - 1), -1)
    ]
    table[k] = min(cands) + 1

print(table[n])
