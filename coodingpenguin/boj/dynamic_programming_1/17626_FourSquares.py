# 문제: [BOJ 17626] Four Squares
# 유형: 동적계획법
# 메모리/시간: 125956kb / 196ms (PyPy3)

import sys
from math import sqrt

input = sys.stdin.readline

n = int(input())  # 자연수
table = [0, 1, 2, 3] + [5] * (n - 3)  # 테이블

for i in range(4, n + 1):
    squared = int(sqrt(i))
    # 제곱수면 1로 채움
    if i == squared ** 2:
        table[i] = 1
    # 제곱수가 아니면
    else:
        # 1부터 최대 제곱수를 뺐을 때의 개수의 최소값을 구해 +1
        table[i] = min([table[i - j ** 2] for j in range(1, squared + 1)]) + 1

print(table[n])  # 제곱수들의 최소 개수
