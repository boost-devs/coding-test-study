# 문제: [BOJ 10870] 피보나치 수2
# 유형: 동적계획법
# 메모리/시간: 29200kb / 72ms

import sys

input = sys.stdin.readline

n = int(input())  # 몇 번째
l = n + 1 if n > 1 else 2  # 테이블 크기
table = [0, 1] + [0] * (l - 2)  # DP 테이블

for i in range(2, n + 1):
    table[i] = table[i - 1] + table[i - 2]

print(table[n])  # n번째 피보나치 수
