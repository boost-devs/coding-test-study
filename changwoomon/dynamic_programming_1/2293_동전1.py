###### 2293번: 동전 1
# https://www.acmicpc.net/problem/2293
# 메모리/시간: 29452KB / 244ms

import sys

input = sys.stdin.readline

n, k = map(int, input().split())

coin = [int(input()) for _ in range(n)]

table = [0] * (k+1)
table[0] = 1

for c in coin:
    for i in range(c, k+1):
        table[i] += table[i-c]

print(table[k])