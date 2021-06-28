###### 1912번: 연속합
# https://www.acmicpc.net/problem/1912
# 메모리/시간: 37288KB / 120ms

import sys

input = sys.stdin.readline

n = int(input())

A = tuple(map(int, input().split()))

table = [x for x in A]

for i in range(n):
    if i == 0:
        continue
    if table[i] < table[i-1] + A[i]:
        table[i] = table[i-1] + A[i]

print(max(table))