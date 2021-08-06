###### 17626번: Four Squares
# https://www.acmicpc.net/problem/17626
# 메모리/시간: KB / ms

import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())

table = [0] * (int(n**0.5)+1)

for i in range(int(n**0.5)+1):
    table[i] = i * i

def four_squares(n):
    for i in range(len(table)-1, 0, -1):
        if table[i] == n:
            return 1
    for i in range(len(table)-1, 0, -1):
        for j in range(i, 0, -1):
            _sum = table[i] + table[j]
            if _sum == n:
                return 2
    for i in range(len(table)-1, 0, -1):
        for j in range(i, 0, -1):
            for k in range(j, 0, -1):
                _sum = table[i] + table[j] + table[k]
                if _sum == n:
                    return 3
    return 4

print(four_squares(n))