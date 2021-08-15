# 문제: [BOJ 2615] 오목
# 유형: 완전 탐색
# 메모리/시간: 29200kb / 80ms

import sys

input = sys.stdin.readline
SIZE = 19  # 바둑판 크기
directions = [(0, 1), (1, 0), (1, 1), (1, -1)]  # 방향


def get_winner(board: list):
    # 바둑판의 모든 알을 탐색하면서
    for y in range(SIZE):
        for x in range(SIZE):
            # 바둑알이 없다면 패스
            if not board[y][x]:
                continue
            # 모든 가능한 방향에 대해서
            for dy, dx in directions:
                ny, nx = y + dy, x + dx  # 새로운 탐색 위치
                # 바둑판을 벗어난다면 패스
                if ny < 0 or ny >= SIZE or nx < 0 or nx >= SIZE:
                    continue
                count = 1  # 연속 바둑알 개수
                # 바둑판 범위 내이고 같은 바독알일 경우 반복
                while (
                    0 <= ny < SIZE and 0 <= nx < SIZE and board[ny][nx] == board[y][x]
                ):
                    if count == 5:
                        break
                    count += 1
                    ny, nx = ny + dy, nx + dx
                # 연속 바둑알 개수가 5가 아니라면
                if count != 5:
                    continue  # 우승자가 아니므로 패스
                # 바로 다음에 같은 바둑알이 있는 경우 6개 이상이므로 패스
                if 0 <= ny < SIZE and 0 <= nx < SIZE and board[ny][nx] == board[y][x]:
                    continue
                # 바로 이전에 같은 바둑알이 있는 경우 이미 본 바둑알이므로 패스
                if (
                    0 <= y - dy < SIZE
                    and 0 <= x - dx < SIZE
                    and board[y - dy][x - dx] == board[y][x]
                ):
                    continue
                # (↙)의 경우
                if dy == 1 and dx == -1:
                    return board[y][x], ny - dy + 1, nx - dx + 1
                # 나머지 방향의 경우
                return board[y][x], y + 1, x + 1
    return 0, None, None


# 입력
board = [list(map(int, input().split())) for _ in range(SIZE)]  # 오목판

# 우승자 선택
winner, y, x = get_winner(board)

# 출력
print(winner)
if winner:
    print(y, x)
