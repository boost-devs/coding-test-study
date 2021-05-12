# 문제: [BOJ 2178] 미로 탐색
# 유형: BFS
# 메모리/시간: 32052kb / 96ms
# 참고: https://www.acmicpc.net/board/view/12343

import sys
from collections import deque

input = sys.stdin.readline
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 우하좌상


def bfs(sy, sx):
    queue = deque([(sy, sx)])
    visited[sy][sx] = True  # 시작위치는 방문체크
    count = 1  # 최소 이동 횟수
    while queue:
        q_size = len(queue)  # 큐의 길이
        for _ in range(q_size):
            y, x = queue.popleft()
            # 도착 지점에 도착했을 경우
            if x == m - 1 and y == n - 1:
                return count
            # 도착하지 않았을 경우 모든 방향에 대해 탐색
            for dy, dx in direction:
                ny, nx = y + dy, x + dx  # 새로운 위치 후보
                # 미로 범위 내에 있고
                if (0 <= nx < m) and (0 <= ny < n):
                    # 방문하지 않고 갈 수 있는 길일 경우
                    if not visited[ny][nx] and maze[ny][nx] == "1":
                        visited[ny][nx] = True
                        queue.append((ny, nx))
        count += 1  # 현재 층을 다 돌면 +1 증가


# 입력
n, m = map(int, input().split())  # 미로의 세로, 가로 길이
maze = [list(input().rstrip()) for _ in range(n)]  # 미로
visited = [[False] * m for _ in range(n)]  # 현재 위치 방문여부

# 출력
print(bfs(0, 0))
