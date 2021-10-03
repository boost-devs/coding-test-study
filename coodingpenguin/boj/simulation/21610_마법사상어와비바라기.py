# 문제: [BOJ 21610] 마법사 상어와 비바라기
# 유형: 시뮬레이션, 구현
# 메모리/시간: 29452kb / 344ms, 126432kb / 192ms (PyPy3)

import sys

input = sys.stdin.readline
dirs = [
    (0, -1),
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, 1),
    (1, 1),
    (1, 0),
    (1, -1),
]  # ←, ↖, ↑, ↗, →, ↘, ↓, ↙
diags = [
    (-1, -1),
    (-1, 1),
    (1, 1),
    (1, -1),
]  # ↖, ↗, ↘, ↙


def move_cloud(n, d, s, clouds):
    new_clouds = set()  # 새로운 구름 위치
    for r, c in clouds:
        nr, nc = (r + s * dirs[d - 1][0]) % n, (c + s * dirs[d - 1][1]) % n
        new_clouds.add((nr, nc))
    return new_clouds


def rain(board, clouds):
    # 구름이 있는 위치에
    for r, c in clouds:
        board[r][c] += 1  # 물의 양을 1 증가시킨다
    return board


def magic_watercopy(n, board, clouds):
    for r, c in clouds:
        count = 0
        for dr, dc in diags:
            nr, nc = r + dr, c + dc
            # 격자판을 벗어난다면
            if (nr < 0 or nr >= n) or (nc < 0 or nc >= n):
                continue  # 패스한다
            # 현재 위치에 물이 있다면
            if board[nr][nc]:
                count += 1  # 카운트를 증가시킨다
        # 물의 양을 카운트만큼 증가시킨다
        board[r][c] += count
    return board


def create_clouds(board, clouds):
    new_clouds = set()  # 새로운 구름 위치
    for r in range(n):
        for c in range(n):
            # 물의 양이 2이상이고
            if board[r][c] >= 2:
                # 구름이 사라진 칸이 아니라면
                if (r, c) not in clouds:
                    board[r][c] -= 2  # 물의 양을 2 감소시키고
                    new_clouds.add((r, c))  # 구름을 생성한다
    return new_clouds


def calculate_total_water(n, board):
    total_water = 0  # 총 물의 양
    for r in range(n):
        for c in range(n):
            total_water += board[r][c]
    return total_water


def magic_rainstorm(n, m, board, info):
    clouds = {(n - 1, 0), (n - 2, 0), (n - 1, 1), (n - 2, 1)}  # 초기 구름 위치
    for d, s in info:
        # 구름을 이동한다
        clouds = move_cloud(n, d, s, clouds)
        # 구름이 있는 위치에 비가 내린다
        board = rain(board, clouds)
        # 물복사버그 마법을 시전한다
        board = magic_watercopy(n, board, clouds)
        # 물의 양이 2이상인 곳에 구름이 생긴다
        clouds = create_clouds(board, clouds)
    # 총 물의 양을 구한다
    return calculate_total_water(n, board)


n, m = map(int, input().split())  # 격자판 크기, 이동 횟수
board = [list(map(int, input().split())) for _ in range(n)]  # 격자판
info = [list(map(int, input().split())) for _ in range(m)]  # 이동 정보

print(magic_rainstorm(n, m, board, info))  # m번 이동 후 총 물의 양
