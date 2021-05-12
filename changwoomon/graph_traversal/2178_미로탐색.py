###### 2178번: 미로 탐색
# https://www.acmicpc.net/problem/2178
# 메모리/시간: 31804KB / 112ms

# import sys
from collections import deque

# input = sys.stdin.readline

N, M = map(int, input().split())

_map = [list(map(int, input())) for _ in range(N)]

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

def bfs(x, y):
    queue = deque()
    queue.append([x, y])

    while queue:
        x, y = queue.popleft()
        for way in range(4):
            xx, yy = x + dx[way], y + dy[way]

            if (xx < 0) or (xx >= N) or (yy < 0) or (yy >= M):
                continue

            if _map[xx][yy] == 0:
                continue

            if _map[xx][yy] == 1:
                _map[xx][yy] = _map[x][y] + 1
                queue.append([xx, yy])
    
    return _map[N-1][M-1]

print(bfs(0, 0))