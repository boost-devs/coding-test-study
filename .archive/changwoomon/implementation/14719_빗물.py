###### 14719번: 빗물
# https://www.acmicpc.net/problem/14719
# 메모리/시간: 29200KB / 76ms

import sys

input = sys.stdin.readline

H, W = map(int, input().split())

block = list(map(int, input().split()))

max_H = 0
max_H_idx = -1

for i, h in enumerate(block):
    if h > max_H:
        max_H = h
        max_H_idx = i

tmp = 0
_sum = 0

for i in range(max_H_idx+1):
    if block[i] > tmp:
        tmp = block[i]
    _sum += tmp - block[i]

tmp = 0

for i in range(W-1, max_H_idx, -1):
    if block[i] > tmp:
        tmp = block[i]
    _sum += tmp - block[i]

print(_sum)