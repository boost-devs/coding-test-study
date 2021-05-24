###### 16973번: 직사각형 탈출
# https://www.acmicpc.net/problem/16973
# 메모리/시간: 152336KB / 864ms

import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

_map = [list(map(int, input().rstrip().split())) for _ in range(N)]

H, W, S_r, S_c, F_r, F_c = map(int, input().split())

S_r, S_c, F_r, F_c = S_r-1, S_c-1, F_r-1, F_c-1

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

def bfs(x, y):
    _map[x][y] = -1
    queue = deque([[x, y]])
    # visited = [[x, y]]
    cnt = 0
    while queue:
        for _ in range(len(queue)):
            x, y = queue.popleft()
            if [x, y] == [F_r, F_c]:
                return cnt
            for way in range(4):
                xx, yy = x + dx[way], y + dy[way]
                if (xx < 0) or (xx+H-1 >= N) or (yy < 0) or (yy+W-1 >= M) or (_map[xx][yy] == -1):
                # if (xx < 0) or (xx+H-1 >= N) or (yy < 0) or (yy+W-1 >= M) or ([xx, yy] in visited):
                    continue
                else:
                    if not_wall(xx, yy, way):
                        _map[xx][yy] = -1
                        queue.append([xx, yy])
                        # visited.append([xx, yy])
        cnt += 1
    return -1

def not_wall(x, y, way):
    if way == 0:
        for z in range(y, y+W):
            if _map[x+H-1][z] == 1:
                return False
    elif way == 1:
        for z in range(x, x+H):
            if _map[z][y+W-1] == 1:
                return False
    elif way == 2:
        for z in range(y, y+W):
            if _map[x][z] == 1:
                return False
    else:
        for z in range(x, x+H):
            if _map[z][y] == 1:
                return False
    return True

print(bfs(S_r, S_c))