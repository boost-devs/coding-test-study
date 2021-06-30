# https://www.acmicpc.net/problem/1890
# 점프
# 29200 KB / 72 ms

def jump(i, j, game_map, table):
    step = game_map[i][j]
    if step > 0:
        curr = table[i][j]
        for di, dj in ((step, 0), (0, step)):
            i_, j_ = i + di, j + dj
            if i_ >= 0 and i_ < N and j_ >= 0 and j_ < N:
                table[i_][j_] += curr


N = int(input())
game_map = []
for _ in range(N):
    game_map.append([int(x) for x in input().split()])

table = [[0] * N for _ in range(N)]
table[0][0] = 1
for i in range(N):
    for j in range(i, N):
        jump(i, j, game_map, table)
        if j > i:
            jump(j, i, game_map, table)

print(table[-1][-1])
