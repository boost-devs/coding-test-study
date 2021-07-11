###### 1463번: 1로 만들기
# https://www.acmicpc.net/problem/1463
# 메모리/시간: 37012KB / 636ms

import sys

input = sys.stdin.readline

N = int(input())

table = [0] * (N+1)

for i in range(2, N+1):
    table[i] = table[i-1] + 1
    if i % 2 == 0:
        table[i] = min(table[i], table[i//2]+1)
    if i % 3 == 0:
        table[i] = min(table[i], table[i//3]+1)

print(table[N])