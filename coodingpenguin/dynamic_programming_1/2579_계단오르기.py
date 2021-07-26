# 문제: [BOJ 2579] 계단 오르기
# 유형: 동적계획법
# 메모리/시간: 32056kb / 100ms

import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
score = [int(input()) for _ in range(n)]
table = defaultdict(int)
table[0] = score[0]

for i in range(1, n):
    table[i] = max(table[i - 2], table[i - 3] + score[i - 1]) + score[i]

print(table[n - 1])  # 점수 최댓값
