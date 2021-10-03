# 문제: [BOJ 1463] 1로 만들기
# 유형: 동적계획법
# 메모리/시간: 37012kb / 604ms

import sys

input = sys.stdin.readline

n = int(input())
table = [0] * (n + 1)

for i in range(2, n + 1):
    # 1을 뺀 경우
    table[i] = table[i - 1] + 1
    if not i % 2:
        # 2로 나누어 떨어지는 경우
        table[i] = min(table[i], table[i // 2] + 1)
    if not i % 3:
        # 3으로 나누어 떨어지는 경우
        table[i] = min(table[i], table[i // 3] + 1)

print(table[n])
