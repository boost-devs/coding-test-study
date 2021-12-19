###### 2579번: 계단 오르기
# https://www.acmicpc.net/problem/2579
# 메모리/시간: 31856KB / 88ms

import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())

table = defaultdict(int)
dp = defaultdict(int)

for i in range(1, N+1):
    table[i] = int(input().rstrip())

for i in range(1, N+1):
    dp[i] = max(dp[i-2]+table[i], dp[i-3]+table[i]+table[i-1])

print(dp[N])