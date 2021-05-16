###### 16918번: 봄버맨
# https://www.acmicpc.net/problem/16918
# 메모리/시간: 35008KB / 3668ms

import sys
from collections import deque

input = sys.stdin.readline

R, C, N = map(int, input().split())

_map = [list(map(str, input().rstrip())) for _ in range(R)]

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

def boom(pos):
    queue = deque(pos)
    while queue:
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for way in range(4):
                xx, yy = x + dx[way], y + dy[way]

                if(xx < 0) or (xx >= R) or (yy < 0) or (yy >= C):
                    continue

                if _map[xx][yy] == "O":
                    _map[xx][yy] = "."

            _map[x][y] = "."

def bomb(_map):
    pos = []
    for i in range(R):
        for j in range(C):
            if _map[i][j] == "O":
                pos.append([i, j])
    return pos

for i in range(1, N):
    if i % 2 == 0:
        boom(pos)
    else:
        pos = bomb(_map)
        _map = [["O" for _ in range(C)] for _ in range(R)]

if N % 2 == 0:
    _map = [["O" for _ in range(C)] for _ in range(R)]

for row in _map:
    print("".join(map(str, row)))