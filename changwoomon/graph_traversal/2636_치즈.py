###### 2636번: 치즈
# https://www.acmicpc.net/problem/2636
# 메모리/시간: 36160KB / 188ms

import sys
from collections import deque

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

R, C = map(int, input().split())

_map = [list(map(int, input().rstrip().split())) for _ in range(R)]

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

def to_melt(pos_set):
    queue = deque(pos_set)
    while queue:
        x, y = queue.popleft()
        for way in range(4):
            xx, yy = x + dx[way], y + dy[way]
            if(xx < 0) or (xx >= R) or (yy < 0) or (yy >= C):
                continue
            if _map[xx][yy] == 1:
                _map[xx][yy] = 0

def dfs(x, y):
    cluster.add((x, y))
    for way in range(4):
        xx, yy = x + dx[way], y + dy[way]
        if (xx < 0) or (xx >= R) or (yy < 0) or (yy >= C):
            continue
        if (xx, yy) in cluster:
            continue
        if _map[xx][yy] == 0:
            dfs(xx, yy)

def cheese_count():
    cnt = 0
    for i in range(R):
        for j in range(C):
            if _map[i][j] == 1:
                cnt += 1
    return cnt

melt_time = 0

while True:
    cluster = set()
    dfs(0, 0)
    if len(cluster) == R*C:
        break
    cnt = cheese_count()
    melt_time += 1
    to_melt(cluster)

print(melt_time)
print(cnt)