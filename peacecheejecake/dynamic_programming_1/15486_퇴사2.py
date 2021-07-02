# https://www.acmicpc.net/problem/15486
# 퇴사 2
# 249784 KB / 2700 ms

import sys
input = sys.stdin.readline

N = int(input())

info = []
for _ in range(N):
    t, p = map(int, input().split())
    info.append((t, p))

table = []
for i, (t, p) in enumerate(info[::-1]):
    if i - t >= 0:
        max_self = p + table[i - t]
    elif i - t == -1:
        max_self = p
    else:
        max_self = 0

    table.append(
        max(max_self, table[i - 1]) if table else max_self
    )

print(table[-1])
