# https://www.acmicpc.net/problem/11660
# 구간 합 구하기 5
# 70636 KB / 1384 ms


import sys
input = sys.stdin.readline

n, m = map(int, input().split())

table = []
for _ in range(n):
    table.append([int(x) for x in input().split()])

for i in range(n):
    for j in range(1, n):
        table[i][j] += table[i][j - 1]

for i in range(1, n):
    for j in range(n):
        table[i][j] += table[i - 1][j]

for _ in range(m):
    x1, y1, x2, y2 = [int(x) - 1 for x in input().split()]
    sum_ = table[x2][y2]
    if x1 > 0:
        sum_ -= table[x1 - 1][y2]
    if y1 > 0:
        sum_ -= table[x2][y1 - 1]
    if x1 > 0 and y1 > 0:
        sum_ += table[x1 - 1][y1 - 1]
    
    print(sum_)
