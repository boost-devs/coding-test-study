###### 2294번: 동전 2
# https://www.acmicpc.net/problem/2294
# 메모리/시간: 29452KB / 444ms

import sys

input = sys.stdin.readline

n, k = map(int, input().split())

coin = [int(input()) for _ in range(n)]

table = [10001] * (k+1)
table[0] = 0

for c in coin:
    for i in range(c, k+1):
        table[i] = min(table[i], table[i-c]+1)

print(table[k] if table[k] != 10001 else -1)