# 문제: [BOJ 9035] 1, 2, 3 더하기
# 유형: 동적계획법
# 메모리/시간: 29200kb / 68ms

import sys

input = sys.stdin.readline

table = [0, 1, 2, 4]
for i in range(4, 11):
    table.append(table[i - 3] + table[i - 2] + table[i - 1])

t = int(input())  # 테스트 케이스
for _ in range(t):
    n = int(input())  # 숫자
    print(table[n])  # 1, 2, 3의 합 방법 수
