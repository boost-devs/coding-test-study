# 문제: [BOJ 11659] 구간 합 구하기 4
# 유형: 구간합
# 메모리/시간: 53564kb / 384ms

import sys

input = sys.stdin.readline


N, M = map(int, input().split())  # 수 개수, 구간 합 예시 수
arr = [0] + list(map(int, input().split()))  # N개의 수
range_sum = [list(map(int, input().split())) for _ in range(M)]  # M개의 구간 예시

# 접두사 합 계산
for i in range(1, N + 1):
    arr[i] += arr[i - 1]

# 구간 별 구간합 계산
for a, b in range_sum:
    print(arr[b] - arr[a - 1])
