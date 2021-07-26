# 문제: [BOJ 4396] 지뢰 찾기
# 유형: 구현
# 메모리/시간: 29200kb / 68ms

import sys

input = sys.stdin.readline
direction = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]


def get_play_info():
    result = [
        [0 if play[y][x] == "x" else "." for x in range(n)] for y in range(n)
    ]  # 격자판 정보
    is_bombed = False  # 터뜨렸는지 여부
    for y in range(n):
        for x in range(n):
            # 폭탄 위치이고
            if game[y][x] == "*":
                # 폭탄을 터뜨렸다면
                if play[y][x] == "x":
                    is_bombed = True  # 터뜨렸다고 체크
                # 모든 방향에 대해
                for dy, dx in direction:
                    ny, nx = y + dy, x + dx
                    # 격자판 범위 내이고
                    if (0 <= ny < n) and (0 <= nx < n):
                        # 플레이한 위치라면
                        if result[ny][nx] != ".":
                            result[ny][nx] += 1  # 폭탄 위치 카운트
    # 터졌다면
    if is_bombed:
        for y in range(n):
            for x in range(n):
                # 폭탄 위치 표시
                if game[y][x] == "*":
                    result[y][x] = "*"
    return result


n = int(input())  # 격자판 크기
game = [list(input().rstrip()) for _ in range(n)]  # 격자판
play = [list(input().rstrip()) for _ in range(n)]  # 플레이 위치

# 플레이 정보 읽기
board = get_play_info()

# 격자판 출력
for row in board:
    print(*row, sep="")
