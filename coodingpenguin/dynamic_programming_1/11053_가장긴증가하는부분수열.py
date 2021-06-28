# 문제: [BOJ 11053] 가장 긴 증가하는 부분 수열
# 유형: 동적계획법
# 메모리/시간: 29200kb / 208ms

import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
table = [1] * n  # 수열 위치별 LIS의 최대 길이

for i in range(n):
    # 위치 i 이전 위치에 대하여
    for j in range(i):
        # i번째 수열값이 j번째 수열값보다 큰 경우
        if arr[i] > arr[j]:
            # 가장 큰 길이로 갱신
            table[i] = max(table[i], table[j] + 1)

print(max(table))
