###### 1890번: 점프
# https://www.acmicpc.net/problem/1890
# 메모리/시간: KB / ms

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
        if (0 <= x1 < N) and (0 <= y1 < N):
            table[x][y] += dfs(x1, y1)
        if (0 <= x2 < N) and (0 <= y2 < N):
            table[x][y] += dfs(x2, y2)
    return table[x][y]

print(dfs(0, 0))