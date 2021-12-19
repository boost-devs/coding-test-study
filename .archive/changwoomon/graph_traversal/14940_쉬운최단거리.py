###### 14940번: 쉬운 최단거리
# https://www.acmicpc.net/problem/14940
# 메모리/시간: 183080KB / 508ms (PyPy3)

import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

_map = [list(map(int, input().rstrip().split())) for _ in range(N)]
output_map = [[0] * M for _ in range(N)]

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

def bfs(pos):
    queue = deque()
    queue.append(pos)
    visited = set()
    visited.add(pos)
    while queue:
        x, y = queue.popleft()
        for way in range(4):
            xx, yy = x + dx[way], y + dy[way]
            if (xx < 0) or (xx >= N) or (yy < 0) or (yy >= M) or ((xx, yy) in visited):
                continue
            if _map[xx][yy] == 0:
                continue
            if _map[xx][yy] == 1:
                output_map[xx][yy] = output_map[x][y] + 1
                queue.append([xx, yy])
                visited.add((xx, yy))
    return output_map, visited

def where_is_2():
    for i in range(N):
        for j in range(M):
            if _map[i][j] == 2:
                return (i, j)

def not_zero():
    c = set()
    for i in range(N):
        for j in range(M):
            if _map[i][j] != 0:
                c.add((i, j))
    return c

def cant_go(pos_set):
    for pos in pos_set:
        x, y = pos
        output_map[x][y] = -1
    return output_map

pos = where_is_2()
nz = not_zero()
output_map, ck = bfs(pos)
remain = nz - ck
if len(remain) != 0:
    output_map = cant_go(remain)

for x in output_map:
    print(" ".join(map(str, x)))