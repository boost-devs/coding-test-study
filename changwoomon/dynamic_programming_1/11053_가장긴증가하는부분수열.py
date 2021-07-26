###### 11053번: 가장 긴 증가하는 부분 수열
# https://www.acmicpc.net/problem/11053
# 메모리/시간: 29200KB / 152ms

import sys

input = sys.stdin.readline

N = int(input())

A = list(map(int, input().split()))

table = [0 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if (A[i] > A[j]) and (table[i] < table[j]):
            table[i] = table[j]
    table[i] += 1

print(max(table))