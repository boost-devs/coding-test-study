# 문제: [BOJ 17073] 나무 위의 빗물
# 유형: 트리
# 메모리/시간: 53048kb / 716ms

import sys

input = sys.stdin.readline

N, W = map(int, input().split())  # 노드 수, 물의 양
degrees = [0] * (N + 1)  # 노드에 연결된 간선수
for _ in range(N - 1):
    a, b = map(int, input().split())
    degrees[a] += 1
    degrees[b] += 1

leaves = []  # 리프 노드
for i in range(2, N + 1):
    if degrees[i] == 1:
        leaves.append(i)

# 출력
print(W / len(leaves))
