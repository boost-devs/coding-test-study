###### 1912번: 연속합
# https://www.acmicpc.net/problem/1912
# 메모리/시간: 37288KB / 124ms

import sys

input = sys.stdin.readline

n = int(input())

A = tuple(map(int, input().split()))

table = [0 for _ in range(n)]

for i in range(n):
    table[i] = A[i]
    if i == 0:
        continue
    if table[i] < table[i-1] + A[i]:
        table[i] = table[i-1] + A[i]

print(max(table))