# https://www.acmicpc.net/problem/2615
# 오목
# 29200 KB / 64 ms


import sys

def input():
    return sys.stdin.readline().rstrip().split()

table = []
for i in range(19):
    table.append(input())

starts = []
for i in range(19):
    for j in range(19):
        stone = table[i][j]
        if stone != '0':
            if (
                (j < 18 and table[i][j + 1] == stone) and
                (j == 0 or table[i][j - 1] != stone)
            ): # 가로
                starts.append(((i, j), (0, 1)))
            if (
                (i < 18 and table[i + 1][j] == stone) and
                (i == 0 or table[i - 1][j] != stone)
            ): # 세로
                starts.append(((i, j), (1, 0)))
            if (
                (i < 18 and j < 18 and table[i + 1][j + 1] == stone) and
                (i == 0 or j == 0 or table[i - 1][j - 1] != stone)
            ): # 대각선 오른쪽 아래
                starts.append(((i, j), (1, 1)))
            if (
                (i > 0 and j < 18 and table[i - 1][j + 1] == stone) and
                (i == 18 or j == 0 or table[i + 1][j - 1] != stone)
            ): # 대각선 오른쪽 위
                starts.append(((i, j), (-1, 1)))

winner = '0'
win_start = None
for (si, sj), (di, dj) in starts:
    count = 1
    stone = table[si][sj]
    i, j = si, sj
    for _ in range(5):
        i, j = i + di, j + dj
        if i == -1 or i == 19 or j == 19 or table[i][j] != stone:
            break
        count += 1
    
    if count == 5:
        winner = stone
        win_start = (si + 1, sj + 1)
        break

print(winner)
if win_start is not None:
    print(*win_start)
