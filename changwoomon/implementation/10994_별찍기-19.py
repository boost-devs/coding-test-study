###### 10994번: 별 찍기 - 19
# https://www.acmicpc.net/problem/10994
# 메모리/시간: 29200KB / 68ms

import sys

input = sys.stdin.readline

N = int(input())

for i in range(1, N):
    j = (N-i)*4 + 1
    print("* " * (i-1) + "*" * j + " *" * (i-1))
    print("* " * i + " " * (j-4) + " *" * i)

print("* " * (N*2-1))

for i in range(N-1, 0, -1):
    j = (N-i)*4 + 1
    print("* " * i + " " * (j-4) + " *" * i)
    print("* " * (i-1) + "*" * j + " *" * (i-1))