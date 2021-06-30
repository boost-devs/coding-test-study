###### 1106번: 호텔
# https://www.acmicpc.net/problem/1106
# 메모리/시간: 29200KB / 72ms

import sys

input = sys.stdin.readline

C, N = map(int, input().split())

info = dict()

for _ in range(N):
    cost, customer = map(int, input().split())
    if customer in info.keys():
        info[customer] = min(info[customer], cost)
    else:
        info[customer] = cost

table = [0] + [999999] * (C+max(info.keys()))

for customer, cost in info.items():
    for i in range(customer, len(table)):
        table[i] = min(table[i], table[i-customer]+cost)

print(min(table[C:]))