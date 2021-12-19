###### 20436번: ZOAC 3
# https://www.acmicpc.net/problem/20436
# 메모리/시간: 29200KB / 76ms

import sys

input = sys.stdin.readline

s_L, s_R = input().split()
string = input().rstrip()

keyboard = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
lefthand = "qwertasdfgzxcv"

def position(pos):
    for i in range(len(keyboard)):
        if pos in keyboard[i]:
            x = i
            y = keyboard[i].index(pos)
    return x, y

def keyboarding(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)

x_L, y_L = position(s_L)
x_R, y_R = position(s_R)

time = 0

for s in string:
    x_s, y_s = position(s)
    if s in lefthand:
        time += keyboarding(x_L, y_L, x_s, y_s)
        x_L, y_L = x_s, y_s
    else:
        time += keyboarding(x_R, y_R, x_s, y_s)
        x_R, y_R = x_s, y_s
    time += 1

print(time)