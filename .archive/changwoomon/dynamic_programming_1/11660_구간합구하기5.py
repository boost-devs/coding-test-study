###### 11660번: 구간 합 구하기 5
# https://www.acmicpc.net/problem/11660
# 메모리/시간: 103704KB / 1372ms

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

_map = [list(map(int, input().split())) for _ in range(N)]
table = [[0] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        table[i][j] = _map[i-1][j-1] + table[i][j-1] + table[i-1][j] - table[i-1][j-1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    x1, y1 = x1 - 1, y1 - 1
    print(table[x2][y2] - table[x1][y2] - table[x2][y1] + table[x1][y1])