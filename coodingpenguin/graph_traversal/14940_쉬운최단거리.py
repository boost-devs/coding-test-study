# 문제: [BOJ 14940] 쉬운 최단거리
# 유형: BFS
# 메모리/시간: 42184kb / 632ms

import sys
from collections import deque

input = sys.stdin.readline
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 우하좌상


def bfs(sy, sx):
    queue = deque([(sy, sx, 0)])
    visited[sy][sx] = True
    while queue:
        y, x, d = queue.popleft()
        dist[y][x] = d  # 거리 정보 갱신
        # 모든 방향에 대해서
        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if (
                (0 <= ny < n)  # 격자판 내에 있고
                and (0 <= nx < m)
                and not visited[ny][nx]  # 방문하지 않았고
                and arr[ny][nx] == 1  # 벽이 아니라면
            ):
                visited[ny][nx] = True  # 방문 처리
                queue.append((ny, nx, d + 1))  # 큐에 삽입


# 입력
n, m = map(int, input().split())  # 지도 세로, 가로
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

# 거리 정보 -1로 초기화
dist = [[-1] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        # 벽은 0으로 초기화
        if arr[i][j] == 0:
            dist[i][j] = 0
        # 시작 지점은 저장
        elif arr[i][j] == 2:
            sy, sx = i, j

# 너비 우선 탐색
bfs(sy, sx)

# 출력
for row in dist:
    print(*row)
