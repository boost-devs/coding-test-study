###### 14502번: 연구소
# https://www.acmicpc.net/problem/14502
# 메모리/시간: 34080KB / 4388ms

import sys
from collections import deque
from itertools import combinations
from copy import deepcopy

input = sys.stdin.readline

N, M = map(int, input().split())

_map = [list(map(int, input().rstrip().split())) for _ in range(N)]

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

def virus_bfs(_map, pos):
    queue = deque(pos)
    while queue:
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for way in range(4):
                xx, yy = x + dx[way], y + dy[way]

                if (xx < 0) or (xx >= N) or (yy < 0) or (yy >= M):
                    continue

                if _map[xx][yy] == 0:
                    _map[xx][yy] = 2
                    queue.append([xx, yy])

def virus():
    pos = []
    for i in range(N):
        for j in range(M):
            if _map[i][j] == 2:
                pos.append([i, j])
    return pos

def empty():
    pos = []
    for i in range(N):
        for j in range(M):
            if _map[i][j] == 0:
                pos.append([i, j])
    return pos

def not_virus(_map):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if _map[i][j] == 0:
                cnt += 1
    return cnt

virus_space = virus()
empty_space = empty()
empty_C_3 = list(combinations(empty_space, 3))

answer = 0

for c1, c2, c3 in empty_C_3:
    tmp_map = deepcopy(_map)
    x1, y1 = c1
    x2, y2 = c2
    x3, y3 = c3
    tmp_map[x1][y1] = 1
    tmp_map[x2][y2] = 1
    tmp_map[x3][y3] = 1
    virus_bfs(tmp_map, virus_space)
    cnt = not_virus(tmp_map)
    if cnt > answer:
        answer = cnt

print(answer)