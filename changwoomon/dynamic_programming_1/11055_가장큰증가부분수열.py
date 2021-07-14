###### 11055번: 가장 큰 증가 부분 수열
# https://www.acmicpc.net/problem/11055
# 메모리/시간: 29200KB / 196ms

import sys

input = sys.stdin.readline

N = int(input())

A = list(map(int, input().split()))

table = [x for x in A]

for i in range(N):
    for j in range(i):
        if (A[i] > A[j]) and (table[i] < table[j] + A[i]):
            table[i] = table[j] + A[i]

print(max(table))