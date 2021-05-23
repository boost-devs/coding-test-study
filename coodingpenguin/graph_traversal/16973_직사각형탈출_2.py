# 문제: [BOJ 16973] 직사각형 탈출
# 유형: BFS
# 메모리/시간: 39680KB / 5720ms
# 참고: https://www.acmicpc.net/source/29306725

import sys
from collections import deque

input = sys.stdin.readline
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 우하좌상


def find_wall():
    walls = []
    for i in range(n):
        for j in range(m):
            # 벽이 있다면 좌표 저장
            if arr[i][j] == 1:
                walls.append((i, j))
    return walls


def can_move(h, w, y, x):
    for wy, wx in walls:
        # 직사각형에 벽이 있다면
        if (y <= wy < y + h) and (x <= wx < x + w):
            return False
    # 벽이 없다면
    return True


def bfs(sy, sx):
    queue = deque([(sy, sx, 0)])
    arr[sy][sx] = -1
    while queue:
        y, x, d = queue.popleft()
        # 도착좌표에 도착했다면 거리를 반환
        if (y, x) == (fy, fx):
            return d
        # 모든 방향에 대해서
        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            # 격자판을 벗어나지 않고 방문하지 않았고
            if (
                (ny >= 0 and ny + h - 1 < n)
                and (nx >= 0 and nx + w - 1 < m)
                and arr[ny][nx] != -1
            ):
                # 이동 가능한 즉, 벽이 없는 경우
                if can_move(h, w, ny, nx):
                    arr[ny][nx] = -1  # 방문 처리
                    queue.append((ny, nx, d + 1))  # 큐에 삽입
    # 도착하지 못했을 경우
    return -1


# 입력
n, m = map(int, input().split())  # 격자판 세로, 가로
arr = [list(map(int, input().split())) for _ in range(n)]  # 격자판
h, w, sy, sx, fy, fx = map(int, input().split())  # 직사각형 세로, 가로, 시작 좌표, 도착 좌표

# (0, 0)부터 시작하기 위해 1씩 빼기
sy, sx, fy, fx = sy - 1, sx - 1, fy - 1, fx - 1

# 벽의 위치 저장
walls = find_wall()

# 너비 우선 탐색
count = bfs(sy, sx)

# 출력
print(count)
