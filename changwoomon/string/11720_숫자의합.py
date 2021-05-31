###### 11720번: 숫자의 합
# https://www.acmicpc.net/problem/11720
# 메모리/시간: 29200KB / 76ms

import sys

input = sys.stdin.readline

N = int(input().rstrip())
number = str(input().rstrip())
_sum = 0

for x in number:
    _sum += int(x)

print(_sum)