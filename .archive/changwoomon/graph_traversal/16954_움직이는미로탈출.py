###### 16954번: 움직이는 미로 탈출
# https://www.acmicpc.net/problem/16954
# 메모리/시간: 33048KB / 96ms

import sys
from collections import deque

input = sys.stdin.readline

_map = [list(input().rstrip()) for _ in range(8)]


direction = ((0, 0), (1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1))

def bfs(xxx, yyy):
    queue = deque()
    queue.append((xxx, yyy))
    while queue:
        wall = wall_pos()
        if len(wall) == 0:
            return 1
        pos_cnd = set()
        for _ in range(len(queue)):
            pos = queue.popleft()
            x, y = pos
            for d in direction:
                dx, dy = d
                xx, yy = x + dx, y + dy
                if (xx < 0) or (xx >= 8) or (yy < 0) or (yy >= 8) or ((xx, yy) in wall):
                    continue
                if (xx, yy) == (0, 7):
                    return 1
                pos_cnd.add((xx, yy))
        new_wall = wall_move(wall)
        if len(pos_cnd) == 0:
            return 0
        else:
            remain = pos_cnd - new_wall
            if len(remain) == 0:
                return 0
            else:
                for xy in remain:
                    queue.append(xy)
    return 0

def wall_pos():
    global _map
    wall = set()
    for i in range(8):
        for j in range(8):
            if _map[i][j] == "#":
                wall.add((i, j))
    return wall

def wall_move(wall):
    global _map
    new_wall = set()
    for pos in wall:
        x, y = pos
        if 0 <= x < 7:
            _map[x+1][y] = "#"
            new_wall.add((x+1, y))
    remain = wall - new_wall
    for pos in remain:
        x, y = pos
        _map[x][y] = "."
    return new_wall

print(bfs(7, 0))
