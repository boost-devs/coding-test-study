# 문제: [BOJ 10994] 별찍기 19
# 유형: 구현
# 메모리/시간: 29908kb / 116ms

import sys

input = sys.stdin.readline

n = int(input())
func = lambda x: 4 * x - 3  # 배열 크기 변환 함수
size = func(n)  # 배열 크기
arr = [[" "] * size for _ in range(size)]  # 빈 배열

for i in range(n, 0, -1):
    pad = (n - i) * 2  # 패딩
    for j in range(pad, size - pad):
        # 가로줄
        arr[pad][j] = "*"
        arr[size - pad - 1][j] = "*"
        # 세로줄
        arr[j][pad] = "*"
        arr[j][size - pad - 1] = "*"

# 배열 출력
for row in arr:
    print(*row, sep="")
