###### 16171번: 나는 친구가 적다 (Small)
# https://www.acmicpc.net/problem/16171
# 메모리/시간: 29200KB / 68ms

import sys

input = sys.stdin.readline

S = list(input().rstrip())
K = input().rstrip()
new = [s if s.isalpha() else "" for s in S]

print(1) if K in "".join(new) else print(0)