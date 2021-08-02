###### 21921번: 블로그
# https://www.acmicpc.net/problem/21921
# 메모리/시간: 58192KB / 228ms

import sys

input = sys.stdin.readline

N, X = map(int, input().split())

blog = list(map(int, input().split()))

_sum = sum(blog[:X])
_max = _sum
cnt = 1

for i in range(1, N-X+1):
    _sum = _sum - blog[i-1] + blog[i+X-1]
    if _sum > _max:
        _max = _sum
        cnt = 0
    if _max == _sum:
        cnt += 1

print(_max, cnt, sep="\n") if _max else print("SAD")