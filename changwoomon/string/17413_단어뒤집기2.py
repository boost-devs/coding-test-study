###### 17413번: 단어 뒤집기 2
# https://www.acmicpc.net/problem/17413
# 메모리/시간: 42932KB / 188ms

import sys
from collections import deque

input = sys.stdin.readline

_input = input().rstrip()
answer = [""] * len(_input)
d = dict()
cond = False

for i, x in enumerate(_input):
    if (x == "<") and not cond:
        answer[i] = x
        cond = True
    elif x == ">":
        answer[i] = x
        cond = False
    elif cond or x == " ":
        answer[i] = x
    else:
        d[i] = x

tmp = ""
word = []
s_idx = []

for i, x in d.items():
    if i+1 in d.keys():
        tmp += x
    else:
        tmp += x
        word.append(tmp[::-1])
        tmp = ""
        s_idx.append(i)

z = 0
for i in s_idx:
    answer[i] = word[z]
    z += 1
print("".join(map(str, answer)))