###### 4396번: 지뢰 찾기
# https://www.acmicpc.net/problem/4396
# 메모리/시간: 29200KB / 68ms

import sys

input = sys.stdin.readline

n = int(input())

mine = [list(input().rstrip()) for _ in range(n)]

_map = [list(input().rstrip()) for _ in range(n)]

direction = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

mine_cond = False

for i in range(n):
    for j in range(n):
        if _map[i][j] == "x":
            if mine[i][j] == "*":
                mine_cond = True
            cnt = 0
            for dx, dy in direction:
                x, y = i + dx, j + dy
                if (x < 0) or (x >= n) or (y < 0) or (y >= n):
                    continue
                if mine[x][y] == "*":
                    cnt += 1
            _map[i][j] = cnt

if mine_cond:
    for i in range(n):
        for j in range(n):
            if mine[i][j] == "*":
                _map[i][j] = "*"

for row in _map:
    print("".join(map(str, row)))