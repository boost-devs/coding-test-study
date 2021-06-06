###### 9342번: 염색체
# https://www.acmicpc.net/problem/9342
# 메모리/시간: 32084KB / 92ms

import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    _input = deque(input().rstrip() + " ")
    cond1, cond2, cond3, cond4, cond5 = True, False, False, False, False
    
    if _input[0] not in "ABCDEF":
        cond1 = False
    if _input[0] != "A":
        _input.popleft()
    if cond1:
        while _input[0] == "A":
            _input.popleft()
            cond2 = True
        if cond2:
            while _input[0] == "F":
                _input.popleft()
                cond3 = True
            if cond3:
                while _input[0] == "C":
                    _input.popleft()
                    cond4 = True
                if cond4:
                    cnt = 0
                    cond5_ = False
                    for x in _input:
                        if x == " ":
                            cond5_ = True
                            continue
                        if x in "ABCDEF":
                            cnt += 1
                            cond5_ = True
                        else:
                            break
                    if cond5_ and (0 <= cnt <= 1):
                        cond5 = True

    print("Infected!") if all([cond1, cond2, cond3, cond4, cond5]) else print("Good")