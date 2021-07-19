# https://www.acmicpc.net/problem/4396
# 지뢰 찾기
# 29200 KB / 76 ms


n = int(input())
hidden, mines = [], []
for i in range(n):
    row = list(input())
    _mines = [(i, j) for j in range(n) if row[j] == '*']
    hidden.append(row)
    mines.extend(_mines)

open_ = [list(input()) for _ in range(n)]

directions = [(1, 0), (1, -1), (0, -1), (-1, -1),
              (-1, 0), (-1, 1), (0, 1), (1, 1)]

lost = False
for i in range(n):
    for j in range(n):
        if open_[i][j] == 'x':
            if hidden[i][j] == '*':
                lost = True
            else:
                num = 0
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if (ni >= 0 and ni < n and 
                        nj >= 0 and nj < n and 
                        hidden[ni][nj] == '*'):
                        num += 1
                open_[i][j] = str(num)

if lost:
    for i, j in mines:
        open_[i][j] = '*'

for row in open_:
    print(''.join(row))
