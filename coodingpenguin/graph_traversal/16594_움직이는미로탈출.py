# 문제: [BOJ 16594] 움직이는 미로 탈출
# 유형: DFS
# 메모리/시간: KB / ms

import sys
from collections import deque

input = sys.stdin.readline
N = 8

action = [(0, 0), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1)]


def down_walls():
    arr.pop()
    arr.insert(0, ["."] * N)


def bfs(sy, sx):
    global walls
    queue = deque([(sy, sx)])
    while queue:
        q_size = len(queue)
        for _ in range(q_size):
            y, x = queue.popleft()
            if arr[y][x] == "#":
                continue
            if (y, x) == (0, N - 1):
                return True
            for dy, dx in action:
                ny, nx = y + dy, x + dx
                if (0 <= ny < N) and (0 <= nx < N) and arr[ny][nx] == ".":
                    queue.append((ny, nx))
            down_walls()
    return False


# 입력
arr = [list(input().rstrip()) for _ in range(N)]  # 체스판

result = bfs(N - 1, 0)

print(result)
