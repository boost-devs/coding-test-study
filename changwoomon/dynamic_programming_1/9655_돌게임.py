###### 9655번: 돌 게임
# https://www.acmicpc.net/problem/9655
# 메모리/시간: 29200KB / 72ms

import sys

input = sys.stdin.readline

N = int(input())

cnt = 0

while N > 0:
    if N % 3 == 0:
        cnt += N // 3
        break
    N -= 1
    cnt += 1

print("SK") if cnt % 2 == 1 else print("CY")