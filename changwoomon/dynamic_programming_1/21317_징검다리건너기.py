###### 21317번: 징검다리 건너기
# https://www.acmicpc.net/problem/21317
# 메모리/시간: 29200KB / 72ms

import sys

input = sys.stdin.readline

N = int(input())

energy = [list(map(int, input().split())) for _ in range(N-1)]

K = int(input())

table = [0] + [100001] * (N-1)

for i, (s, b) in enumerate(energy):
    table[i+1] = min(table[i+1], table[i]+s)
    if i + 2 >= N:
        continue
    table[i+2] = min(table[i+2], table[i]+b)

answer = table[N-1]

for j in range(N-3):
    table = [0] + [100001] * (N-1)
    for i, (s, b) in enumerate(energy):
        table[i+1] = min(table[i+1], table[i]+s)
        if i + 2 >= N:
            continue
        table[i+2] = min(table[i+2], table[i]+b)
        if i == j:
            table[i+3] = table[i] + K
    answer = min(answer, table[N-1])

print(answer)