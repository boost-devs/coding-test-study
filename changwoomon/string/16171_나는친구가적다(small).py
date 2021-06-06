###### 16171번: 나는 친구가 적다 (Small)
# https://www.acmicpc.net/problem/16171
# 메모리/시간: 29200KB / 68ms

import sys

input = sys.stdin.readline

S = list(input().rstrip())
K = input().rstrip()
new = ""

for s in S:
    if s.isalpha():
        new += s

print(1) if K in new else print(0)