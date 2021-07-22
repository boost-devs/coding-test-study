###### 21608번: 상어 초등학교
# https://www.acmicpc.net/problem/21608
# 메모리/시간: 32036KB / 272ms

import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())

classroom = [[0] * N for _ in range(N)]

info = defaultdict(list)

direction = ((1, 0), (0, 1), (-1, 0), (0, -1))

pos_set = set()

def positioning(num, classroom):
    global pos_set
    position = rule_1(num)
    if len(position) == 1:
        x, y = position[0]
        classroom[x][y] = num
        pos_set.add((x, y))
    else:
        position = rule_2(position)
        if len(position) == 1:
            x, y = position[0]
            classroom[x][y] = num
            pos_set.add((x, y))
        else:
            position = rule_3_1(position)
            min_row = position[0][0]
            candidate = []
            for pos in position:
                if pos[0] == min_row:
                    candidate.append(pos)
            if len(candidate) == 1:
                x, y = candidate[0]
                classroom[x][y] = num
                pos_set.add((x, y))
            else:
                position = rule_3_2(candidate)
                x, y = position[0]
                classroom[x][y] = num
                pos_set.add((x, y))
    return classroom


def rule_1(num):
    global info
    _max = 0
    position = []
    for x in range(N):
        for y in range(N):
            if (x, y) in pos_set:
                continue
            cnt = 0
            for dx, dy in direction:
                xx, yy = x + dx, y + dy
                if (0 <= xx < N) and (0 <= yy < N):
                    if classroom[xx][yy] in info[num]:
                        cnt += 1
            if cnt > _max:
                _max = cnt
                position = [(x, y)]
            elif cnt == _max:
                position.append((x, y))
    return position

def rule_2(pos):
    _max = 0
    position = []
    for x, y in pos:
        cnt = 0
        for dx, dy in direction:
            xx, yy = x + dx, y + dy
            if (0 <= xx < N) and (0 <= yy < N):
                if classroom[xx][yy] == 0:
                    cnt += 1
        if cnt > _max:
            _max = cnt
            position = [(x, y)]
        elif cnt == _max:
            position.append((x, y))
    return position

def rule_3_1(pos):
    position = sorted(pos, key=lambda x: x[0])
    return position

def rule_3_2(pos):
    position = sorted(pos, key=lambda x: x[1])
    return position

for _ in range(N*N):
    num, *like = map(int, input().split())
    info[num] = like
    classroom = positioning(num, classroom)

satisfaction = 0

for x in range(N):
    for y in range(N):
        cnt = -1
        for dx, dy in direction:
            xx, yy = x + dx, y + dy
            if (0 <= xx < N) and (0 <= yy < N):
                if classroom[xx][yy] in info[classroom[x][y]]:
                    cnt += 1
        if cnt == -1:
            continue
        satisfaction += 10**cnt

print(satisfaction)