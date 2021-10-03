# 문제: [BOJ 11055] 가장 큰 증가 부분 수열
# 유형: 동적계획법
# 메모리/시간: 29200kb / 220ms

import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

table = arr[:]  # 테이블 수열로 초기화
for i in range(1, n):
    # 위치 i 이전 위치 j에 대하여
    for j in range(i):
        # i번째 수열값이 j번째 수열값보다 큰 경우
        if arr[j] < arr[i]:
            # 가장 큰 값으로 갱신
            table[i] = max(table[i], table[j] + arr[i])

print(max(table))
