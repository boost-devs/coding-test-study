# 문제: [BOJ 11403] 경로 찾기
# 유형: 그래프 탐색, 플로이드
# 메모리/시간: 29452kb / 316ms

import sys

input = sys.stdin.readline

n = int(input())  # 정점 개수
arr = []  # 인접 행렬
for _ in range(n):
    row = list(map(int, input().split()))
    arr.append(row)

for k in range(n):
    for i in range(n):
        for j in range(n):
            # k에 의해 i와 j가 이어진다면
            if arr[i][k] and arr[k][j]:
                arr[i][j] = 1

# 출력
for row in arr:
    print(*row)
