###### 11659번: 구간 합 구하기 4
# https://www.acmicpc.net/problem/11659
# 메모리/시간: 48840KB / 344ms

import sys
from collections import defaultdict

input = sys.stdin.readline

N, M = map(int, input().split())

array = list(map(int, input().split()))

_sum = defaultdict(int)

for i in range(N):
    _sum[i] = _sum[i-1] + array[i]

for _ in range(M):
    i, j = map(int, input().split())
    print(_sum[j-1]-_sum[i-2])