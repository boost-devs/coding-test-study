###### 11365번: !밀비 급일
# https://www.acmicpc.net/problem/11365
# 메모리/시간: 29200KB / 64ms

import sys

input = sys.stdin.readline

while True:
    _input = input().rstrip()
    if _input == "END":
        break
    print(_input[::-1])