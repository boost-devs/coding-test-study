###### 2578번: 빙고
# https://www.acmicpc.net/problem/2578
# 메모리/시간: 29200KB / 68ms

import sys

input = sys.stdin.readline

chulsoo = [list(map(int, input().split())) for _ in range(5)]

bingo = []

for i in range(5):
    tmp = []
    tmp2 = []
    for j in range(5):
        tmp.append((i, j))
        tmp2.append((j, i))
    bingo.append(tmp)
    bingo.append(tmp2)

tmp = []
tmp2 = []

for i in range(5):
    tmp.append((i, i))
    tmp2.append((4-i, i))

bingo.append(tmp)
bingo.append(tmp2)

MC = [0]

for _ in range(5):
    MC.extend(map(int, input().split()))

def bingo_game():
    game = set()
    for i, x in enumerate(MC):
        for j in range(5):
            for k in range(5):
                if chulsoo[j][k] == x:
                    game.add((j, k))
        cnt = 0
        for x in bingo:
            if set(x).intersection(game) == set(x):
                cnt += 1
            if cnt == 3:
                return i

print(bingo_game())