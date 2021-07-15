###### 10844번: 쉬운 계단 수
# https://www.acmicpc.net/problem/10844
# 메모리/시간: 29200KB / 68ms

import sys

input = sys.stdin.readline

N = int(input())

table = [[1] * 10] + [[0] * 10 for _ in range(N-1)]

for i in range(N-1):
    for j in range(10):
        if j >= 1:
            table[i+1][j-1] += table[i][j]
        if j <= 8:
            table[i+1][j+1] += table[i][j]

print(sum(table[N-1][1:])%1000000000)