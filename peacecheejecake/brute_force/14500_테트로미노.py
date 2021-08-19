# https://www.acmicpc.net/problem/14500
# 34996 KB / 6700 ms

N, M = map(int, input().split())
numbers = []
for _ in range(N):
    numbers.append([int(x) for x in input().split()])

tetrominos = [
    ((0, 1), (0, 2), (0, 3)), # cyan
    ((1, 0), (2, 0), (3, 0)),
    ((0, 1), (1, 0), (1, 1)), # yellow
    ((0, 1), (1, 0), (2, 0)), # orange
    ((0, 1), (1, 1), (2, 1)),
    ((1, 0), (2, 0), (2, 1)),
    ((1, 0), (2, 0), (2, -1)),
    ((1, 0), (0, 1), (0, 2)),
    ((1, 0), (1, 1), (1, 2)),
    ((0, 1), (0, 2), (1, 2)),
    ((0, 1), (0, 2), (-1, 2)),
    ((1, 0), (1, 1), (2, 1)), # green
    ((1, 0), (1, -1), (2, -1)),
    ((0, 1), (1, 0), (1, -1)),
    ((0, 1), (1, 1), (1, 2)),
    ((0, 1), (1, 1), (0, 2)), # magenta
    ((1, -1), (1, 0), (1, 1)),
    ((1, 0), (1, -1), (2, 0)),
    ((1, 0), (1, 1), (2, 0)),
]

max_sum = 0
for i in range(N):
    for j in range(M):
        for tetromino in tetrominos:
            _sum = numbers[i][j]
            for di, dj in tetromino:
                ni, nj = i + di, j + dj
                if ni < 0 or ni >= N or nj < 0 or nj >= M:
                    break
                _sum += numbers[ni][nj]
            else:
                max_sum = max(max_sum, _sum)

print(max_sum)
