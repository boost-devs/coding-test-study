###### 20207번: 달력
# https://www.acmicpc.net/problem/20207
# 메모리/시간: 33900KB / 312ms

import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())

info = [list(map(int, input().split())) for _ in range(N)]
info = sorted(info, key=lambda x: (x[0], x[0]-x[1]))

calendar = defaultdict(lambda: [0] * N)

for S, E in info:
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