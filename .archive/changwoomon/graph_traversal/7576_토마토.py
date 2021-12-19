###### 7576번: 토마토
# https://www.acmicpc.net/problem/7576
# 메모리/시간: 162360KB / 2524ms

import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().split())

_map = [list(map(int, input().rstrip().split())) for _ in range(N)]

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

def bfs(pos):
    queue = deque(pos)
    day = -1
    while queue:
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for way in range(4):
                xx, yy = x + dx[way], y + dy[way]

                if (xx < 0) or (xx >= N) or (yy < 0) or (yy >= M):
                    continue

                if _map[xx][yy] == 0:
                    _map[xx][yy] = 1
                    queue.append([xx, yy])

        day += 1
    return day

def check_all():
    for i in range(N):
        for j in range(M):
            if _map[i][j] == 0:
                return False
    return True

pos = []
for i in range(N):
    for j in range(M):
        if _map[i][j] == 1:
            pos.append([i, j])

day = bfs(pos)

if not check_all():
    day = -1

print(day)