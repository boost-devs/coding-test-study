# 문제: [BOJ 16973] 직사각형 탈출
# 유형: BFS
# 메모리/시간: 153988KB / 872ms (PyPy3)
# 참고: https://blog.naver.com/adamdoha/221952199421

import sys
from collections import deque

input = sys.stdin.readline
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 우하좌상


def can_move(h, w, ny, nx, dir):
    # 오른쪽으로 이동
    if dir == 0:
        for i in range(h):
            if arr[ny + i][nx + w - 1] == 1:
                return False
    # 아래쪽으로 이동
    elif dir == 1:
        for i in range(w):
            if arr[ny + h - 1][nx + i] == 1:
                return False
    # 왼쪽으로 이동
    elif dir == 2:
        for i in range(h):
            if arr[ny + i][nx] == 1:
                return False
    # 위쪽으로 이동
    else:
        for i in range(w):
            if arr[ny][nx + i] == 1:
                return False
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
        for i, (dy, dx) in enumerate(direction):
            ny, nx = y + dy, x + dx
            # 격자판을 벗어나지 않고 방문하지 않았고
            if (
                (ny >= 0 and ny + h - 1 < n)
                and (nx >= 0 and nx + w - 1 < m)
                and arr[ny][nx] != -1
            ):
                # 이동 가능한 즉, 벽이 없는 경우
                if can_move(h, w, ny, nx, dir=i):
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

# 너비 우선 탐색
count = bfs(sy, sx)

# 출력
print(count)
