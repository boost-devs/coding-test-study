# 문제: [BOJ 2578] 빙고
# 유형: 구현
# 메모리/시간: 29200kb / 72ms

import sys

input = sys.stdin.readline


def is_bingo():
    count = 0  # 지워지는 줄의 개수

    # 가로줄
    for row in check:
        if all(row):
            count += 1
    # 세로줄
    for col in zip(*check):
        if all(col):
            count += 1

    # 대각선
    left = [check[i][i] for i in range(5)]  # 왼쪽위에서 오른쪽아래
    if all(left):
        count += 1
    right = [check[i][4 - i] for i in range(5)]  # 오른쪽위에서 왼쪽아래
    if all(right):
        count += 1

    # 그어진 줄이 3개 이상이라면
    if count >= 3:
        # 빙고!
        return True
    return False


bingo = [list(map(int, input().split())) for _ in range(5)]  # 빙고판
pos = {}  # 숫자별 위치
for i in range(5):
    for j in range(5):
        pos[bingo[i][j]] = (i, j)
check = [[False] * 5 for _ in range(5)]  # 지운 여부
calls = []  # 사회자 숫자 순서
for _ in range(5):
    calls.extend(list(map(int, input().split())))

for i, num in enumerate(calls):
    # 사회자 숫자를 지운다
    y, x = pos[num]
    check[y][x] = True

    # 빙고가 되는지 체크
    if is_bingo():
        print(i + 1)
        break
