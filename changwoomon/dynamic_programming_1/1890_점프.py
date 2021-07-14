###### 1890번: 점프
# https://www.acmicpc.net/problem/1890
# 메모리/시간: 29200KB / 68ms

import sys

input = sys.stdin.readline

N = int(input())

_map = tuple(tuple(map(int, input().split())) for _ in range(N))
table = [[-1] * N for _ in range(N)]

def dfs(x, y):
    if (x, y) == (N-1, N-1):
        return 1
    if table[x][y] == -1:
        table[x][y] = 0
        x1, y1 = x + _map[x][y], y
        x2, y2 = x, y + _map[x][y]
        if (x1 >= 0) and (x1 < N) and (y1 >= 0) and (y1 < N):
            table[x][y] += dfs(x1, y1)
        if (x2 >= 0) and (x2 < N) and (y2 >= 0) and (y2 < N):
            table[x][y] += dfs(x2, y2)
    return table[x][y]

print(dfs(0, 0))