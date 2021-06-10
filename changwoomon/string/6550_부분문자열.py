###### 6550번: 부분 문자열
# https://www.acmicpc.net/problem/6550
# 메모리/시간: 32064KB / 120ms

import sys
from collections import deque

input = sys.stdin.readline

while True:
    _input = input().rstrip()
    if len(_input) == 0:
        break
    s, t = _input.split()
    s, t = deque(s), deque(t)
    cond = False
    while t:
        if len(s) == 0:
            cond = True
            break
        x = t.popleft()
        if x == s[0]:
            s.popleft()
    if len(s) == 0:
        cond = True
    print("Yes") if cond else print("No")