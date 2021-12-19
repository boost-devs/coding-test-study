###### 17413번: 단어 뒤집기 2
# https://www.acmicpc.net/problem/17413
# 메모리/시간: 40484KB / 152ms

import sys

input = sys.stdin.readline

S = input().rstrip()

answer = [""] * len(S)
d = dict()
cond = False

for i, s in enumerate(S):
    if (s == "<") and not cond:
        answer[i] = s
        cond = True
    elif s == ">":
        answer[i] = s
        cond = False
    elif (s == " ") or cond:
        answer[i] = s
    else:
        d[i] = s

tmp = ""

for i, s in d.items():
    if i + 1 in d.keys():
        tmp += s
    else:
        tmp += s
        answer[i] = tmp[::-1]
        tmp = ""

print("".join(map(str, answer)))