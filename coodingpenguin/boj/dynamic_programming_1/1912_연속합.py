# 문제: [BOJ 1912] 연속합
# 유형: 동적계획법
# 메모리/시간: 37164kb / 128ms

import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))  # 수열

table = [0] * n  # 테이블
table[0] = arr[0]  # 테이블 초기화

for i in range(1, n):
    table[i] = max(table[i - 1] + arr[i], arr[i])

print(max(table))  # 최대 연속합
