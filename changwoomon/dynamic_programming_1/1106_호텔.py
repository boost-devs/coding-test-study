###### 1106번: 호텔
# https://www.acmicpc.net/problem/1106
# 메모리/시간: 29200KB / 72ms

import sys

input = sys.stdin.readline

C, N = map(int, input().split())

info = [list(map(int, input().split())) for _ in range(N)]
_max = sorted(info, key=lambda x: x[1], reverse=True)[0][1]

table = [0] + [999999] * (C+_max)

for cost, customer in info:
    for i in range(customer, len(table)):
        table[i] = min(table[i], table[i-customer]+cost)

print(min(table[C:]))