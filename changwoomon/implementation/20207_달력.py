###### 20207번: 달력
# https://www.acmicpc.net/problem/20207
# 메모리/시간: 33916KB / 324ms

import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())

calendar = defaultdict(lambda: [0] * N)

info = []

for _ in range(N):
    S, E = map(int, input().split())
    gap = E - S + 1
    info.append((S, E, gap))

info = sorted(info, key=lambda x: (x[0], -x[2]))

for S, E, _ in info:
    for j in range(N):
        if calendar[S][j] == 0:
            for i in range(S, E+1):
                calendar[i][j] = 1
            break

width, height = 0, 0
area = 0

for i in range(min(calendar), max(calendar)+2):
    for j in range(N):
        if calendar[i][j] == 1:
            height = max(height, j+1)
    if any(calendar[i]):
        width += 1
    else:
        area += width * height
        width, height = 0, 0

print(area)