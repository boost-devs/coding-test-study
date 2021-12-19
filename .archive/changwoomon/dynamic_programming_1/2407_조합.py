###### 2407번: 조합
# https://www.acmicpc.net/problem/2407
# 메모리/시간: 29200KB / 64ms

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
table = [1] * (n+1)

num = 1
for i in range(1, n+1):
    num *= i
    table[i] = num

print(table[n] // (table[m] * table[n-m]))