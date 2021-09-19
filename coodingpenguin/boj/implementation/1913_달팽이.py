# 문제: [BOJ 1913] 달팽이
# 유형: 구현
# 메모리/시간: 67980kb / 1124ms

import sys

input = sys.stdin.readline

n, m = int(input()), int(input())  # 테이블 크기, 위치
table = [[1] * n for i in range(n)]
count = n ** 2
for i in range(0, n // 2):
    k = 2 * (n // 2 - i)
    # 위에서 아래로
    for j in range(i, i + k + 1):
        table[j][i] = count
        count -= 1

    # 왼쪽에서 오른쪽으로
    for j in range(i + 1, i + k):
        table[i + k][j] = count
        count -= 1

    # 아래에서 위로
    for j in range(i + k, i, -1):
        table[j][i + k] = count
        count -= 1

    # 오른쪽으로 왼쪽으로
    for j in range(i + k, i, -1):
        table[i][j] = count
        count -= 1

y, x = 1, 1
for i in range(n):
    for j in range(n):
        if table[i][j] == m:
            y, x = i + 1, j + 1
        print(table[i][j], end=" ")
    print()
print(y, x)
