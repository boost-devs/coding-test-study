###### 15486번: 퇴사 2
# https://www.acmicpc.net/problem/15486
# 메모리/시간: 273336KB / 4044ms

import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())

info = [list(map(int, input().split())) for _ in range(N)]
table = defaultdict(int)

for i in range(N):
    if i + info[i][0] <= N:
        table[i+info[i][0]] = max(table[i+info[i][0]], table[i]+info[i][1])
    table[i+1] = max(table[i+1], table[i])

print(table[N])