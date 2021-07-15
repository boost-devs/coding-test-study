###### 17609번: 회문
# https://www.acmicpc.net/problem/17609
# 메모리/시간: 29200KB / 260ms

import sys

input = sys.stdin.readline

T = int(input())

def check_2(string, left, right):
    while (left < right):
        if string[left] == string[right]:
            left += 1
            right -= 1
        else:
            return False
    return True

def check(string, left, right):
    while (left < right):
        if string[left] == string[right]:
            left += 1
            right -= 1
        else:
            cond1 = check_2(string, left+1, right)
            cond2 = check_2(string, left, right-1)
            if any([cond1, cond2]):
                return 1
            else:
                return 2
    return 0

for _ in range(T):
    _input = input().rstrip()
    left = 0
    right = len(_input) - 1
    print(check(_input, left, right))