# 문제: [BOJ 11727] 2xn 타일링 2
# 유형: 동적계획법
# 메모리/시간: 29200kb / 68ms

import sys

input = sys.stdin.readline

n = int(input())
table = [1] * (n + 1)

for i in range(2, n + 1):
    # i가 짝수이면
    if not i % 2:
        table[i] = table[i - 1] * 2 + 1
    # i가 홀수이면
    else:
        table[i] = table[i - 1] * 2 - 1

print(table[n] % 10007)

