###### 2470번: 두 용액
# https://www.acmicpc.net/problem/2470
# 메모리/시간: 40620KB / 164ms

import sys

input = sys.stdin.readline

N = int(input())

array = sorted(list(map(int, input().split())))

left, ans_left = 0, 0
right, ans_right = N-1, N-1
answer = array[left] + array[right]

while (left < right):
    tmp = array[left] + array[right]
    if abs(tmp) < abs(answer):
        answer = tmp
        ans_left = left
        ans_right = right
        if answer == 0:
            break
    if tmp < 0:
        left += 1
    else:
        right -= 1

print(array[ans_left], array[ans_right])