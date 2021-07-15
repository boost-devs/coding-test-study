###### 15486번: 퇴사 2
# https://www.acmicpc.net/problem/15486
# 메모리/시간: 344988KB / 4384ms

import sys

input = sys.stdin.readline

N = int(input())

info = [[0, 0]] + [list(map(int, input().split())) for _ in range(N)]
table = [0] * (N+2)

for i in range(1, N+1):
    if i + info[i][0] <= N + 1:
        table[i+info[i][0]] = max(table[i+info[i][0]], table[i]+info[i][1])
    table[i+1] = max(table[i+1], table[i])

print(table[N+1])