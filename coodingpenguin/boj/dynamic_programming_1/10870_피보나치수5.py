# 문제: [BOJ 10870] 피보나치 수5
# 유형: 동적계획법
# 메모리/시간: 29200kb / 72ms

import sys

input = sys.stdin.readline

n = int(input())  # 몇 번째
l = n + 1 if n > 1 else 2  # 테이블 길이

# 테이블 생성 및 초기화
table = [0] * l
table[1] = 1

# 테이블 채우기
for i in range(2, n + 1):
    table[i] = table[i - 1] + table[i - 2]

print(table[n])  # n번째 피보나치 수
