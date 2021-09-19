# 문제: [BOJ 11726] 2xn 타일링
# 유형: 동적계획법
# 메모리/시간: 29200kb / 68ms

import sys

input = sys.stdin.readline

n = int(input())
table = [1] * (n + 1)

for i in range(2, n + 1):
    table[i] = table[i - 1] + table[i - 2]

print(table[n] % 10007)  # 2xn 크기의 직사각형 채우는 방법 수
