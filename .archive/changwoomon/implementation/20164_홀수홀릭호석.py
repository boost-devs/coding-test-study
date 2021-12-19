###### 20164번: 홀수 홀릭 호석
# https://www.acmicpc.net/problem/20164
# 메모리/시간: 29200KB / 72ms

import sys
from itertools import combinations

input = sys.stdin.readline

N = input().rstrip()

def num_of_odd(num):
    cnt = 0
    for x in num:
        if int(x) % 2:
            cnt += 1
    return cnt

_min = 10**9
_max = 0

def odd_holic_hoseok(num, cnt):
    global _min, _max
    num = str(num)
    cnt += num_of_odd(num)
    if len(num) == 1:
        _min = min(_min, cnt)
        _max = max(_max, cnt)
    elif len(num) == 2:
        new_num = int(num[0]) + int(num[1])
        odd_holic_hoseok(new_num, cnt)
    else:
        for e1, e2 in combinations(range(1, len(num)), 2):
            new_num = int(num[:e1]) + int(num[e1:e2]) + int(num[e2:])
            odd_holic_hoseok(new_num, cnt)

odd_holic_hoseok(N, 0)

print(_min, _max)