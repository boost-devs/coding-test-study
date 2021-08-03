###### 1806번: 부분합
# https://www.acmicpc.net/problem/1806
# 메모리/시간: 40236KB / 204ms

import sys

input = sys.stdin.readline

N, S = map(int, input().split())

array = list(map(int, input().split()))

left, right = 0, 0
cond_left, cond_right = False, True
_sum = 0
min_len = 100001

while (right < N) and (left <= right):
    if cond_right:
        _sum += array[right]
        cond_right = False
    if cond_left:
        _sum -= array[left-1]
        cond_left = False
    if _sum >= S:
        min_len = min(min_len, right-left+1)
        if left + 1 <= right:
            left += 1
            cond_left = True
        else:
            right += 1
            cond_right = True
    else:
        right += 1
        cond_right = True

print(min_len if min_len != 100001 else 0)