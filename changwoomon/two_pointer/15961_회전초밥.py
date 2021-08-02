###### 15961번: 회전 초밥
# https://www.acmicpc.net/problem/15961
# 메모리/시간: 139288KB / 3772ms

import sys

input = sys.stdin.readline

N, d, k, c = map(int, input().split())

sushi = [int(input()) for _ in range(N)]

eat = [0] * (d+1)
eat[c] = 1

cnt = 1

for i in range(k-1):
    if eat[sushi[i]] == 0:
        cnt += 1
    eat[sushi[i]] += 1

_max = cnt
left, right = 0, k-1

while (left < N):
    if eat[sushi[right]] == 0:
        cnt += 1
    eat[sushi[right]] += 1
    _max = max(_max, cnt)
    eat[sushi[left]] -= 1
    if eat[sushi[left]] == 0:
        cnt -= 1
    left += 1
    right = (right+1) % N

print(_max)