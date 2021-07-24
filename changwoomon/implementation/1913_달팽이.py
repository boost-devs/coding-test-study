###### 1913번: 달팽이
# https://www.acmicpc.net/problem/1913
# 메모리/시간: 67980KB / 1228ms

import sys

input = sys.stdin.readline

N = int(input())
find_num = int(input())

snail = [[0] * N for _ in range(N)]

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

way = 0

n = N * N

i, j = -1, 0

while n >= 1:
    while True:
        ii, jj = i + dx[way], j + dy[way]
        if (0 <= ii < N) and (0 <= jj < N) and (snail[ii][jj] == 0):
            break
        way = (way + 1) % 4
    snail[ii][jj] = n
    if n == find_num:
        answer = (ii+1, jj+1)
    n -= 1
    i, j = ii, jj

for row in snail:
    print(*row)

print(*answer)