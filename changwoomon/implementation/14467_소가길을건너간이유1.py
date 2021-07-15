###### 14467번: 소가 길을 건너간 이유 1
# https://www.acmicpc.net/problem/14467
# 메모리/시간: 29200KB / 68ms

import sys

input = sys.stdin.readline

N = int(input())

cows = dict()

cnt = 0

for _ in range(N):
    cow, position = map(int, input().split())
    if cow not in cows.keys():
        cows[cow] = position
    elif cows[cow] != position:
        cows[cow] = position
        cnt += 1

print(cnt)