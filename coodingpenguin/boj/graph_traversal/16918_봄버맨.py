# 문제: [BOJ 16918] 봄버맨
# 유형: BFS
# 메모리/시간: 35412kb / 3468ms

import sys
from collections import deque

input = sys.stdin.readline
direction = [(0, 1), (-1, 0), (0, -1), (1, 0)]  # 우하상좌


def get_pos():
    pos = []
    for i in range(r):
        for j in range(c):
            if arr[i][j] == "O":
                pos.append((i, j))
    return pos


def fill_bomb():
    for i in range(r):
        for j in range(c):
            # 빈 공간이면
            if arr[i][j] == ".":
                arr[i][j] = "O"  # 폭탄 넣기


def explode_bomb(pos):
    queue = deque(pos)
    for _ in range(len(queue)):
        y, x = queue.popleft()
        arr[y][x] = "."  # 폭탄 폭발
        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            # 격자판 내에 있고
            if (0 <= ny < r) and (0 <= nx < c):
                # 폭탄이 있다면
                if arr[ny][nx] == "O":
                    arr[ny][nx] = "."  # 폭탄 폭발


def bfs(limit):
    for time in range(2, limit + 1):
        cmd = time % 2
        if not cmd:
            # 초기 폭탄 위치 확인
            pos = get_pos()
            # 폭탄 채우기
            fill_bomb()
        else:
            # 폭탄 터뜨리기
            explode_bomb(pos)


# 입력
r, c, n = map(int, input().split())  # 격자판 세로, 가로, 초
arr = [list(input().rstrip()) for _ in range(r)]

# 너비 우선 탐색
bfs(n)

# 출력
for row in arr:
    print("".join(row))
