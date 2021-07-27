###### 16719번: ZOAC
# https://www.acmicpc.net/problem/16719
# 메모리/시간: 29200KB / 76ms

import sys

input = sys.stdin.readline

_input = input().rstrip()

answer = [""] * len(_input)

def ZOAC(string, i):
    if string == "":
        return
    _min = min(string)
    idx = string.index(_min)
    answer[i+idx] = _min
    print("".join(map(str, answer)))
    ZOAC(string[idx+1:], i+idx+1)
    ZOAC(string[:idx], i)

ZOAC(_input, 0)