import sys

input = sys.stdin.readline


def is_bingo():
    count = 0
    # 로우
    for row in check:
        if all(row):
            count += 1
    # 컬럼
    for col in zip(*check):
        if all(col):
            count += 1

    # 대각선
    left_bottom = [check[i][i] for i in range(5)]
    if all(left_bottom):
        count += 1
    right_bottom = [check[i][4 - i] for i in range(5)]
    if all(right_bottom):
        count += 1

    if count >= 3:
        return True
    return False


bingo = [list(map(int, input().split())) for _ in range(5)]
pos = {}
for i in range(5):
    for j in range(5):
        pos[bingo[i][j]] = (i, j)
check = [[False] * 5 for _ in range(5)]
calls = []
for _ in range(5):
    calls.extend(list(map(int, input().split())))

for i, num in enumerate(calls):
    # 숫자 True로 바꿈
    y, x = pos[num]
    check[y][x] = True

    # 빙고 되는 부분 있는지 체크
    if is_bingo():
        print(i + 1)
        break
