###### 2615번: 오목
# https://www.acmicpc.net/problem/2615
# 메모리/시간: 29200KB / 76ms

import sys

input = sys.stdin.readline

black = []
white = []

for i in range(19):
    for j, x in enumerate(map(int, input().split())):
        if x == 1:
            black.append((i, j))
        if x == 2:
            white.append((i, j))

direction = [(1, 0), (0, 1), (1, 1), (-1, 1)]

def omok(arr):
    for x, y in arr:
        for dx, dy in direction:
            xx, yy = x, y
            cnt = 1

            while (0 <= xx < 19) and (0 <= yy < 19):
                xxx, yyy = xx + dx, yy + dy
                if (xxx, yyy) in arr:
                    cnt += 1
                else:
                    break
                xx, yy = xxx, yyy
                if cnt == 5:
                    break

            if cnt == 5:
                if ((x-dx, y-dy) not in arr) and ((xxx+dx, yyy+dy) not in arr):
                    return True, x+1, y+1
                    
    return False, -1, -1

cond_black, x_black, y_black = omok(black)
cond_white, x_white, y_white = omok(white)

if not cond_black and not cond_white:
    print(0)
elif cond_black:
    print(1)
    print(x_black, y_black)
elif cond_white:
    print(2)
    print(x_white, y_white)