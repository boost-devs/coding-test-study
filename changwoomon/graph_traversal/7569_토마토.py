###### 7569번: 토마토
# https://www.acmicpc.net/problem/7569
# 메모리/시간: 52264KB / 3484ms

import sys
from collections import deque

input = sys.stdin.readline

M, N, H = map(int, input().split())

_map = [[list(map(int, input().rstrip().split())) for _ in range(N)] for _ in range(H)]

dz, dx, dy = [1, 0, 0, -1, 0, 0], [0, 1, 0, 0, -1, 0], [0, 0, 1, 0, 0, -1]

def bfs(pos):
    queue = deque(pos)
    day = -1
    while queue:
        for _ in range(len(queue)):
            z, x, y = queue.popleft()
            for way in range(6):
                zz, xx, yy = z + dz[way], x + dx[way], y + dy[way]

                if (zz < 0) or (zz >= H) or (xx < 0) or (xx >= N) or (yy < 0) or (yy >= M):
                    continue

                if _map[zz][xx][yy] == 0:
                    _map[zz][xx][yy] = 1
                    queue.append([zz, xx, yy])

        day += 1
    return day

def check_all():
    for i in range(N):
        for j in range(M):
            for k in range(H):
                if _map[k][i][j] == 0:
                    return False
    return True

pos = []
for i in range(N):
    for j in range(M):
        for k in range(H):
            if _map[k][i][j] == 1:
                pos.append([k, i, j])

day = bfs(pos)

if not check_all():
    day = -1

print(day)